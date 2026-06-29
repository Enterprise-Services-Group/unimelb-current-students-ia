#!/usr/bin/env node
// Interactive auth crawl — pauses for manual authentication, then crawls logged-in pages
// Usage: node crawl_auth.js

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const OUT_BASE = path.join(__dirname, '..', 'crawl', 'auth-core');
const DELAY_MS = 500; // polite crawl delay

// Hosts to crawl — ordered by SSO session sharing
const HOSTS = [
  // Tier 1: main SSO — auth once here should carry to most others
  { url: 'https://my.unimelb.edu.au/', name: 'my-unimelb', label: 'my.unimelb (SIS)' },
  
  // Tier 2: services that share the main SSO
  { url: 'https://lms.unimelb.edu.au/', name: 'lms', label: 'LMS / Canvas (resume)' },
  { url: 'https://canvas.lms.unimelb.edu.au/', name: 'canvas', label: 'Canvas Direct' },
  
  // Tier 3: forms and apps
  { url: 'https://forms.your.unimelb.edu.au/', name: 'forms-your', label: 'Forms (FormAssembly)' },
  { url: 'https://mycounselling.app.unimelb.edu.au/', name: 'mycounselling', label: 'Counselling (CAPS)' },
  { url: 'https://tes.app.unimelb.edu.au/', name: 'tes', label: 'Thesis Exam System' },
  
  // Tier 4: specialised
  { url: 'https://intlstudaccept.unimelb.edu.au/', name: 'intlstudaccept', label: 'Intl Acceptance' },
  { url: 'https://course-planner.unimelb.edu.au/', name: 'course-planner', label: 'Course Planner' },
  { url: 'https://ecommerce.unimelb.edu.au/', name: 'ecommerce-auth', label: 'Ecommerce (logged in)' },
];

const MAX_PAGES_PER_HOST = 60;
const AUTH_TIMEOUT_MS = 300000; // 5 min per auth

function fingerprint(url) {
  return crypto.createHash('sha1').update(url).digest('hex').slice(0, 16);
}

function shouldSkip(url) {
  return /\.(pdf|docx?|xlsx?|pptx?|zip|jpg|jpeg|png|gif|svg|mp4|mp3|webm|ico|xml|css|js|woff2?)(\?.*)?$/i.test(url)
    || /mailto:|javascript:|^#|tel:/i.test(url)
    || /\/_nocache/i.test(url)
    || /logout/i.test(url);
}

async function waitForAuth(page, host) {
  console.log(`\n⏳ Waiting for auth on ${host}...`);
  console.log('   (Browser window is open — please log in)');
  
  const start = Date.now();
  while (Date.now() - start < AUTH_TIMEOUT_MS) {
    await page.waitForTimeout(3000);
    const title = await page.title();
    const url = page.url();
    
    // Detect successful auth
    const notSignIn = !/sign in|login|log in|captcha|just a moment|403|404|error/i.test(title);
    const hasContent = title.length > 5;
    const notSSO = !url.includes('/sso/') && !url.includes('/login') && !url.includes('/auth');
    
    if (notSignIn && hasContent && notSSO) {
      console.log(`   ✅ Authenticated! Title: "${title.slice(0,80)}"`);
      return true;
    }
    
    if (Date.now() % 15000 < 3000) {
      console.log(`   ... waiting (${Math.round((Date.now() - start)/1000)}s) — current: "${title.slice(0,60)}"`);
    }
  }
  console.log('   ⚠ Auth timeout — continuing without auth');
  return false;
}

async function crawlHost(browser, context, hostConfig) {
  const { url, name, label } = hostConfig;
  const outDir = path.join(OUT_BASE, name);
  
  // Skip if already crawled
  const idxPath = path.join(outDir, 'index.json');
  if (fs.existsSync(idxPath)) {
    const idx = JSON.parse(fs.readFileSync(idxPath, 'utf8'));
    if (idx.pagesCrawled > 0) {
      console.log(`\n⏭ Skipping ${label} — already has ${idx.pagesCrawled} pages`);
      return { host: name, pages: idx.pagesCrawled, status: 'skipped' };
    }
  }
  
  fs.mkdirSync(path.join(outDir, 'pages'), { recursive: true });
  
  console.log(`\n${'='.repeat(60)}`);
  console.log(`🔐 ${label}: ${url}`);
  console.log('='.repeat(60));
  
  const page = await context.newPage();
  
  try {
    await page.goto(url, { timeout: 30000, waitUntil: 'domcontentloaded' });
  } catch(e) {
    console.log(`   ⚠ Navigation error: ${e.message.slice(0,80)}`);
    await page.close();
    return { host: name, pages: 0, status: 'nav_error' };
  }
  
  const title = await page.title();
  console.log(`   Initial: "${title.slice(0,80)}"`);
  
  // Check if already authenticated
  const needsAuth = /sign in|login|log in|403|404|error|just a moment/i.test(title) || title.length < 5;
  
  if (needsAuth) {
    console.log('   🔑 Authentication required');
    const authed = await waitForAuth(page, label);
    if (!authed) {
      // Save whatever page we have
      const html = await page.content();
      const fp = fingerprint(url);
      const pageDir = path.join(outDir, 'pages', fp);
      fs.mkdirSync(pageDir, { recursive: true });
      fs.writeFileSync(path.join(pageDir, 'page.html'), html);
      fs.writeFileSync(path.join(pageDir, 'meta.json'), JSON.stringify({
        url, title: await page.title(), crawledAt: new Date().toISOString(), auth: 'failed'
      }));
      await page.close();
      return { host: name, pages: 1, status: 'auth_failed' };
    }
  }
  
  // Crawl — BFS from the authenticated page
  const visited = new Set();
  const frontier = [page.url()];
  const index = [];
  let crawled = 0;
  
  console.log(`   🔍 Crawling (max ${MAX_PAGES_PER_HOST} pages)...`);
  
  while (frontier.length > 0 && crawled < MAX_PAGES_PER_HOST) {
    const currentUrl = frontier.shift();
    const normalized = currentUrl.split('?')[0].replace(/\/$/, '');
    
    if (visited.has(normalized) || shouldSkip(currentUrl)) continue;
    visited.add(normalized);
    
    try {
      await page.goto(currentUrl, { timeout: 15000, waitUntil: 'domcontentloaded' });
      await page.waitForTimeout(DELAY_MS);
    } catch(e) {
      continue;
    }
    
    const pageTitle = await page.title();
    let html = '';
    // Retry page.content — it can fail during navigation
    for (let retry = 0; retry < 5; retry++) {
      try {
        html = await page.content();
        break;
      } catch(e) {
        if (retry < 4) { await page.waitForTimeout(1000); continue; }
        console.log(`\n   ⚠ Skipping ${currentUrl.slice(0,60)} — content unavailable`);
        continue; // skip to next frontier item
      }
    }
    if (!html) continue;
    
    // Save page
    const fp = fingerprint(currentUrl);
    const pageDir = path.join(outDir, 'pages', fp);
    fs.mkdirSync(pageDir, { recursive: true });
    fs.writeFileSync(path.join(pageDir, 'page.html'), html);
    fs.writeFileSync(path.join(pageDir, 'meta.json'), JSON.stringify({
      url: currentUrl, title: pageTitle, byteLength: html.length,
      crawledAt: new Date().toISOString()
    }));
    
    index.push({ url: currentUrl, title: pageTitle, byteLength: html.length, fingerprint: fp });
    crawled++;
    
    // Extract internal links
    const links = await page.evaluate(() => {
      return Array.from(document.querySelectorAll('a[href]')).map(a => ({
        href: a.href,
        text: (a.textContent || '').trim().slice(0, 100)
      }));
    });
    
    const internalLinks = new Set();
    for (const link of links) {
      try {
        const u = new URL(link.href, currentUrl);
        if (u.hostname === new URL(currentUrl).hostname || u.hostname.endsWith('.unimelb.edu.au')) {
          const norm = u.href.split('?')[0].replace(/\/$/, '');
          if (!visited.has(norm) && !shouldSkip(u.href)) {
            internalLinks.add(u.href);
          }
        }
      } catch(e) {}
    }
    
    for (const link of internalLinks) {
      if (!frontier.includes(link)) frontier.push(link);
    }
    
    if (crawled % 10 === 0) {
      process.stdout.write(`\r   ${crawled} pages, ${frontier.length} in queue`);
    }
  }
  
  console.log(`\r   ✅ Crawled ${crawled} pages, ${frontier.length} remaining in queue`);
  
  // Save index
  fs.writeFileSync(path.join(outDir, 'index.json'), JSON.stringify({
    host: name, url, pagesCrawled: crawled, pages: index, crawledAt: new Date().toISOString()
  }, null, 2));
  
  await page.close();
  return { host: name, pages: crawled, status: 'ok' };
}

(async () => {
  console.log('🔐 Interactive Auth Crawl');
  console.log(`   Output: ${OUT_BASE}`);
  console.log(`   Hosts: ${HOSTS.length}`);
  console.log(`   Auth timeout: ${AUTH_TIMEOUT_MS/1000}s per host`);
  console.log(`   Max pages per host: ${MAX_PAGES_PER_HOST}`);
  console.log('\n📌 A browser window will open. Please authenticate when prompted.');
  console.log('   Your SSO session should carry across most hosts.\n');
  
  const browser = await chromium.launch({ 
    headless: false,
    args: ['--no-sandbox']
  });
  const context = await browser.newContext({
    viewport: { width: 1280, height: 900 }
  });
  
  const results = [];
  
  for (const host of HOSTS) {
    const result = await crawlHost(browser, context, host);
    results.push(result);
  }
  
  console.log(`\n${'='.repeat(60)}`);
  console.log('📊 Results:');
  for (const r of results) {
    const icon = r.status === 'ok' ? '✅' : r.status === 'auth_failed' ? '⚠️' : '❌';
    console.log(`   ${icon} ${r.host.padEnd(25)} ${r.pages} pages (${r.status})`);
  }
  
  // Write summary
  fs.writeFileSync(path.join(OUT_BASE, 'summary.json'), JSON.stringify(results, null, 2));
  
  const totalPages = results.reduce((s, r) => s + r.pages, 0);
  console.log(`\n   Total: ${totalPages} pages across ${results.length} hosts`);
  
  await browser.close();
  console.log('Done.');
})();
