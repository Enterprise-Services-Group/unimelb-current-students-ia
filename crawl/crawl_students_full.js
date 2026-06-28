#!/usr/bin/env node
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { URL } = require('url');

const DOMAIN = 'students.unimelb.edu.au';
const BASE = `https://${DOMAIN}`;
const OUT_ROOT = path.join(process.env.HOME, 'Documents/Claude/projects/unimelb-current-students-ia/crawl/students-full');
const PAGES_DIR = path.join(OUT_ROOT, 'pages');
const MAX_PAGES = 3000;

function fingerprint(url) {
  return crypto.createHash('sha1').update(url).digest('hex').slice(0, 16);
}

function shouldSkip(url) {
  if (!url) return true;
  return /\.(pdf|docx?|xlsx?|pptx?|zip|tar|gz|jpg|jpeg|png|gif|svg|mp4|mp3|webm|webp|ico|xml|rss|css|js|woff2?|ttf|eot)(\?.*)?$/i.test(url)
    || /mailto:|^javascript:|^#|tel:|login/i.test(url);
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
  const fp = fingerprint(url);
  const pageDir = path.join(PAGES_DIR, fp);
  fs.mkdirSync(pageDir, { recursive: true });

  try {
    await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
  } catch {
    try { await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 15000 }); } catch {}
  }
  await page.waitForTimeout(1000);

  let html = '', title = '';
  try { html = await page.content(); } catch {}
  try { title = await page.title(); } catch {}
  const byteLength = Buffer.byteLength(html, 'utf8');

  let allLinks = [];
  try {
    allLinks = await page.evaluate((baseUrl) => {
      const links = [], seen = new Set();
      document.querySelectorAll('a[href]').forEach(a => {
        try {
          const u = new URL(a.href, baseUrl); u.hash = ''; const href = u.href;
          if (!seen.has(href)) { seen.add(href); links.push({ href, text: (a.textContent||'').trim().slice(0,200), hostname: u.hostname, path: u.pathname }); }
        } catch {}
      });
      return links;
    }, url);
  } catch {}

  const seen = new Set(), uniqueLinks = [];
  for (const l of allLinks) {
    if (!seen.has(l.href) && !shouldSkip(l.href)) { seen.add(l.href); l.category = categorizeUrl(l.href); uniqueLinks.push(l); }
  }

  fs.writeFileSync(path.join(pageDir, 'page.html'), html);
  fs.writeFileSync(path.join(pageDir, 'links.json'), JSON.stringify({
    total: uniqueLinks.length, internal: uniqueLinks.filter(l=>l.category==='internal').length,
    unimelb: uniqueLinks.filter(l=>l.category==='unimelb').length, external: uniqueLinks.filter(l=>l.category==='external').length,
    links: uniqueLinks,
  }, null, 2));
  fs.writeFileSync(path.join(pageDir, 'meta.json'), JSON.stringify({
    url, fingerprint: fp, title, byteLength, linkCount: uniqueLinks.length, crawledAt: new Date().toISOString(),
  }, null, 2));

  const internalLinks = uniqueLinks.filter(l => l.category === 'internal').map(l => l.href);
  console.log(`    [SAVED] ${byteLength}b HTML, ${uniqueLinks.length} links (${internalLinks.length} internal)`);
  return { url, title, byteLength, links: uniqueLinks, internalLinks };
}

async function main() {
  console.log(`\n${'='.repeat(60)}\nFULL CRAWL: ${DOMAIN}\nOutput: ${OUT_ROOT}\n${'='.repeat(60)}`);
  fs.mkdirSync(PAGES_DIR, { recursive: true });

  let browser;
  try { browser = await chromium.connectOverCDP('http://localhost:9222'); console.log('Connected to Chrome CDP'); }
  catch { browser = await chromium.launch({ headless: true }); console.log('Using headless Chromium'); }

  const page = await browser.newPage();
  await page.setViewportSize({ width: 1440, height: 900 });

  try {
    await page.goto(`${BASE}/`, { waitUntil: 'domcontentloaded', timeout: 15000 });
    console.log(`  Homepage: "${await page.title()}"`);
  } catch (e) { console.log(`  CANNOT LOAD: ${e.message.slice(0,100)}`); process.exit(1); }

  const visited = new Set(), frontier = [`${BASE}/`], crawled = [];
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

  await page.close(); await browser.close();
  fs.writeFileSync(path.join(OUT_ROOT, 'index.json'), JSON.stringify({
    domain: DOMAIN, pagesCrawled: crawled.length, urlsVisited: visited.size, frontierRemaining: frontier.length, pages: crawled, frontier,
  }, null, 2));
  console.log(`\nDONE: ${crawled.length} pages → ${OUT_ROOT}/`);
}
main().catch(e => { console.error(e); process.exit(1); });
