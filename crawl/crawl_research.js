#!/usr/bin/env node
/**
 * BFS crawl of research.unimelb.edu.au via Playwright + existing Chrome CDP.
 * Same pattern as full_domain_crawler.js — saves raw text + structured JSON.
 */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { URL } = require('url');

const DOMAIN = 'research.unimelb.edu.au';
const OUT_DIR = path.join(process.env.HOME, 'Documents/Claude/projects/unimelb-current-students-ia/crawl/full-faculty');
const MAX_PAGES = 1000;

function fingerprint(url) {
  return crypto.createHash('sha1').update(url).digest('hex').slice(0, 16);
}

function shouldSkip(url) {
  if (!url) return true;
  const skipPatterns = [
    /\.(pdf|docx?|xlsx?|pptx?|zip|tar|gz|jpg|jpeg|png|gif|svg|mp4|mp3|webm|css|js|ico|xml|rss)$/i,
    /mailto:/i, /^javascript:/i, /^#/, /tel:/i, /login/i,
  ];
  return skipPatterns.some(p => p.test(url));
}

function isInternal(url, domain) {
  try {
    const u = new URL(url);
    return u.hostname === domain || u.hostname.endsWith('.' + domain);
  } catch { return false; }
}

async function crawlPage(page, url) {
  console.log(`  [FETCH] ${url.slice(0, 120)}`);
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 20000 });
  } catch (e) {
    console.log(`    NAV FAIL: ${e.message.slice(0, 80)}`);
    return null;
  }
  await page.waitForTimeout(1500);

  let title = '';
  try { title = await page.title(); } catch {}

  let text = '';
  try {
    text = await page.evaluate(() => {
      const main = document.querySelector('main') || document.querySelector('article') || document.body;
      if (!main) return '';
      const clone = main.cloneNode(true);
      clone.querySelectorAll('script, style, nav, footer, header, [role="navigation"]').forEach(el => el.remove());
      return (clone.innerText || clone.textContent || '').trim();
    });
  } catch {}

  const wordCount = text ? text.split(/\s+/).filter(w => w.length > 0).length : 0;
  if (wordCount === 0) {
    console.log('    EMPTY');
    return null;
  }

  let links = [];
  try {
    links = await page.evaluate((baseUrl) => {
      const links = new Set();
      document.querySelectorAll('a[href]').forEach(a => {
        try { const u = new URL(a.href, baseUrl); u.hash = ''; links.add(u.href); } catch {}
      });
      return [...links];
    }, url);
  } catch {}

  const internalLinks = [...new Set(
    links.filter(l => isInternal(l, DOMAIN))
      .filter(l => !shouldSkip(l))
  )];

  const fp = fingerprint(url);
  const rawDir = path.join(OUT_DIR, 'raw_research');
  fs.mkdirSync(rawDir, { recursive: true });
  fs.writeFileSync(path.join(rawDir, `${fp}.txt`),
    `URL: ${url}\nTITLE: ${title}\nWORD_COUNT: ${wordCount}\n\n${text}`);

  return { url, normalizedUrl: url, title, wordCount, outboundLinks: internalLinks, fingerprint: fp };
}

async function main() {
  console.log(`\n${'='.repeat(60)}`);
  console.log(`CRAWLING: research (${DOMAIN})`);
  console.log(`${'='.repeat(60)}`);

  const browser = await chromium.connectOverCDP('http://localhost:9222');
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1440, height: 900 });

  // Quick homepage check
  try {
    await page.goto(`https://${DOMAIN}/`, { waitUntil: 'domcontentloaded', timeout: 15000 });
    const t = await page.title();
    console.log(`  Homepage: "${t}"`);
  } catch (e) {
    console.log(`  CANNOT LOAD: ${e.message.slice(0, 100)}`);
    await page.close();
    await browser.close();
    return;
  }

  const visited = new Set();
  const frontier = [`https://${DOMAIN}/`];
  const pages = [];
  let pageCount = 0;

  while (frontier.length > 0 && pageCount < MAX_PAGES) {
    const url = frontier.shift();
    if (visited.has(url)) continue;
    visited.add(url);

    const pageData = await crawlPage(page, url);
    if (pageData) {
      pages.push(pageData);
      pageCount++;
      const newLinks = pageData.outboundLinks.filter(l => !visited.has(l) && !frontier.includes(l));
      frontier.push(...newLinks);
      console.log(`    [${pageCount}] ${pageData.wordCount}w, +${newLinks.length} links, frontier=${frontier.length}`);
    }
    await page.waitForTimeout(600);
  }

  await page.close();
  await browser.close();

  const outPath = path.join(OUT_DIR, 'research.json');
  fs.writeFileSync(outPath, JSON.stringify({
    domain: DOMAIN, slug: 'research',
    pages_crawled: pages.length, urls_visited: visited.size, frontier_remaining: frontier.length, pages,
  }, null, 2));
  console.log(`\n  DONE: ${pages.length} pages → ${outPath}`);
}

main().catch(e => { console.error(e); process.exit(1); });
