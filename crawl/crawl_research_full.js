#!/usr/bin/env node
/**
 * Full-domain BFS crawl of research.unimelb.edu.au — saves raw HTML + all outbound links.
 * Each page gets a directory with: page.html, links.json, meta.json
 */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { URL } = require('url');

const DOMAIN = 'research.unimelb.edu.au';
const BASE = `https://${DOMAIN}`;
const OUT_ROOT = path.join(process.env.HOME, 'Documents/Claude/projects/unimelb-current-students-ia/crawl/research-full');
const PAGES_DIR = path.join(OUT_ROOT, 'pages');
const MAX_PAGES = 2000;

function fingerprint(url) {
  return crypto.createHash('sha1').update(url).digest('hex').slice(0, 16);
}

function shouldSkip(url) {
  if (!url) return true;
  const skipPatterns = [
    /\.(pdf|docx?|xlsx?|pptx?|zip|tar|gz|jpg|jpeg|png|gif|svg|mp4|mp3|webm|webp|ico|xml|rss|css|js|woff2?|ttf|eot)(\?.*)?$/i,
    /mailto:/i, /^javascript:/i, /^#/, /tel:/i, /login/i,
  ];
  return skipPatterns.some(p => p.test(url));
}

function categorizeUrl(url) {
  try {
    const u = new URL(url);
    if (u.hostname === DOMAIN) return 'internal';
    if (u.hostname.endsWith('.unimelb.edu.au')) return 'unimelb';
    return 'external';
  } catch { return 'unknown'; }
}

async function crawlPage(page, url) {
  console.log(`  [FETCH] ${url.slice(0, 130)}`);
  const fp = fingerprint(url);
  const pageDir = path.join(PAGES_DIR, fp);
  fs.mkdirSync(pageDir, { recursive: true });

  try {
    await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
  } catch (e) {
    // Still try to get what we can
    try { await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 15000 }); } catch {}
  }

  await page.waitForTimeout(1000);

  // Get HTML
  let html = '';
  try { html = await page.content(); } catch {}
  
  const byteLength = Buffer.byteLength(html, 'utf8');
  
  // Get title  
  let title = '';
  try { title = await page.title(); } catch {}

  // Extract ALL links with full categorization
  let allLinks = [];
  try {
    allLinks = await page.evaluate((baseUrl) => {
      const links = [];
      const seen = new Set();
      document.querySelectorAll('a[href]').forEach(a => {
        try {
          const u = new URL(a.href, baseUrl);
          u.hash = '';
          const href = u.href;
          if (!seen.has(href)) {
            seen.add(href);
            links.push({
              href,
              text: (a.textContent || '').trim().slice(0, 200),
              hostname: u.hostname,
              path: u.pathname,
            });
          }
        } catch {}
      });
      return links;
    }, url);
  } catch {}

  // Categorize and deduplicate
  const seen = new Set();
  const uniqueLinks = [];
  for (const l of allLinks) {
    if (!seen.has(l.href) && !shouldSkip(l.href)) {
      seen.add(l.href);
      l.category = categorizeUrl(l.href);
      uniqueLinks.push(l);
    }
  }

  // Save HTML
  fs.writeFileSync(path.join(pageDir, 'page.html'), html);
  
  // Save links inventory
  fs.writeFileSync(path.join(pageDir, 'links.json'), JSON.stringify({
    total: uniqueLinks.length,
    internal: uniqueLinks.filter(l => l.category === 'internal').length,
    unimelb: uniqueLinks.filter(l => l.category === 'unimelb').length,
    external: uniqueLinks.filter(l => l.category === 'external').length,
    links: uniqueLinks,
  }, null, 2));

  // Save metadata
  fs.writeFileSync(path.join(pageDir, 'meta.json'), JSON.stringify({
    url, fingerprint: fp, title,
    byteLength, linkCount: uniqueLinks.length,
    crawledAt: new Date().toISOString(),
  }, null, 2));

  // Return internal links for BFS frontier
  const internalLinks = uniqueLinks
    .filter(l => l.category === 'internal')
    .map(l => l.href);

  console.log(`    [SAVED] ${byteLength}b HTML, ${uniqueLinks.length} links (${internalLinks.length} internal)`);
  return { url, title, byteLength, links: uniqueLinks, internalLinks };
}

async function main() {
  console.log(`\n${'='.repeat(60)}`);
  console.log(`FULL CRAWL: ${DOMAIN} (raw HTML + all links)`);
  console.log(`Output: ${OUT_ROOT}`);
  console.log(`${'='.repeat(60)}`);

  fs.mkdirSync(PAGES_DIR, { recursive: true });

  let browser;
  try {
    browser = await chromium.connectOverCDP('http://localhost:9222');
    console.log('Connected to Chrome CDP');
  } catch {
    console.log('CDP not available — launching Chromium');
    browser = await chromium.launch({ headless: true });
  }

  const page = await browser.newPage();
  await page.setViewportSize({ width: 1440, height: 900 });

  // Check homepage
  try {
    await page.goto(`${BASE}/`, { waitUntil: 'domcontentloaded', timeout: 15000 });
    console.log(`  Homepage: "${await page.title()}"`);
  } catch (e) {
    console.log(`  CANNOT LOAD: ${e.message.slice(0, 100)}`);
    process.exit(1);
  }

  const visited = new Set();
  const frontier = [`${BASE}/`];
  const crawled = [];
  let count = 0;

  while (frontier.length > 0 && count < MAX_PAGES) {
    const url = frontier.shift();
    if (visited.has(url)) continue;
    visited.add(url);

    const result = await crawlPage(page, url);
    if (result) {
      crawled.push({ url, title: result.title, byteLength: result.byteLength, linkCount: result.links.length });
      count++;
      const newLinks = result.internalLinks.filter(l => !visited.has(l) && !frontier.includes(l));
      frontier.push(...newLinks);
    }
    await page.waitForTimeout(500);
  }

  await page.close();
  await browser.close();

  // Save master index
  const index = {
    domain: DOMAIN,
    pagesCrawled: crawled.length,
    urlsVisited: visited.size,
    frontierRemaining: frontier.length,
    pages: crawled,
    frontier,
  };
  fs.writeFileSync(path.join(OUT_ROOT, 'index.json'), JSON.stringify(index, null, 2));

  console.log(`\n${'='.repeat(60)}`);
  console.log(`DONE: ${crawled.length} pages`);
  console.log(`HTML + links in: ${PAGES_DIR}/`);
  console.log(`Index: ${path.join(OUT_ROOT, 'index.json')}`);
  console.log(`${'='.repeat(60)}`);
}

main().catch(e => { console.error(e); process.exit(1); });
