import json, glob, os, re, collections

CRAWL='/Users/djmulholland/Documents/Claude/projects/unimelb-current-students-ia/crawl'

# 1) Build a set of URLs that are 404 / error pages (by title) across ALL domains
not_found_paths = set()        # (host, normalized_path_with_query)
nf_examples = []
n_pages=0; n_404=0
title_404 = re.compile(r'page not found|not found|error 404', re.I)
for meta in glob.glob(f'{CRAWL}/*/pages/*/meta.json'):
    try: m=json.load(open(meta))
    except: continue
    n_pages+=1
    t=(m.get('title') or '').strip()
    if title_404.search(t):
        n_404+=1
        u=m['url']
        # store full url (strip scheme)
        key=u.split('://',1)[-1].rstrip('/')
        not_found_paths.add(key)
        if len(nf_examples)<15: nf_examples.append((u,t))
print(f'PAGES scanned: {n_pages}')
print(f'404/error-titled pages in corpus: {n_404}')
print('sample 404 pages:')
for u,t in nf_examples[:12]: print(f'   [{t}] {u}')
print()

# save the 404 url-key set
json.dump(sorted(not_found_paths), open('/Users/djmulholland/Documents/Claude/projects/unimelb-current-students-ia/scratchpad_404set.json','w'))
print('saved 404 set:', len(not_found_paths))
