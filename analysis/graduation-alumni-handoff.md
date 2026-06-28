# Graduation → Alumni Handoff — Deep-Dive

*The last transition in the student lifecycle — and the most severed. 35 completion pages, 0 alumni links. The graduation-day page links Facebook and Instagram but not the alumni relationship. This is the seam where the University loses every graduating student as a lifelong connection. June 2026.*

---

## Executive summary

The graduation→alumni handoff is the single most broken transition in the student lifecycle. After 3–5 years of interacting with the University across 20+ systems, a graduating student is handed to the alumni relationship by essentially nothing. The evidence is stark: **after stripping navigation chrome, only ~97 contextual links reach the alumni estate** — and **zero of them come from any completion page**. The graduation-day page links Facebook and Instagram but not alumni.unimelb. 35 completion/conferral pages across the hub exist to mark the end of a degree, and not one of them bridges to what comes next.

This is not a content problem. The alumni estate exists — 16 mentoring pages across 12 faculty-specific streams, a global alumni network, events, giving, and benefits. It's a **design problem**: the join between "I've finished" and "I'm an alum" was never built. The fix is the highest-leverage, lowest-cost service-design intervention in the improvements register: add one prominent, consistent "Stay connected" bridge from every completion page, and the alumni relationship activates for every graduating student.

---

## The seam by the numbers

| Metric | Value | Source |
|---|---|---|
| Completion/conferral pages on students.unimelb | 35 | crawl/students-full |
| Contextual links from completion pages → alumni | **0** | link-graph audit |
| Total contextual links estate-wide → alumni hosts | ~97 | cross-site-flow.csv |
| Graduation-day page links to alumni | 0 | page audit — links Facebook, Instagram, Twitter, TikTok |
| Alumni mentoring streams | 12 (per faculty) | www.unimelb/alumni |
| Faculty student-mentoring programs | 8+ | faculty CMSes |
| Cross-links between faculty mentoring and alumni mentoring | 0 | link-graph audit |

---

## The journey as it actually works

### "I'm graduating — now what?"

A student completes their final semester, receives results via my.unimelb (behind login), and is told they're eligible to graduate. The public estate's "complete → graduate" transition is partial but functional:

1. **Apply to graduate** — a clean spine on students.unimelb (conferral, ceremony, academic dress)
2. **Check completion** — course completion checks via my.unimelb
3. **Attend ceremony** — graduation-day page with logistics, tickets, dress
4. **Receive testamur** — parchment and academic transcript

This spine exists and works. It's split across two URL trees (the hub's mid-migration debt again) but it's navigable.

### The missing step: "You're an alum now"

After the ceremony, the estate goes silent. The graduation-day page — the highest-traffic completion moment — carries social media links (Facebook, Instagram, Twitter, TikTok) but **nothing to alumni.unimelb**. No "Stay connected," no "Join your alumni network," no "Mentor the next cohort." The student who just spent 3–5 years as the University's most important customer is discharged without a forward path.

From the alumni side, www.unimelb/alumni runs:
- 16 mentoring pages across 12 faculty-specific streams (accounting, arts, business, education, engineering, law, MDHS, science, vet science…)
- A global alumni network with events and chapters
- Giving and volunteering pathways
- Benefits and services (library access, career support, discounts)

But none of this is wired to the moment a student becomes an alum. The alumni estate is nav-only — reachable only if a graduate already knows to type "unimelb alumni" into Google.

---

## What makes this different from the rest of the estate

The graduation→alumni seam is unique in three ways:

### 1. It's the only purely additive fix in the register
Every other seam requires collapsing trees, retiring deprecated pages, or rewiring systems. This one requires **adding one bridge** — nothing to unpick, nothing to migrate.

### 2. The downstream service already exists
The alumni estate is built, staffed, and functional. Careers Online exists. The mentoring programs exist. The gap is a **missing handoff**, not a missing service. Adding the bridge costs nothing in service-delivery terms.

### 3. It closes the lifecycle loop
A graduating student who becomes an alum becomes a mentor, a donor, an employer of graduates, a postgraduate applicant. The alumni→mentoring→careers→prospective loop is the University's most valuable flywheel. It currently doesn't spin because the first connection was never made.

---

## The faculty mentoring disconnect

A compounding failure: faculty student-mentoring and alumni mentoring are **the same service for adjacent life stages, and they never link**.

- Faculties run their own student-mentoring programs (8+ across the estate)
- Alumni runs 12 faculty-specific mentoring streams
- A final-year student in a faculty mentoring program graduates into the alumni mentoring stream for the SAME faculty
- **Zero pages cross-reference the two**

This is the highest-value, lowest-cost careers connection in the estate: at the completion moment, tell the graduating student "your faculty mentoring continues as alumni mentoring — here's the link." This single bridge serves Sam, Priya, Jordan, AND Taylor simultaneously — every graduating student benefits.

---

## The alumni footprint

| Component | Pages | Note |
|---|---|---|
| www.unimelb/alumni home | 1 | Global alumni front door |
| Faculty-specific mentoring streams | 16 | 12 streams (accounting, arts, business, education, engineering, law, MDHS, science, vet science…) |
| Alumni events | ~5 | Global + chapter events |
| Giving / volunteering | ~8 | Donation and volunteer pathways |
| Benefits & services | ~10 | Library access, career support, discounts |
| **Total contextual inbound links** | **~97** | Entire estate → any alumni host |

Compare ~97 alumni links to:
- ask.unimelb FAQ: **396** links
- my.unimelb (the SIS): **187** links
- Handbook: **195** links

The alumni estate gets fewer contextual links than a single FAQ knowledge base. The student's 3–5 year relationship with the University receives less connective tissue than a census-date article.

---

## The completion-page audit

| Page type | Count | Links to alumni |
|---|---|---|
| Apply to graduate | ~8 | 0 |
| Conferral / ceremony dates | ~5 | 0 |
| Academic dress / tickets | ~6 | 0 |
| Graduation day | 1 | 0 (links Facebook, Instagram, Twitter, TikTok) |
| Testamur / transcripts | ~6 | 0 |
| Course completion | ~4 | 0 |
| After graduation / what's next | ~5 | 0 |
| **Total** | **~35** | **0** |

---

## Recommendations

### 1. Add one "Stay connected" bridge to every completion page `[HIGH · quick-win]`
On all 35 completion/conferral pages, add a consistent, prominent "Stay connected — join your alumni network" CTA. One link, one destination (alumni.unimelb), one line of design. This is the single highest-leverage fix in the improvements register — zero migration cost, maximum impact.

### 2. Replace social media links on the graduation-day page with alumni `[HIGH · quick-win]`
The graduation-day page currently links Facebook, Instagram, Twitter, and TikTok. Replace (or supplement) with "Join your alumni network" → alumni.unimelb. A graduating student at their highest-engagement moment should be handed to the University's own relationship, not a social media platform.

### 3. Bridge faculty mentoring → alumni mentoring at completion `[HIGH · quick-win]`
On every faculty student-mentoring page and every completion page, add "Your mentoring continues after graduation — join the [faculty] alumni mentoring program." The same service, adjacent life stages, one link.

### 4. Add alumni to the "Get Started" reverse sequence `[MEDIUM · medium]`
The University has a "Get Started at Melbourne" sequence for new students. Build a "Stay Connected with Melbourne" sequence for graduating students — alumni network, mentoring, careers, events, benefits. Same pattern, opposite end of the lifecycle.

### 5. Wire "After graduation" pages to actual alumni services `[MEDIUM · medium]`
The ~5 "after graduation / what's next" pages currently describe what alumni status *means*. Wire them to what alumni status *does*: mentoring signup, events calendar, career services, library access.

---

## Linked improvements from the register

| # | Improvement | Severity · Effort |
|---|---|---|
| 7 | Build the graduation→alumni bridge (35 completion pages, 0 alumni links) | HIGH · quick-win |
| 8 | Wire faculty + hub to central Careers Online at the apply-for-jobs moment | HIGH · medium |
| — | Bridge faculty student-mentoring to alumni mentoring at final-year/graduation | HIGH · quick-win |

---

## Related deep-dives

- `analysis/lifecycle-journeys.md` — Lifecycle seam map (graduate→alumni = severed)
- `analysis/careers-employability-wil.md` — Faculty + alumni mentoring disconnect
- `analysis/improvements-register.md` — Item #7, Top 12
- `personas/` — All 5 personas end with this broken seam
- `report/Lifecycle-Journeys.html` — Formatted lifecycle report

---

*Built from: improvements-register.md (Top 12, Item #7), lifecycle-journeys.md (seam map), careers-employability-wil.md (alumni mentoring section), full-scrape link graph (cross-site-flow.csv, hub crawl), and the completion-page audit over crawl/students-full/. June 2026.*
