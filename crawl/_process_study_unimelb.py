#!/usr/bin/env python3
"""Post-process the study.unimelb raw crawl into pages/study-unimelb.json + summary."""
import json
import re
from collections import Counter
from urllib.parse import urlparse

BASE = "/Users/djmulholland/Documents/Claude/projects/unimelb-current-students-ia/crawl"
RAW = f"{BASE}/raw/_study_unimelb_raw_crawl.json"
OUT_JSON = f"{BASE}/pages/study-unimelb.json"
OUT_MD = f"{BASE}/pages/study-unimelb-summary.md"
OUT_DISC = f"{BASE}/pages/study-unimelb-discovered.txt"

UNIT = "study-unimelb"
PARENT = "prospective"
HOST = "study.unimelb.edu.au"
PRE = "/"

AUTH_HOSTS = {
    "my.unimelb.edu.au", "lms.unimelb.edu.au", "canvas.lms.unimelb.edu.au",
    "studentit.unimelb.edu.au", "services.unimelb.edu.au", "sso.unimelb.edu.au",
    "login.unimelb.edu.au", "auth.unimelb.edu.au", "apply.unimelb.edu.au",
}
AUTH_PAT = re.compile(r"(^|\.)(my|lms|canvas\.lms|sis|studentit|sso|login|auth|apply)\.", re.I)

raw = json.load(open(RAW))
recs = raw["records"]

TAG_RULES = [
    # Existing tags (for cross-site comparison with current-students)
    ("enrolment", r"\benrol|enrolment|enrolling|census date|study load\b"),
    ("course-planning", r"course plan|course planning|study plan|program structure|sequenc|advanced standing|credit|subject selection"),
    ("subjects-timetable", r"timetable|class registration|subject|lecture|tutorial|breadth"),
    ("exams-results", r"\bexam|assessment|results|grade|hurdle"),
    ("special-consideration", r"special consideration|extension|academic adjustment"),
    ("fees-finance", r"\bfee|fees|tuition|finance|payment|invoice|loan|FEE-HELP|HECS"),
    ("scholarships", r"scholarship|bursary|stipend|grant\b"),
    ("placements-WIL", r"placement|internship|work integrated|industry project|WIL|practicum"),
    ("careers-employability", r"career|employab|employment|job|professional development|industry connect"),
    ("academic-skills", r"academic skill|study skill|writing|maths|numeracy|language support"),
    ("student-life", r"student life|community|peer|ambassador|society|campus life"),
    ("clubs-events", r"\bclub|event|workshop|seminar"),
    ("wellbeing-health", r"wellbeing|wellness|health|counsel|mental health|support service"),
    ("IT-systems", r"\bIT\b|computing|software|wi-?fi|computer|laptop|systems|portal"),
    ("library", r"\blibrary|librarie"),
    ("graduation", r"graduat|completion|award ceremony|conferral"),
    ("forms-admin", r"\bform\b|application form|administration|admin|request|how to apply"),
    ("contacts-support", r"contact|enquir|help|ask\b|student centre|get in touch"),
    ("research-candidature", r"candidatur|PhD|doctora|thesis|research pathway|MPhil|research student|graduate researcher"),
    ("international", r"international|dual degree|exchange|overseas|study abroad|visa|global|offshore"),
    ("inclusion-equity", r"indigenous|inclusion|equity|accessibilit|disabilit|diversity"),
    ("orientation", r"orientation|getting started|welcome|first week|commencing|new student"),
    # Study-specific extended tags
    ("study-course-info", r"course information|degree|bachelor|master|graduate|undergraduate|program|postgrad"),
    ("study-entry-requirements", r"entry requirement|prerequisite|admission|ATAR|selection rank|VCE|English proficiency|IELTS|TOEFL|prerequisite"),
    ("study-fees-costs", r"cost|fee|tuition|FEE-HELP|annual fee|total cost|budget|living cost|estimate"),
    ("study-scholarships", r"scholarship|bursary|stipend|financial support|award"),
    ("study-how-to-apply", r"how to apply|apply online|application|accept offer|defer|confirm|offer"),
    ("study-campus-life", r"campus|life at unimelb|student life|housing|accommodation|sport|recreation"),
    ("study-international", r"international student|study in australia|student visa|CoE|overseas|OSHC"),
]


def tag_page(rec):
    hay = " ".join([
        rec.get("title", ""),
        urlparse(rec.get("normalizedUrl") or rec["url"]).path.replace("-", " ").replace("/", " "),
        rec.get("excerpt", ""),
    ]).lower()
    scored = []
    for tag, pat in TAG_RULES:
        hits = len(re.findall(pat, hay, re.I))
        if hits:
            scored.append((hits, tag))
    scored.sort(reverse=True)
    tags = [t for _, t in scored[:4]]
    if not tags:
        tags = ["study-course-info"]
    return tags


def classify(rec):
    wc = rec.get("wordCount", 0)
    if rec.get("is404") or rec.get("redirectedOffHost"):
        return "redirect", "is404/off-host redirect"
    outbound_total = sum(rec.get("outboundHosts", {}).values())
    hub = rec.get("hubLinks", 0)
    # For study.unimelb, "mixed" means heavy links to unimelb.edu.au main site or apply portal
    central = rec.get("outboundHosts", {}).get("unimelb.edu.au", 0)
    apply_links = rec.get("outboundHosts", {}).get("apply.unimelb.edu.au", 0)
    if wc < 160 and (outbound_total >= 10 or hub > 0):
        return "link-farm", f"wc<160 & outbound={outbound_total}"
    if wc >= 160:
        if central >= 6 or apply_links >= 4:
            return "mixed", f"unique prose + {central} main-site links"
        return "unique", f"wc={wc}"
    return "link-farm", f"thin wc={wc} outbound={outbound_total}"


out_records = []
for rec in recs:
    norm = rec.get("normalizedUrl") or rec["url"]
    cls, sig = classify(rec)
    tags = tag_page(rec)
    out_records.append({
        "url": rec["url"],
        "normalizedUrl": norm,
        "faculty": UNIT,
        "parentFaculty": PARENT,
        "unitLevel": "site",
        "title": rec.get("title", ""),
        "depth": rec.get("depth", 0),
        "wordCount": rec.get("wordCount", 0),
        "classification": cls,
        "classificationSignal": sig,
        "topicTags": tags,
        "outboundHosts": rec.get("outboundHosts", {}),
        "hubLinks": rec.get("hubLinks", 0),
        "inSectionCount": rec.get("inSectionCount", 0),
        "status": rec.get("status"),
        "excerpt": rec.get("excerpt", ""),
    })

out_records.sort(key=lambda r: (r["depth"], r["normalizedUrl"]))
json.dump(out_records, open(OUT_JSON, "w"), indent=2, ensure_ascii=False)

# Aggregates
by_cls = Counter(r["classification"] for r in out_records)
by_topic = Counter()
for r in out_records:
    for t in r["topicTags"]:
        by_topic[t] += 1
by_depth = Counter(r["depth"] for r in out_records)
max_depth = max((r["depth"] for r in out_records), default=0)

outbound_total = Counter()
for r in out_records:
    for h, c in r["outboundHosts"].items():
        outbound_total[h] += c

auth_seen = Counter()
for h, c in outbound_total.items():
    if h in AUTH_HOSTS or AUTH_PAT.search(h):
        auth_seen[h] += c

notable = sorted(
    [r for r in out_records if r["classification"] in ("unique", "mixed")],
    key=lambda r: -r["wordCount"],
)[:15]

paths = sorted(set(urlparse(r["normalizedUrl"]).path for r in out_records))
tree = {}
for p in paths:
    parts = [x for x in p.split("/") if x]
    node = tree
    for part in parts:
        node = node.setdefault(part, {})


def render_tree(node, depth=0, lines=None):
    if lines is None:
        lines = []
    for k in sorted(node.keys()):
        lines.append("  " * depth + k)
        render_tree(node[k], depth + 1, lines)
    return lines


tree_lines = render_tree(tree)


def md_counter(c):
    return "\n".join(f"- **{k}:** {v}" for k, v in c.most_common())


lines = []
lines.append("# study.unimelb.edu.au — crawl summary\n")
lines.append(f"- **Unit:** {UNIT}")
lines.append(f"- **Type:** Prospective-student and course-discovery site")
lines.append(f"- **Root:** https://{HOST}/")
lines.append(f"- **Pages captured:** {len(out_records)}")
lines.append(f"- **Max IA depth:** {max_depth}")
lines.append(f"- **Fetch errors:** {len(raw.get('errors', []))}")
lines.append(f"- **HTTP/parse 404s:** {by_cls.get('redirect', 0)}")
lines.append(f"- **Crawled:** {raw.get('meta', {}).get('crawledAt', 'unknown')[:10]}\n")

lines.append("## Classification breakdown\n")
lines.append(md_counter(by_cls))
lines.append("")

lines.append("## Topic breakdown\n")
lines.append(md_counter(by_topic))
lines.append("")

lines.append("## Depth distribution\n")
lines.append("\n".join(f"- depth {k}: {v} pages" for k, v in sorted(by_depth.items())))
lines.append("")

lines.append("## Cross-site overlap flags\n")
overlap_tags = {"course-planning", "fees-finance", "scholarships", "careers-employability", "research-candidature", "international"}
for tag in overlap_tags:
    count = by_topic.get(tag, 0)
    if count:
        lines.append(f"- **{tag}**: {count} pages — potential overlap with current-students estate")
lines.append("")

lines.append("## Top outbound destinations\n")
for h, c in outbound_total.most_common(20):
    flag = "  ⚠ auth-gated" if (h in AUTH_HOSTS or AUTH_PAT.search(h)) else ""
    lines.append(f"- `{h}`: {c}{flag}")
lines.append("")

lines.append("## Auth-gated hosts seen\n")
if auth_seen:
    for h, c in auth_seen.most_common():
        lines.append(f"- `{h}`: {c} links")
else:
    lines.append("- (none)")
lines.append("")

lines.append("## Notable unique pages\n")
for r in notable:
    p = urlparse(r["normalizedUrl"]).path
    lines.append(f"- **{r['title']}** ({r['wordCount']}w, d{r['depth']}, {'/'.join(r['topicTags'])}) — `{p}`")
lines.append("")

lines.append("## Section IA tree\n```")
lines.extend(tree_lines[:80])
if len(tree_lines) > 80:
    lines.append(f"... ({len(tree_lines) - 80} more paths)")
lines.append("```\n")

open(OUT_MD, "w").write("\n".join(lines))

disc_lines = [
    "# study.unimelb.edu.au — discovered subpaths",
    f"# crawl root: https://{HOST}/",
]
for p in paths[:100]:
    disc_lines.append(f"https://{HOST}{p}")
if len(paths) > 100:
    disc_lines.append(f"# ... {len(paths) - 100} more paths")
open(OUT_DISC, "w").write("\n".join(disc_lines) + "\n")

top_topics = [t for t, _ in by_topic.most_common(8)]
top_outbound = {h: c for h, c in outbound_total.most_common(8)}
ret = {
    "unit": UNIT,
    "pagesCaptured": len(out_records),
    "byClassification": dict(by_cls),
    "topTopics": top_topics,
    "iaDepthMax": max_depth,
    "notableUniquePages": [urlparse(r["normalizedUrl"]).path for r in notable[:8]],
    "topOutboundHosts": top_outbound,
    "authGatedHosts": list(auth_seen.keys()),
}
print(json.dumps(ret, indent=2))
print("\n--- files written ---")
print(OUT_JSON)
print(OUT_MD)
print(OUT_DISC)
