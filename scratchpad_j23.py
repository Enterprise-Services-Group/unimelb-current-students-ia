import json, os
from collections import Counter

ROOT='crawl'
def load(domdir):
    d=os.path.join(ROOT,domdir,'pages')
    for h in os.listdir(d):
        pdir=os.path.join(d,h)
        mp,lp=os.path.join(pdir,'meta.json'),os.path.join(pdir,'links.json')
        if os.path.exists(mp) and os.path.exists(lp):
            try: yield json.load(open(mp)),json.load(open(lp))
            except: pass

FAC=['msd-unimelb-edu-au','eng-unimelb-edu-au','arts-unimelb-edu-au','fbe-unimelb-edu-au',
     'mdhs-unimelb-edu-au','science-unimelb-edu-au','law-unimelb-edu-au','education-unimelb-edu-au',
     'medicine-unimelb-edu-au','finearts-music-unimelb-edu-au','biomedicalsciences-unimelb-edu-au','dental-unimelb-edu-au']

# JOURNEY 2: PLACEMENTS / WIL. Where do faculty placement pages link? Do they link to central students.unimelb or a central WIL hub?
print("=== JOURNEY 2: PLACEMENTS/WIL — faculty placement-page outbound hosts ===")
hosts=Counter(); pl_pages=[]
central_hits=Counter()
for fd in FAC:
    for meta,links in load(fd):
        u=meta['url'].lower()
        if any(k in u for k in ['placement','internship','work-integrated','vocational','wil','industry-experience','professional-experience']):
            pl_pages.append(meta['url'])
            for l in links.get('links',[]):
                h=l.get('hostname','')
                if h and 'unimelb' in h: hosts[h]+=1
                if h=='students.unimelb.edu.au': central_hits[l.get('path','')]+=1
print(f"found {len(pl_pages)} placement/WIL pages across 12 faculties")
for h,c in hosts.most_common(20): print(f"  {c:5d}  {h}")
print(f"\n  Of those, links to central students.unimelb: {sum(central_hits.values())}")
for p,c in central_hits.most_common(8): print(f"    {c:3d}  students.unimelb{p}")

# JOURNEY 3: WELLBEING. Trace where wellbeing/counselling lives and whether faculty pages link to it.
print("\n=== JOURNEY 3: WELLBEING — where is counselling/wellbeing authored & linked? ===")
# central students.unimelb wellbeing pages
sw=[]
for meta,links in load('students-full'):
    u=meta['url'].lower()
    if any(k in u for k in ['wellbeing','counsel','mental-health','health-service','safer','crisis','support']):
        sw.append(meta['url'])
print(f"central students.unimelb wellbeing/support pages: {len(sw)}")
# How many faculty pages link to a wellbeing/counselling destination at all?
fac_to_wellbeing=Counter()
fac_total_pages=0
for fd in FAC:
    for meta,links in load(fd):
        fac_total_pages+=1
        for l in links.get('links',[]):
            h=l.get('hostname',''); p=l.get('path','').lower()
            if h in ('students.unimelb.edu.au','services.unimelb.edu.au','safercommunity.unimelb.edu.au','health.unimelb.edu.au','casemanagementform.unimelb.edu.au') and any(k in p for k in ['wellbeing','counsel','mental','health','safer','crisis','support']):
                fac_to_wellbeing[h+p]+=1
print(f"faculty pages scanned: {fac_total_pages}; distinct faculty->wellbeing contextual link targets: {len(fac_to_wellbeing)}; total such links: {sum(fac_to_wellbeing.values())}")
for k,c in fac_to_wellbeing.most_common(12): print(f"  {c:4d}  {k}")
