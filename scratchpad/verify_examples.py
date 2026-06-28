import sys, glob, os, json
sys.path.insert(0,'.')
from a11y_verify import ROOT, parse_page, is_shell

def find_by_url(dirn, urlpart):
    for m in glob.glob(f'{ROOT}/{dirn}/pages/*/meta.json'):
        d=json.load(open(m))
        if urlpart in d.get('url',''):
            return os.path.dirname(m), d
    return None, None

# Claim 3 example: mdhs research-library renders 11 h1s
pd, meta = find_by_url('mdhs-unimelb-edu-au','research/research-library')
if pd:
    html=open(os.path.join(pd,'page.html'),encoding='utf-8',errors='replace').read()
    print("=== mdhs research-library ===", meta['url'])
    print("shell?", is_shell(html), "bytes", len(html))
    p=parse_page(html)
    h1s=[t for l,t in p.headings if l==1]
    print(f"H1 count: {len(h1s)}")
    for t in h1s[:14]: print("  H1:", repr(t[:60]))
else:
    print("mdhs research-library NOT FOUND")

print()
# Claim 1 example: study change-of-preference/key-dates -> h1 then h3
pd, meta = find_by_url('study-unimelb-edu-au','change-of-preference/key-dates')
if not pd:
    pd, meta = find_by_url('study-unimelb-edu-au','change-of-preference')
if pd:
    html=open(os.path.join(pd,'page.html'),encoding='utf-8',errors='replace').read()
    print("=== study change-of-preference ===", meta['url'])
    print("shell?", is_shell(html))
    p=parse_page(html)
    print("First 6 headings:", [(l,t[:40]) for l,t in p.headings[:6]])
else:
    print("study change-of-preference NOT FOUND")
