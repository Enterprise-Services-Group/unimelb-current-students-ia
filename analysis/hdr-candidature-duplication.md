# HDR Candidature Duplication — Deep-Dive

*The graduate research candidature lifecycle is authored identically across two faculty CMSes while a canonical owner already exists — off the crawled estate. ~8 faculties each maintain their own copy. The faculties with the largest research estates carry the least HDR-student support. June 2026.*

---

## Executive summary

Higher Degree by Research (HDR) candidates — PhD and MPhil students — navigate a distinct lifecycle: candidature, milestones, supervision, thesis, examination, completion. The canonical owner of this lifecycle is gradresearch.unimelb.edu.au (the Graduate Research Hub). But it sits **outside the crawled student estate**, and ~8 faculties independently re-host the same content — including **33 path-tails that are byte-identical (Jaccard 1.000) across education.unimelb and mdhs.unimelb**.

The duplication is not approximate. It's literal copy-paste across two CMSes. And it's compounded by the "research paradox": the faculties with the largest research estates carry the least HDR-student support. MDHS has 63 research pages and 1 HDR-student page. The lifecycle is broken at both ends — near-absent prospective PhD funnel (6 pages) and a single research-alumni page.

The fix is clean because the canonical owner already exists: 301 the byte-identical clones to gradresearch.unimelb, reconcile the drifted remainder, and connect the prospective-PhD and research-alumni ends.

---

## The duplication map

### Byte-identical pairs (Jaccard 1.000)

near_dup.py confirmed **33 path-tails are byte-for-byte identical** across education.unimelb.edu.au and mdhs.unimelb.edu.au. These cover the full candidature lifecycle:

| Lifecycle stage | Path-tail example | Both on |
|---|---|---|
| Candidature milestones | /graduate-research/milestones | education + mdhs |
| Supervision | /graduate-research/supervision | education + mdhs |
| Thesis submission | /graduate-research/thesis | education + mdhs |
| Examination | /graduate-research/examination | education + mdhs |
| Completion | /graduate-research/completion | education + mdhs |

Two faculties maintain identical copies of the same HDR candidature content, on different CMSes, under different URL trees. The maintenance burden is doubled. The drift risk is guaranteed. The student arriving from either faculty sees the same content — but it's authored, hosted, and governed separately.

### The drifted remainder

Beyond the 33 byte-identical pairs, ~8 faculty CMSes each carry their own version of HDR content under different URL trees. Some have localised content (faculty-specific contacts, discipline-specific milestone variations). Most are template re-hosts with minor edits that have already begun to drift.

### The canonical owner — already exists

gradresearch.unimelb.edu.au is the Graduate Research Hub — the designated system of record for the HDR candidature lifecycle. It covers milestones, supervision, thesis, examination, completion, and professional development. It has a clean IA and is actively maintained.

But it sits **outside the crawled student estate** — it was not included in the 20-domain crawl because it's a separate host under a different governance model. The lifecycle's spine is off to the side, invisible to the link-graph analysis that mapped every other student journey.

---

## The research paradox

| Faculty | Research pages | HDR-student support pages | Verdict |
|---|---|---|---|
| MDHS | 63 | **1** | Strongest research identity, weakest research-student journey |
| Medicine | Large research estate | Minimal HDR | Same pattern |
| Biomed | Large research estate | Minimal HDR | Same pattern |
| Education | 28 | Multiple (but duplicated) | Duplicated, not genuinely local |
| Arts | Modest | Scattered | Variable |

The faculties with the largest research estates — the ones that produce the most PhDs — carry the least support content for their own HDR students. The research identity dominates the faculty CMS; the HDR student is an afterthought.

---

## The broken ends

The HDR journey is broken at both ends of the lifecycle:

### Prospective — near-absent PhD funnel

study.unimelb carries only ~6 prospective research-degree pages. A prospective PhD student browsing courses finds a near-empty funnel compared to the 440-page coursework catalogue. The research-degree discovery experience is essentially: "Find a supervisor → apply." No course structure, no career outcomes, no student profiles.

### Alumni — 1 page

Research alumni gets exactly 1 page. The PhD graduate — the University's most intensive research investment — is handed to the alumni relationship by a single page. The prospective→HDR→research-alumni lifecycle is broken at both seams.

---

## The gradresearch handoff gap

Cross-site-flow.csv shows significant faculty→gradresearch links (education 1,972, mdhs 1,882) — evidence that faculties DO route HDR students to the Graduate Research Hub. But the same faculties ALSO re-host the content they're routing to. The student gets two versions: the canonical one at gradresearch, and the faculty's slightly-different copy. No rel=canonical, no redirect, no indication which is authoritative.

---

## Recommendations

### 1. 301-redirect the 33 byte-identical pairs to gradresearch.unimelb `[HIGH · medium]`
The 33 Jaccard=1.000 education+mdhs pages should immediately 301 to their gradresearch equivalents. No eyeballing needed — they're byte-identical. The canonical owner exists. This removes 33 pages of duplicated maintenance instantly.

### 2. Reconcile the drifted remainder: audit and either redirect or justify localisation `[MEDIUM · medium]`
For the remaining ~8 faculty HDR trees, audit each page: if it's genuinely faculty-specific (local contacts, discipline-specific milestones), keep it with a rel=canonical pointing to gradresearch for the shared content. If it's a template re-host, 301 it.

### 3. Make gradresearch.unimelb the single source of truth for the HDR lifecycle `[HIGH · medium]`
Declare gradresearch the canonical owner. Every faculty HDR page either 301s to it or carries rel=canonical to it. No more dual-authoring the candidature lifecycle.

### 4. Connect the prospective-PhD funnel `[MEDIUM · medium]`
Build out the study.unimelb research-degree discovery experience: course structure, career outcomes, student profiles, supervisor search. The 6-page funnel is not enough to recruit PhD candidates.

### 5. Connect research-alumni to the alumni mentoring streams `[MEDIUM · medium]`
Bridge the 1-page research-alumni stub to the 12 faculty-specific alumni mentoring streams. A PhD graduate should flow into research-alumni mentoring, not a dead end.

### 6. Add a standing near-duplicate CI check `[MEDIUM · medium]`
near_dup.py already exists and works. Run it as a CI gate so cross-domain content forks are detected when they're created, not discovered years later.

---

## Linked improvements from the register

| § | Improvement | Severity · Effort |
|---|---|---|
| 4.1 / 9b.1 | Redirect the 18 byte-identical HDR candidature/thesis pages (education+mdhs) to gradresearch.unimelb | HIGH · medium |
| 9b.4 | Add a standing near-duplicate CI check (near_dup.py) to the web governance toolchain | MEDIUM · medium |
| 3.3 | Resolve the HDR-support paradox at the seam — route research-intensive faculties to the Graduate Research Hub | MEDIUM · quick-win |
| — | Connect prospective-PhD funnel and research-alumni to close the research lifecycle | MEDIUM · medium |

---

*Built from: near_dup.py output (33 byte-identical pairs), improvements-register.md (§4.1, §9b.1, §3.3), lifecycle-journeys.md (HDR persona trace), cross-site-flow.csv (faculty→gradresearch links), and the gradresearch.unimelb crawl gap analysis. June 2026.*
