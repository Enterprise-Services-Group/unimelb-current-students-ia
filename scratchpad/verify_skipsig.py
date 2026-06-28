import sys, collections
sys.path.insert(0,'.')
from a11y_verify import DOMAINS, iter_rendered, parse_page, first_skip

# Confirm scholarships dominant first-skip jump, and law/mbs.
for key in ['scholarships','law','mbs','fbe','finearts-music']:
    dirn=DOMAINS[key]
    jumps=collections.Counter()
    for m,hp,html in iter_rendered(dirn, limit=200):
        p=parse_page(html)
        sk,j=first_skip(p.headings)
        if sk: jumps[j]+=1
    print(f"{key:16s} first-skip jumps: {dict(jumps.most_common(4))}")

# Verify scholarships: do detail pages even have an h1? (h2->h4 implies h1 then h2 then jump)
print("\n=== scholarships heading shape (why h2->h4?) ===")
dirn=DOMAINS['scholarships']
shapes=collections.Counter()
for i,(m,hp,html) in enumerate(iter_rendered(dirn, limit=30)):
    p=parse_page(html)
    seq=[l for l,t in p.headings]
    shapes[tuple(seq[:5])]+=1
for s,c in shapes.most_common(6):
    print(f"  {c:3d}  first5-levels={s}")
