#!/usr/bin/env python3
"""
near_dup.py — reproducible shingle-Jaccard near-duplicate detection.

Purpose
-------
Round-1 findings 4.1 (HDR candidature/thesis pages mirrored education<->mdhs),
4.2 (FBE /bcom/career vs MBS /career), and 4.3 ('Employability in X' clones)
cited shingle-Jaccard scores from an ad-hoc analysis that was never saved.
This script makes those claims reproducible end-to-end:

  1. Builds named candidate clusters by matching URL/title patterns in each
     domain's index.json (the fingerprint there == the page-dir name).
  2. Reads crawl/<domain>/pages/<fingerprint>/page.html, strips tags+boilerplate
     to visible text, lowercases, collapses whitespace.
  3. Computes word k-shingle (default k=8) Jaccard similarity for every pair
     WITHIN a cluster.
  4. Clusters pairs at THRESHOLD (default 0.85) via union-find and writes
     near-duplicates.csv (one row per scored pair >= a reporting floor).

Run:  python3 near_dup.py
Out:  near-duplicates.csv  (+ a console summary that confirms/corrects 4.1/4.2/4.3)

No network calls — operates entirely on the existing crawl corpus.
"""
import csv
import glob
import html
import json
import os
import re
import sys
from collections import defaultdict

# ---- config -----------------------------------------------------------------
CRAWL = os.path.join(os.path.dirname(__file__), "..", "..", "crawl")
CRAWL = os.path.abspath(CRAWL)
OUT_CSV = os.path.join(os.path.dirname(__file__), "near-duplicates.csv")
K = 8                    # shingle length (words)
THRESHOLD = 0.85         # clustering threshold (matches round-1's >=0.85 claim)
REPORT_FLOOR = 0.30      # write any pair >= this to the CSV so 4.3's 0.28-0.52 is visible

# ---- html -> text -----------------------------------------------------------
_SCRIPT_STYLE = re.compile(r"<(script|style|noscript|svg|head)\b[^>]*>.*?</\1>",
                           re.IGNORECASE | re.DOTALL)
_TAG = re.compile(r"<[^>]+>")
_WS = re.compile(r"\s+")
_NAV_HINT = re.compile(r"(skip to (main )?content|breadcrumb|cookie|©|acknowledg)",
                       re.IGNORECASE)


def html_to_text(raw: str) -> str:
    """Strip tags/scripts/styles, unescape entities, collapse whitespace, lowercase."""
    raw = _SCRIPT_STYLE.sub(" ", raw)
    # drop <head> already removed; remove comments
    raw = re.sub(r"<!--.*?-->", " ", raw, flags=re.DOTALL)
    txt = _TAG.sub(" ", raw)
    txt = html.unescape(txt)
    txt = _WS.sub(" ", txt).strip().lower()
    return txt


def shingles(text: str, k: int = K):
    words = text.split()
    if len(words) < k:
        return frozenset([" ".join(words)]) if words else frozenset()
    return frozenset(" ".join(words[i:i + k]) for i in range(len(words) - k + 1))


def jaccard(a: frozenset, b: frozenset) -> float:
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


# ---- corpus access ----------------------------------------------------------
def load_index(domain_dir: str):
    """Return list of {url,title,fingerprint,byteLength} for a crawl domain dir."""
    idx_path = os.path.join(CRAWL, domain_dir, "index.json")
    if not os.path.isfile(idx_path):
        return []
    with open(idx_path, encoding="utf-8") as f:
        idx = json.load(f)
    return idx.get("pages", [])


def page_text(domain_dir: str, fingerprint: str):
    p = os.path.join(CRAWL, domain_dir, "pages", fingerprint, "page.html")
    if not os.path.isfile(p):
        return None
    with open(p, encoding="utf-8", errors="replace") as f:
        return html_to_text(f.read())


def tail_after(url: str, marker: str) -> str:
    """Path tail after a marker substring, query stripped — for matching mirrors."""
    u = url.split("?")[0].split("#")[0].rstrip("/")
    i = u.find(marker)
    return u[i + len(marker):] if i >= 0 else u


# ---- candidate cluster builders ---------------------------------------------
def build_clusters():
    """
    Returns dict: cluster_name -> list of dicts {domain_dir,url,title,fingerprint,key}
    'key' is the comparable path-tail used to pair mirrors across domains
    (None means 'compare everything in the cluster pairwise', used for 4.3).
    """
    clusters = {}

    # --- 4.1 HDR candidature/thesis: education vs mdhs (mirror by path tail) ---
    hdr = []
    for dom, marker in [
        ("education-unimelb-edu-au", "/study/graduate-research/current-students/"),
        ("mdhs-unimelb-edu-au", "/research/research-training/current-students/"),
    ]:
        for p in load_index(dom):
            if marker in p["url"]:
                hdr.append({
                    "domain_dir": dom, "url": p["url"], "title": p.get("title", ""),
                    "fingerprint": p["fingerprint"],
                    "key": tail_after(p["url"], marker),
                })
    clusters["4.1_HDR_education_vs_mdhs"] = hdr

    # --- 4.2 BCom careers: FBE /bcom/career vs MBS /career (mirror by tail) ----
    careers = []
    for dom, marker in [
        ("fbe-unimelb-edu-au", "/bcom/career/"),
        ("mbs-unimelb-edu-au", "/career/"),
    ]:
        for p in load_index(dom):
            if marker in p["url"]:
                careers.append({
                    "domain_dir": dom, "url": p["url"], "title": p.get("title", ""),
                    "fingerprint": p["fingerprint"],
                    "key": tail_after(p["url"], marker),
                })
    clusters["4.2_BCom_careers_FBE_vs_MBS"] = careers

    # --- 4.3 'Employability in X' template clones (compare all pairwise) -------
    emp = []
    for f in sorted(glob.glob(os.path.join(CRAWL, "*", "index.json"))):
        dom = os.path.basename(os.path.dirname(f))
        for p in load_index(dom):
            t = (p.get("title") or "").lower()
            if t.startswith("employability in") or t == "employability":
                # science page is titled just 'Employability'
                if "employability" in t and "/student" in p["url"] or t.startswith("employability"):
                    emp.append({
                        "domain_dir": dom, "url": p["url"], "title": p.get("title", ""),
                        "fingerprint": p["fingerprint"], "key": None,
                    })
    clusters["4.3_Employability_in_X"] = emp

    return clusters


# ---- pairing / scoring ------------------------------------------------------
def score_cluster(name, members):
    """
    Yields rows (dicts) for pairs.
    If members carry a non-None 'key', only pairs that share the same key across
    DIFFERENT domains are scored (mirror detection, 4.1/4.2). Otherwise all
    cross-domain pairs are scored (4.3).
    Returns (rows, text_cache) where rows is a list of pair dicts.
    """
    # load text once per member
    tcache = {}
    for m in members:
        txt = page_text(m["domain_dir"], m["fingerprint"])
        m["_text"] = txt
        m["_shingles"] = shingles(txt) if txt else frozenset()
        m["_words"] = len(txt.split()) if txt else 0

    rows = []
    keyed = members and members[0].get("key") is not None

    if keyed:
        bykey = defaultdict(list)
        for m in members:
            bykey[m["key"]].append(m)
        for key, group in bykey.items():
            # only cross-domain pairs (a mirror = same tail on 2 different domains)
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    a, b = group[i], group[j]
                    if a["domain_dir"] == b["domain_dir"]:
                        continue
                    sim = jaccard(a["_shingles"], b["_shingles"])
                    rows.append(_row(name, a, b, sim, key))
    else:
        for i in range(len(members)):
            for j in range(i + 1, len(members)):
                a, b = members[i], members[j]
                sim = jaccard(a["_shingles"], b["_shingles"])
                rows.append(_row(name, a, b, sim, ""))
    return rows


def _row(cluster, a, b, sim, key):
    return {
        "cluster": cluster,
        "jaccard": round(sim, 4),
        "shared_key": key,
        "url_a": a["url"], "url_b": b["url"],
        "domain_a": a["domain_dir"], "domain_b": b["domain_dir"],
        "words_a": a["_words"], "words_b": b["_words"],
        "shell_a": int(a["_words"] < 50), "shell_b": int(b["_words"] < 50),
    }


# ---- union-find clustering at THRESHOLD --------------------------------------
class UF:
    def __init__(self):
        self.p = {}

    def find(self, x):
        self.p.setdefault(x, x)
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[ra] = rb


def main():
    if not os.path.isdir(CRAWL):
        sys.exit(f"crawl dir not found: {CRAWL}")
    clusters = build_clusters()
    all_rows = []
    summary = {}

    for name, members in clusters.items():
        rows = score_cluster(name, members)
        all_rows.extend(rows)
        # union-find at threshold over the pairs in this cluster
        uf = UF()
        n_at_thresh = 0
        for r in rows:
            if r["jaccard"] >= THRESHOLD:
                uf.union(r["url_a"], r["url_b"])
                n_at_thresh += 1
        groups = defaultdict(set)
        for r in rows:
            if r["jaccard"] >= THRESHOLD:
                groups[uf.find(r["url_a"])].add(r["url_a"])
                groups[uf.find(r["url_b"])].add(r["url_b"])
        scored = [r["jaccard"] for r in rows]
        summary[name] = {
            "members": len(members),
            "pairs_scored": len(rows),
            "pairs_ge_threshold": n_at_thresh,
            "clusters_ge_threshold": len(groups),
            "urls_in_dup_clusters": sum(len(g) for g in groups.values()),
            "min": round(min(scored), 4) if scored else None,
            "max": round(max(scored), 4) if scored else None,
            "median": round(sorted(scored)[len(scored)//2], 4) if scored else None,
        }

    # write CSV (pairs >= REPORT_FLOOR), sorted by cluster then jaccard desc
    out = [r for r in all_rows if r["jaccard"] >= REPORT_FLOOR]
    out.sort(key=lambda r: (r["cluster"], -r["jaccard"]))
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=[
            "cluster", "jaccard", "shared_key", "domain_a", "domain_b",
            "url_a", "url_b", "words_a", "words_b", "shell_a", "shell_b"])
        w.writeheader()
        w.writerows(out)

    # console summary
    print(f"k={K} threshold={THRESHOLD}  ->  {OUT_CSV}  ({len(out)} rows >= {REPORT_FLOOR})\n")
    for name, s in summary.items():
        print(f"[{name}]")
        for kk, vv in s.items():
            print(f"    {kk}: {vv}")
        print()


if __name__ == "__main__":
    main()
