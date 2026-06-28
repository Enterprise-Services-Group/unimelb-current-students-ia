#!/usr/bin/env node
// Generic full-domain resumable crawler with full HTML per page.
// Usage: node crawl_domain.js <domain> [output-dir] [max-pages]
//   node crawl_domain.js eng.unimelb.edu.au
//   node crawl_domain.js study.unimelb.edu.au ~/path/to/output 2000

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { URL } = require('url');

const DOMAIN = process.argv[2];
if (!DOMAIN) { console.error('Usage: node crawl_domain.js <domain> [output-dir] [max-pages] [--path-prefix=/path]'); process.exit(1); }

const BASE = `https://${DOMAIN}`;
// Parse --path-prefix from args
let PATH_PREFIX = '';
for (const arg of process.argv) {
  if (arg.startsWith('--path-prefix=')) {
    PATH_PREFIX = arg.split('=')[1];
    // Ensure leading /, no trailing /
    if (!PATH_PREFIX.startsWith('/')) PATH_PREFIX = '/' + PATH_PREFIX;
    if (PATH_PREFIX.endsWith('/') && PATH_PREFIX.length > 1) PATH_PREFIX = PATH_PREFIX.slice(0, -1);
  }
}
const START_URL = PATH_PREFIX ? `${BASE}${PATH_PREFIX}` : `${BASE}/`;
const OUT_ROOT = process.argv[3] || path.join(process.env.HOME, 'Documents/Claude/projects/unimelb-current-students-ia/crawl',
  DOMAIN.replace(/\./g, '-') + (PATH_PREFIX ? '-' + PATH_PREFIX.replace(/\//g, '-').replace(/^-+|-+$/g, '') : ''));
const PAGES_DIR = path.join(OUT_ROOT, 'pages');
const CHECKPOINT_FILE = path.join(OUT_ROOT, 'checkpoint.json');
const INDEX_FILE = path.join(OUT_ROOT, 'index.json');
const CHECKPOINT_INTERVAL = 50;
const MAX_PAGES = parseInt(process.argv[4] || '3000', 10);
const DELAY_MS = 300;

function fingerprint(url) {
  return crypto.createHash('sha1').update(url).digest('hex').slice(0, 16);
}

function shouldSkip(url) {
  if (!url) return true;
  return /\.(pdf|docx?|xlsx?|pptx?|zip|tar|gz|jpg|jpeg|png|gif|svg|mp4|mp3|webm|webp|ico|xml|rss|css|js|woff2?|ttf|eot)(\?.*)?$/i.test(url)
    || /mailto:|^javascript:|^#|tel:|login/i.test(url)
    || /\/_nocache/i.test(url)
    || /[?&]f\./i.test(url);
}

function categorizeUrl(url) {
  try {
    const u = new URL(url);
    if (u.hostname === DOMAIN) return 'internal';
    if (u.hostname.endsWith('.unimelb.edu.au')) return 'unimelb';
    return 'external';
  } catch { return 'unknown'; }
}

function shouldFollow(url) {
  if (categorizeUrl(url) !== 'internal') return false;
  if (!PATH_PREFIX) return true;
  // With path-prefix, only follow URLs under that path
  try {
    const u = new URL(url);
    return u.pathname.startsWith(PATH_PREFIX + '/') || u.pathname === PATH_PREFIX || u.pathname === PATH_PREFIX + '/';
  } catch { return false; }
}

// Priority crawling: substantive content first, news last (gets capped first)
function isNewsUrl(url) {
  try {
    const u = new URL(url);
    const path = u.pathname.toLowerCase();
    return /\/(news|news-and-events|articles|blog|events|whats-on|announcements|media-releases|latest|updates)\b/i.test(path)
        || /\/(news|events|blog|articles)\//i.test(path)
        || /\/news\//i.test(path);
  } catch { return false; }
}

// Two-tier frontier: high priority (content), low priority (news)
function getNextUrl(frontier) {
  if (frontier.high.length > 0) return frontier.high.shift();
  if (frontier.low.length > 0) return frontier.low.shift();
  return undefined;
}

function addToFrontier(frontier, urls) {
  for (const u of urls) {
    if (isNewsUrl(u)) {
      frontier.low.push(u);
    } else {
      frontier.high.push(u);
    }
  }
}

function frontierLength(frontier) {
  return frontier.high.length + frontier.low.length;
}

function flattenFrontier(frontier) {
  return [...frontier.high, ...frontier.low];
}

function loadState() {
  const visited = new Set();
  let frontier = { high: [], low: [] };

  if (fs.existsSync(INDEX_FILE)) {
    try {
      const idx = JSON.parse(fs.readFileSync(INDEX_FILE, 'utf8'));
      if (idx.pages) {
        for (const p of idx.pages) {
          if (p.url) visited.add(p.url);
        }
        console.log(`Loaded ${visited.size} visited from index.json`);
      }
      // Load frontier in either format, filtering out skip URLs
      if (idx.frontier) {
        if (Array.isArray(idx.frontier)) {
          addToFrontier(frontier, idx.frontier.filter(u => !visited.has(u) && !shouldSkip(u)));
        } else if (idx.frontier.high || idx.frontier.low) {
          if (idx.frontier.high) addToFrontier(frontier, idx.frontier.high.filter(u => !visited.has(u) && !shouldSkip(u)));
          if (idx.frontier.low) addToFrontier(frontier, idx.frontier.low.filter(u => !visited.has(u) && !shouldSkip(u)));
        }
        const skipped = (Array.isArray(idx.frontier) ? idx.frontier.length : (idx.frontier.high?.length || 0) + (idx.frontier.low?.length || 0)) - frontierLength(frontier);
        console.log(`Loaded frontier from index: high=${frontier.high.length} low=${frontier.low.length} (${skipped} skipped)`);
      }
    } catch (e) { console.log(`Index parse warning: ${e.message.slice(0,80)}`); }
  }

  if (fs.existsSync(CHECKPOINT_FILE)) {
    try {
      const ck = JSON.parse(fs.readFileSync(CHECKPOINT_FILE, 'utf8'));
      if (ck.visited) {
        for (const u of ck.visited) visited.add(u);
        console.log(`Loaded ${ck.visited.length} extra visited from checkpoint`);
      }
      if (ck.frontier) {
        if (Array.isArray(ck.frontier)) {
          // Old flat format — re-sort into priority queues, filter skips
          const newUrls = ck.frontier.filter(u => !visited.has(u) && !shouldSkip(u));
          if (frontier.high.length === 0 && frontier.low.length === 0) {
            addToFrontier(frontier, newUrls);
          }
        } else if (ck.frontier.high || ck.frontier.low) {
          // New format
          if (ck.frontier.high && frontier.high.length === 0) addToFrontier(frontier, ck.frontier.high.filter(u => !visited.has(u) && !shouldSkip(u)));
          if (ck.frontier.low && frontier.low.length === 0) addToFrontier(frontier, ck.frontier.low.filter(u => !visited.has(u) && !shouldSkip(u)));
        }
        const skipped = (Array.isArray(ck.frontier) ? ck.frontier.length : (ck.frontier.high?.length || 0) + (ck.frontier.low?.length || 0)) - frontierLength(frontier);
        console.log(`Loaded frontier from checkpoint: high=${frontier.high.length} low=${frontier.low.length} (${skipped} skipped)`);
      }
    } catch (e) { console.log(`Checkpoint parse warning: ${e.message.slice(0,80)}`); }
  }

  return { visited, frontier };
}

function saveCheckpoint(visited, frontier) {
  fs.writeFileSync(CHECKPOINT_FILE, JSON.stringify({
    visited: [...visited],
    frontier: { high: frontier.high, low: frontier.low },
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
          const u = new URL(href, baseUrl); u.hash = ''; const h = u.href;
          if (!s.has(h)) { s.add(h); results.push({ href: h, text: (text||'').trim().slice(0,200), hostname: u.hostname, path: u.pathname }); }
        } catch {}
      }
      document.querySelectorAll('a[href]').forEach(a => addLink(a.href, a.textContent));
      // Shadow DOM
      function walkShadow(root) {
        root.querySelectorAll('a[href]').forEach(a => addLink(a.href, a.textContent));
        root.querySelectorAll('*').forEach(el => { if (el.shadowRoot) walkShadow(el.shadowRoot); });
      }
      document.querySelectorAll('*').forEach(el => { if (el.shadowRoot) walkShadow(el.shadowRoot); });
      // data- attributes
      document.querySelectorAll('[data-href]').forEach(el => addLink(el.getAttribute('data-href'), ''));
      document.querySelectorAll('[data-url]').forEach(el => addLink(el.getAttribute('data-url'), ''));
      return results;
    }, baseUrl);
    for (const l of extracted) {
      if (!seen.has(l.href)) { seen.add(l.href); links.push(l); }
    }
  } catch (e) { /* silently skip */ }
  return links;
}

async function crawlPage(page, url) {
  const fp = fingerprint(url);
  const pageDir = path.join(PAGES_DIR, fp);

  // Skip if already fully crawled
  if (fs.existsSync(path.join(pageDir, 'page.html'))) {
    const stat = fs.statSync(path.join(pageDir, 'page.html'));
    if (stat.size > 100 && fs.existsSync(path.join(pageDir, 'links.json')) && fs.statSync(path.join(pageDir, 'links.json')).size > 40) {
      // Already complete — still re-read links for frontier expansion
      try {
        const lj = JSON.parse(fs.readFileSync(path.join(pageDir, 'links.json'), 'utf8'));
        if (lj.links) {
          const internal = lj.links.filter(l => l.category === 'internal').map(l => l.href);
          return { url, title: '', byteLength: stat.size, linkCount: lj.total || 0, internalLinks: internal, cached: true };
        }
      } catch {}
    }
  }

  fs.mkdirSync(pageDir, { recursive: true });

  let html = '', title = '';
  try {
    await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
  } catch {
    try { await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 15000 }); } catch { return null; }
  }
  await page.waitForTimeout(800);

  try { html = await page.content(); } catch {}
  try { title = await page.title(); } catch {}
  const byteLength = Buffer.byteLength(html, 'utf8');

  if (byteLength < 500) {
    fs.writeFileSync(path.join(pageDir, 'page.html'), html);
    fs.writeFileSync(path.join(pageDir, 'links.json'), JSON.stringify({ total: 0, internal: 0, unimelb: 0, external: 0, links: [], _skipped: 'tiny-response' }, null, 2));
    fs.writeFileSync(path.join(pageDir, 'meta.json'), JSON.stringify({ url, fingerprint: fp, title, byteLength, linkCount: 0, crawledAt: new Date().toISOString(), skipped: true }, null, 2));
    return { url, title, byteLength, internalLinks: [], linkCount: 0 };
  }

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

  const internalLinks = uniqueLinks.filter(l => shouldFollow(l.href)).map(l => l.href);
  return { url, title, byteLength, linkCount: uniqueLinks.length, internalLinks };
}

function saveIndex(visited, frontier) {
  const allPages = [];
  for (const url of visited) {
    const fp = fingerprint(url);
    const metaPath = path.join(PAGES_DIR, fp, 'meta.json');
    if (fs.existsSync(metaPath)) {
      try {
        const meta = JSON.parse(fs.readFileSync(metaPath, 'utf8'));
        allPages.push({ url, title: meta.title || '', byteLength: meta.byteLength || 0, linkCount: meta.linkCount || 0, fingerprint: fp });
      } catch { allPages.push({ url, title: '', byteLength: 0, linkCount: 0, fingerprint: fp }); }
    } else {
      allPages.push({ url, title: '', byteLength: 0, linkCount: 0, fingerprint: fp });
    }
  }
  const flat = flattenFrontier(frontier);
  fs.writeFileSync(INDEX_FILE, JSON.stringify({
    domain: DOMAIN,
    pagesCrawled: allPages.length,
    urlsVisited: visited.size,
    frontierRemaining: frontierLength(frontier),
    frontierHigh: frontier.high.length,
    frontierLow: frontier.low.length,
    pages: allPages,
    frontier: flat,
    lastCrawledAt: new Date().toISOString(),
  }, null, 2));
  return allPages.length;
}

async function main() {
  const BAR = '='.repeat(60);
  const scope = PATH_PREFIX ? `${DOMAIN}${PATH_PREFIX}` : DOMAIN;
  console.log(`\n${BAR}\nCRAWL: ${scope}\nOutput: ${OUT_ROOT}\nMax: ${MAX_PAGES} pages\n${BAR}`);

  fs.mkdirSync(PAGES_DIR, { recursive: true });

  const { visited, frontier } = loadState();

  let context, browser;
  try {
    context = await chromium.launchPersistentContext(
      path.join(process.env.HOME, '.hermes', 'chrome-profile'),
      { channel: 'chrome', headless: false, viewport: { width: 1440, height: 900 } }
    );
    console.log('Chrome launched with profile');
  } catch (e) {
    console.log(`Chrome profile failed: ${e.message.slice(0,80)}`);
    browser = await chromium.launch({ headless: true });
    context = browser;
  }

  const page = await context.newPage();

  // Test start page
  let homeOk = false;
  try {
    await page.goto(START_URL, { waitUntil: 'domcontentloaded', timeout: 15000 });
    const t = await page.title();
    homeOk = !t.includes('Just a moment');
    console.log(`Start page (${START_URL}): "${t.slice(0,80)}" ${homeOk ? '✓' : '✗ (Cloudflare)'}`);
  } catch (e) {
    console.log(`Homepage FAIL: ${e.message.slice(0,80)}`);
  }

  if (!homeOk) {
    console.log('Cloudflare blocking — cannot crawl. Exiting.');
    await page.close();
    if (browser) await browser.close(); else await context.close();
    process.exit(2);
  }

  // Build frontier from saved state or seed from homepage
  if (frontierLength(frontier) > 0) {
    console.log(`Resuming: ${frontierLength(frontier)} frontier URLs (${frontier.high.length} content + ${frontier.low.length} news), ${visited.size} visited`);
  } else {
    const homeLinks = await extractLinksDeep(page, START_URL);
    const internal = homeLinks
      .filter(l => shouldFollow(l.href) && !shouldSkip(l.href))
      .map(l => l.href);
    const newUrls = internal.filter(u => !visited.has(u));
    addToFrontier(frontier, newUrls);
    console.log(`Homepage: ${internal.length} internal links, ${newUrls.length} new (${visited.size} already visited)`);
    console.log(`  Content: ${frontier.high.length}  |  News: ${frontier.low.length}`);
  }

  if (frontierLength(frontier) === 0) {
    console.log('No new pages — coverage complete!');
    await page.close();
    if (browser) await browser.close(); else await context.close();
    saveIndex(visited, frontier);
    process.exit(0);
  }

  console.log(`Crawling: ${frontierLength(frontier)} in frontier (${frontier.high.length} content + ${frontier.low.length} news), ${visited.size} visited`);
  let count = 0, newCount = 0;

  while (frontierLength(frontier) > 0 && count < MAX_PAGES) {
    const url = getNextUrl(frontier);
    if (!url) break;
    if (visited.has(url)) continue;
    if (shouldSkip(url)) { visited.add(url); count++; continue; }  // mark skip URLs as visited
    visited.add(url);

    const result = await crawlPage(page, url);
    count++;
    if (!result) continue;

    newCount++;
    const newLinks = result.internalLinks.filter(l => !visited.has(l) && !frontier.high.includes(l) && !frontier.low.includes(l));
    if (newLinks.length > 0) {
      addToFrontier(frontier, newLinks);
    }

    // Progress
    const short = url.replace(`https://${DOMAIN}`, '').slice(0, 50) || '/';
    const cached = result.cached ? ' [cached]' : '';
    const isNews = isNewsUrl(url) ? ' [news]' : '';
    console.log(`  [${count}/${visited.size} | q:${frontierLength(frontier)} h:${frontier.high.length} l:${frontier.low.length}] ${short} (${result.byteLength}b)${cached}${isNews}`);

    if (count % CHECKPOINT_INTERVAL === 0) {
      saveCheckpoint(visited, frontier);
      saveIndex(visited, frontier);
    }

    await page.waitForTimeout(DELAY_MS);
  }

  saveCheckpoint(visited, frontier);
  const total = saveIndex(visited, frontier);

  await page.close();
  if (browser) await browser.close(); else await context.close();

  const capped = count >= MAX_PAGES;
  console.log(`\n${BAR}`);
  console.log(`DONE: ${total} pages → ${OUT_ROOT}/`);
  console.log(`Frontier remaining: ${frontierLength(frontier)} (${frontier.high.length} content + ${frontier.low.length} news)${capped ? ' — CAPPED at ' + MAX_PAGES : ''}`);
  console.log(BAR);
}

main().catch(e => {
  console.error('FATAL:', e.message);
  // Try to save what we have
  try {
    const { visited, frontier } = loadState();
    saveIndex(visited, frontier || []);
  } catch {}
  process.exit(1);
});
