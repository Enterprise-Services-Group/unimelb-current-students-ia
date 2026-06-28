import sys, glob, os, json, collections, re
sys.path.insert(0,'.')
from a11y_verify import ROOT, DOMAINS, is_shell

# Claim 6: generic link text + href="#" on students.unimelb
print("=== CLAIM 6: generic link text & href=# on students ===")
dirn=DOMAINS['students']
generic_re = re.compile(r'>\s*(show more|find out more|learn more|more information|read more|click here)\s*<', re.I)
href_hash_generic=0
phrase_counts=collections.Counter()
total_links=0; generic_links=0
example_page=None
for m in glob.glob(f'{ROOT}/{dirn}/pages/*/meta.json'):
    pd=os.path.dirname(m); hp=os.path.join(pd,'page.html')
    if not os.path.exists(hp): continue
    html=open(hp,encoding='utf-8',errors='replace').read()
    if is_shell(html): continue
    d=json.load(open(m))
    # count anchors
    anchors = re.findall(r'<a\b[^>]*>(.*?)</a>', html, re.I|re.S)
    total_links += len(anchors)
    for a in anchors:
        txt = re.sub(r'<[^>]+>','',a).strip().lower()
        if txt in ('show more','find out more','learn more','more information','read more','click here'):
            phrase_counts[txt]+=1; generic_links+=1
    # href="#" with generic text
    for mt in re.finditer(r'<a\b[^>]*href\s*=\s*["\']#["\'][^>]*>(.*?)</a>', html, re.I|re.S):
        t=re.sub(r'<[^>]+>','',mt.group(1)).strip().lower()
        if t in ('show more','find out more','learn more','more information','read more'):
            href_hash_generic+=1
            if 'workshops-and-sessions' in d.get('url','') and example_page is None:
                example_page=d['url']
print(f"students rendered links scanned={total_links} generic-text links={generic_links} ({100*generic_links/max(total_links,1):.2f}%)")
print("phrase counts:", dict(phrase_counts))
print(f"href='#' + generic text instances: {href_hash_generic}")
print("workshops example present:", example_page)

# Claim 7: privacy_pref radios with commented-out label, {{opt_in}} unsubstituted
print("\n=== CLAIM 7: privacy_pref consent radios (students) ===")
found=0; commented=0; mustache=0; pages_with=0
for m in glob.glob(f'{ROOT}/{dirn}/pages/*/meta.json'):
    pd=os.path.dirname(m); hp=os.path.join(pd,'page.html')
    if not os.path.exists(hp): continue
    html=open(hp,encoding='utf-8',errors='replace').read()
    if 'privacy_pref_optin' in html:
        pages_with+=1
        if '<!-- <label for="privacy_pref_optin">' in html or re.search(r'<!--\s*<label for="privacy_pref', html):
            commented+=1
        if '{{opt_in}}' in html or '{{ opt_in }}' in html:
            mustache+=1
print(f"pages with privacy_pref_optin radio: {pages_with}")
print(f"  with commented-out <label>: {commented}")
print(f"  with literal {{{{opt_in}}}} token unrendered: {mustache}")
