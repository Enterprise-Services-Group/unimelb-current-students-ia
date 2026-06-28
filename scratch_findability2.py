import json, glob, os, re, collections
from urllib.parse import urlparse, urldefrag

CRAWL='/Users/djmulholland/Documents/Claude/projects/unimelb-current-students-ia/crawl'

def norm(u):
    if not u: return ''
    u=urldefrag(u)[0]; u=re.sub(r'\?.*$','',u); u=u.rstrip('/')
    u=re.sub(r'^https?://','',u).lower()
    return u

nf=set(json.load(open('/Users/djmulholland/Documents/Claude/projects/unimelb-current-students-ia/scratchpad_404set.json')))
nf_norm=set(norm('http://'+x) for x in nf)

# Pass: load pages, compute per-domain href frequency (for chrome stripping)
pages={}
dom_href_freq=collections.defaultdict(collections.Counter)
dom_pagecount=collections.Counter()
for mj in glob.glob(f'{CRAWL}/*/pages/*/meta.json'):
    pdir=os.path.dirname(mj)
    try:
        m=json.load(open(mj)); lk=json.load(open(f'{pdir}/links.json'))
    except: continue
    url=m.get('url',''); nu=norm(url)
    if not nu: continue
    dom=urlparse(url).netloc
    dom_pagecount[dom]+=1
    links=[]; seen=set()
    for L in lk.get('links',[]):
        nh=norm(L.get('href',''))
        if not nh: continue
        links.append((nh,(L.get('text','') or '').strip()))
        if nh not in seen:
            dom_href_freq[dom][nh]+=1; seen.add(nh)
    pages[nu]={'dom':dom,'links':links}

# chrome = href appearing on >60% of a domain's pages
chrome=collections.defaultdict(set)
for dom,cnt in dom_href_freq.items():
    thr=0.6*max(1,dom_pagecount[dom])
    for h,c in cnt.items():
        if c>=thr: chrome[dom].add(h)

# Count CONTEXTUAL inbound links pointing at 404 pages
ctx_to_404=collections.Counter()
total_ctx_to_404=0
vague=collections.Counter()
total_ctx_links=0
VAGUE_RE=re.compile(r'^(click here|here|read more|view more|learn more|more|find out more|view|read|link|this page|website|click|go|see more|details|view detailed information.*)$',re.I)
for nu,p in pages.items():
    dom=p['dom']; ch=chrome[dom]
    for nh,text in p['links']:
        if nh in ch: continue   # strip chrome
        total_ctx_links+=1
        # vague anchor?
        tt=text.strip()
        if not tt:
            vague['(no text/empty)']+=1
        elif VAGUE_RE.match(tt):
            vague[tt.lower()[:30]]+=1
        elif re.match(r'^https?://',tt) or tt.startswith('www.'):
            vague['(bare URL as anchor)']+=1
        # points to 404?
        if nh in nf_norm:
            ctx_to_404[nh]+=1; total_ctx_to_404+=1

print(f'=== BROKEN-LINK SCALE ===')
print(f'Total contextual links (chrome-stripped): {total_ctx_links:,}')
print(f'Contextual links pointing at 404/error pages: {total_ctx_to_404:,}')
print(f'Distinct 404 destinations receiving >=1 contextual link: {len(ctx_to_404):,}')
print(f'Share of contextual links that 404: {100*total_ctx_to_404/max(1,total_ctx_links):.2f}%')
print()
print('Top 20 most-linked-to 404 pages:')
for h,c in ctx_to_404.most_common(20):
    print(f'  {c:5d}  {h}')
print()
print(f'=== VAGUE ANCHOR TEXT (contextual links) ===')
nt=vague.get('(no text/empty)',0)
bu=vague.get('(bare URL as anchor)',0)
vsum=sum(vague.values())
print(f'Total vague/empty/bare-URL anchors: {vsum:,} ({100*vsum/max(1,total_ctx_links):.1f}% of contextual links)')
print(f'  (no text/empty): {nt:,}')
print(f'  (bare URL as anchor): {bu:,}')
print('Top vague phrases:')
for k,v in vague.most_common(18):
    print(f'  {v:6d}  {k}')

# save for reuse
json.dump({'total_ctx':total_ctx_links,'ctx_to_404':total_ctx_to_404,'distinct404':len(ctx_to_404),
           'top404':ctx_to_404.most_common(25),'vague_total':vsum,'no_text':nt,'bare_url':bu,
           'vague_top':vague.most_common(20)},
          open('/Users/djmulholland/Documents/Claude/projects/unimelb-current-students-ia/scratch_results.json','w'))
