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
const CHECKPOINT_FILE = path.join(OUT_ROOT, 'checkpoint.json');
const INDEX_FILE = path.join(OUT_ROOT, 'index.json');
const CHECKPOINT_INTERVAL = 50;
const MAX_PAGES = 5000;

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

function loadState() {
  const visited = new Set();
  let frontier = [];
  let crawledCount = 0;

  // Load from index.json (previous crawl's pages)
  if (fs.existsSync(INDEX_FILE)) {
    try {
      const idx = JSON.parse(fs.readFileSync(INDEX_FILE, 'utf8'));
      if (idx.pages && Array.isArray(idx.pages)) {
        for (const p of idx.pages) {
          if (p.url) visited.add(p.url);
        }
        crawledCount = idx.pages.length;
        console.log(`Loaded ${crawledCount} visited URLs from index.json`);
      }
    } catch (e) { console.log(`Could not parse index.json: ${e.message}`); }
  }

  // Load checkpoint (may have frontier that wasn't saved to index)
  if (fs.existsSync(CHECKPOINT_FILE)) {
    try {
      const ck = JSON.parse(fs.readFileSync(CHECKPOINT_FILE, 'utf8'));
      if (ck.visited && Array.isArray(ck.visited)) {
        for (const u of ck.visited) visited.add(u);
        console.log(`Loaded ${ck.visited.length} additional visited from checkpoint`);
      }
      if (ck.frontier && Array.isArray(ck.frontier) && ck.frontier.length > 0) {
        frontier = ck.frontier;
        console.log(`Loaded ${frontier.length} frontier URLs from checkpoint`);
      }
    } catch (e) { console.log(`Could not parse checkpoint: ${e.message}`); }
  }

  return { visited, frontier, crawledCount };
}

function saveCheckpoint(visited, frontier, crawledCount) {
  fs.writeFileSync(CHECKPOINT_FILE, JSON.stringify({
    visited: [...visited],
    frontier,
    crawledCount,
    savedAt: new Date().toISOString(),
  }, null, 2));
}

async function extractLinksDeep(page, baseUrl) {
  const links = [], seen = new Set();
  try {
    const extracted = await page.evaluate((baseUrl) => {
      const results = [], s = new Set();

      function addLink(href, text) {
        try {
          const u = new URL(href, baseUrl); u.hash = '';
          const h = u.href;
          if (!s.has(h)) {
            s.add(h);
            results.push({ href: h, text: (text || '').trim().slice(0, 200), hostname: u.hostname, path: u.pathname });
          }
        } catch {}
      }

      // Standard <a href> links
      document.querySelectorAll('a[href]').forEach(a => addLink(a.href, a.textContent));

      // Shadow DOM traversal
      function walkShadow(root) {
        root.querySelectorAll('a[href]').forEach(a => addLink(a.href, a.textContent));
        root.querySelectorAll('*').forEach(el => {
          if (el.shadowRoot) walkShadow(el.shadowRoot);
        });
      }
      document.querySelectorAll('*').forEach(el => {
        if (el.shadowRoot) walkShadow(el.shadowRoot);
      });

      // Links from onclick handlers and data-href
      document.querySelectorAll('[data-href]').forEach(el => addLink(el.getAttribute('data-href'), ''));
      document.querySelectorAll('[data-url]').forEach(el => addLink(el.getAttribute('data-url'), ''));
      document.querySelectorAll('[href]').forEach(el => {
        const h = el.getAttribute('href');
        if (h && (h.startsWith('http://') || h.startsWith('https://') || h.startsWith('/')))
          addLink(h, el.textContent);
      });

      return results;
    }, baseUrl);

    for (const l of extracted) {
      if (!seen.has(l.href)) {
        seen.add(l.href);
        links.push(l);
      }
    }
  } catch (e) { console.log(`    [WARN] Link extraction error: ${e.message.slice(0,100)}`); }

  return links;
}

async function crawlPage(page, url) {
  const fp = fingerprint(url);
  const pageDir = path.join(PAGES_DIR, fp);

  // Skip if already crawled (page.html exists and > 0 bytes)
  if (fs.existsSync(path.join(pageDir, 'page.html'))) {
    const stat = fs.statSync(path.join(pageDir, 'page.html'));
    if (stat.size > 100) {
      // Still need to extract links if links.json is missing or empty
      if (!fs.existsSync(path.join(pageDir, 'links.json')) || fs.statSync(path.join(pageDir, 'links.json')).size < 50) {
        // Will re-crawl below
      } else {
        return null; // Already complete
      }
    }
  }

  fs.mkdirSync(pageDir, { recursive: true });

  let html = '', title = '';
  try {
    await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
  } catch {
    try {
      await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 15000 });
    } catch (e) {
      console.log(`    [FAIL] ${url} — ${e.message.slice(0,80)}`);
      return null;
    }
  }
  await page.waitForTimeout(800);

  try { html = await page.content(); } catch {}
  try { title = await page.title(); } catch {}
  const byteLength = Buffer.byteLength(html, 'utf8');

  // Skip tiny responses (likely error pages or redirects)
  if (byteLength < 500) {
    console.log(`    [SKIP] ${url} — only ${byteLength}b (likely error/redirect)`);
    fs.writeFileSync(path.join(pageDir, 'page.html'), html);
    fs.writeFileSync(path.join(pageDir, 'links.json'), JSON.stringify({ total: 0, internal: 0, unimelb: 0, external: 0, links: [], _skipped: 'tiny-response' }, null, 2));
    fs.writeFileSync(path.join(pageDir, 'meta.json'), JSON.stringify({ url, fingerprint: fp, title, byteLength, linkCount: 0, crawledAt: new Date().toISOString(), skipped: true }, null, 2));
    return { url, title, byteLength, internalLinks: [], linkCount: 0 };
  }

  // Deep link extraction (shadow DOM, data-href, etc.)
  const allLinks = await extractLinksDeep(page, url);

  const uniqueLinks = [];
  const seenUrls = new Set();
  for (const l of allLinks) {
    if (!seenUrls.has(l.href) && !shouldSkip(l.href)) {
      seenUrls.add(l.href);
      l.category = categorizeUrl(l.href);
      uniqueLinks.push(l);
    }
  }

  // Write page artifacts
  fs.writeFileSync(path.join(pageDir, 'page.html'), html);
  fs.writeFileSync(path.join(pageDir, 'links.json'), JSON.stringify({
    total: uniqueLinks.length,
    internal: uniqueLinks.filter(l => l.category === 'internal').length,
    unimelb: uniqueLinks.filter(l => l.category === 'unimelb').length,
    external: uniqueLinks.filter(l => l.category === 'external').length,
    links: uniqueLinks,
  }, null, 2));
  fs.writeFileSync(path.join(pageDir, 'meta.json'), JSON.stringify({
    url, fingerprint: fp, title, byteLength, linkCount: uniqueLinks.length, crawledAt: new Date().toISOString(),
  }, null, 2));

  const internalLinks = uniqueLinks.filter(l => l.category === 'internal').map(l => l.href);
  console.log(`    [SAVED] ${byteLength}b HTML, ${uniqueLinks.length} links (${internalLinks.length} internal)`);
  return { url, title, byteLength, linkCount: uniqueLinks.length, internalLinks };
}

async function main() {
  console.log(`\n${'='.repeat(60)}`);
  console.log(`RESUMABLE FULL CRAWL: ${DOMAIN}`);
  console.log(`Output: ${OUT_ROOT}`);
  console.log(`${'='.repeat(60)}`);

  fs.mkdirSync(PAGES_DIR, { recursive: true });

  const { visited, frontier: savedFrontier, crawledCount: baseCount } = loadState();

  // Use launchPersistentContext with the user's Chrome profile to bypass Cloudflare
  const userDataDir = path.join(process.env.HOME, '.hermes', 'chrome-profile');
  let context;
  let browser;  // for fallback only
  try {
    context = await chromium.launchPersistentContext(userDataDir, {
      channel: 'chrome',
      headless: false,
      viewport: { width: 1440, height: 900 },
    });
    console.log('Launched Chrome with user profile');
  } catch (e) {
    console.log(`launchPersistentContext failed: ${e.message.slice(0, 120)}`);
    console.log('Falling back to headless Chromium...');
    browser = await chromium.launch({ headless: true });
    context = browser;  // context = browser (API compatibility)
  }

  const page = await context.newPage();

  // Verify homepage loads
  try {
    await page.goto(`${BASE}/`, { waitUntil: 'domcontentloaded', timeout: 15000 });
    console.log(`Homepage OK: "${await page.title()}"`);
  } catch (e) {
    console.log(`CANNOT LOAD homepage: ${e.message.slice(0, 100)}`);
    process.exit(1);
  }

  // Re-extract homepage for any new JS links
  let frontier;
  if (savedFrontier.length > 0) {
    frontier = savedFrontier.filter(u => !visited.has(u));
    console.log(`Resuming with ${frontier.length} frontier URLs from checkpoint`);
  } else {
    // Seed with homepage — but discover links afresh in case new pages exist
    const homeLinks = await extractLinksDeep(page, `${BASE}/`);
    const newInternal = homeLinks
      .filter(l => categorizeUrl(l.href) === 'internal' && !shouldSkip(l.href))
      .map(l => l.href);
    frontier = newInternal.filter(u => !visited.has(u));
    console.log(`Homepage re-scanned: ${newInternal.length} internal links, ${frontier.length} new (not in ${visited.size} visited)`);
  }

  if (frontier.length === 0) {
    console.log('No new pages to crawl — coverage is complete!');
    await page.close();
    if (browser) await browser.close(); else await context.close();
    process.exit(0);
  }

  console.log(`Starting crawl with ${frontier.length} URLs in frontier, ${visited.size} already visited`);
  let count = 0;
  let newPageCount = 0;

  while (frontier.length > 0 && count < MAX_PAGES) {
    const url = frontier.shift();
    if (visited.has(url)) continue;
    visited.add(url);

    const result = await crawlPage(page, url);
    count++;

    if (result && result.internalLinks && result.internalLinks.length > 0) {
      newPageCount++;
      const newLinks = result.internalLinks.filter(l => !visited.has(l) && !frontier.includes(l));
      if (newLinks.length > 0) {
        frontier.push(...newLinks);
        console.log(`  +${newLinks.length} new frontier URLs (total frontier: ${frontier.length})`);
      }
    }

    // Checkpoint every N pages
    if (count % CHECKPOINT_INTERVAL === 0) {
      saveCheckpoint(visited, frontier, baseCount + newPageCount);
      console.log(`[CHECKPOINT] ${count} pages processed this run, ${visited.size} total visited, ${frontier.length} in frontier`);
    }

    await page.waitForTimeout(300);
  }

  // Final save
  saveCheckpoint(visited, frontier, baseCount + newPageCount);

  // Build final index
  const allPages = [];
  for (const url of visited) {
    const fp = fingerprint(url);
    const metaPath = path.join(PAGES_DIR, fp, 'meta.json');
    if (fs.existsSync(metaPath)) {
      try {
        const meta = JSON.parse(fs.readFileSync(metaPath, 'utf8'));
        allPages.push({ url, title: meta.title || '', byteLength: meta.byteLength || 0, linkCount: meta.linkCount || 0, fingerprint: fp });
      } catch {}
    } else {
      allPages.push({ url, title: '', byteLength: 0, linkCount: 0, fingerprint: fp });
    }
  }

  fs.writeFileSync(INDEX_FILE, JSON.stringify({
    domain: DOMAIN,
    pagesCrawled: allPages.length,
    urlsVisited: visited.size,
    frontierRemaining: frontier.length,
    pages: allPages,
    frontier,
    lastCrawledAt: new Date().toISOString(),
  }, null, 2));

  await page.close();
  if (browser) {
    await browser.close();
  } else {
    await context.close();
  }

  console.log(`\n${'='.repeat(60)}`);
  console.log(`DONE: ${allPages.length} total pages (${newPageCount} new this run)`);
  console.log(`Frontier remaining: ${frontier.length}`);
  console.log(`Index: ${INDEX_FILE}`);
  console.log(`${'='.repeat(60)}`);
}

main().catch(e => {
  console.error('FATAL:', e.message);
  process.exit(1);
});
