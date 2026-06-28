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

# HANDBOOK orphans: confirm subject/course pages orphaned. The handbook is the spine of enrolment.
# Count how handbook subject pages are reached: only via search hub?
print("=== HANDBOOK as enrolment spine: link structure ===")
subj=0; crs=0; total=0
for meta,links in load('handbook-unimelb-edu-au'):
    total+=1
    u=meta['url']
    if '/subjects/' in u: subj+=1
    elif '/courses/' in u: crs+=1
print(f"handbook pages: {total}; subject pages: {subj}; course pages: {crs}")

# forms.your.unimelb (prospective lead-capture "Register your interest") appearing where?
print("\n=== 'Register your interest' lead-capture leak onto current-student paths ===")
# Which current-student / faculty current-student pages link to forms.your.unimelb (prospective enquiry)?
FAC=['msd-unimelb-edu-au','eng-unimelb-edu-au','arts-unimelb-edu-au','fbe-unimelb-edu-au',
     'mdhs-unimelb-edu-au','science-unimelb-edu-au','law-unimelb-edu-au','education-unimelb-edu-au',
     'medicine-unimelb-edu-au','finearts-music-unimelb-edu-au','biomedicalsciences-unimelb-edu-au','dental-unimelb-edu-au']
# Find faculty CURRENT-STUDENT pages that link to forms.your (prospective enquiry form)
leak=0; leak_pages=[]
for fd in FAC:
    for meta,links in load(fd):
        u=meta['url'].lower()
        if any(k in u for k in ['/current-students','/students/','current-student']):
            for l in links.get('links',[]):
                if l.get('hostname','')=='forms.your.unimelb.edu.au':
                    leak+=1
                    if len(leak_pages)<10: leak_pages.append(meta['url'])
print(f"faculty CURRENT-student pages linking to prospective enquiry form (forms.your): {leak}")
for p in leak_pages[:8]: print("   ",p)

# students.unimelb pages linking to forms.your
sleak=0
for meta,links in load('students-full'):
    for l in links.get('links',[]):
        if l.get('hostname','')=='forms.your.unimelb.edu.au': sleak+=1
print(f"\nstudents.unimelb -> forms.your.unimelb (prospective enquiry) total links: {sleak}")

# ASK.unimelb.edu.au — is there a single answer hub? who links to it?
print("\n=== ask.unimelb.edu.au (answer hub) inbound from journey domains ===")
for fd in ['students-full','study-unimelb-edu-au','handbook-unimelb-edu-au','scholarships-unimelb-edu-au']+FAC:
    cnt=0
    for meta,links in load(fd):
        for l in links.get('links',[]):
            if l.get('hostname','')=='ask.unimelb.edu.au': cnt+=1
    if cnt: print(f"  {fd:35s} -> ask.unimelb: {cnt}")
