#!/usr/bin/env python3
"""
Phase I — Internal audit cleanup pipeline.

Reads the frozen per-unit JSON in crawl/pages/*.json, applies the Bucket-A
data/synthesis corrections (D1-D14) as explicit, logged transforms, and writes
a cleaned dataset + regenerated count tables + a reconciliation changelog to
data/clean/.

Baseline inputs are NOT modified. Deterministic: same inputs -> same outputs.

Reuses tag_page()/classify()/TAG_RULES from crawl/_process_mbs.py, with the
corrected rules for IT-systems (D2) and graduation (D12).
"""
import csv
import json
import os
import re
import statistics
from collections import Counter, defaultdict
from urllib.parse import urlparse

ROOT = "/Users/djmulholland/Documents/Claude/projects/unimelb-current-students-ia"
PAGES_DIR = f"{ROOT}/crawl/pages"
OUT_DIR = f"{ROOT}/data/clean"
os.makedirs(OUT_DIR, exist_ok=True)

# unit_slug -> (faculty label, level). Current-students estate + the two separate corpora.
UNIT_META = {
    "abp": ("ABP", "faculty"), "arts": ("Arts", "faculty"),
    "biomedical": ("MDHS", "school"), "dental": ("MDHS", "school"),
    "education": ("Education", "faculty"), "fbe": ("FBE", "faculty"),
    "feit": ("FEIT", "faculty"), "ffam": ("FFAM", "faculty"),
    "law": ("Law", "faculty"), "mbs": ("FBE", "school"),
    "mdhs": ("MDHS", "faculty"), "science": ("Science", "faculty"),
    "study-unimelb": ("study", "site"), "alumni-unimelb": ("alumni", "site"),
}
CORPUS = {s: ("study" if s == "study-unimelb" else "alumni" if s == "alumni-unimelb"
              else "current-students") for s in UNIT_META}
# topic-faculty-matrix column order (the 12 current-students units)
CS_UNITS = ["law", "feit", "arts", "science", "abp", "fbe",
            "education", "ffam", "mdhs", "mbs", "biomedical", "dental"]

# ---- D5: chrome hosts + binary assets -----------------------------------
def is_chrome_host(h):
    h = h.lower()
    if h in ("www.unimelb.edu.au", "about.unimelb.edu.au", "safety.unimelb.edu.au"):
        return True
    return any(s in h for s in ("facebook.", "linkedin.", "instagram."))

BINARY_EXT = re.compile(r"\.(pdf|xlsx?|docx?|pptx?|csv|zip)(\?|$)", re.I)

# ---- Topic tagging (corrected TAG_RULES) --------------------------------
# Base ruleset lifted from crawl/_process_mbs.py. CORRECTIONS:
#  D2  IT-systems: was r"\bIT\b|computing|...|systems|...|portal..." which fired on
#      "Engineering & IT" and bare "systems"/"portal". Now service-specific only.
#  D12 graduation -> graduation-ceremony (ceremony tokens only, drop bare "graduat"
#      stem) + route graduate-research/HDR signals into research-candidature.
TAG_RULES = [
    ("enrolment", r"\benrol|enrolment|enrolling|census date|study load|withdraw\b"),
    ("course-planning", r"course plan|course planning|study plan|program structure|sequenc|advanced standing|credit|subject selection|core subject|elective"),
    ("subjects-timetable", r"timetable|class registration|subject|lecture|tutorial|breadth"),
    ("exams-results", r"\bexam|assessment|results|grade|hurdle|special exam|supplementary"),
    ("special-consideration", r"special consideration|extension|academic adjustment"),
    ("fees-finance", r"\bfee|fees|tuition|finance|payment|invoice|loan|FEE-HELP|HECS"),
    ("scholarships", r"scholarship|bursary|stipend|grant\b"),
    ("placements-WIL", r"placement|internship|work integrated|industry project|WIL|practicum"),
    ("careers-employability", r"career|employab|employment|job|professional development|industry connect|networking"),
    # Phase II: dropped bare writing/maths/learning (matched "Experiential Learning",
    # "Academic resources", studio names). Require academic-support-specific phrasing.
    ("academic-skills", r"academic skill|study skill|academic support|academic writing|essay writing|\breferencing\b|numeracy|maths support|language and learning|learning (?:skill|advis|lab|hub|support)|writing (?:skill|support|centre|guide)|peer (?:assisted|learning|mentor)|\bPASS\b|study (?:support|advice|smarter)"),
    ("student-life", r"student life|community|peer|ambassador|society|representativ"),
    ("clubs-events", r"\bclub|event|workshop|seminar|networking event"),
    ("wellbeing-health", r"wellbeing|wellness|health|counsel|mental health|safer community|support service"),
    # D2 corrected: drop bare \bIT\b (caught "Engineering & IT") and bare systems/portal,
    # but keep genuine IT-service signals incl. computing/computer-space (the FEIT
    # faculty-abbrev pages contain neither, so they stay excluded).
    ("IT-systems", r"wi-?fi|eduroam|\bvpn\b|password (?:reset|manager)|computing|computer (?:lab|space|facilit|requirement|access)|software (?:download|licen|catalog|access)|\blms\b|canvas|my\.unimelb|student email|email account|IT (?:help|support|service|facilit)|services and it|service desk|student ?it\b|multi-factor|\bMFA\b|printing|unimelb account"),
    ("library", r"\blibrary|librarie"),
    # D12 corrected: ceremony-only (dropped bare "graduat" which caught "graduate research")
    ("graduation-ceremony", r"graduation ceremony|award ceremony|conferral|testamur|parchment|\bAHEGS\b|apply to graduate|applying to graduate|eligibility to graduate|graduate in absentia"),
    ("forms-admin", r"\bform\b|application form|administration|admin|request|apply for|how to apply"),
    ("contacts-support", r"contact|stop ?1|stop one|enquir|help|ask\b|student centre|reception|support team|get in touch"),
    # D12: absorb graduate-research / HDR signals here
    ("research-candidature", r"candidatur|PhD|doctora|thesis|research pathway|MPhil|research student|graduate research|graduate researcher|\bHDR\b|higher degree"),
    ("international", r"international|dual degree|exchange|overseas|inbound|outbound|study abroad|visa|CoE|global"),
    ("inclusion-equity", r"indigenous|inclusion|equity|accessibilit|disabilit|diversity"),
    # Tightened: bare "welcome"/"commencing"/"new student" over-fired (esp. FEIT excerpts).
    # Require orientation-specific phrasing.
    ("orientation", r"\borientation\b|getting started|welcome week|welcome to (?:the )?(?:university|unimelb|melbourne)|first week|commencing student|new students?(?: start| guide| checklist| to| should)|start of (?:semester|year|your studies)|o-?week|o-?day"),
]
COMPILED = [(t, re.compile(p, re.I)) for t, p in TAG_RULES]


def hays_of(rec, denest=False):
    """Return (title+path, excerpt) lowercased separately so the two signals can be
    weighted. Phase II: a single tangential excerpt mention must NOT qualify a tag."""
    path = urlparse(rec.get("normalizedUrl") or rec["url"]).path
    if denest:
        # D11: strip the FEIT /student-experience/orientation/ ancestor so it stops
        # driving the orientation tag for non-orientation content.
        path = re.sub(r"/student-experience/orientation(?=/)", "", path)
    tp = (rec.get("title", "") or "") + " " + path.replace("-", " ").replace("/", " ")
    return tp.lower(), (rec.get("excerpt", "") or "").lower()


def tag_page(rec, denest=False):
    # Phase II weighted scoring: a tag qualifies only if it matches the title/path
    # (strong signal) OR appears >=2x in the excerpt (sustained signal). This kills
    # tangential single-excerpt false positives (e.g. a course-plan page that mentions
    # "internship" once -> placements-WIL). Title/path hits weighted 2x.
    tp, ex = hays_of(rec, denest)
    scored, anyhit = [], []
    for tag, pat in COMPILED:
        tph = len(pat.findall(tp))
        exh = len(pat.findall(ex))
        if tph or exh:
            anyhit.append((2 * tph + exh, tag))
        if tph >= 1 or exh >= 2:
            scored.append((2 * tph + exh, tag))
    scored.sort(reverse=True)
    if scored:
        return [t for _, t in scored[:4]]
    # Fallback: a page with only tangential hits keeps its SINGLE strongest tag
    # (rescues topical pages like "Diploma in Languages" without re-adding 4 loose tags).
    if anyhit:
        anyhit.sort(reverse=True)
        return [anyhit[0][1]]
    return ["<untagged>"]


# ---- Classification (recomputed uniformly) ------------------------------
def classify(rec):
    wc = rec.get("wordCount", 0) or 0
    status = rec.get("status")
    if rec.get("classification") == "redirect" or rec.get("is404") or rec.get("redirectedOffHost") \
       or (isinstance(status, int) and status in (301, 302, 303, 307, 308)):
        return "redirect"
    outbound_total = sum((rec.get("outboundHosts") or {}).values())
    hub = rec.get("hubLinks", 0) or 0
    central = (rec.get("outboundHosts") or {}).get("students.unimelb.edu.au", 0)
    if wc < 160 and (outbound_total >= 10 or hub > 0):
        return "link-farm"
    if wc >= 160:
        if central >= 6 or hub >= 6:
            return "mixed"
        return "unique"
    return "link-farm"


# ---- D1: page_type ------------------------------------------------------
# Precise, directory-anchored detection (validated against the real collections:
# Law /students/grd/students/<person> = 66 GRD bios; Science committee-bios/
# committee-members/<person> = 28 SSRC bios; MSD studio archives in abp.json).
ARCHIVE_TOKENS = re.compile(r"past-studio|studio-archive|/archives?/", re.I)
PROFILE_PATH = re.compile(
    r"/grd/students/[^/]+$"                                    # Law GRD researcher bios
    r"|(?:committee-bios|committee-members|-bios)/[^/]+$"      # Science SSRC bios
    r"|/(?:our-people|people|our-staff|staff|profiles?|researchers?|mentors|ambassadors"
    r"|student-profiles|alumni-profiles|chancellors-scholars|our-students|student-stories"
    r"|council|board)/[^/]+$", re.I)
PERSON_SLUG = re.compile(r"^[a-z]+(?:-[a-z]+){1,3}$")


def page_type(rec, cls):
    if cls == "redirect":
        return "redirect"
    url = rec.get("normalizedUrl") or rec["url"]
    path = urlparse(url).path
    title = (rec.get("title", "") or "").strip()
    wc = rec.get("wordCount", 0) or 0
    slug = rec["unit_slug"]
    # archive (D3) — MSD studio archives (gated to ABP so bare-year paths elsewhere don't match)
    if ARCHIVE_TOKENS.search(path) or "past studio" in title.lower():
        return "archive"
    if slug == "abp" and re.search(r"/(?:19|20)\d\dm?(?:-and-(?:19|20)?\d\dm?)?/?$", path):
        return "archive"  # year-as-final-segment index (e.g. /past-studios/2019), not /2026-subjects-...
    # profile (D1) — person pages directly under a people-collection directory
    seg = [s for s in path.split("/") if s]
    if seg and PROFILE_PATH.search(path) and PERSON_SLUG.match(seg[-1]) and wc < 900:
        return "profile"
    if wc < 160:
        return "stub"
    return "content"


# ---- D13: canonical URL + dedup -----------------------------------------
def canon(u):
    p = urlparse(u)
    path = re.sub(r"/_(?:no|re)cache(?=/|$)", "", p.path).rstrip("/").lower()
    return p.netloc.lower(), path


# ---- Load + normalise (step 1) ------------------------------------------
def load_unit(slug):
    fp = f"{PAGES_DIR}/{slug}.json"
    d = json.load(open(fp))
    pages = d["pages"] if isinstance(d, dict) and "pages" in d else d
    fac, level = UNIT_META[slug]
    out = []
    for rec in pages:
        rec = dict(rec)
        rec["unit_slug"] = slug
        rec["faculty"] = fac
        rec["level"] = level
        rec["corpus"] = CORPUS[slug]
        out.append(rec)
    return out


changelog = []  # (section, line)
def log(section, line):
    changelog.append((section, line))


records = []
for slug in UNIT_META:
    records.extend(load_unit(slug))
raw_total = len(records)
log("load", f"Loaded {raw_total} pages across {len(UNIT_META)} units "
            f"({sum(1 for r in records if r['corpus']=='current-students')} current-students, "
            f"{sum(1 for r in records if r['corpus']=='study')} study, "
            f"{sum(1 for r in records if r['corpus']=='alumni')} alumni).")

# ---- D13 dedup ----------------------------------------------------------
# Pass 1: exact canonical collisions (handles _nocache/_recache/trailing-slash/query)
groups = defaultdict(list)
for r in records:
    groups[(r["unit_slug"], canon(r.get("normalizedUrl") or r["url"]))].append(r)
deduped, collapse_by_unit = [], Counter()
for key, grp in groups.items():
    if len(grp) == 1:
        deduped.append(grp[0])
        continue
    grp.sort(key=lambda r: -(r.get("wordCount", 0) or 0))
    deduped.append(grp[0])
    collapse_by_unit[key[0]] += len(grp) - 1
    for dropped in grp[1:]:
        log("dedup", f"  collapsed twin [{key[0]}]: {dropped.get('url')} -> {grp[0].get('url')}")

# Pass 2: trailing-digit twins (X2 -> X when base X present in same unit)
present = defaultdict(set)
for r in deduped:
    present[r["unit_slug"]].add(canon(r.get("normalizedUrl") or r["url"])[1])
keep, digit_twins = [], Counter()
for r in deduped:
    host, path = canon(r.get("normalizedUrl") or r["url"])
    seg = path.rsplit("/", 1)
    base = None
    if seg[-1] and re.search(r"[a-z]\d+$", seg[-1]):
        cand = (seg[0] + "/" if len(seg) == 2 else "") + re.sub(r"\d+$", "", seg[-1])
        cand = cand.rstrip("/")
        if cand in present[r["unit_slug"]] and cand != path:
            base = cand
    if base:
        digit_twins[r["unit_slug"]] += 1
        log("dedup", f"  collapsed digit-twin [{r['unit_slug']}]: {path} -> {base}")
    else:
        keep.append(r)
records = keep
for u in CS_UNITS:
    tot = collapse_by_unit[u] + digit_twins[u]
    if tot:
        log("dedup", f"{u}: collapsed {tot} URL twins "
                     f"({collapse_by_unit[u]} canonical + {digit_twins[u]} digit).")
dedup_total = collapse_by_unit.total() + digit_twins.total() if hasattr(collapse_by_unit, "total") \
    else sum(collapse_by_unit.values()) + sum(digit_twins.values())
log("dedup", f"TOTAL collapsed: {dedup_total}. {raw_total} -> {len(records)} canonical pages.")

# ---- D1 page_type + D5 flags + D2/D12 re-tag + classify -----------------
for r in records:
    r["topicTags_old"] = r.get("topicTags", []) or []
    cls = classify(r)
    r["classification_clean"] = cls
    r["page_type"] = page_type(r, cls)
    if r["corpus"] == "current-students":
        # Full re-tag scoped to the current-students estate (where the findings + count
        # tables live). study/alumni keep their purpose-built specialized tags
        # (e.g. alumni-careers-mentoring), so the established alumni careers=38 holds.
        r["topicTags_new"] = tag_page(r, denest=(r["unit_slug"] == "feit"))
    else:
        r["topicTags_new"] = list(r["topicTags_old"])
    url = r.get("normalizedUrl") or r["url"]
    r["is_binary"] = bool(BINARY_EXT.search(url))
    r["exclude_from_wordstats"] = r["is_binary"]

# page_type tallies
pt = Counter(r["page_type"] for r in records if r["corpus"] == "current-students")
log("page_type", f"Current-students page_type split: " +
    ", ".join(f"{k}={v}" for k, v in pt.most_common()))
binset = [r for r in records if r["is_binary"]]
log("D5", f"Binary-asset URLs flagged (excluded from word stats): {len(binset)} "
         f"({sum(1 for r in binset if r['corpus']=='study')} on study).")
log("D5", f"Chrome hosts excluded from link aggregation: www.unimelb, about.unimelb, "
         f"safety.unimelb, facebook, linkedin, instagram.")

# ---- Helpers ------------------------------------------------------------
def write_csv(name, header, rows):
    with open(f"{OUT_DIR}/{name}", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def top_outbound(rec, n=3):
    hosts = [(h, c) for h, c in (rec.get("outboundHosts") or {}).items() if not is_chrome_host(h)]
    hosts.sort(key=lambda x: -x[1])
    return ";".join(f"{h}:{c}" for h, c in hosts[:n])


def pipe(tags):
    return "|".join(tags)


cs = [r for r in records if r["corpus"] == "current-students"]
cs_content = [r for r in cs if r["page_type"] == "content"]

# ---- pages-clean.csv (master, all corpora) ------------------------------
write_csv("pages-clean.csv",
          ["unit_slug", "faculty", "level", "corpus", "page_type", "classification",
           "wordCount", "depth", "hubLinks", "url", "title", "topicTags", "topicTags_old",
           "is_binary"],
          [[r["unit_slug"], r["faculty"], r["level"], r["corpus"], r["page_type"],
            r["classification_clean"], r.get("wordCount", 0), r.get("depth", 0),
            r.get("hubLinks", 0), r["url"], r.get("title", ""),
            pipe(r["topicTags_new"]), pipe(r["topicTags_old"]), int(r["is_binary"])]
           for r in records])

# ---- pages-by-topic.clean.csv (content-only, new tags) ------------------
rows = []
for r in cs_content:
    for t in r["topicTags_new"]:
        rows.append([t, r["unit_slug"], r["faculty"], r["url"], r.get("title", ""),
                     r.get("wordCount", 0), r["classification_clean"], r["page_type"]])
rows.sort(key=lambda x: (x[0], x[1]))
write_csv("pages-by-topic.clean.csv",
          ["topic", "unit_slug", "faculty", "url", "title", "wordCount", "classification", "page_type"],
          rows)

# ---- topic-faculty-matrix.clean.csv (content-only counts) ---------------
mat = defaultdict(lambda: Counter())
for r in cs_content:
    for t in r["topicTags_new"]:
        mat[t][r["unit_slug"]] += 1
topic_order = sorted(mat, key=lambda t: -sum(mat[t].values()))
mrows = []
for t in topic_order:
    total = sum(mat[t].values())
    mrows.append([t, total] + [mat[t].get(u, 0) for u in CS_UNITS])
write_csv("topic-faculty-matrix.clean.csv", ["topic", "total"] + CS_UNITS, mrows)

# ---- unique-vs-linkfarm.clean.csv (CS, chrome stripped) -----------------
write_csv("unique-vs-linkfarm.clean.csv",
          ["unit_slug", "faculty", "classification", "page_type", "wordCount", "hubLinks",
           "url", "title", "topOutboundHosts_exclChrome"],
          [[r["unit_slug"], r["faculty"], r["classification_clean"], r["page_type"],
            r.get("wordCount", 0), r.get("hubLinks", 0), r["url"], r.get("title", ""),
            top_outbound(r)] for r in sorted(cs, key=lambda r: (r["unit_slug"], r.get("depth", 0)))])

# ---- url-inventory.clean.csv (CS) ---------------------------------------
write_csv("url-inventory.clean.csv",
          ["unit_slug", "faculty", "level", "page_type", "url", "title", "wordCount",
           "classification", "topics"],
          [[r["unit_slug"], r["faculty"], r["level"], r["page_type"], r["url"],
            r.get("title", ""), r.get("wordCount", 0), r["classification_clean"],
            pipe(r["topicTags_new"])] for r in sorted(cs, key=lambda r: (r["unit_slug"], r.get("depth", 0)))])

# ---- D4: topic false-positive rates (old-all vs new-content) ------------
old_counts, new_all, new_content = Counter(), Counter(), Counter()
for r in cs:
    for t in set(r["topicTags_old"]):
        old_counts[t] += 1
    for t in set(r["topicTags_new"]):
        new_all[t] += 1
        if r["page_type"] == "content":
            new_content[t] += 1
all_topics = sorted(set(old_counts) | set(new_all), key=lambda t: -old_counts.get(t, 0))
fp_rows = []
for t in all_topics:
    oc = old_counts.get(t, 0)
    nc = new_content.get(t, 0)
    fp = round(1 - nc / oc, 3) if oc else ""
    fp_rows.append([t, oc, new_all.get(t, 0), nc, fp])
write_csv("topic-false-positive-rates.csv",
          ["topic", "old_count_allpages", "new_count_allpages", "new_count_content", "fp_rate_vs_old"],
          fp_rows)

# ---- D7 + D14: unit metrics ---------------------------------------------
um_rows = []
for u in CS_UNITS:
    ur = [r for r in cs if r["unit_slug"] == u]
    ucontent = [r for r in ur if r["page_type"] == "content"]
    hubs = [r.get("hubLinks", 0) or 0 for r in ur]
    const = statistics.mode(hubs) if hubs else 0
    autonomy_adj = round(statistics.mean([max((r.get("hubLinks", 0) or 0) - const, 0) for r in ur]), 2) if ur else 0
    broken = sum(1 for r in ur if r["classification_clean"] == "redirect")
    dups = collapse_by_unit[u] + digit_twins[u]
    # topic HHI over content tag distribution
    tc = Counter()
    for r in ucontent:
        for t in r["topicTags_new"]:
            tc[t] += 1
    tot = sum(tc.values())
    hhi = round(sum((c / tot) ** 2 for c in tc.values()), 3) if tot else 0
    um_rows.append([u, UNIT_META[u][0], len(ur), len(ucontent),
                    round(statistics.mean(hubs), 2) if hubs else 0, const, autonomy_adj,
                    broken, dups, round(broken / len(ur), 3) if ur else 0, hhi])
um_rows.sort(key=lambda x: -x[10])
write_csv("unit-metrics.csv",
          ["unit_slug", "faculty", "pages", "content_pages", "hub_per_page_raw",
           "template_sidebar_const", "autonomy_adj", "broken_redirect", "dups_collapsed",
           "redirect_rate", "topic_hhi"], um_rows)

# ---- D10: depth + wordcount (cleaned) -----------------------------------
dw_rows = []
for u in CS_UNITS:
    ur = [r for r in cs if r["unit_slug"] == u]
    uc = [r for r in ur if r["page_type"] == "content"]
    depths = [r.get("depth", 0) for r in ur]
    words = [r.get("wordCount", 0) or 0 for r in uc if not r["is_binary"]]
    dw_rows.append([u, UNIT_META[u][0], len(ur), max(depths) if depths else 0,
                    round(statistics.mean(depths), 1) if depths else 0, len(uc),
                    sum(words), int(statistics.median(words)) if words else 0])
write_csv("depth-wordcount.clean.csv",
          ["unit_slug", "faculty", "pages", "max_depth", "mean_depth", "content_pages",
           "total_words_content", "median_words_content"], dw_rows)

# ---- corrections-changelog.md -------------------------------------------
ch = ["# Corrections changelog — Phase I internal cleanup",
      "",
      "*Generated by `data/clean/build_clean_dataset.py` from the frozen `crawl/pages/*.json`. "
      "Baseline inputs unchanged. Deterministic.*", ""]

# group changelog by section
secorder = ["load", "dedup", "page_type", "D5"]
sectitle = {"load": "Load & scope", "dedup": "D13 — URL-twin dedup",
            "page_type": "D1 — page_type classification", "D5": "D5 — chrome/binary flags"}
for s in secorder:
    lines = [ln for sec, ln in changelog if sec == s]
    if lines:
        ch.append(f"## {sectitle[s]}")
        # collapse the verbose per-twin lines into a count for readability
        verbose = [ln for ln in lines if ln.startswith("  collapsed")]
        summary = [ln for ln in lines if not ln.startswith("  collapsed")]
        ch += summary
        if verbose:
            ch.append(f"<details><summary>{len(verbose)} individual twin collapses</summary>\n")
            ch += verbose
            ch.append("</details>")
        ch.append("")

# D2/D12 re-tag reconciliation table
ch.append("## D2 + D12 + full re-tag — topic count reconciliation (current-students)")
ch.append("")
ch.append("`old` = pages carrying the tag under the legacy tags; `new(all)` = under corrected "
          "rules, any page_type; `new(content)` = corrected rules, content pages only (the "
          "canonical cleaned count). `fp` = 1 − new(content)/old.")
ch.append("")
ch.append("| topic | old | new(all) | new(content) | fp_rate | note |")
ch.append("|---|--:|--:|--:|--:|---|")
notes = {"IT-systems": "D2 regex tightened (dropped bare \\bIT\\b/systems/portal; kept computing/computer-space)",
         "graduation-ceremony": "D12 split — ceremony only. ~0 in faculty estate: validates F26 (ceremony is owned by students.unimelb.edu.au, absent from faculties)",
         "graduation": "D12 — retired. Old tag was ~100% false positive (graduate-stem: Graduate Diploma, graduate research, Dean's Honours)",
         "research-candidature": "D12 — absorbs graduate-research/HDR signals; Law GRD bios now page_type=profile (excluded)",
         "orientation": "D11 + tightened regex — FEIT inflation is partly content-framing, not only path nesting (see reconciliation)"}
for t in all_topics:
    oc, na, nc = old_counts.get(t, 0), new_all.get(t, 0), new_content.get(t, 0)
    fp = f"{round(1 - nc/oc, 2)}" if oc else "—"
    ch.append(f"| {t} | {oc} | {na} | {nc} | {fp} | {notes.get(t, '')} |")
ch.append("")
ch.append("## Reconciliation note (full re-tag drift)")
ch.append("")
ch.append("Per the agreed **full corpus re-tag**, every page was re-tagged from scratch with the "
          "corrected rules, so counts move for two reasons: (a) the named fixes (IT-systems, "
          "graduation, FEIT de-nest, page_type exclusions), and (b) drift where the unified ruleset "
          "differs from the unknown legacy processor that tagged the 11 legacy units. Rows above "
          "with no note and a non-zero fp_rate are drift, not a defect — they reflect one consistent "
          "ruleset replacing per-unit legacy tagging. The `new(content)` column is the canonical count.")
ch.append("")
ch.append("**Phase II refinement (weighted scoring).** A tag now qualifies only if it matches the "
          "title/path (strong signal) or appears ≥2× in the excerpt; a single tangential "
          "excerpt mention no longer adds a tag. This removed the placements-WIL (+126→+27) and "
          "academic-skills (+53→+11) over-tagging surfaced in the first pass, plus the bare "
          "`learning`/`writing`/`maths` tokens in academic-skills. Otherwise-untagged pages keep their "
          "single strongest tag as a fallback.")
ch.append("")
ch.append("### Drift flags — unified ruleset BROADER than legacy (review before quoting)")
ch.append("")
ch.append("Topics where the corrected ruleset tags MORE pages than the legacy tags (negative fp_rate). "
          "These are not named D-fixes — they are over-broad base rules surfaced by the full re-tag "
          "(e.g. academic-skills' `learning`/`writing`, subjects-timetable's bare `subject`). "
          "**Recommend a Phase II rule-tightening review before these specific counts are quoted.**")
ch.append("")
drift = [(t, old_counts.get(t, 0), new_all.get(t, 0), new_content.get(t, 0))
         for t in all_topics if new_all.get(t, 0) > old_counts.get(t, 0) and t != "<untagged>"]
if drift:
    ch.append("| topic | old | new(all) | new(content) | over-tag |")
    ch.append("|---|--:|--:|--:|--:|")
    for t, o, na, nc in sorted(drift, key=lambda x: -(x[2] - x[1])):
        ch.append(f"| {t} | {o} | {na} | {nc} | +{na - o} |")
    ch.append("")
else:
    ch.append("_None material after the Phase II weighted-scoring + academic-skills fix._")
    ch.append("")
ch.append(f"**Untagged residual:** {new_content.get('<untagged>', 0)} content pages match no "
          f"topic keyword (e.g. \"Student Newsletters\", \"Key dates\", committee pages) and are "
          f"left untagged by design — conservative (under-count) rather than the old over-count. "
          f"They are excluded from topic counts.")
ch.append("")
open(f"{OUT_DIR}/corrections-changelog.md", "w").write("\n".join(ch) + "\n")

# ---- VERIFICATION PRINTS ------------------------------------------------
def topic_total(counter):
    return counter

print(f"\n=== Phase I complete: {raw_total} raw → {len(records)} canonical "
      f"({dedup_total} twins collapsed) ===")
print(f"page_type (CS): " + ", ".join(f"{k}={v}" for k, v in pt.most_common()))
print(f"profile pages: {sum(1 for r in cs if r['page_type']=='profile')} "
      f"(Law {sum(1 for r in cs if r['unit_slug']=='law' and r['page_type']=='profile')}, "
      f"Science {sum(1 for r in cs if r['unit_slug']=='science' and r['page_type']=='profile')})")
print(f"archive pages: {sum(1 for r in cs if r['page_type']=='archive')}")
print("\n--- Spot-checks (old → new content) ---")
for t in ["IT-systems", "orientation", "graduation", "graduation-ceremony",
          "research-candidature", "subjects-timetable", "careers-employability"]:
    print(f"  {t:24} {old_counts.get(t,0):4} → {new_content.get(t,0):4}  "
          f"(new all-types {new_all.get(t,0)})")
print("\n--- FEIT it-systems / orientation footprint ---")
feit_it_old = sum(1 for r in cs if r['unit_slug']=='feit' and 'IT-systems' in r['topicTags_old'])
feit_it_new = sum(1 for r in cs if r['unit_slug']=='feit' and 'IT-systems' in r['topicTags_new'] and r['page_type']=='content')
feit_or_old = sum(1 for r in cs if r['unit_slug']=='feit' and 'orientation' in r['topicTags_old'])
feit_or_new = sum(1 for r in cs if r['unit_slug']=='feit' and 'orientation' in r['topicTags_new'] and r['page_type']=='content')
print(f"  FEIT IT-systems: {feit_it_old} → {feit_it_new}    FEIT orientation: {feit_or_old} → {feit_or_new}")
print("\n--- ABP autonomy (D7): hub_per_page_raw vs autonomy_adj ---")
for row in um_rows:
    if row[0] in ("abp", "ffam", "feit", "mbs"):
        print(f"  {row[0]:6} raw={row[4]:5}  sidebar_const={row[5]:3}  autonomy_adj={row[6]:5}  hhi={row[10]}")
print("\n--- alumni careers (should be 38) ---")
alum_careers = sum(1 for r in records if r['unit_slug']=='alumni-unimelb' and 'careers-employability' in r['topicTags_new'])
print(f"  alumni careers-employability (new): {alum_careers}")
print(f"\nFiles written to {OUT_DIR}/:")
for fn in sorted(os.listdir(OUT_DIR)):
    print(f"  {fn}")
