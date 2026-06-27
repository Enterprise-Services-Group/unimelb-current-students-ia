#!/usr/bin/env python3
"""Classify every crawled page by the student SERVICE it carries, then measure
how fragmented each service is across the estate's domains and URL trees.

A service is "fragmented" when its pages are spread across many domains and many
distinct top-level URL trees, with no single dominant owner. Output feeds the
per-service deep-dive workflow.

Outputs (analysis/full-scrape/): service-pages.csv (page→service),
service-fragmentation.csv (per-service metrics), service-frag-SUMMARY.md.
Run: python3 analysis/full-scrape/service_fragmentation.py
"""
import json, glob, re, collections, csv, os
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# service -> compiled pattern over (path + ' ' + title), lowercased
SVC = {
 'enrolment & subjects':     r'enrol|/subjects?\b|my-?course|study-plan|course-plan|overload|intermission|leave-of-absence|withdraw|re-enrol|variation',
 'timetable & class rego':   r'timetable|my-?timetable|class-registration|allocate|census',
 'exams, results & progress':r'\bexam|results?\b|assessment|academic-progress|\bgrades?\b|gpa|wam|remark',
 'special consideration':    r'special-consider|special-con|extension|deferred-exam',
 'fees, finance & census':   r'\bfees?\b|census-date|payment|fee-help|hecs|refund|financial-hardship|tuition|invoice|fee-remission',
 'scholarships & awards':    r'scholarship|bursar|\bgrant\b|financial-aid|prize',
 'careers & employability':  r'career|employab|\bmentor|internship|graduate-outcome|job-ready|work-experience',
 'placements & WIL':         r'placement|work-integrated|\bwil\b|practicum|clinical-placement|industry-experience|sonia',
 'wellbeing, health & safety':r'wellbeing|\bhealth\b|counsel|mental-health|safer-community|safety|medical|psycholog',
 'academic skills & language':r'academic-skill|study-skill|academic-english|writing-support|maths-support|language-support|learning-support',
 'IT, systems & tools':      r'\bit-|/it\b|canvas|\blms\b|password|\bwi-?fi\b|software|student-(portal|email)|my\.unimelb|technolog|computer',
 'library & resources':      r'\blibrary\b|/lib\b|borrow|database|referencing|\bcitation',
 'international & visa':      r'international-student|student-visa|\bvisa\b|\boshc\b|\bcoe\b|\besos\b|study-load|overseas-student',
 'equity, disability & Indigenous':r'disabilit|\bequity\b|access-melbourne|accessibility-service|reasonable-adjust|indigenous|murrup|first-nations|low-ses',
 'student life & community': r'\bclubs?\b|societ|\bumsu\b|\bgsa\b|student-union|student-life|orientation|getting-started|belonging|student-event',
 'contacts, Stop 1 & help':  r'stop-?1|contact-us|\bask\b|enquir|student-centre|help-and-support|get-help|service-centre',
 'research candidature (HDR)':r'candidature|\bthesis\b|\bhdr\b|milestone|gradresearch|research-degree|graduate-research|supervis',
 'graduation & transition':  r'graduation|testamur|ahegs|conferral|apply-to-graduate|completion|ceremony|alumni',
 'forms & transactions':     r'forms?\.your|/forms?\b|\.app\.unimelb|application-form|submit-a|e-?form',
}
SVC = {k: re.compile(v, re.I) for k, v in SVC.items()}

# central vs faculty/system domain role
def role(dom):
    if dom == 'students.unimelb.edu.au': return 'central hub'
    if dom in ('study.unimelb.edu.au',): return 'prospective'
    if dom in ('handbook.unimelb.edu.au','scholarships.unimelb.edu.au','services.unimelb.edu.au',
               'research.unimelb.edu.au','gradresearch.unimelb.edu.au'): return 'central service site'
    if 'alumni' in dom or dom == 'www.unimelb.edu.au': return 'alumni/www'
    return 'faculty'

pages = []
for idx in sorted(glob.glob(f'{ROOT}/crawl/*/index.json')):
    try: d = json.load(open(idx))
    except: continue
    dom = d.get('domain', '')
    for p in d.get('pages', []):
        url = p.get('url', ''); title = p.get('title', '')
        blob = (urlparse(url).path + ' ' + title).lower()
        svcs = [k for k, rx in SVC.items() if rx.search(blob)]
        if svcs:
            pages.append((dom, url, title, svcs))

print(f"classified {len(pages)} service-bearing pages across {len({p[0] for p in pages})} domains")

# per-service metrics
rows = []
svc_pagelist = collections.defaultdict(list)
for svc in SVC:
    sp = [(dom, url, title) for dom, url, title, svcs in pages if svc in svcs]
    for dom, url, title in sp: svc_pagelist[svc].append((dom, url, title))
    doms = collections.Counter(d for d, u, t in sp)
    # distinct top-level URL trees (domain + first path segment)
    trees = set()
    for d, u, t in sp:
        seg = urlparse(u).path.strip('/').split('/')
        trees.add(d + '/' + (seg[0] if seg and seg[0] else ''))
    roles = collections.Counter(role(d) for d, u, t in sp)
    central = doms.get('students.unimelb.edu.au', 0)
    top_dom, top_n = doms.most_common(1)[0] if doms else ('', 0)
    rows.append({
        'service': svc, 'pages': len(sp), 'domains': len(doms), 'url_trees': len(trees),
        'central_hub_pages': central, 'top_domain': top_dom, 'top_domain_pages': top_n,
        'faculty_pages': roles.get('faculty', 0), 'prospective_pages': roles.get('prospective', 0),
        'frag_score': len(doms) * len(trees),  # spread × tree-sprawl
    })

rows.sort(key=lambda r: -r['frag_score'])
with open(f'{ROOT}/analysis/full-scrape/service-fragmentation.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
with open(f'{ROOT}/analysis/full-scrape/service-pages.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['service', 'domain', 'url', 'title'])
    for svc, lst in svc_pagelist.items():
        for dom, url, title in lst: w.writerow([svc, dom, url, title[:80]])

with open(f'{ROOT}/analysis/full-scrape/service-frag-SUMMARY.md', 'w') as f:
    f.write("# Student-service fragmentation — across the estate\n\n")
    f.write("Each current-student service, by how widely it is spread. **domains** = distinct hosts that carry the service; "
            "**url_trees** = distinct domain+top-level-path trees (parallel structures); **frag_score** = domains × url_trees.\n\n")
    f.write("| Service | Pages | Domains | URL trees | Central hub | Top owner (pages) | Frag score |\n|---|--:|--:|--:|--:|---|--:|\n")
    for r in rows:
        f.write(f"| {r['service']} | {r['pages']} | {r['domains']} | {r['url_trees']} | {r['central_hub_pages']} | "
                f"{r['top_domain'].split('.')[0]} ({r['top_domain_pages']}) | {r['frag_score']} |\n")

print("\n=== fragmentation ranking ===")
for r in rows:
    print(f"  {r['service']:34} pages={r['pages']:5} domains={r['domains']:2} trees={r['url_trees']:3} "
          f"central={r['central_hub_pages']:3} top={r['top_domain'].split('.')[0]}({r['top_domain_pages']}) frag={r['frag_score']}")
