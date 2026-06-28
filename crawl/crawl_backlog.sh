#!/bin/bash
# Backlog re-crawl for capped domains — uses NEW priority crawler (content first, news last)
# Run AFTER main batch completes. Safe to run anytime — resumable.

set -e
SCRIPT="$(dirname "$0")/crawl_domain.js"
LOG="$(dirname "$0")/batch_backlog.txt"

log() { echo "[$(date '+%Y-%m-%dT%H:%M:%S')] $*" | tee -a "$LOG"; }

# Kill any lingering Chrome
killall -9 "Google Chrome" 2>/dev/null || true
sleep 2

# === law ===
log "BACKLOG: law.unimelb.edu.au (140 content pages remaining from cap)"
node "$SCRIPT" law.unimelb.edu.au 2>&1 | tail -20 | tee -a "$LOG"

killall -9 "Google Chrome" 2>/dev/null || true
sleep 2

# === medicine ===
log "BACKLOG: medicine.unimelb.edu.au (153 pages remaining)"
node "$SCRIPT" medicine.unimelb.edu.au 2>&1 | tail -20 | tee -a "$LOG"

killall -9 "Google Chrome" 2>/dev/null || true
sleep 2

log "BACKLOG COMPLETE"
