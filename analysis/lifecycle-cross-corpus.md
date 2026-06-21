# Cross-Corpus Lifecycle Analysis — connections across the end-to-end student journey

*Joins all four corpora — prospective (`study.unimelb.edu.au`, 300 pages), current-students (faculty domains + `students.unimelb.edu.au`, 1,153), full faculty estates (9 domains, 2,363), and alumni (`www.unimelb.edu.au/alumni`, 116) — to find what no single-corpus view can see: the connections, overlaps, and broken seams along the lifecycle prospective → enrolled → graduate → alumni. Figures reproducible via [`data/clean/cross_corpus_lifecycle.py`](../data/clean/cross_corpus_lifecycle.py). June 2026.*

> **The frame.** A single student's relationship with the University runs **prospective → current → alumni**, but on the web that journey crosses **four domains, four architectures, and four vocabularies** with no shared addressing and no visible handoffs. Almost every cross-corpus finding below is a version of one thing: *the University's services are organised by who-owns-the-page, not by where-the-student-is-in-their-life.*

---

## 1. The careers spine — the one service authored at every stage, connected at none

Careers is the single clearest cross-lifecycle pattern. The same service — "help me turn study into work" — is independently authored at **10 distinct locations across all four domains**:

| Lifecycle stage | Where careers lives | Pages |
|---|---|--:|
| Prospective | `study.unimelb.edu.au` ("turn your passion into a career") | 38 |
| Current (central) | `students.unimelb.edu.au` Careers service | ~core |
| Current (faculty) | 8 faculties run their own (Education 28, FEIT 23, Law 22, Arts 16, MDHS 14, ABP 11, Science 5, FFAM 4) | ~123 |
| Alumni | `www.unimelb.edu.au/alumni` careers + mentoring | 38 |

The audit's [Finding 4 / Finding 24](structural-findings.md) said careers is "authored three times." Across the **full lifecycle it is authored ~10 times across four domains** — and the alumni mentoring layer (20 pages) was never previously in scope. **The most consequential new connection: faculty student-mentoring and alumni mentoring are the same service for adjacent lifecycle stages, run by different teams on different domains, never linked.** A final-year student in a faculty mentoring program and the alumni mentoring program they graduate into do not cross-reference. Careers is where the lifecycle should be *most* continuous and is in fact *most* fragmented.

---

## 2. The research paradox — the faculties strongest in research support their research students least

Mapping the **research domain** across the lifecycle (prospective PhD → HDR candidate → research alumni) exposes a sharp inversion. The faculties with the **largest research estates** carry the **least HDR-candidature support** for their own research students:

| Faculty | Faculty `/research/` estate | Current HDR-candidature support |
|---|--:|--:|
| MDHS | **63** (largest) | **1** |
| Science | 60 | 6 |
| ABP (MSD) | 46 | 29 |
| Education | 44 | 0 |
| Arts | 34 | 27 |
| FBE | 30 | 21 |
| Law | 19 | **79*** |

\* Law's 79 is the exception that proves the rule: **61 of the 79 are researcher *profile/bio* pages**, not support — only ~18 are genuine candidature content. So even the one faculty that looks well-supported is mostly a staff directory.

**Research is run as a reputation asset, decoupled from the research-student experience.** And the research *funnel* is broken at both ends: only **6 prospective research-degree pages** exist on `study.unimelb.edu.au` (the PhD recruitment front door is nearly absent), and only **1 alumni page** is research-tagged (no research-alumni relationship). MDHS — the University's research powerhouse by page count — is the most extreme: 63 research pages, **one** HDR-student support page.

---

## 3. Alumni is not a new relationship — it is current-student services, re-hosted on a fourth domain

The central alumni corpus (116 pages, all on `www.unimelb.edu.au` — a domain that appears *nowhere else* in the student journey) is overwhelmingly a **parallel re-run of services students already had**:

| Alumni page topic | Pages | Same service exists at current stage? |
|---|--:|---|
| careers / employability | 38 | ✔ faculty + central careers |
| mentoring (alumni) | 20 | ✔ faculty mentoring |
| alumni benefits | 20 | new (genuinely alumni) |
| student-life | 21 | ✔ |
| international | 20 | ✔ |
| graduation | 18 | — (see seam below) |
| wellbeing-health | 17 | ✔ |

On top of the central 116, **all 9 faculties independently run their own `/alumni/` section** (MDHS 23, Education 10, Science 9, Arts 6). So alumni content is authored in **10 places** too — exactly mirroring careers.

**The graduation→alumni seam is structurally invisible.** "Graduation" resolves to **0 pages at the current stage** (the apply-to-graduate / ceremony spine the audit flagged as missing in [Finding 17](structural-findings.md)) and 18 at the alumni stage — there is no web-level moment where a finishing student is handed to the alumni relationship. The relationship simply restarts on a new domain.

---

## 4. The prospective side is as fragmented as the current side — one domain earlier

The audit scoped *current* students. The prospective corpus shows the **identical fragmentation pattern repeated upstream**: alongside the 300-page central `study.unimelb.edu.au`, faculties host **~210 of their own prospective `/study/` pages** — Education 70, Law 44, Science 36, FFAM 20, FBE 17, ABP 15, FEIT 8. The same "central site + every faculty also does its own" structure the audit documented for current students exists wholesale for prospective students.

This means the **apply→enrol handoff crosses a domain boundary with zero shared vocabulary**: a student moves from `study.unimelb.edu.au/how-to-apply/...` to `{faculty}.unimelb.edu.au/students/...` or `students.unimelb.edu.au/...`, and nothing in the URL, taxonomy, or navigation tells them it is the same university or the next step. Whatever consolidation logic applies to current students applies one stage earlier — and the two efforts are currently unaware of each other.

---

## 5. IA across the lifecycle — four websites pretending to be one university

One journey, four architectures, no shared vocabulary:

| Stage | Domain | Top URL vocabulary | Median depth |
|---|---|---|--:|
| Prospective | `study.unimelb.edu.au` | `find` · `how-to-apply` · `study-with-us` · `student-life` | 2 (shallow/marketing) |
| Current | `{faculty}.unimelb.edu.au` + `students.unimelb.edu.au` | `students` · `current-students` · `study` | 3 |
| Alumni | `www.unimelb.edu.au/alumni` | `alumni` | 3 |

There is **no token in common** across the three stage vocabularies, no shared template, and (per [Finding 1](structural-findings.md)) not even a single URL convention *within* the current stage. A student does not experience one University website that follows them through life; they experience four unrelated sites that happen to share a brand. The cross-lifecycle version of the audit's "no shared vocabulary" ([Finding 21](structural-findings.md)) is more severe than the within-current version it documented.

---

## 6. Every cross-cutting service is reinvented at every stage

The topic × lifecycle-stage matrix shows which services are **pastoral/cross-cutting** (and therefore reinvented three times) versus genuinely **stage-specific**:

| Service | Prospective | Current | Alumni | Pattern |
|---|--:|--:|--:|---|
| careers-employability | 37 | 80 | 38 | **authored at all 3 stages** |
| student-life | 156 | 108 | 21 | all 3 |
| international | 121 | 100 | 20 | all 3 |
| scholarships | 75 | 113 | 1 | prospective + current split |
| wellbeing-health | 17 | 46 | 17 | all 3 |
| clubs-events | 14 | 52 | 4 | all 3 |
| contacts-support | 16 | 29 | 7 | all 3 |
| placements-WIL | 10 | 230 | 0 | **current-only (genuinely faculty-owned)** |
| course-planning | 2 | 115 | 0 | current-only |
| research-candidature | 1 | 192 | 1 | current-only (but see §2) |

The cross-cutting services (careers, student-life, international, wellbeing, clubs, contacts) are each written **three times in three voices** — a glossy prospective version, a functional current version, a nostalgic alumni version — for the same person at different ages. The genuinely stage-bound content (placements/WIL, course planning) is exactly what the audit already said to leave with faculties.

**Scholarships** is the cleanest split-catalogue: 75 prospective pages + 113 current pages (FEIT alone 66) describing the same award programs at two stages, while a central `scholarships.unimelb.edu.au` catalogue already exists.

---

## 7. Current students are the smallest tenant in the faculty estate

Composition of the full 2,363-page faculty estate by section:

| Section | Pages | Share |
|---|--:|--:|
| about | 439 | 19% |
| news | 251 | 11% |
| **research** | **203** | **9%** |
| study (prospective) | 195 | 8% |
| **current students** | **85** | **4%** |
| (remainder: schools, centres, engage, events…) | ~990 | 49% |

Faculty web estates are built for **reputation and recruitment** (about + news + research + prospective study ≈ 47%); explicit current-student content is the **smallest of the named sections at 4%**. This is the lifecycle framing of the [full-faculty-context finding](full-faculty-context.md): a current student is the lowest-priority audience on the very domains that host their faculty's content.

---

## What this adds to the recommendations

The cross-corpus view doesn't overturn central-and-spoke — it **extends the case along the time axis**:

1. **Scope the strategy to the lifecycle, not just current students.** The apply→enrol and graduate→alumni seams are the same fragmentation, one stage earlier and one stage later. A current-students-only fix leaves two of the three handoffs untouched.
2. **Careers is the highest-value cross-lifecycle connector.** Bridging faculty ↔ central ↔ alumni mentoring/careers is a bigger prize than the within-current careers fix already identified — it spans the moment students most need continuity.
3. **Give research students a candidature spine that connects to research identity.** The faculties richest in research (MDHS, Science, Education) need an HDR-student layer that doesn't exist; today research reputation and research-student support are run by different owners and never meet.
4. **Treat alumni as continuation, not restart.** Alumni services duplicate current-student services on a fourth domain with no handoff. The fix is a graduation→alumni bridge, not 116 + faculty-by-faculty re-authoring of careers and wellbeing.

**Lifecycle headline:** *the University runs four student websites — prospective, faculty-current, central-current, and alumni — on four domains with four architectures, and re-authors the same cross-cutting services (careers, student-life, international, wellbeing) at each one. The fragmentation the audit found inside the current-students estate is the same fragmentation that runs the full length of the student lifecycle.*
