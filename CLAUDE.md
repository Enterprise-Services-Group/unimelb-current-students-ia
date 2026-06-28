# Current Students IA — Claude Code Guide

## What this is
Cross-university website analysis for UoM's Student Experience & Design team. Crawls faculty current-student pages, analyzes content patterns, produces reports.

## CRITICAL — Phase decomposition
**NEVER do all work in one session.** The last project run was 42 Hermes sessions + 1 monster Claude session with 19 restarts. See `.claude/PHASE_DECOMPOSITION.md`.

Use 3 phases:
1. **Crawl** (claude -p) — `crawl_domain.js` per faculty, output to `crawl/<domain>/`
2. **Analyze** (claude -p or Hermes) — cross-site overlap, lifecycle traces
3. **Report** (claude -p) — synthesize into `report/<topic>.md`

Each phase starts fresh. Output persists in files. No --continue restarts.

## Session startup
Read `.claude/.session_context.txt` before exploring. Do not `ls`/`find`/`grep` — the overview script already captured the project structure.

## Key commands
- `node crawl/crawl_domain.js <url>` — crawl a faculty site
- `node crawl/crawl_batch.js` — batch crawl all faculties
- Analysis files in `analysis/` — cross-site-overlap, lifecycle traces, etc.

## Rules
- Crawl politely — no hammering, respect rate limits
- WAF bypass is fragile — don't change the crawl technique without testing
- Crawl data in `crawl/<domain>/pages/` is large — don't load it all into context
- Chrome/Playwright required for crawling — this is headful, not headless

## Model tiering
- **Opus**: cross-site analysis, lifecycle patterns, synthesis
- **Sonnet**: crawl execution, data processing, report generation
- Default to Sonnet for crawl and report phases
