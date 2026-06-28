import sys, glob, os, json, collections, re
sys.path.insert(0,'.')
from a11y_verify import ROOT, DOMAINS, parse_page, is_shell, iter_rendered

# scholarships imgs: are they on search pages only, or every detail page?
print("=== scholarships: which pages carry the missing-alt imgs? ===")
dirn=DOMAINS['scholarships']
search_imgs=0; detail_imgs=0; detail_pages_with_img=0; search_pages=0; detail_pages=0
for m,hp,html in iter_rendered(dirn, limit=300):
    d=json.load(open(m)); url=d['url']
    p=parse_page(html)
    n=len(p.imgs)
    if 'search' in url or 'collection=' in url:
        search_imgs+=n; search_pages+=1
    else:
        detail_imgs+=n; detail_pages+=1
        if n>0: detail_pages_with_img+=1
print(f"search/listing pages={search_pages} imgs={search_imgs}")
print(f"detail pages={detail_pages} imgs={detail_imgs} (pages w/ >=1 img: {detail_pages_with_img})")

# Claim 5: target=_blank missing rel
print("\n=== TARGET=_BLANK missing rel=noopener (claim 5) ===")
total_blank=0; total_norel=0
for key in ['students','study','law','scholarships','mdhs','arts','services','fbe','alumni']:
    dirn=DOMAINS[key]
    tb=0; nr=0
    for m,hp,html in iter_rendered(dirn, limit=150):
        p=parse_page(html)
        tb+=p.target_blank; nr+=p.target_blank_no_rel
    total_blank+=tb; total_norel+=nr
    if tb: print(f"{key:14s} target_blank={tb:5d} no-rel={nr:5d} ({100*nr/max(tb,1):4.1f}%)")
print(f"TOTAL target_blank={total_blank} no-rel={total_norel} ({100*total_norel/max(total_blank,1):.1f}%)")
