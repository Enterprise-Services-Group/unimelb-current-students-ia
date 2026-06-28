import json, glob, os, re, collections
from urllib.parse import urlparse, urldefrag
CRAWL='/Users/djmulholland/Documents/Claude/projects/unimelb-current-students-ia/crawl'

def norm(u):
    if not u: return ''
    u=urldefrag(u)[0]; u=re.sub(r'\?.*$','',u); u=u.rstrip('/')
    u=re.sub(r'^https?://','',u).lower()
    return u

# How much of the estate's linking points INTO search/results pages vs real content?
# Identify "search/results/listing" destinations by URL+title signature.
search_re=re.compile(r'/search|[?&](query|queries|q|search_page|result_|current_result_page|page=)',re.I)
search_title=re.compile(r'^search\b|—\s*the university of melbourne handbook',re.I)

n_pages=0
search_pages=0     # pages that ARE search/results pages
# inbound contextual links to search pages:  reuse chrome strip quickly via per-dom freq
pages={}; dom_href_freq=collections.defaultdict(collections.Counter); dom_pc=collections.Counter()
page_is_search={}
for mj in glob.glob(f'{CRAWL}/*/pages/*/meta.json'):
    pdir=os.path.dirname(mj)
    try: m=json.load(open(mj)); lk=json.load(open(f'{pdir}/links.json'))
    except: continue
    url=m.get('url',''); nu=norm(url)
    if not nu: continue
    n_pages+=1
    dom=urlparse(url).netloc; dom_pc[dom]+=1
    t=(m.get('title') or '')
    raw=url.split('://',1)[-1]
    is_s = bool(search_re.search(url)) or bool(search_title.search(t.strip()))
    page_is_search[nu]=is_s
    if is_s: search_pages+=1
    links=[]; seen=set()
    for L in lk.get('links',[]):
        nh=norm(L.get('href','')); 
        if not nh: continue
        links.append(nh)
        if nh not in seen: dom_href_freq[dom][nh]+=1; seen.add(nh)
    pages[nu]={'dom':dom,'links':links,'rawhref':[ (norm(L.get('href','')),) for L in lk.get('links',[])]}

chrome=collections.defaultdict(set)
for dom,cnt in dom_href_freq.items():
    thr=0.6*max(1,dom_pc[dom])
    for h,c in cnt.items():
        if c>=thr: chrome[dom].add(h)

ctx_to_search=0; total_ctx=0
# also: how many DISTINCT search-result destinations get linked (deep-linked search)
search_dests=collections.Counter()
for nu,p in pages.items():
    ch=chrome[p['dom']]
    for nh in p['links']:
        if nh in ch: continue
        total_ctx+=1
        if page_is_search.get(nh):
            ctx_to_search+=1; search_dests[nh]+=1

print(f'Pages scanned: {n_pages:,}')
print(f'Pages that ARE search/results/listing pages: {search_pages:,} ({100*search_pages/n_pages:.1f}%)')
print(f'Total contextual links: {total_ctx:,}')
print(f'Contextual links pointing INTO search/results pages: {ctx_to_search:,} ({100*ctx_to_search/total_ctx:.1f}%)')
print(f'Distinct search/results destinations that are deep-linked: {len(search_dests):,}')
print('Top deep-linked search/results destinations:')
for h,c in search_dests.most_common(12): print(f'  {c:5d}  {h}')
