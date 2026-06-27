#!/usr/bin/env python3
"""Prospective-student estate evidence: study.unimelb structure, the funnel it
feeds, the reverse-funnel from current students, and faculty prospective sprawl.
Run: python3 analysis/full-scrape/prospective_estate.py
"""
import json, glob, csv, re, collections, os
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = f'{ROOT}/analysis/full-scrape'

# 1) study.unimelb structure
d = json.load(open(f'{ROOT}/crawl/study-unimelb-edu-au/index.json'))
seg1 = collections.Counter(); seg2 = collections.Counter()
for p in d['pages']:
    pt = urlparse(p['url']).path.strip('/').split('/')
    s1 = pt[0] if pt and pt[0] else '(root)'
    seg1[s1] += 1
    if len(pt) >= 2: seg2[s1 + '/' + pt[1]] += 1

# 2) study.unimelb flows from the contextual graph
flows = list(csv.DictReader(open(f'{OUT}/cross-site-flow.csv')))
study_out = [(r['dst_domain'], int(r['contextual_links'])) for r in flows if r['src_domain'] == 'study.unimelb.edu.au']
study_in = [(r['src_domain'], int(r['contextual_links'])) for r in flows if r['dst_domain'] == 'study.unimelb.edu.au']
CURRENT = {'students.unimelb.edu.au'}  # current-student hub
FACULTY = lambda h: h.endswith('unimelb.edu.au') and h.split('.')[0] in (
    'law','arts','science','education','fbe','eng','mdhs','medicine','msd','finearts-music','biomedicalsciences','dental','mbs')

# 3) faculty-hosted /study/ prospective pages
fac_study = collections.Counter()
for idx in glob.glob(f'{ROOT}/crawl/*/index.json'):
    dd = json.load(open(idx)); dom = dd.get('domain', '')
    if dom in ('study.unimelb.edu.au', 'students.unimelb.edu.au'): continue
    n = sum(1 for p in dd.get('pages', []) if re.match(r'/study(-with-us)?(/|$)', urlparse(p['url']).path))
    if n: fac_study[dom] = n

# write CSVs
with open(f'{OUT}/prospective-sections.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['section', 'pages'])
    for s, c in seg1.most_common(): w.writerow([s, c])
    for s, c in seg2.most_common():
        if c >= 5: w.writerow([s, c])

with open(f'{OUT}/prospective-estate-SUMMARY.md', 'w') as f:
    f.write("# Prospective-student estate — study.unimelb + faculty /study/\n\n")
    f.write(f"**study.unimelb.edu.au = {len(d['pages']):,} crawled pages.** Dominated by the course catalogue.\n\n")
    f.write("## Top-level sections\n\n| Section | Pages |\n|---|--:|\n")
    for s, c in seg1.most_common(12): f.write(f"| /{s}/ | {c} |\n")
    f.write("\n## The application journey (/how-to-apply)\n\n| Path | Pages |\n|---|--:|\n")
    for s, c in seg2.most_common(60):
        if s.startswith('how-to-apply/'): f.write(f"| /{s}/ | {c} |\n")
    f.write("\n## Where study.unimelb sends prospective students (top contextual flows out)\n\n| Destination | Links |\n|---|--:|\n")
    for h, c in sorted(study_out, key=lambda x: -x[1])[:15]: f.write(f"| {h} | {c} |\n")
    f.write("\n## Who links INTO study.unimelb — incl. the reverse-funnel from current students\n\n| Source | Links | Note |\n|---|--:|---|\n")
    for h, c in sorted(study_in, key=lambda x: -x[1])[:15]:
        note = 'CURRENT-STUDENT HUB (reverse-funnel)' if h in CURRENT else ('faculty' if FACULTY(h) else '')
        f.write(f"| {h} | {c} | {note} |\n")
    f.write("\n## Faculty-hosted prospective /study/ content (parallel to the central site)\n\n| Faculty domain | /study/ pages |\n|---|--:|\n")
    for dom, c in fac_study.most_common(): f.write(f"| {dom} | {c} |\n")
    f.write(f"\n**Total faculty /study/ prospective pages: {sum(fac_study.values())}** — duplicating the central study.unimelb funnel.\n")

def short(h): return h.split('.')[0]
print(f"study.unimelb {len(d['pages'])} pages | /find/courses {seg2.get('find/courses',0)} | how-to-apply {seg1.get('how-to-apply',0)}")
print("top outbound:", [short(h)+':'+str(c) for h, c in sorted(study_out, key=lambda x:-x[1])[:8]])
print("top inbound:", [short(h)+':'+str(c) for h, c in sorted(study_in, key=lambda x:-x[1])[:8]])
print(f"faculty /study/ total: {sum(fac_study.values())} across {len(fac_study)} faculties")
print("wrote prospective-estate-SUMMARY.md + prospective-sections.csv")
