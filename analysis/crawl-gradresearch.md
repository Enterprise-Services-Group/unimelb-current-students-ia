# gradresearch.unimelb.edu.au — Crawl Analysis

*The Graduate Research Hub — 302 pages, the canonical owner of the HDR candidature lifecycle. 122 pages are 404s. Well-structured IA but a massive dead-link problem. Confirms the duplication story: the content exists here; the faculty clones are unnecessary. June 2026.*

---

## What we found

The HDR deep-dive identified gradresearch.unimelb.edu.au as the canonical owner of the HDR candidature lifecycle, sitting off the crawled estate with 4,123 inbound links from 18 domains. The crawl reveals it as a **302-page site with a clear, well-structured IA** — and a **massive dead-link problem**: 122 of 302 pages (40%) return 404.

### Structure

| Section | Pages | Content |
|---|---|---|
| `/being-a-candidate/making-changes` | 35 | Study rate, supervisors, department, withdrawal, leave, re-enrolment — the operational core |
| `/getting-started/resources-for-students` | 32 | IT, email, library, scholarships, finances, keep-informed |
| `/preparing-my-thesis/thesis-with-publication` | 25 | Thesis formatting, authorship, publication inclusion, examination |
| `/developing-my-skills/research-skills` | 21 | Workshops, resources, training |
| `/being-a-candidate/study-away` | 8 | Study away application, approval, return |
| `/home/surveys` | 7 | Melbourne Research Experience Survey, QILT |
| `/being-a-candidate/reviewing-my-progress` | 6 | At-risk, formal warning, unsatisfactory progress |
| Other | 46 | Remaining sections |

The IA is sensible: **getting-started → being-a-candidate → developing-skills → preparing-thesis → examination → planning-future.** This is exactly the HDR lifecycle the faculty clones duplicate.

### The 404 problem

**122 of 302 pages (40%)** have the title "404 : Page" — these are dead pages that were crawled because they're still linked internally. This is the worst dead-link ratio of any domain analyzed. The gradresearch site has significant content rot, possibly from a recent restructure or migration.

The 404s cluster in specific sections:
- `/being-a-candidate/making-changes` — many variation form pages are dead
- `/getting-started/resources-for-students` — resource link pages
- `/preparing-my-thesis` — thesis preparation guides

### Link analysis

| Outbound destination | Links in 30-page sample | Role |
|---|---|---|
| www.unimelb.edu.au | 199 | Heavy chrome/nav — every page carries extensive unimelb chrome |
| about.unimelb.edu.au | 128 | Policy/administrative |
| students.unimelb.edu.au | 53 | Student hub — moderate connection |
| gateway.research.unimelb.edu.au | 36 | Research gateway |
| safety.unimelb.edu.au | 32 | Safety chrome |
| staff.unimelb.edu.au | 28 | Staff pages — potential access-boundary leak |
| library.unimelb.edu.au | 15 | Library |
| research.unimelb.edu.au | 14 | Research |
| search.unimelb.edu.au | 14 | Site search |

### Page weight

Median 156KB — moderately heavy. Max 705KB — some pages are very large (likely the thesis-with-publication detail pages). The chrome overhead (www + about + safety links on every page) contributes significantly.

---

## What this means

### 1. The canonical owner exists, works, and is well-structured — but rotting

gradresearch.unimelb.edu.au IS the HDR hub. Its IA maps cleanly to the HDR lifecycle. The content exists here. **The 33 byte-identical faculty clones on education and mdhs are unnecessary — they duplicate content that already has a canonical home.**

### 2. The 40% 404 rate is an emergency

This is the worst dead-link ratio we've found. If the 4,123 inbound links from 18 domains are routing HDR students to this site, 40% of those links may be landing on dead pages. This needs immediate triage: which sections are dead, which inbound links point to them, and whether redirects exist.

### 3. The chrome overhead is extreme

199 www.unimelb + 128 about.unimelb + 32 safety links in just 30 sampled pages — every gradresearch page carries ~12 chrome links to the corporate site. This inflates page weight and dilutes the student's attention.

### 4. The research paradox is confirmed

The site is comprehensive for HDR candidates — candidature management, skills development, thesis preparation, examination. But it's off the student hub. The hub sends only 60 links; the faculties send 4,123. The content exists; the routing doesn't.

---

## Recommendations

1. **Triage and fix the 122 404 pages.** Audit which sections are dead, identify inbound links, add 301 redirects or restore content. This is the #1 priority for gradresearch.

2. **301 the 33 byte-identical faculty clones to their gradresearch equivalents.** The canonical content exists here. The education+mdhs duplicates are maintenance debt with no value.

3. **Wire the hub to gradresearch.** The hub sends only 60 links to the HDR lifecycle. Add prominent "Research candidates → Graduate Research Hub" links from students.unimelb.

4. **Reduce chrome overhead.** Trim the 12+ corporate chrome links per page to the essential 3-4.

5. **Add the HDR lifecycle to the prospective PhD funnel.** The 6-page study.unimelb research-degree discovery experience should link to gradresearch's getting-started section.

---

*Built from: gradresearch crawl (302 pages), links.json sampling (30 pages), index.json structural analysis, near_dup.py byte-identical pair list. June 2026.*
