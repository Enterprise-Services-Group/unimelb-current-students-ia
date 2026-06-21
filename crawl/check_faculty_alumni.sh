#!/bin/bash
# Quick check: do faculty homepages link to alumni.unimelb.edu.au?
# Run: bash check_faculty_alumni.sh

DOMAINS=(
  "law.unimelb.edu.au"
  "feit.unimelb.edu.au"
  "arts.unimelb.edu.au"
  "science.unimelb.edu.au"
  "education.unimelb.edu.au"
  "fbe.unimelb.edu.au"
  "finearts-music.unimelb.edu.au"
  "mdhs.unimelb.edu.au"
  "msd.unimelb.edu.au"
  "students.unimelb.edu.au"
)

echo "=========================================="
echo "FACULTY ALUMNI LINK CHECK"
echo "Checking for links to alumni.unimelb.edu.au"
echo "=========================================="
echo ""

for domain in "${DOMAINS[@]}"; do
  echo "--- $domain ---"
  
  # 1. Fetch homepage
  HP="https://${domain}/"
  echo "  Homepage: $HP"
  html=$(curl -sL --max-time 15 -H "User-Agent: Mozilla/5.0" "$HP" 2>/dev/null)
  
  if [ -z "$html" ]; then
    echo "  FAILED: Could not fetch homepage"
    echo ""
    continue
  fi
  
  # 2. Check for alumni.unimelb.edu.au links
  alumni_links=$(echo "$html" | grep -oi 'alumni\.unimelb\.edu\.au[^"'"'"'[:space:]<>]*' | head -20)
  
  # 3. Check nav for "Alumni" text
  nav_alumni=$(echo "$html" | grep -oiP '(?<=>)[^<]*alumni[^<]*(?=<)' | head -10)
  
  # 4. Footer check
  footer_alumni=$(echo "$html" | grep -oP '<footer[^>]*>.*?</footer>' 2>/dev/null | grep -oi 'alumni' | head -5)
  
  echo "  Alumni.unimelb.edu.au links found: $(echo "$alumni_links" | grep -c '.' 2>/dev/null || echo 0)"
  if [ -n "$alumni_links" ]; then
    echo "    Links:"
    echo "$alumni_links" | while IFS= read -r line; do echo "      $line"; done
  fi
  if [ -n "$nav_alumni" ]; then
    echo "  Nav text containing 'alumni':"
    echo "$nav_alumni" | while IFS= read -r line; do echo "    $line"; done
  fi
  
  # 5. Check subpages: /alumni, /engage, /community
  for sub in "/alumni" "/engage" "/community"; do
    url="https://${domain}${sub}"
    status=$(curl -sL -o /dev/null -w "%{http_code}" --max-time 10 -H "User-Agent: Mozilla/5.0" "$url" 2>/dev/null)
    echo "  ${sub}: HTTP $status"
  done
  
  echo ""
  sleep 1
done

echo ""
echo "=========================================="
echo "DONE"
echo "=========================================="
