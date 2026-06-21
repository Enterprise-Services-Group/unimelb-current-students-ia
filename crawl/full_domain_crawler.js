#!/usr/bin/env node
/**
 * Full-domain BFS crawler using Playwright (Chromium via CDP).
 * Crawls every reachable page on each faculty domain.
 * Saves raw text + structured JSON — same pattern as the original CS crawl.
 *
 * Usage: npx playwright install chromium && node full_domain_crawler.js
 */

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { URL } = require('url');

const OUT_DIR = path.join(process.env.HOME, 'Documents/Claude/projects/unimelb-current-students-ia/crawl/full-faculty');
const MAX_PAGES = 500;
const MAX_DEPTH = 6;

const FACULTIES = [
  // law already done (266 pages)
  ['feit', 'eng.unimelb.edu.au'],
  ['arts', 'arts.unimelb.edu.au'],
  ['science', 'science.unimelb.edu.au'],
  ['education', 'education.unimelb.edu.au'],
  ['fbe', 'fbe.unimelb.edu.au'],
  ['ffam', 'finearts-music.unimelb.edu.au'],
  ['mdhs', 'mdhs.unimelb.edu.au'],
  ['msd', 'msd.unimelb.edu.au'],
];

fs.mkdirSync(OUT_DIR, { recursive: true });

function fingerprint(url) {
  return crypto.createHash('sha1').update(url).digest('hex').slice(0, 16);
}

function normalizeUrl(url, base) {
  try {
    const u = new URL(url, base);
    u.hash = '';
    return u.href;
  } catch {
    return null;
  }
}

function isInternal(url, domain) {
  try {
    const u = new URL(url);
    return u.hostname === domain || u.hostname.endsWith('.' + domain);
  } catch {
    return false;
  }
}

function shouldSkip(url) {
  // Skip binary files, auth-gated, external, anchors
  if (!url) return true;
  const skipPatterns = [
    /\.(pdf|docx?|xlsx?|pptx?|zip|tar|gz|jpg|jpeg|png|gif|svg|mp4|mp3|webm|css|js|ico|xml|rss)$/i,
    /mailto:/i,
    /^javascript:/i,
    /^#/,
    /tel:/i,
    /my\.unimelb/i,
    /lms\.unimelb/i,
    /canvas\.unimelb/i,
    /login/i,
  ];
  return skipPatterns.some(p => p.test(url));
}

async function crawlPage(page, url) {
  console.log(`  [FETCH] ${url.slice(0, 100)}`);
  
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 20000 });
  } catch (e) {
    console.log(`    NAV FAIL: ${e.message.slice(0, 80)}`);
    return null;
  }
  
  // Wait for any JS rendering
  await page.waitForTimeout(2000);
  
  // Get page title
  let title = '';
  try { title = await page.title(); } catch {}
  
  // Get body text
  let text = '';
  try {
    text = await page.evaluate(() => {
      const main = document.querySelector('main') || document.querySelector('article') || document.body;
      if (!main) return '';
      const clone = main.cloneNode(true);
      clone.querySelectorAll('script, style, nav, footer, header, .uom-megamenu, .site-nav, .breadcrumb, [role="navigation"]').forEach(el => el.remove());
      return (clone.innerText || clone.textContent || '').trim();
    });
  } catch {}
  
  const wordCount = text ? text.split(/\s+/).filter(w => w.length > 0).length : 0;
  
  if (wordCount === 0) {
    console.log(`    EMPTY — likely WAF or render failure`);
    return null;
  }
  
  // Extract internal links
  let links = [];
  try {
    links = await page.evaluate((baseUrl) => {
      const links = new Set();
      document.querySelectorAll('a[href]').forEach(a => {
        try {
          const u = new URL(a.href, baseUrl);
          u.hash = '';
          links.add(u.href);
        } catch {}
      });
      return [...links];
    }, url);
  } catch {}
  
  // Filter links
  const currentDomain = new URL(url).hostname;
  const internalLinks = links
    .filter(l => isInternal(l, currentDomain))
    .filter(l => !shouldSkip(l))
    .map(l => normalizeUrl(l, url))
    .filter(Boolean);
  
  // Deduplicate
  const uniqueLinks = [...new Set(internalLinks)];
  
  // Save raw text
  const fp = fingerprint(url);
  const rawDir = path.join(OUT_DIR, `raw_${currentDomain.split('.')[0]}`);
  fs.mkdirSync(rawDir, { recursive: true });
  fs.writeFileSync(path.join(rawDir, `${fp}.txt`), 
    `URL: ${url}\nTITLE: ${title}\nWORD_COUNT: ${wordCount}\n\n${text}`);
  
  return {
    url,
    normalizedUrl: url,
    title,
    wordCount,
    outboundLinks: uniqueLinks,
    fingerprint: fp,
  };
}

async function crawlDomain(browser, slug, domain) {
  const base = `https://${domain}`;
  const visited = new Set();
  const frontier = [base + '/'];
  const pages = [];
  let pageCount = 0;
  
  console.log(`\n${'='.repeat(60)}`);
  console.log(`CRAWLING: ${slug} (${domain})`);
  console.log(`${'='.repeat(60)}`);
  
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1440, height: 900 });
  
  // Quick check: can we load the homepage?
  try {
    await page.goto(base + '/', { waitUntil: 'domcontentloaded', timeout: 15000 });
    const title = await page.title();
    console.log(`  Homepage loaded: "${title}"`);
  } catch (e) {
    console.log(`  CANNOT LOAD HOMEPAGE: ${e.message.slice(0, 100)}`);
    await page.close();
    return { domain, slug, error: e.message, pages_crawled: 0 };
  }
  
  while (frontier.length > 0 && pageCount < MAX_PAGES) {
    const url = frontier.shift();
    if (visited.has(url)) continue;
    visited.add(url);
    
    const pageData = await crawlPage(page, url);
    
    if (pageData) {
      pages.push(pageData);
      pageCount++;
      
      // Add new links to frontier
      const newLinks = pageData.outboundLinks.filter(l => !visited.has(l) && !frontier.includes(l));
      frontier.push(...newLinks);
      
      console.log(`    [${pageCount}] ${pageData.wordCount} words, +${newLinks.length} links, frontier=${frontier.length}`);
    }
    
    // Polite delay
    await page.waitForTimeout(800);
  }
  
  await page.close();
  
  // Save structured JSON
  const output = {
    domain,
    slug,
    pages_crawled: pages.length,
    urls_visited: visited.size,
    frontier_remaining: frontier.length,
    pages,
  };
  
  const outPath = path.join(OUT_DIR, `${slug}.json`);
  fs.writeFileSync(outPath, JSON.stringify(output, null, 2));
  console.log(`  SAVED: ${pages.length} pages → ${outPath}`);
  
  return output;
}

async function main() {
  console.log('Starting full-domain faculty crawler...');
  console.log(`Output: ${OUT_DIR}\n`);
  
  // Connect to existing Chrome via CDP or launch new browser
  let browser;
  try {
    browser = await chromium.connectOverCDP('http://localhost:9222');
    console.log('Connected to existing Chrome via CDP');
  } catch (e) {
    console.log('No existing Chrome CDP — launching Chromium...');
    browser = await chromium.launch({ headless: true });
  }
  
  const allResults = {};
  
  for (const [slug, domain] of FACULTIES) {
    try {
      allResults[slug] = await crawlDomain(browser, slug, domain);
    } catch (e) {
      console.log(`\n  FATAL for ${slug}: ${e.message}`);
      allResults[slug] = { domain, slug, error: e.message, pages_crawled: 0 };
    }
  }
  
  // Save summary
  const summaryPath = path.join(OUT_DIR, '_summary.json');
  fs.writeFileSync(summaryPath, JSON.stringify(allResults, null, 2));
  
  console.log(`\n\n${'='.repeat(60)}`);
  console.log('FULL CRAWL COMPLETE');
  console.log(`${'='.repeat(60)}`);
  for (const [slug, data] of Object.entries(allResults)) {
    if (data.error) {
      console.log(`  ${slug}: ERROR — ${data.error.slice(0, 60)}`);
    } else {
      console.log(`  ${slug}: ${data.pages_crawled} pages, ${data.urls_visited} visited`);
    }
  }
  console.log(`\nData: ${OUT_DIR}/`);
  
  await browser.close();
}

main().catch(e => { console.error(e); process.exit(1); });
