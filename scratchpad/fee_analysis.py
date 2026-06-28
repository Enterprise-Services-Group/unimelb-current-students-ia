import json, glob, os, collections, urllib.parse, re

PAGES = glob.glob('crawl/study-unimelb-edu-au/pages/*/')
def load(d):
    try:
        m=json.load(open(d+'meta.json')); 
    except: return None
    u=m.get('url','')
    L=None
    try: L=json.load(open(d+'links.json'))
    except: pass
    return d,u,m,L

idx={}
for d in PAGES:
    r=load(d)
    if r: idx[r[1]]=r  # url -> (dir,url,meta,links)

# --- 1. Master fees hub: where do its links point ---
def hub_links(url):
    if url not in idx: return None
    d,_,m,L=idx[url]
    out=[]
    if L:
        for l in L['links']:
            out.append((l.get('text','').strip()[:45], l.get('hostname',''), l.get('path','')))
    return m.get('title'), m.get('byteLength'), out

print("="*70)
print("MASTER /how-to-apply/fees hub — outbound destinations")
t=hub_links('https://study.unimelb.edu.au/how-to-apply/fees')
if t:
    print("title:",t[0],"bytes:",t[1])
    hostct=collections.Counter(h for _,h,_ in t[2])
    for h,c in hostct.most_common(): print(f"  {c:3d}  {h}")
    print("  -- funding/help anchors --")
    for txt,h,p in t[2]:
        if re.search(r'help|hecs|loan|csp|contribution|scholar|cost|sa-help|os-help|census|defer',(txt+p).lower()):
            print(f"    {txt!r:50s} {h}{p}")

# --- 2. Per-course fees pages: dollar figures present? bounce to handbook? ---
print("="*70)
print("PER-COURSE /fees/ pages — content check (sample 12)")
course_fees=[u for u in idx if re.search(r'/find/courses/.+/fees/?$',u)]
print(f"total per-course fees pages crawled: {len(course_fees)}")
import random
sample=course_fees[:12]
dollar_re=re.compile(r'\$[\s]?[0-9][0-9,]{2,}')
for u in sample:
    d,_,m,L=idx[u]
    html=open(d+'page.html',encoding='utf-8',errors='ignore').read()
    # strip tags crudely for text
    txt=re.sub(r'<[^>]+>',' ',html)
    dollars=sorted(set(dollar_re.findall(txt)))[:6]
    hb = 0; forms=0; schol=0
    if L:
        for l in L['links']:
            h=l.get('hostname','')
            if 'handbook' in h: hb+=1
            if 'forms.your' in h: forms+=1
            if 'scholarship' in h: schol+=1
    slug=u.replace('https://study.unimelb.edu.au/find/courses/','').replace('/fees/','')
    print(f"  {slug[:45]:45s} $figs={len(dollars):2d} hb={hb} forms={forms} schol={schol}  e.g.{dollars[:3]}")

# --- 3. cost-of-living page ---
print("="*70)
print("COST-OF-LIVING page(s)")
col=[u for u in idx if 'cost-of-living' in u.lower() or 'cost-of-study' in u.lower()]
for u in col:
    d,_,m,L=idx[u]
    print(" ",u,"|",m.get('title'),"| bytes",m.get('byteLength'))
    if L:
        hc=collections.Counter(l.get('hostname','') for l in L['links'])
        print("    out hosts:",dict(hc.most_common(8)))

# --- 4. accommodation footprint ---
print("="*70)
print("ACCOMMODATION pages (study.unimelb)")
acc=[u for u in idx if '/accommodation' in u]
print("count:",len(acc))
for u in sorted(acc)[:12]: print("  ",u.replace('https://study.unimelb.edu.au',''))

# --- 5. Scholarship discovery: how does study link to scholarships.unimelb? from where? ---
print("="*70)
print("SCHOLARSHIP links from study.unimelb -> scholarships.unimelb (anchor texts)")
schol_anchors=collections.Counter()
schol_src=collections.Counter()
for u,(d,_,m,L) in idx.items():
    if not L: continue
    for l in L['links']:
        if 'scholarships.unimelb' in l.get('hostname',''):
            schol_anchors[l.get('text','').strip()[:40]]+=1
            sect=urllib.parse.urlparse(u).path.split('/')[1] if urllib.parse.urlparse(u).path.split('/')[1:] else '(root)'
            schol_src[sect]+=1
print("  top anchor texts:")
for a,c in schol_anchors.most_common(12): print(f"    {c:4d}  {a!r}")
print("  source sections on study.unimelb that link to scholarships:")
for s,c in schol_src.most_common(12): print(f"    {c:4d}  /{s}")
