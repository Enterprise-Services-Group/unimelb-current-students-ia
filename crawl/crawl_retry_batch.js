#!/usr/bin/env node
// Retry failed/missing domains — sequential execution to avoid Chrome contention
const { execFileSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const CRAWLER = path.join(__dirname, 'crawl_domain.js');
const OUT_BASE = path.join(__dirname, '..');

const DOMAINS = [
  // Tier 1 remaining
  { domain: 'murrupbarak.unimelb.edu.au', max: 1000 },
  { domain: 'safercommunity.unimelb.edu.au', max: 500 },
  { domain: 'studyos.students.unimelb.edu.au', max: 500 },
  // Tier 2 remaining
  { domain: 'library.unimelb.edu.au', max: 1000 },
  { domain: 'studentit.unimelb.edu.au', max: 800 },
  { domain: 'gsa.unimelb.edu.au', max: 600 },
  // Tier 3 failed
  { domain: 'orientation.unimelb.edu.au', max: 300 },
  { domain: 'breadth.unimelb.edu.au', max: 300 },
  // Auth-gated — try splash pages only
  { domain: 'my.unimelb.edu.au', max: 50 },
  { domain: 'lms.unimelb.edu.au', max: 50 },
  { domain: 'canvas.lms.unimelb.edu.au', max: 50 },
];

const logFile = path.join(OUT_BASE, 'crawl', 'batch_retry.log');
fs.writeFileSync(logFile, `Retry batch started: ${new Date().toISOString()}\n`);

console.log(`=== Retry crawl: ${DOMAINS.length} domains (sequential) ===\n`);

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
    // Count pages
    const pagesDir = path.join(outDir, 'pages');
    const pageCount = fs.existsSync(pagesDir) ? fs.readdirSync(pagesDir).length : 0;
    ok++;
    console.log(`  DONE: ${pageCount} pages, ${elapsed}s\n`);
    fs.appendFileSync(logFile, `${new Date().toISOString()} DONE ${domain} (${pageCount} pages, ${elapsed}s)\n`);
    results.push({ domain, pages: pageCount, elapsed, status: 'ok' });
  } catch (err) {
    const elapsed = Math.round((Date.now() - start) / 1000);
    failed++;
    console.error(`  FAILED: ${elapsed}s - ${err.message?.slice(0, 200)}\n`);
    fs.appendFileSync(logFile, `${new Date().toISOString()} FAILED ${domain} (${elapsed}s) - ${err.message}\n`);
    results.push({ domain, elapsed, status: 'failed', error: err.message?.slice(0, 500) });
  }
}

console.log(`\n=== Retry complete: ${ok} ok, ${failed} failed ===`);
fs.appendFileSync(logFile, `\nRetry complete: ${new Date().toISOString()} - ${ok} ok, ${failed} failed\n`);
fs.writeFileSync(path.join(OUT_BASE, 'crawl', 'batch_retry_summary.json'), JSON.stringify(results, null, 2));
process.exit(failed > 0 ? 1 : 0);
