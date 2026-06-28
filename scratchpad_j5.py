import json, os
from collections import Counter

ROOT='crawl'
def load(domdir):
    d=os.path.join(ROOT,domdir,'pages')
    for h in os.listdir(d):
        pdir=os.path.join(d,h)
        mp,lp=os.path.join(pdir,'meta.json'),os.path.join(pdir,'links.json')
        if os.path.exists(mp) and os.path.exists(lp):
            try: yield json.load(open(mp)),json.load(open(lp)),pdir
            except: pass

# Inspect the graduation-day page outbound links specifically
print("=== students.unimelb graduation-day & graduation pages: do they link to alumni at all? ===")
for meta,links,pdir in load('students-full'):
    u=meta['url']
    if '/graduation/graduation-day' in u or u.endswith('/manage-your-course/graduation'):
        print(f"\nPAGE: {u}  ({links['total']} links)")
        outs=Counter()
        for l in links.get('links',[]):
            outs[l.get('hostname','')]+=1
        for h,c in outs.most_common(12): print(f"    {c:3d}  {h}")

# CAREERS / MENTORING continuity: faculty mentoring pages, do any link to alumni mentoring (mentoring.unimelb)?
print("\n\n=== CAREERS/MENTORING continuity gap ===")
FAC=['msd-unimelb-edu-au','eng-unimelb-edu-au','arts-unimelb-edu-au','fbe-unimelb-edu-au',
     'mdhs-unimelb-edu-au','science-unimelb-edu-au','law-unimelb-edu-au','education-unimelb-edu-au',
     'medicine-unimelb-edu-au','finearts-music-unimelb-edu-au','biomedicalsciences-unimelb-edu-au','dental-unimelb-edu-au']
ment_pages=0; ment_to_alumni=0; ment_targets=Counter()
for fd in FAC:
    for meta,links,_ in load(fd):
        u=meta['url'].lower()
        if 'mentor' in u:
            ment_pages+=1
            for l in links.get('links',[]):
                h=l.get('hostname','')
                if 'alumni' in h or h=='mentoring.unimelb.edu.au':
                    ment_to_alumni+=1; ment_targets[h]+=1
print(f"faculty mentoring pages: {ment_pages}; links from them to alumni/mentoring hub: {ment_to_alumni} {dict(ment_targets)}")

# Where does mentoring.unimelb (the alumni mentoring platform) get linked FROM?
print("\n=== Who links to mentoring.unimelb.edu.au (alumni mentoring platform)? ===")
for fd in ['students-full','study-unimelb-edu-au','www-unimelb-edu-au-alumni']+FAC:
    cnt=0
    for meta,links,_ in load(fd):
        for l in links.get('links',[]):
            if l.get('hostname','')=='mentoring.unimelb.edu.au': cnt+=1
    if cnt: print(f"  {fd:35s} -> mentoring.unimelb: {cnt}")

# careersonline.unimelb (the current-student careers platform) - who links to it?
print("\n=== Who links to careersonline.unimelb.edu.au (current careers platform)? ===")
for fd in ['students-full','www-unimelb-edu-au-alumni']+FAC:
    cnt=0
    for meta,links,_ in load(fd):
        for l in links.get('links',[]):
            if l.get('hostname','')=='careersonline.unimelb.edu.au': cnt+=1
    if cnt: print(f"  {fd:35s} -> careersonline: {cnt}")
