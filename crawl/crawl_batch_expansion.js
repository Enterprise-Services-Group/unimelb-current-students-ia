#!/usr/bin/env node
// Batch crawl for tier 1-3 expansion domains
// Usage: node crawl_batch_expansion.js [tier] [max-pages-per-domain]

const { execFileSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const CRAWLER = path.join(__dirname, 'crawl_domain.js');
const OUT_BASE = path.join(__dirname, '..');

const DOMAINS = {
  tier1: [
    { domain: 'gradresearch.unimelb.edu.au', max: 2000 },
    { domain: 'ask.unimelb.edu.au', max: 1500 },
    { domain: 'murrupbarak.unimelb.edu.au', max: 1000 },
    { domain: 'safercommunity.unimelb.edu.au', max: 500 },
    { domain: 'studyos.students.unimelb.edu.au', max: 500 },
  ],
  tier2: [
    { domain: 'library.unimelb.edu.au', max: 1000 },
    { domain: 'umsu.unimelb.edu.au', max: 800 },
    { domain: 'studentit.unimelb.edu.au', max: 800 },
    { domain: 'gsa.unimelb.edu.au', max: 600 },
    { domain: 'my.unimelb.edu.au', max: 200 },    // auth-gated, splash only
    { domain: 'lms.unimelb.edu.au', max: 200 },    // auth-gated, splash only
    { domain: 'canvas.lms.unimelb.edu.au', max: 200 }, // auth-gated, splash only
  ],
  tier3: [
    { domain: 'online.unimelb.edu.au', max: 500 },
    { domain: 'sport.unimelb.edu.au', max: 500 },
    { domain: 'orientation.unimelb.edu.au', max: 300 },
    { domain: 'exams.unimelb.edu.au', max: 200 },
    { domain: 'breadth.unimelb.edu.au', max: 300 },
  ]
};

const tier = process.argv[2] || 'tier1';
const perDomainMax = parseInt(process.argv[3] || '0', 10);
const domains = DOMAINS[tier];

if (!domains) {
  console.error(`Unknown tier: ${tier}. Use tier1, tier2, or tier3`);
  process.exit(1);
}

console.log(`=== Batch crawl: ${tier} (${domains.length} domains) ===`);
console.log(`Output base: ${OUT_BASE}/crawl/`);
console.log('');

const batchLog = path.join(OUT_BASE, 'crawl', `batch_expansion_${tier}.log`);
fs.writeFileSync(batchLog, `Batch crawl started: ${new Date().toISOString()}\n`);

let completed = 0;
let failed = 0;

async function crawlOne(domainConfig, index) {
  const { domain, max } = domainConfig;
  const effectiveMax = perDomainMax > 0 ? perDomainMax : max;
  const label = `[${index + 1}/${domains.length}]`;
  
  console.log(`${label} Starting: ${domain} (max ${effectiveMax} pages)`);
  fs.appendFileSync(batchLog, `${new Date().toISOString()} ${label} START ${domain}\n`);
  
  const startTime = Date.now();
  
  try {
    const result = execFileSync(
      'node', [CRAWLER, domain, path.join(OUT_BASE, 'crawl', domain.replace(/\./g, '-')), String(effectiveMax)],
      { 
        cwd: __dirname,
        stdio: 'pipe',
        timeout: 7200000, // 2 hour timeout per domain
        maxBuffer: 10 * 1024 * 1024,
      }
    );
    
    const elapsed = Math.round((Date.now() - startTime) / 1000);
    completed++;
    console.log(`${label} DONE: ${domain} (${elapsed}s, ${completed}/${domains.length} complete)`);
    fs.appendFileSync(batchLog, `${new Date().toISOString()} ${label} DONE ${domain} (${elapsed}s)\n`);
    return { domain, status: 'ok', elapsed };
  } catch (err) {
    const elapsed = Math.round((Date.now() - startTime) / 1000);
    failed++;
    console.error(`${label} FAILED: ${domain} (${elapsed}s) - ${err.message?.slice(0, 200)}`);
    fs.appendFileSync(batchLog, `${new Date().toISOString()} ${label} FAILED ${domain} (${elapsed}s) - ${err.message}\n`);
    return { domain, status: 'failed', elapsed, error: err.message?.slice(0, 500) };
  }
}

(async () => {
  const results = [];
  for (let i = 0; i < domains.length; i++) {
    const r = await crawlOne(domains[i], i);
    results.push(r);
  }
  
  console.log(`\n=== Batch complete: ${completed} ok, ${failed} failed ===`);
  fs.appendFileSync(batchLog, `\nBatch complete: ${new Date().toISOString()} - ${completed} ok, ${failed} failed\n`);
  
  // Write summary
  const summary = {
    tier,
    started: new Date().toISOString(),
    results
  };
  fs.writeFileSync(
    path.join(OUT_BASE, 'crawl', `batch_expansion_${tier}_summary.json`),
    JSON.stringify(summary, null, 2)
  );
  
  process.exit(failed > 0 ? 1 : 0);
})();
