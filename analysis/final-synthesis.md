# Final Synthesis — Current Students IA Project

*The complete picture after 40,533 pages crawled across 27 domains, 26 deep-dive analyses, 5 persona profiles, and ~75 improvements. Every finding is grounded in evidence, cross-referenced across analyses, and ready for action. June 2026.*

---

## The estate by the numbers

| Metric | Value |
|---|---|
| Domains crawled | 29 (20 original + 9 expansion) |
| Total pages | 41,533 |
| Contextual links mapped | 261,652 |
| Deep-dive analyses | 28 |
| Persona profiles | 5 |
| Improvements registered | ~75 |
| Quick wins ready to execute | 28 |

---

## The five root findings

After 40,533 pages and 26 analyses, five patterns emerge that explain every fault in the estate:

### 1. The estate describes; it never transacts

Every student journey terminates in a walled system. The public estate describes enrolment, payment, counselling booking, special consideration, and visa compliance — but the actual action happens behind a login wall (my.unimelb, eStudent, Canvas, `*.app` forms). The find→act gap is the estate's defining failure. **The public estate is an instruction manual for systems it cannot show.**

**Evidence:** 187 hub→my.unimelb links. 444 hub→ask.unimelb FAQ links. 2 links to enrolmentvariations.app. 3 links to mycounselling.app. 2,044 links to forms.your (opaque SID params).

### 2. The hub competes with itself

students.unimelb.edu.au is 833 pages, not the "74" the deck asserts. It's mid-migration, dual-serving 120 leaf pages under two parallel URL trees. 12 domains link the deprecated trees. MSD has ~8,000 links pointed at legacy paths. **The central hub's own URLs are unstable — and faculties are being told to link into it.**

**Evidence:** 19 core leaves byte-near duplicated across `/course-admin` and `/your-course`. 24 leaves across `/support-and-wellbeing` and `/student-support`. Old Stop 1 linked 1,648× vs 224× new. Census-dates canonicalises to `/page-not-found`.

### 3. The joints between stages are broken — and they're the cheapest to fix

The stages are mostly well-built. The transitions are thin or absent. The graduation→alumni handoff has 35 completion pages and 0 alumni links. The apply→enrol seam has 373 contextual links (fewer than MSD's 8,069). These are the highest-leverage, lowest-cost fixes in the register — purely additive, nothing to unpick.

**Evidence:** Graduate→alumni: 35 pages, 0 links, grad page links Instagram not alumni. Prospective→current: 373 study→hub links, 9/19 domains below 100. Faculty mentoring→alumni mentoring: same service, adjacent life stages, 0 cross-links.

### 4. Fragmentation is regressive — it costs the most to those with the least margin

The international postgraduate navigating visa compliance across 3 forked trees. The Indigenous student with zero hub presence. The disabled student landing on one of 3 equity trees — 2 without the registration wizard. The at-risk student finding counselling branded "Academic Skills Unit." **The students who can least afford to hunt across 5-8 systems are the ones who must.**

**Evidence:** SEDS wizard on 1 of 3 trees, 12 domains link the 2 without it. Murrup Barak: 19 hub links vs 614 MSD. Counselling: 614× "Academic Skills Unit" vs 39× "Counselling." International visa: 3 live trees, highest-risk pages link to 0 action forms.

### 5. The fix is structural, not visual

The University already runs Squiz/Matrix everywhere. The problem isn't the platform — it's that no two faculties share a top-level taxonomy, no subdomain registry exists, 415 distinct hosts have no owner, and the student entry is at 5 different URL depths. The fix is a thin student overlay on the platform every faculty already uses, a subdomain registry, and governance — not 12 separate redesigns.

**Evidence:** 415 distinct hosts in the contextual graph. 19 single-purpose `*.app` hosts with no retirement date. 28 www-twins splitting link equity. 5 URL conventions for "current students" at different depths.

---

## Domain-by-domain: what each new crawl revealed

### Ask.unimelb (515 pages)

**What it is.** The legacy FAQ knowledge base — 393 FAQ articles. The hub's #1 outbound destination (444 links).

**Key findings.** Two URL formats confirmed (`/app/answers/detail/a_id/` and `/faq/`). 100 backlinks to hub in 30-page sample — tight hub↔FAQ coupling. 10 dead FAQ pages. Median 45KB — lightweight, portable.

**Action.** Standardise to one URL format. Migrate high-traffic answers (census, fees, enrolment procedures) into the hub. Keep FAQ for long-tail.

### Gradresearch (302 pages)

**What it is.** The canonical Graduate Research Hub — the HDR candidature lifecycle.

**Key findings.** Well-structured IA mapping to the full HDR journey. **122/302 pages (40%) are 404s** — worst dead-link ratio in the estate. Confirms faculty clones (33 byte-identical pairs) are unnecessary — content exists here. 4,123 inbound links from 18 domains routing students to a site that's 40% dead.

**Action.** Emergency: triage and fix the 122 404s. 301 the 33 faculty clones to gradresearch. Wire the hub to gradresearch (currently only 60 links).

### Murrupbarak (37 pages)

**What it is.** Indigenous student support unit — comprehensive, well-structured.

**Key findings.** Covers study, financial support, accommodation, careers, community. Service is real and good. **19 hub links vs 614 MSD links** — routing failure, not content gap. Consistent 142KB pages.

**Action.** One Indigenous-students landing page on the hub. Fix the www-twin. Repoint the 17 linking domains to the new hub page.

### Safercommunity (17 pages)

**What it is.** Crisis, safety, and sexual misconduct support.

**Key findings.** Comprehensive coverage: sexual assault, harassment, bullying, discrimination, family violence, stalking, child safety. **Healthy bidirectional hub connection (62↔53)** — one of the few balanced seams. 300KB pages — too heavy for crisis access.

**Action.** Add to unified "I need help now" front door. Cross-link with counselling. Trim page weight.

### UMSU (800 pages)

**What it is.** Independent student union — not University CMS.

**Key findings.** 33% clubs directory. **720KB median, 6.4MB max** — heaviest pages in the estate. **Extremely insular:** 8 outbound unimelb links in 19 pages. Parallel student universe.

**Action.** Flag page weight. Propose cross-links to hub services. Strengthen hub→UMSU connection.

### Online (87 pages)

**What it is.** Online learning marketing funnel.

**Key findings.** **52% are lead-capture RFI forms.** 1 link to student hub. Pure marketing — no current-learner infrastructure. Confirms the orphaned cohort gap.

**Action.** "Already enrolled?" bridge. Current-learner section on hub or online.unimelb.

### Sport (444 pages)

**What it is.** MU Sport — well-structured, well-performing.

**Key findings.** **Best page weight in the estate: 67KB median.** Strong ecommerce integration (29 links). Low IA priority for current-students project.

**Action.** Study template for page-weight best practices. No urgent issues.

### Library (1,000 pages — hit max)

**What it is.** University Library — academic skills and research support.

**Key findings.** **370 pages are referencing/citation guides** — the library is the University's citation authority. 178 pages archives/special collections. 66 pages reference management software. 36 links to student hub in 30-page sample — moderate connection. Well-maintained, 7 dead pages only.

**Action.** Add Library referencing to the hub's academic skills section. Cross-link more prominently.

### StudentIT (74 pages)

**What it is.** Student IT support — printing, wifi, VPN, software.

**Key findings.** Task-focused operational content: "Student Print," "UniWireless," "VPN," "Microsoft 365 Update." 34 links to hub — healthy connection. **13 offboarding pages** — the IT side of the graduation→alumni transition.

**Action.** Link graduation offboarding pages from the graduation→alumni bridge. Add to hub's "IT & systems" section.

### Orientation & Breadth (0 pages)

**What they are.** Dead domains — both homepages return "Page not found."

**Key finding.** orientation.unimelb.edu.au and breadth.unimelb.edu.au are no longer live. The 1 contextual link to orientation (from biomed) and 7 links to breadth (from handbook) point to dead destinations.

**Action.** Either restore content or 301-redirect both domains to their students.unimelb equivalents.

---

## The unchanged priority list

Every deep-dive, every crawl analysis, every link-graph audit reinforces the same 10 priorities. The order is unchanged because the evidence accumulates in one direction:

| # | Fix | New evidence |
|---|---|---|
| 1 | Finish the hub migration | Still the prerequisite for everything |
| 2 | Student overlay on Squiz | Still the only lever that touches all 12 architectures |
| 3 | Subdomain registry | Confirmed by 415 hosts + 19 *.app + 28 www-twins |
| 4 | Handbook baseline | The #1 dependency, worst web standards |
| 5 | Graduate→alumni bridge | Still purely additive, zero migration cost |
| 6 | Wire Careers Online | 5 faculties at zero, confirmed by crawl |
| 7 | Collapse SEDS + Indigenous hub page | **New:** Murrupbarak crawl proves service exists, just needs routing |
| 8 | Fix census-date canonical | Still one line, still broken |
| 9 | Fix 2,038 scholarship titles | Still one template change |
| 10 | Fix Cookiebot duplicate icons | Still one config change, drops 5MB→200KB |

---

## What this project proved

1. **Link-graph analysis is a valid proxy for journey quality.** Where the links are thin, the journey breaks. Where the links fork, the student gets lost. Where zero links exist, the seam is severed. The link graph predicted every fault the crawls confirmed.

2. **The most expensive-looking problems have the cheapest fixes.** The graduation→alumni bridge costs one CTA. The census-date fix costs one line. The Cookiebot fix costs one config change. The scholarship titles fix costs one template change. The project's #1 finding is that the worst seams are the easiest to close.

3. **The Estate is competent in parts, broken at the joints.** Analysed stage by stage, it looks fine. Traced as a journey, the transitions fail — and they're the transitions no team owns.

4. **Crawling the uncrawled domains confirmed every inference.** Ask.unimelb really does have two URL formats. Gradresearch really is the canonical HDR owner (with a 40% 404 rate). Murrupbarak really is comprehensive and unlinked. Safercommunity really is well-connected to the hub. The link graph told the truth.

---

## What remains

1. **The authenticated core** — my.unimelb, Canvas, eStudent, `*.app` forms — remains uncrawlable. The public→authenticated seam can only be verified by walking through the logged-in experience
2. **User validation** — every finding is structural evidence, not observed student failure. The costliest seams should be validated with real users before implementation
3. **Analytics** — the `in_c=` tracking params in crawled URLs imply GA/search-log data exists. Requesting it is the single highest-value next step so priority can follow pages students actually hit
4. **Deeper content analysis** — the current crawl analyses cover structure and links. Page content (reading level, actionability, tone) would reveal further quality gaps
5. **Dead domain cleanup** — orientation.unimelb.edu.au and breadth.unimelb.edu.au return "Page not found." Their inbound links should be redirected or removed

---

*Built from: 41,533 pages across 29 domains, 261,652 contextual links, 28 deep-dive analyses, 5 persona profiles, ~75 improvements, 28 quick wins. June 2026.*
