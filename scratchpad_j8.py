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

# Anchor text quality for the BIGGEST cross-site seam: msd -> students (8069 links). What's the link text?
print("=== Anchor text on the biggest seam msd->students (8069 links) ===")
at=Counter()
for meta,links in load('msd-unimelb-edu-au'):
    for l in links.get('links',[]):
        if l.get('hostname','')=='students.unimelb.edu.au':
            t=(l.get('text','') or '(no text)').strip()[:40]
            at[t]+=1
for t,c in at.most_common(12): print(f"  {c:5d}  '{t}'")

# Generic anchor text across all journey hops: how many cross-site links use vague text?
print("\n=== Vague anchor text ('here','read more','view more','learn more','find out more') on cross-site links ===")
VAGUE={'here','read more','view more','learn more','find out more','click here','more','more information','this page','link'}
FAC=['students-full','study-unimelb-edu-au','msd-unimelb-edu-au','eng-unimelb-edu-au','arts-unimelb-edu-au',
     'fbe-unimelb-edu-au','mdhs-unimelb-edu-au','law-unimelb-edu-au','education-unimelb-edu-au','medicine-unimelb-edu-au']
vague=0; crosssite=0
for fd in FAC:
    src_host=None
    for meta,links in load(fd):
        if src_host is None:
            src_host=meta['url'].split('//')[1].split('/')[0]
        for l in links.get('links',[]):
            h=l.get('hostname','')
            if h and 'unimelb' in h and h!=src_host:
                crosssite+=1
                t=(l.get('text','') or '').strip().lower()
                if t in VAGUE: vague+=1
print(f"cross-site contextual links (10 domains): {crosssite}; vague-text: {vague} ({100*vague//max(crosssite,1)}%)")

# International student support journey: visa changes. Where authored, where linked from faculty?
print("\n=== Visa/international support: faculty pages linking to central visa pages ===")
vis=Counter()
for fd in ['msd-unimelb-edu-au','eng-unimelb-edu-au','arts-unimelb-edu-au','fbe-unimelb-edu-au','mdhs-unimelb-edu-au','law-unimelb-edu-au','education-unimelb-edu-au']:
    for meta,links in load(fd):
        for l in links.get('links',[]):
            h=l.get('hostname',''); p=l.get('path','').lower()
            if h=='students.unimelb.edu.au' and 'visa' in p:
                vis[l.get('path','')]+=1
print(f"faculty->central visa links: {sum(vis.values())} across {len(vis)} distinct targets")
for p,c in vis.most_common(6): print(f"  {c:4d}  students.unimelb{p}")
