#!/bin/bash
# Current Students IA project overview
echo "=== Current Students IA Project ==="
echo ""
echo "## Structure"
find . -maxdepth 2 -not -path './crawl/*/pages/*' -not -path './.git/*' | sort | head -50
echo ""
echo "## Crawl data"
echo "crawl/ — domain crawlers and batch scripts"
for d in crawl/*/; do
    count=$(find "$d" -type f 2>/dev/null | wc -l | tr -d ' ')
    echo "  $d — $count files"
done
echo ""
echo "## Analysis files"
ls analysis/*.md 2>/dev/null | head -15
echo ""
echo "## Key commands"
echo "  node crawl/crawl_domain.js <url>     — crawl a domain"
echo "  node crawl/crawl_batch.js            — batch crawl"
echo "  python3 analysis/...                 — analysis scripts"
echo ""
echo "## Git status"
git status --short 2>/dev/null | head -15
