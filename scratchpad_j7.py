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

# Handbook subject pages: where do they send a CURRENT student who needs to enrol in that subject?
print("=== HANDBOOK subject page -> enrolment action? (sample 200 subject pages) ===")
to_students=0; to_study=0; to_my=0; n=0; any_enrol=0
host_agg=Counter()
for meta,links in load('handbook-unimelb-edu-au'):
    u=meta['url']
    if '/subjects/' in u:
        n+=1
        hosts=set()
        for l in links.get('links',[]):
            h=l.get('hostname','')
            hosts.add(h); host_agg[h]+=1
        if 'students.unimelb.edu.au' in hosts: to_students+=1
        if 'study.unimelb.edu.au' in hosts: to_study+=1
        if 'my.unimelb.edu.au' in hosts: to_my+=1
print(f"subject pages sampled: {n}")
print(f"  link to students.unimelb (enrol how-to): {to_students} ({100*to_students//max(n,1)}%)")
print(f"  link to study.unimelb (prospective):    {to_study} ({100*to_study//max(n,1)}%)")
print(f"  link to my.unimelb (the actual SIS):     {to_my} ({100*to_my//max(n,1)}%)")
print("  top outbound hosts from subject pages:")
for h,c in host_agg.most_common(12): print(f"    {c:6d}  {h}")

# Stop 1 as the universal hub - how many distinct domains route to Stop 1?
print("\n=== Stop 1 — the de-facto front door — who routes to it? ===")
FAC=['msd-unimelb-edu-au','eng-unimelb-edu-au','arts-unimelb-edu-au','fbe-unimelb-edu-au',
     'mdhs-unimelb-edu-au','science-unimelb-edu-au','law-unimelb-edu-au','education-unimelb-edu-au',
     'medicine-unimelb-edu-au','finearts-music-unimelb-edu-au','biomedicalsciences-unimelb-edu-au','dental-unimelb-edu-au']
stop1=Counter()
for fd in ['students-full','study-unimelb-edu-au','handbook-unimelb-edu-au','services-unimelb-edu-au']+FAC:
    cnt=0
    for meta,links in load(fd):
        for l in links.get('links',[]):
            p=l.get('path','').lower()
            if l.get('hostname','')=='students.unimelb.edu.au' and 'stop-1' in p:
                cnt+=1
    if cnt: stop1[fd]=cnt
for d,c in stop1.most_common(): print(f"  {d:35s} -> Stop 1: {c}")
