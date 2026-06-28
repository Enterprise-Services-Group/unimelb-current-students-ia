#!/bin/bash
# Current Students IA — phase decomposition rule
# This project had 42 Hermes planning sessions but only 1 Claude monster session.
# NEVER repeat that pattern. Use this 3-phase decomposition.

echo "=== Current Students IA — Session Rules ==="
echo ""
echo "NEVER do all work in one session. Use 3 phases:"
echo ""
echo "Phase 1 — Crawl (Claude Code -p, headless):"
echo "  claude -p 'Crawl <domain> using crawl_domain.js, save to crawl/<domain>/' --max-turns 20"
echo "  Output: crawl/<domain>/pages/*.json"
echo ""
echo "Phase 2 — Analyze (Claude Code -p or Hermes):"
echo "  claude -p 'Analyze crawl/<domain>/, produce analysis/<domain>-findings.md' --max-turns 15"
echo "  Or: Hermes session with obsidian skill"
echo ""
echo "Phase 3 — Report (Claude Code -p):"
echo "  claude -p 'Synthesize analysis/*.md into report/<topic>.md' --max-turns 10"
echo ""
echo "Each phase starts fresh. Output persists in files. No restarts needed."
