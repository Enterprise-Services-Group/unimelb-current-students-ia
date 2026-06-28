import json, os
from collections import Counter
from urllib.parse import urlparse

ROOT='crawl'
def load(domdir):
    d=os.path.join(ROOT,domdir,'pages')
    for h in os.listdir(d):
        pdir=os.path.join(d,h)
        mp,lp=os.path.join(pdir,'meta.json'),os.path.join(pdir,'links.json')
        if os.path.exists(mp) and os.path.exists(lp):
            try: yield json.load(open(mp)),json.load(open(lp))
            except: pass

# JOURNEY 1: ENROLMENT. Find students.unimelb enrolment/course-planning pages, see where they send students.
print("=== JOURNEY 1: ENROLMENT — students.unimelb enrolment pages outbound host distribution ===")
hosts=Counter()
enrol_pages=[]
for meta,links in load('students-full'):
    u=meta['url']
    if any(k in u for k in ['enrol','course-planning','manage-your-course','subject','planning-your-course','timetable']):
        enrol_pages.append((u,meta.get('title','')))
        for l in links.get('links',[]):
            h=l.get('hostname','')
            if h and 'unimelb' in h: hosts[h]+=1
print(f"found {len(enrol_pages)} enrolment-related pages on students.unimelb")
for h,c in hosts.most_common(25): print(f"  {c:5d}  {h}")

print("\n=== Do students.unimelb enrolment pages link to study.unimelb (prospective bounce-back)? ===")
study_targets=Counter()
for meta,links in load('students-full'):
    u=meta['url']
    if any(k in u for k in ['enrol','course-planning','manage-your-course','planning-your-course']):
        for l in links.get('links',[]):
            if l.get('hostname','')=='study.unimelb.edu.au':
                study_targets[l.get('path','')]+=1
for p,c in study_targets.most_common(20): print(f"  {c:4d}  study.unimelb{p}")
print(f"  TOTAL prospective-site links from current enrolment pages: {sum(study_targets.values())}")
