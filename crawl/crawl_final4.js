#!/usr/bin/env node
// Final 4 Cloudflare domains — sequential headful Chrome crawl
const { execFileSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const CRAWLER = path.join(__dirname, 'crawl_domain.js');
const OUT_BASE = path.join(__dirname, '..');

const DOMAINS = [
  { domain: 'library.unimelb.edu.au', max: 1000 },
  { domain: 'studentit.unimelb.edu.au', max: 800 },
  { domain: 'orientation.unimelb.edu.au', max: 300 },
  { domain: 'breadth.unimelb.edu.au', max: 300 },
];

const logFile = path.join(OUT_BASE, 'crawl', 'batch_final4.log');
fs.writeFileSync(logFile, `Final 4 started: ${new Date().toISOString()}\n`);

console.log(`=== Final 4 Cloudflare domains (sequential headful) ===\n`);

let ok = 0, failed = 0;
const results = [];

for (let i = 0; i < DOMAINS.length; i++) {
  const { domain, max } = DOMAINS[i];
  const label = `[${i + 1}/${DOMAINS.length}]`;
  const outDir = path.join(OUT_BASE, 'crawl', domain.replace(/\./g, '-'));
  
  console.log(`${label} ${domain} (max ${max})`);
  fs.appendFileSync(logFile, `${new Date().toISOString()} START ${domain}\n`);
  
  const start = Date.now();
  try {
    execFileSync('node', [CRAWLER, domain, outDir, String(max)], {
      cwd: __dirname,
      stdio: 'inherit',
      timeout: 7200000,
    });
    const elapsed = Math.round((Date.now() - start) / 1000);
    const pagesDir = path.join(outDir, 'pages');
    const pageCount = fs.existsSync(pagesDir) ? fs.readdirSync(pagesDir).length : 0;
    ok++;
    console.log(`  DONE: ${pageCount} pages, ${elapsed}s\n`);
    fs.appendFileSync(logFile, `${new Date().toISOString()} DONE ${domain} (${pageCount}p, ${elapsed}s)\n`);
    results.push({ domain, pages: pageCount, elapsed, status: 'ok' });
  } catch (err) {
    const elapsed = Math.round((Date.now() - start) / 1000);
    failed++;
    console.error(`  FAILED: ${elapsed}s\n`);
    fs.appendFileSync(logFile, `${new Date().toISOString()} FAILED ${domain}\n`);
    results.push({ domain, elapsed, status: 'failed' });
  }
}

console.log(`\n=== Complete: ${ok} ok, ${failed} failed ===`);
fs.appendFileSync(logFile, `\nComplete: ${new Date().toISOString()} - ${ok} ok, ${failed} failed\n`);
fs.writeFileSync(path.join(OUT_BASE, 'crawl', 'batch_final4_summary.json'), JSON.stringify(results, null, 2));
process.exit(failed > 0 ? 1 : 0);
