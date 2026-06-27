#!/usr/bin/env python3
"""Build the contextual link graph + evidence pack from the full estate scrape.

Input: crawl/<domain>/pages/<hash>/{meta.json,links.json} — 27k content pages,
each links.json carrying every outbound link's {href,text,hostname,path}.

Key idea: a link whose href appears on >60% of a domain's pages is GLOBAL NAV /
footer chrome, not a content connection. We strip chrome to isolate CONTEXTUAL
links — the real "who points to what, on purpose" graph. Everything downstream
(orphans, hubs, cross-site seams, the alumni/careers handoffs) uses that graph.

Outputs (analysis/full-scrape/): cross-site-flow.csv, hubs.csv, orphans.csv,
anchor-text.csv, dup-fingerprints.csv, contextual-crosslinks.csv, SUMMARY.md.
Deterministic. Run: python3 analysis/full-scrape/build_linkgraph.py
"""
import json, glob, os, collections, csv, re
from urllib.parse import urlparse, urldefrag

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'analysis/full-scrape')


def norm(u):
    if not u:
        return ''
    u = urldefrag(u)[0]
    u = re.sub(r'\?.*$', '', u)            # drop query
    u = u.rstrip('/')
    u = re.sub(r'^https?://', '', u).lower()
    return u


# ---- load all pages -------------------------------------------------------
pages = {}   # norm_url -> {domain,url,title,fp,links:[(nhref,host,path,text)]}
dom_href_freq = collections.defaultdict(collections.Counter)   # domain -> norm_href -> pages-containing
print("loading pages...")
for idx in sorted(glob.glob(os.path.join(ROOT, 'crawl/*/index.json'))):
    cdir = os.path.dirname(idx)
    for mj in glob.glob(f'{cdir}/pages/*/meta.json'):
        pdir = os.path.dirname(mj)
        try:
            m = json.load(open(mj)); lk = json.load(open(f'{pdir}/links.json'))
        except Exception:
            continue
        url = m.get('url', '')
        nu = norm(url)
        if not nu:
            continue
        dom = urlparse(url).netloc
        links = []
        seen_h = set()
        for L in lk.get('links', []):
            nh = norm(L.get('href', ''))
            if not nh:
                continue
            links.append((nh, L.get('hostname', ''), L.get('path', '') or '', (L.get('text', '') or '').strip()))
            if nh not in seen_h:
                dom_href_freq[dom][nh] += 1
                seen_h.add(nh)
        pages[nu] = {'domain': dom, 'url': url, 'title': m.get('title', ''),
                     'fp': m.get('fingerprint', ''), 'links': links}
print(f"  {len(pages)} pages")

# ---- detect chrome (href on >60% of a domain's pages) ---------------------
dom_pagecount = collections.Counter(p['domain'] for p in pages.values())
chrome = set()    # (domain, norm_href) that are global nav/footer
for dom, freq in dom_href_freq.items():
    n = dom_pagecount[dom]
    if n < 10:
        continue
    for nh, c in freq.items():
        if c >= 0.6 * n:
            chrome.add((dom, nh))
print(f"  chrome links flagged: {len(chrome)} (domain,href) pairs")

# ---- build contextual graph: inbound counts, cross-site flow ---------------
inbound = collections.Counter()                 # norm_url -> contextual inbound count
flow = collections.Counter()                    # (src_dom, dst_dom) contextual links
anchor = collections.defaultdict(collections.Counter)  # dst_dom -> anchor text counts
ctx_crosslinks = []                             # notable contextual cross-domain links
UNIMELB = re.compile(r'unimelb\.edu\.au$')
for nu, p in pages.items():
    sdom = p['domain']
    for nh, host, path, text in p['links']:
        if (sdom, nh) in chrome:
            continue                            # skip global nav/footer
        if not UNIMELB.search(host or ''):
            continue                            # internal-to-UoM only
        inbound[nh] += 1
        if host != sdom:
            flow[(sdom, host)] += 1
            anchor[host][text[:40] or '(no text)'] += 1

# ---- outputs --------------------------------------------------------------
os.makedirs(OUT, exist_ok=True)

# cross-site flow (contextual, domain->domain)
with open(f'{OUT}/cross-site-flow.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['src_domain', 'dst_domain', 'contextual_links'])
    for (s, d), c in flow.most_common():
        w.writerow([s, d, c])

# hubs: most contextually-linked-to pages
with open(f'{OUT}/hubs.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['inbound', 'domain', 'url', 'title'])
    for nu, c in inbound.most_common(150):
        p = pages.get(nu, {})
        w.writerow([c, p.get('domain', ''), p.get('url', nu), p.get('title', '')[:70]])

# orphans: crawled content pages with 0 contextual inbound (only reachable via chrome/search)
orphans = [(p['domain'], p['url'], p['title']) for nu, p in pages.items() if inbound.get(nu, 0) == 0]
orph_by_dom = collections.Counter(o[0] for o in orphans)
with open(f'{OUT}/orphans.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['domain', 'url', 'title'])
    for o in orphans:
        w.writerow([o[0], o[1], o[2][:70]])

# anchor text for key destinations
with open(f'{OUT}/anchor-text.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['dst_domain', 'anchor_text', 'count'])
    for dom in sorted(anchor, key=lambda d: -sum(anchor[d].values())):
        for txt, c in anchor[dom].most_common(8):
            w.writerow([dom, txt, c])

# duplicate content by fingerprint (same content hash on multiple URLs/domains)
fp_map = collections.defaultdict(list)
for nu, p in pages.items():
    if p['fp']:
        fp_map[p['fp']].append(p)
dups = {fp: ps for fp, ps in fp_map.items() if len(ps) > 1}
cross_dom_dups = {fp: ps for fp, ps in dups.items() if len({x['domain'] for x in ps}) > 1}
with open(f'{OUT}/dup-fingerprints.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['copies', 'domains', 'sample_title', 'sample_url'])
    for fp, ps in sorted(dups.items(), key=lambda kv: -len(kv[1]))[:200]:
        w.writerow([len(ps), len({x['domain'] for x in ps}), ps[0]['title'][:50], ps[0]['url']])

# ---- summary --------------------------------------------------------------
total_links = sum(len(p['links']) for p in pages.values())
ctx_links = sum(inbound.values())
with open(f'{OUT}/SUMMARY.md', 'w') as f:
    f.write("# Full-scrape link-graph — headline facts\n\n")
    f.write(f"- **{len(pages):,} content pages** across {len(dom_pagecount)} UoM domains; "
            f"{total_links:,} total outbound links, **{ctx_links:,} contextual** (chrome stripped).\n")
    f.write(f"- **{len(chrome):,}** global-nav/footer link patterns stripped as chrome.\n")
    f.write(f"- **Orphans:** {len(orphans):,} content pages have ZERO contextual inbound links "
            f"(reachable only via nav/search).\n")
    f.write(f"- **Duplicate content:** {len(dups):,} fingerprints on >1 URL; "
            f"{len(cross_dom_dups):,} span >1 domain.\n\n")
    f.write("## Orphan pages by domain (findability risk)\n\n| Domain | Orphans | Pages | % |\n|---|--:|--:|--:|\n")
    for d, n in dom_pagecount.most_common():
        o = orph_by_dom.get(d, 0)
        f.write(f"| {d} | {o} | {n} | {100*o/n:.0f}% |\n")
    f.write("\n## Top contextual cross-site flows\n\n| From | To | Contextual links |\n|---|---|--:|\n")
    for (s, d), c in flow.most_common(25):
        f.write(f"| {s} | {d} | {c} |\n")

print(f"\nwrote evidence pack to {OUT}/")
print(f"  pages={len(pages)} chrome={len(chrome)} orphans={len(orphans)} "
      f"dups={len(dups)} cross_dom_dups={len(cross_dom_dups)}")
print(f"  contextual cross-site flows: {len(flow)} domain pairs")
EOF_GUARD = None
