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

# WELLBEING URL inconsistency: how many distinct top-level paths host wellbeing on students.unimelb?
print("=== Wellbeing IA split WITHIN students.unimelb ===")
buckets=Counter()
for meta,links in load('students-full'):
    u=meta['url']
    if 'students.unimelb.edu.au/' in u:
        path=u.split('students.unimelb.edu.au',1)[1]
        if any(k in path.lower() for k in ['wellbeing','counsel','mental','health-and-well']):
            seg=path.strip('/').split('/')[0] if path.strip('/') else '(root)'
            buckets[seg]+=1
for s,c in buckets.most_common(): print(f"  {c:3d} pages under  students.unimelb/{s}/...  (wellbeing-related)")

# JOURNEY 4: GRADUATION -> ALUMNI
print("\n=== JOURNEY 4: GRADUATION->ALUMNI handoff ===")
# 4a: graduation pages on students.unimelb
grad=[]
for meta,links in load('students-full'):
    u=meta['url'].lower()
    if any(k in u for k in ['graduat','ceremony','completion','finishing','transition']):
        grad.append(meta['url'])
print(f"students.unimelb graduation/completion/transition pages: {len(grad)}")
for g in grad[:15]: print("   ",g)

# 4b: contextual links from students.unimelb -> alumni (any alumni host)
alumni_links=Counter()
for meta,links in load('students-full'):
    for l in links.get('links',[]):
        h=l.get('hostname','')
        if 'alumni' in h:
            alumni_links[h]+=1
print(f"\nstudents.unimelb -> *alumni* hosts (all contexts incl nav): {dict(alumni_links)}")

# 4c: faculty -> alumni contextual links (excluding global nav /alumni homepage)
fac_alumni=Counter()
for fd in FAC:
    for meta,links in load(fd):
        for l in links.get('links',[]):
            h=l.get('hostname','')
            if 'alumni' in h:
                fac_alumni[h+l.get('path','')]+=1
print(f"\nfaculty pages -> alumni destinations (top, raw incl nav):")
for k,c in fac_alumni.most_common(12): print(f"  {c:5d}  {k}")

# 4d: Does the alumni site link BACK to current students (continuity)? And to careers/mentoring?
print("\n=== Alumni site outbound: does it connect back to current-student services? ===")
ah=Counter()
for meta,links in load('www-unimelb-edu-au-alumni'):
    for l in links.get('links',[]):
        h=l.get('hostname','')
        if h and 'unimelb' in h: ah[h]+=1
for h,c in ah.most_common(20): print(f"  {c:4d}  {h}")
