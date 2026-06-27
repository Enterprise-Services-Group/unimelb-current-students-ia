# Careers, Employability & WIL — Deep-Dive

*The University’s careers offer, traced across the whole estate and the whole lifecycle — prospective “career outcomes” → the central Careers service → faculty careers → work-integrated learning → graduate outcomes → alumni mentoring. Careers is the most cross-cutting student service there is; this is how fragmented it has become. June 2026.*

---

## Executive summary

Careers is the service that should bind the student lifecycle together — it is the through-line from “why this degree?” to “here is my first job” to “now mentor the next cohort.” The University authors a great deal of it: **1,058 careers and employability pages across 18 domains**, plus 92 work-integrated-learning pages. But it is **authored everywhere and connected nowhere.** The central Careers *service* is hollow — ~42 pages of advice on the hub — while the substance sprawls across a 440-page prospective persuasion layer and 539 pages of faculty careers content, and the **actual service** (the jobs board, employer connections and appointment booking on Careers Online) sits behind a login wall reached by just 73 contextual links estate-wide. The public estate describes careers; it almost never lets a student *do* careers.

Three gaps compound this. **Work-integrated learning has no centre at all** — 4 hub pages against 87 on the faculties — so a student cannot discover a placement from anywhere but their own faculty silo. **Faculty mentoring and alumni mentoring are the same service for adjacent life stages, and never link** — a final-year student’s faculty mentoring and the twelve alumni mentoring streams they graduate into do not cross-reference (alumni gets ~97 contextual links total, 0 from any completion page). And the **prospective “career outcomes”** sold to applicants (440 per-course pages) are wired to nothing that delivers them once the student enrols.

The prize is unusually clean: careers is one service with one obvious owner. Make the hub the front door, surface Careers Online as the action, build the missing WIL centre, and bridge faculty→alumni mentoring — and the most fragmented service becomes the connective tissue the whole lifecycle is missing.


## The careers spine across the lifecycle

| Stage | Where it lives | Footprint | Note |
|---|---|---|---|
| Prospective — “career outcomes” | `study.unimelb` | 440 pages | per-course career-outcomes tabs — a persuasion layer, separate from the service |
| Central Careers service | `students.unimelb/careers` | 42 pages | the hub careers section — thin |
| Careers Online (the action) | `careersonline.unimelb · behind login` | ~115 links in | jobs board + appointments — the actual service, barely pointed to |
| Faculty careers | `8+ faculties` | 539 pages | fbe 100, arts 84, mbs 72, eng 64, education 54, law 40… |
| WIL / placements | `faculty-owned` | 92 pages · 4 central | no central front door — undiscoverable from the centre |
| Alumni mentoring | `www.unimelb/alumni` | 16 pages · 12 streams | the same mentoring service, severed from faculty careers |

The spine exists at every stage but the joins are thin: ~115 contextual links reach the careers platforms, WIL has 4 central pages, and the alumni mentoring end is severed (0 links from completion pages).

## The findings


### Careers is authored everywhere and connected nowhere  `[HIGH]`

**Evidence.** 1,058 careers/employability pages span 18 domains — but only ~115 contextual links reach the careers platforms (careersonline 73, careers.unimelb 27, career-checklist 13). Several faculties send near-zero contextual links into the central careers service. The lifecycle's most cross-cutting service is its least connected.

**Recommendation.** Name one canonical Careers owner spanning the lifecycle and make every careers page (prospective, faculty, alumni) deep-link the central service + Careers Online. Treat careers as connective tissue, not a per-site feature.

### The central Careers service is hollow — the action is behind login  `[HIGH]`

**Evidence.** students.unimelb/careers is ~42 pages of advice, while the actual service — the jobs board, employer connections and appointment booking — lives on careersonline.unimelb.edu.au behind a login wall, reached by only 73 contextual links estate-wide. The public estate describes careers; it never lets the student DO careers.

**Recommendation.** Make the hub the unambiguous front door that prominently and consistently deep-links Careers Online (and the appointment booking) from every careers and faculty page — surface the action, don’t just describe it.

### WIL & placements has no central front door  `[HIGH]`

**Evidence.** Work-integrated learning is 92 pages across 11 faculty domains (fbe 25, medicine 19, education 17, MBS 7…) but only 4 pages on the central hub. A student cannot discover their own or another faculty’s placement/WIL offerings from the centre; MDHS clinical-placement compliance and the SONIA placement system are siloed.

**Recommendation.** Create a single central ‘Work-Integrated Learning & Placements’ landing that explains WIL in one shared vocabulary and aggregates/deep-links every faculty’s offering — the missing centre of this service.

### Faculty and alumni mentoring are the same service, never linked  `[HIGH]`

**Evidence.** Alumni runs 16 mentoring pages across 12 faculty-specific streams (accounting, arts, business, education, engineering, law, MDHS, science, vet science…), and faculties run their own student-mentoring — the same service for adjacent life stages. A final-year student’s faculty mentoring and the alumni mentoring they graduate into do not cross-reference. The alumni estate gets ~97 contextual links total and 0 from any completion page.

**Recommendation.** Bridge faculty student-mentoring to the alumni mentoring streams at the final-year/graduation moment — the highest-value, lowest-cost careers connection across the lifecycle.

### FBE and MBS double-host the entire BCom careers tree  `[HIGH]`

**Evidence.** Two faculties maintain near-identical copies of the same Bachelor of Commerce careers estate — ~59 near-duplicate pages (confirmed by the shingle-Jaccard near-duplicate detector) — so the same careers content is authored, maintained and drifts out of sync twice.

**Recommendation.** Pick one owner for the BCom careers content and 301-redirect the duplicate tree; the other links it rather than re-hosting.

### ‘Employability in X’ is a seven-faculty template clone  `[MEDIUM]`

**Evidence.** Seven faculties each run a near-identical ‘Employability in <discipline>’ page that restates the same central careers service with a discipline label — template duplication, not discipline-specific value.

**Recommendation.** One shared central employability page; each faculty contributes only its genuinely discipline-specific layer (regulated pathways, internship subjects, professional registration) and links the centre for the rest.

### Prospective ‘career outcomes’ is a marketing layer disconnected from the service  `[MEDIUM]`

**Evidence.** study.unimelb carries 440 per-course ‘career outcomes’ pages (the persuasion that sells the degree), but they are separate from the 42-page current Careers service — the promise made to the applicant is never wired to the service that would deliver it once enrolled.

**Recommendation.** Connect the prospective career-outcomes promise to the current Careers service and Careers Online, so the outcome a student was sold becomes a service they can use.

### No shared careers vocabulary or owner across the lifecycle  `[MEDIUM]`

**Evidence.** Careers, employability, WIL, placements, internships, mentoring and graduate-outcomes are named and located differently at every stage and on every faculty site — there is no single careers taxonomy a student (or a search) can rely on across prospective → current → alumni.

**Recommendation.** Define one careers service taxonomy and front door used identically across the lifecycle; standardise the labels (Careers, WIL, Mentoring) and the entry path on every faculty site.


---

*Source: `analysis/full-scrape/careers-pages.csv` (the careers/WIL footprint), the careers + placements service profiles in `analysis/student-services-profiles.json`, the careers spine in `analysis/lifecycle-cross-corpus.md`, and the near-duplicate detector. Careers Online and the placement systems (SONIA) are behind login and uncrawled — inferred from outbound links.*