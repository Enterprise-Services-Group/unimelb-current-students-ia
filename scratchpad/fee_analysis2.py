import json, glob, re, collections, urllib.parse

PAGES=glob.glob('crawl/study-unimelb-edu-au/pages/*/')
idx={}
for d in PAGES:
    try: m=json.load(open(d+'meta.json'))
    except: continue
    idx[m.get('url','')]=(d,m)

def text(d):
    h=open(d+'page.html',encoding='utf-8',errors='ignore').read()
    return re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',h))

# 1. FEE-HELP / HECS-HELP / loan scheme coverage in BODY of journey-level fee pages
print("="*70)
print("FEE-HELP / HECS-HELP / CSP loan-scheme mentions in journey fee pages (body text)")
terms=['FEE-HELP','HECS-HELP','HECS','SA-HELP','OS-HELP','Commonwealth supported','student contribution','census date','Commonwealth Assistance']
journey_fee=[u for u in idx if '/how-to-apply/' in u and ('fees' in u or 'payment' in u)]
journey_fee+=[u for u in idx if u.endswith('/student-life/cost-of-living')]
for u in sorted(journey_fee):
    d,m=idx[u]
    t=text(d)
    hits={term:len(re.findall(re.escape(term),t,re.I)) for term in terms}
    present=[k for k,v in hits.items() if v>0]
    short=u.replace('https://study.unimelb.edu.au','')
    print(f"  {short[:62]:62s} -> {', '.join(present) if present else 'NONE'}")

# 2. Domestic vs international fee page existence per audience
print("="*70)
print("Journey fee pages inventory (audience x domestic/intl)")
for u in sorted(journey_fee):
    print("  ",u.replace('https://study.unimelb.edu.au',''),"|",idx[u][1].get('title','')[:50])

# 3. A per-course fees page: does it explain HOW to pay / loan schemes, or just list $?
print("="*70)
print("Per-course fees page — does body mention FEE-HELP/HECS/loan? (sample 8)")
cf=[u for u in idx if re.search(r'/find/courses/.+/fees/?$',u)][:8]
for u in cf:
    d,m=idx[u]; t=text(d)
    present=[term for term in ['FEE-HELP','HECS','Commonwealth supported','loan','census','SA-HELP'] if re.search(re.escape(term),t,re.I)]
    slug=u.replace('https://study.unimelb.edu.au/find/courses/','').replace('/fees/','')[:40]
    print(f"  {slug:40s} -> {present}")
