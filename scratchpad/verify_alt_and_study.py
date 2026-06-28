import sys, glob, os, json, collections
sys.path.insert(0,'.')
from a11y_verify import ROOT, DOMAINS, parse_page, is_shell, iter_rendered, first_skip

# --- Claim 1: find a study page that actually has h1->h3 first skip (no h2) ---
print("=== STUDY pages whose FIRST skip is h1->h3 (analyst's claimed signature) ===")
found=0
for m,hp,html in iter_rendered(DOMAINS['study'], limit=250):
    p=parse_page(html)
    sk,j=first_skip(p.headings)
    if sk and j=='h1->h3':
        d=json.load(open(m))
        # confirm no h2 before that h3
        print("  ", d['url'][:90])
        print("     headings:", [(l,t[:30]) for l,t in p.headings[:5]])
        found+=1
        if found>=3: break
if not found: print("  (none with first-skip h1->h3 in sample)")

# --- Claim 4: alt-text. Count imgs missing alt, cluster by page. ---
print("\n=== IMG ALT across content domains (claim 4) ===")
test_domains = ['students','arts','law','alumni','mdhs','study','scholarships']
for key in test_domains:
    dirn=DOMAINS[key]
    pages=iter_rendered(dirn, limit=200)
    total_imgs=0; missing=0; pages_with_missing=collections.Counter()
    worst=[]
    for m,hp,html in pages:
        p=parse_page(html)
        miss=sum(1 for im in p.imgs if not im['has_alt'])
        total_imgs+=len(p.imgs); missing+=miss
        if miss>0:
            d=json.load(open(m))
            worst.append((miss, d['url']))
    worst.sort(reverse=True)
    pct = 100*missing/max(total_imgs,1)
    print(f"{key:14s} imgs={total_imgs:5d} missing_alt={missing:4d} ({pct:4.1f}%)  top-missing-pages:")
    for mm,u in worst[:3]:
        print(f"      {mm:3d} missing  {u[:80]}")
