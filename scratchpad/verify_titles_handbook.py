import sys, glob, os, json, collections, re
sys.path.insert(0,'.')
from a11y_verify import ROOT, DOMAINS, parse_page, is_shell, iter_rendered

# Claim 2: scholarships title uniqueness over ALL rendered detail pages
print("=== CLAIM 2: scholarships <title> uniqueness (all rendered) ===")
dirn=DOMAINS['scholarships']
titles=collections.Counter(); n=0
for m,hp,html in iter_rendered(dirn):  # NO limit - full
    p=parse_page(html); titles[p.title or '(none)']+=1; n+=1
print(f"rendered pages={n}, distinct titles={len(titles)}")
for t,c in titles.most_common(5):
    print(f"  {c:5d} ({100*c/n:4.1f}%)  {t[:65]!r}")

# mdhs 'Search' duplicate group claim
print("\n=== mdhs title duplicates (analyst: 'Search' x18) ===")
dirn=DOMAINS['mdhs']
titles=collections.Counter(); n=0
for m,hp,html in iter_rendered(dirn, limit=400):
    p=parse_page(html); titles[p.title or '(none)']+=1; n+=1
print(f"mdhs sampled={n}")
for t,c in titles.most_common(4):
    print(f"  {c:4d}  {t[:55]!r}")

# Claim 8: handbook shells
print("\n=== CLAIM 8: handbook Incapsula shells ===")
dirn=DOMAINS['handbook']
metas=glob.glob(f'{ROOT}/{dirn}/pages/*/meta.json')
shell=0; rendered=0; empty_title=0; total=0
subj_course_shell=0; subj_course_total=0
for m in metas:
    pd=os.path.dirname(m); hp=os.path.join(pd,'page.html')
    if not os.path.exists(hp): continue
    total+=1
    d=json.load(open(m)); url=d.get('url','')
    html=open(hp,encoding='utf-8',errors='replace').read()
    sh = ('Request unsuccessful' in html) or (len(html)<1500)
    is_sc = '/subjects/' in url or '/courses/' in url
    if is_sc: subj_course_total+=1
    if sh:
        shell+=1
        if is_sc: subj_course_shell+=1
        if not d.get('title'): empty_title+=1
    else:
        rendered+=1
print(f"handbook total-with-html={total} shells={shell} ({100*shell/max(total,1):.0f}%) rendered={rendered}")
print(f"  subject/course URLs={subj_course_total} of which shell={subj_course_shell} ({100*subj_course_shell/max(subj_course_total,1):.0f}%)")
