# Full-Faculty Context — the denominator the slice never had

*From full-domain crawls of 9 faculty marketing sites (`crawl/full-faculty/*.json`, 2,363 pages, June 2026). The structural audit crawled only the current-students **slice** of each domain; this crawl captured the whole faculty estate around it. Figures reproducible via [`data/clean/full_faculty_stats.py`](../data/clean/full_faculty_stats.py).*

> **Why this matters.** Every earlier finding measured the current-students estate in isolation — it had no "outside" to compare against. The full-domain crawl supplies that outside: it shows the current-students content sitting inside the faculty's *actual* web presence. The headline is a reframe, not a reversal — it makes the central-and-spoke case stronger.

---

## The reframe: faculty domains are outward-facing estates; current students are a minority tenant

By the site's own navigation, current-student content is a thin, often unsigned slice of each faculty domain. The rest is research, news/newsroom, about, prospective `/study/`, and industry/engagement — content built for prospective students, media, industry, and donors, not enrolled students.

| Faculty domain | Full domain pages | Explicit `/students/` section | Audit's content-tagged "student" slice |
|---|--:|--:|--:|
| eng (FEIT) | 239 | 18 (7.5%) | 204 |
| law | 266 | 9 (3.4%) | 195 |
| science | 263 | 35 (13.3%) | 94 |
| mdhs | 313 | 3 (1.0%) | 112 |
| arts | 259 | 2 (0.8%) | 84 |
| education | 380 | 68 (17.9%) | 47 |
| msd (ABP) | 220 | 31 (14.1%) | 250 |
| fbe | 161 | 3 (1.9%) | 36 |
| finearts-music (FFAM) | 262 | 2 (0.8%) | 37 |
| **All 9** | **2,363** | **171 (7.2%)** | — |

The two right-hand columns are the two honest answers to "how much of a faculty site is for current students," and the gap between them *is* the insight:
- **By the site's own IA**, ~7% is explicitly sign-posted for current students.
- **By content relevance** (the audit's generous tagging boundary), a majority of some domains is student-usable.

So student content is **pervasive but rarely sign-posted as such** — it lives in `/about/`, `/grd/`, `/jd/`, `/study/`, and discipline areas, not a dedicated, liftable student estate. A current student on a faculty domain is navigating a marketing/research site where their tasks are a side-quest. That is the structural reason the seams are bad and why a central `students.unimelb.edu.au` has to exist.

---

## Six connections the slice couldn't make

### 1. No shared faculty IA — nine domains, nine architectures
The dominant top-level section is different in every faculty:

| Faculty | Biggest section | Share |
|---|---|--:|
| eng | `/ingenium/` (a magazine) | 182/239 = 76% |
| finearts-music | `/about-us/` | 226/262 = 86% |
| law | `/about/` | 92/266 = 35% |
| science | `/engage/` | 71/263 = 27% |
| education | `/aerc/` (a research centre) | 80/380 = 21% |
| arts | `/news/` (then five named schools) | 49/259 = 19% |
| mdhs | `/engage/` | 56/313 = 18% |
| fbe | `/newsroom/` | 30/161 = 19% |
| msd | `/news/` | 38/220 = 17% |

No two faculties share a top-level taxonomy. **This is the parent-level root cause of the student-slice inconsistency the audit documented** — the student sections inherit nine unrelated site architectures, so they were never able to be consistent. ([Finding 1](structural-findings.md) — four URL conventions — is the visible tip of this.)

### 2. Parallel reinvention, now provable at the front door
Identical page titles recur across domains, each independently maintained:
- **"Current Students"** — 6 faculties (arts, education, eng, mdhs, msd, science)
- **"Research"** and **"Contact us"** — 7 faculties each
- **"Engage with us"**, **"Alumni"**, **"Events"** — 4 faculties each
- **"Future Students"**, **"Study"** — 3 faculties each

Every faculty rebuilds the same shell. This confirms the estate's duplication thesis ([Finding 12](structural-findings.md), [Finding 21](structural-findings.md)) one level up from the student content itself.

### 3. The audit's per-faculty counts drew a generous boundary
law 195 / eng 204 pages were content-tagged "current-students," but those domains explicitly section only 9 / 18 under `/students/`. Most "faculty student content" is general faculty content that happens to be student-relevant — **not a dedicated student estate that can be lifted wholesale.** This sharpens consolidation targeting: less is cleanly liftable than the slice counts implied, which makes "connect the seams" beat "relocate the estate" even more decisively.

### 4. Prospective beats current, quantitatively
Faculties invest more in `/study/` (prospective) than in explicit current-student sections: education 69, law 40, science 36 prospective pages. The outward-facing tilt is now measured, not asserted — it reinforces [Finding 16](structural-findings.md) (the reverse funnel back to the prospective site).

### 5. Soft cross-posting exists (where fingerprints don't catch it)
Single research/news stories appear across 3 faculty news sections — e.g. *"Co-winners of the 2022 Ernest Scott Prize"* on arts + education + mdhs. Shared content is real but detectable only by title, not by content hash (see null result below).

### 6. Thin content at estate scale
12% of all 2,363 pages are under 160 words — **fbe 32%, mdhs 21%, education 18%**. The maintenance-liability pattern of [Finding 19](structural-findings.md) holds across the full estate, not just the student slice.

---

## One dead end, reported honestly

The crawl records a per-page `fingerprint` content hash. It yields **0 collisions** within or across domains — it only matches byte-identical pages, of which there are none (every page differs in nav/timestamp chrome). The near-duplicate clusters the audit found by hand ("Employability in X" ×7, [Finding 14](structural-findings.md); "Wellbeing + Ambassadors" ×6) need title/shingle similarity, not this hash. **The full crawl therefore adds no new cross-faculty *literal*-duplicate finding** — connection 5 (title-level cross-posting) is the most this data supports.

---

## What it changes for the recommendations

Nothing reverses; the central-and-spoke direction is reinforced:
- **Full centralisation is even less viable** — there is no common faculty IA to centralise *into*, and most faculty "student" content is entangled with non-student content that wouldn't move with it.
- **The prize is still the seams** — a 7%-sign-posted, content-pervasive student layer inside nine unrelated outward-facing estates is exactly the case for a consistent student-facing overlay (URL convention, signposting, careers/scholarships cross-linking) rather than a migration.
- **A standardised student template** ([recommendations §4h](../report/recommendations.md)) is the only lever that touches all nine architectures without trying to unify their parent sites.

**Deck headline:** *the fragmentation isn't a student-content problem layered on tidy faculty sites — the faculty sites themselves share no architecture, and current-student tasks are a ~7% unsigned tenant inside nine unrelated outward-facing estates.*
