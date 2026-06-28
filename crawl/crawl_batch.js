#!/usr/bin/env node
// Batch runner: crawls all domains sequentially with Chrome lifecycle management.
// Run: node crawl_batch.js
// Resumable — skips domains where index.json already exists with frontier: [].

const { execSync, spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

const CRAWL_SCRIPT = path.join(__dirname, 'crawl_domain.js');
const LOG_FILE = path.join(__dirname, 'batch_log.txt');
const OUT_BASE = path.join(process.env.HOME, 'Documents/Claude/projects/unimelb-current-students-ia/crawl');

// All domains to crawl (full domain, not just CS sections)
// Special format: "domain --path-prefix=/path" for path-scoped crawls
const DOMAINS = [
  // Faculty/school sites
  'msd.unimelb.edu.au',
  'arts.unimelb.edu.au',
  'fbe.unimelb.edu.au',
  'education.unimelb.edu.au',
  'eng.unimelb.edu.au',
  'finearts-music.unimelb.edu.au',
  'law.unimelb.edu.au',
  'medicine.unimelb.edu.au',
  'mdhs.unimelb.edu.au',
  'science.unimelb.edu.au',
  'mbs.unimelb.edu.au',
  'biomedicalsciences.unimelb.edu.au',
  'dental.unimelb.edu.au',
  // Additional sites
  'study.unimelb.edu.au',
  'services.unimelb.edu.au',
  'scholarships.unimelb.edu.au',
  'handbook.unimelb.edu.au',
  // Path-scoped crawls
  'unimelb.edu.au --path-prefix=/alumni',
];

function log(msg) {
  const ts = new Date().toISOString().slice(0, 19);
  const line = `[${ts}] ${msg}`;
  console.log(line);
  fs.appendFileSync(LOG_FILE, line + '\n');
}

function isComplete(domain) {
  const dirName = domain.replace(/\./g, '-');
  const indexPath = path.join(OUT_BASE, dirName, 'index.json');
  if (!fs.existsSync(indexPath)) return false;
  try {
    const idx = JSON.parse(fs.readFileSync(indexPath, 'utf8'));
    // Complete if frontier is empty and pages exist
    return (!idx.frontier || idx.frontier.length === 0) && idx.pages && idx.pages.length > 0;
  } catch { return false; }
}

function killChrome() {
  try { execSync('killall -9 "Google Chrome" 2>/dev/null', { timeout: 5000 }); } catch {}
  // Wait for Chrome to fully die
  const start = Date.now();
  while (Date.now() - start < 5000) {
    try {
      const out = execSync('pgrep -l "Google Chrome" 2>/dev/null || true', { encoding: 'utf8' }).trim();
      if (!out) return true;
    } catch { return true; }
    // Still running — wait
    const ms = Date.now() - start;
    if (ms < 5000) { const wait = Math.min(200, 5000 - ms); execSync(`sleep ${wait / 1000}`); }
  }
  return false;
}

function runDomain(entry) {
  // Parse entry: "domain" or "domain --path-prefix=/path"
  let domain = entry, extraArgs = [];
  if (entry.includes(' --path-prefix=')) {
    const parts = entry.split(' ');
    domain = parts[0];
    extraArgs = parts.slice(1); // ['--path-prefix=/path']
  }
  const dirName = domain.replace(/\./g, '-');
  const outDir = path.join(OUT_BASE, dirName);

  return new Promise((resolve) => {
    log(`STARTING: ${entry} → ${dirName}/`);

    const args = [CRAWL_SCRIPT, domain, outDir, ...extraArgs];
    const child = spawn('node', args, {
      stdio: ['ignore', 'pipe', 'pipe'],
      timeout: 2 * 60 * 60 * 1000, // 2 hour per-domain max
    });

    let lastLine = '';

    child.stdout.on('data', (data) => {
      const lines = data.toString().split('\n').filter(l => l.trim());
      for (const line of lines) {
        lastLine = line;
        // Only log summary lines, not every page
        if (line.includes('DONE:') || line.includes('CRAWL:') || line.includes('Homepage') ||
            line.includes('No new pages') || line.includes('Load') || line.includes('FATAL') ||
            line.includes('STARTING') || line.includes('checkpoint') || line.includes('Chrome') ||
            line.includes('Cloudflare') || line.includes('===')) {
          log(`  ${domain}: ${line.slice(0, 150)}`);
        }
      }
    });

    child.stderr.on('data', (data) => {
      log(`  ${domain} [stderr]: ${data.toString().trim().slice(0, 200)}`);
    });

    child.on('close', (code) => {
      const status = code === 0 ? 'DONE' : code === 2 ? 'SKIPPED (CF)' : `ERROR(${code})`;
      log(`COMPLETED: ${domain} → ${status}`);
      resolve(code);
    });

    child.on('error', (err) => {
      log(`FAILED: ${domain} → ${err.message}`);
      resolve(1);
    });
  });
}

async function main() {
  log(`\n${'='.repeat(60)}`);
  log(`BATCH CRAWL STARTING — ${DOMAINS.length} domains`);
  log(`${'='.repeat(60)}`);

  let completed = 0, skipped = 0, failed = 0;

  for (let i = 0; i < DOMAINS.length; i++) {
    const entry = DOMAINS[i];
    // Extract plain domain for isComplete check
    const domain = entry.includes(' --') ? entry.split(' ')[0] : entry;
    log(`\n[${i + 1}/${DOMAINS.length}] ${entry}`);

    if (isComplete(domain)) {
      log(`  SKIPPING — already complete`);
      skipped++;
      continue;
    }

    // Kill Chrome before launching (ensures clean profile)
    log('  Killing Chrome...');
    killChrome();

    // Small delay for Chrome to fully die
    await new Promise(r => setTimeout(r, 3000));

    const code = await runDomain(entry);
    if (code === 0) completed++;
    else if (code === 2) skipped++;
    else failed++;

    // Kill Chrome after each domain
    killChrome();
    await new Promise(r => setTimeout(r, 2000));
  }

  log(`\n${'='.repeat(60)}`);
  log(`BATCH COMPLETE`);
  log(`  Completed: ${completed}  |  Skipped: ${skipped}  |  Failed: ${failed}`);
  log(`${'='.repeat(60)}`);
}

main().catch(e => {
  log(`BATCH FATAL: ${e.message}`);
  process.exit(1);
});
