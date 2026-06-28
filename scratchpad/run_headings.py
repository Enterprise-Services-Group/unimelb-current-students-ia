import sys, collections
sys.path.insert(0,'.')
from a11y_verify import DOMAINS, iter_rendered, parse_page, first_skip

# Claim 1: heading-skip. Claim 3: multi-h1.
# Analyst used "482 clean pages". We'll sample similarly across the SAME domains they cite.
# Their per-domain denominators: finearts 54, study 31, mbs 60, scholarships 196, law 42, fbe ?, services ?
# Let's process ALL rendered pages per cited domain (capped) and report.

cited = ['finearts-music','study','mbs','scholarships','law','fbe','services','mdhs','msd']
grand_total=0; grand_skip=0; grand_multi=0
per = {}
for key in cited:
    dirn = DOMAINS[key]
    pages = iter_rendered(dirn, limit=250)  # cap for speed
    nskip=0; nmulti=0; jumps=collections.Counter()
    for m,hp,html in pages:
        p = parse_page(html)
        sk, j = first_skip(p.headings)
        if sk:
            nskip+=1; jumps[j]+=1
        h1s = [t for l,t in p.headings if l==1]
        if len(h1s) > 1:
            nmulti+=1
    n=len(pages)
    per[key]=(n,nskip,nmulti,jumps)
    grand_total+=n; grand_skip+=nskip; grand_multi+=nmulti
    topj = ', '.join(f"{k} x{v}" for k,v in jumps.most_common(2))
    print(f"{key:16s} n={n:4d}  skip={nskip:4d} ({100*nskip/max(n,1):4.0f}%)  multi-h1={nmulti:3d} ({100*nmulti/max(n,1):3.0f}%)  topjumps[{topj}]")
print(f"\nTOTAL over cited domains (capped 250/dom): n={grand_total}  skip={grand_skip} ({100*grand_skip/max(grand_total,1):.0f}%)  multi-h1={grand_multi} ({100*grand_multi/max(grand_total,1):.0f}%)")
