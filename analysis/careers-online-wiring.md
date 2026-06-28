# Careers Online Wiring — Deep-Dive

*The most cross-cutting student service in the estate is its least connected. 1,150 careers pages exist across 18 domains — but only 115 contextual links reach the careers platforms. 5 faculties send 0. This is the seam where the promise made to applicants ("career outcomes") never connects to the service that would deliver it. June 2026.*

---

## Executive summary

Careers is the service that should bind the student lifecycle together — from "why this degree?" on study.unimelb to "here is my first job" on Careers Online to "now mentor the next cohort" on the alumni platform. The University authors a great deal of it: **1,150 careers and employability pages across 18 domains**, plus 92 work-integrated-learning pages. But the **actual service** — the jobs board, employer connections, and appointment booking on careersonline.unimelb.edu.au — sits behind a login wall reached by just **73 contextual links estate-wide**. Another 27 reach the marketing site careers.unimelb.edu.au. 13 reach the career-checklist tool. 2 reach the employer portal. Total: **115**.

Compare that to ask.unimelb (396), my.unimelb (187), or the Handbook (195) — and Careers Online carries fewer contextual links than a legacy FAQ knowledge base. The estate describes careers everywhere; it almost never lets a student *do* careers.

---

## The wiring by the numbers

### The careers footprint

| Component | Pages | Locations |
|---|---|---|
| Faculty careers content | 547 | 12+ faculty domains |
| Prospective "career outcomes" | 440 | study.unimelb (per-course tabs) |
| Central hub careers section | 46 | students.unimelb /careers |
| Alumni careers | 38 | www.unimelb /alumni |
| **Total careers pages** | **1,150** | **18 domains** |

### Contextual links to careers platforms

| Careers platform | Role | Contextual links | Behind login? |
|---|---|---|---|
| careersonline.unimelb.edu.au | Jobs board, appointments, employer connections — the actual service | 73 | Yes |
| careers.unimelb.edu.au | Marketing / service information site | 27 | No |
| career-checklist.unimelb.edu.au | Career readiness self-assessment tool | 13 | No |
| employers.careersonline.unimelb.edu.au | Employer portal | 2 | Yes |
| **Total** | | **115** | |

### Faculty-by-faculty: who wires careers and who doesn't

| Faculty | careersonline | careers.unimelb | career-checklist | Total | Verdict |
|---|---|---|---|---|---|
| eng | 15 | 3 | 2 | **20** | ✅ Wired properly |
| fbe | 12 | 4 | 1 | **17** | ✅ Wired properly |
| mbs | 9 | 7 | 1 | **17** | ✅ Wired properly |
| arts | 10 | 0 | 2 | **12** | ⚠ Below floor |
| finearts-music | 2 | 0 | 1 | **3** | ⚠ Below floor |
| biomed | 1 | 0 | 1 | **2** | ❌ Near-zero |
| msd | 0 | 1 | 1 | **2** | ❌ Near-zero |
| science | 0 | 0 | 1 | **1** | ❌ Effectively zero |
| law | 0 | 1 | 0 | **1** | ❌ Effectively zero |
| dental | 0 | 0 | 0 | **0** | ❌ Zero |
| education | 0 | 0 | 0 | **0** | ❌ Zero |
| mdhs | 0 | 0 | 0 | **0** | ❌ Zero |
| medicine | 0 | 0 | 0 | **0** | ❌ Zero |

**Five faculties send zero links to any careers platform.** Three more send exactly one. Together they cover medicine, health sciences, education, law, science, architecture — the majority of the University's student population.

### The central hub's own wiring

Even `students.unimelb.edu.au` — which hosts a 36-page careers section — sends only **32** contextual links to careers platforms:
- 22 to careersonline
- 8 to careers.unimelb
- 2 to career-checklist

The hub's own careers section describes the service but barely links to the transactional platform. The find→act gap is present even at the centre.

### The MSD paradox

MSD sends **8,069 contextual links to students.unimelb** — the most of any faculty by a factor of 40. But it sends exactly **1 link to a careers platform** (career-checklist). The faculty that links deepest into the student hub is the faculty that links least to the careers service.

---

## Where the careers pages actually go

The 211 faculty placement/WIL pages emit 347 links to students.unimelb, but **201 (57%) go to the bare homepage** — generic, not careers content. Only a handful reach specific careers targets (Stop 1 ×18, /careers ×13, working-on-a-student-visa ×7). careersonline gets just **11 inbound from all 211 placement pages combined**. Placements and WIL — the most current-only, faculty-owned careers topic — dead-ends at the homepage.

---

## The BCom duplicate tree

FBE and MBS double-host the entire Bachelor of Commerce careers estate: 59 shared tails, 46 scoring Jaccard ≥0.85. 35 MBS /career/ URLs contain "fbe" — MBS is literally serving FBE-branded student-calendar content. The two faculties maintain near-identical copies that drift out of sync across two CMSes, splitting link equity and confusing students.

---

## Recommendations

### 1. Add a "Find jobs & book a careers adviser → Careers Online" CTA to every faculty landing page `[HIGH · medium]`
Template change ×13 faculties. One consistent CTA, one destination. Target: lift every faculty to a floor of ~18 links (the eng/FBE pattern). This immediately serves the 8 faculties currently at or near zero.

### 2. Make the central hub careers section wire Careers Online prominently `[HIGH · quick-win]`
The 36-page central careers section describes the service. Add a consistent "Find jobs / Book an appointment → Careers Online" CTA from every page. The hub should be the exemplar, not another gap.

### 3. Replace bare-homepage links from placement/WIL pages with deep careers links `[MEDIUM · medium]`
201 of 347 placement→students links go to the bare homepage. Replace with deep links to the central careers service + Careers Online + WIL-relevant pages. Establish one central WIL hub page.

### 4. De-duplicate the BCom careers tree — one owner, one URL `[HIGH · medium]`
Designate fbe.unimelb.edu.au/bcom/career as the single owner. 301-redirect the 46 MBS /career/ tails scoring ≥0.85. Eyeball the remaining 12 for MBS-specific localisation.

### 5. Surface Careers Online from prospective career-outcomes pages `[MEDIUM · medium]`
The 440 per-course "career outcomes" tabs on study.unimelb sell the career promise. Add a forward link: "See how we help you get there → Careers and Employability" so the promise connects to the service before enrolment.

### 6. Establish a floor of 18 contextual links per faculty `[MEDIUM · medium]`
Make it a governance requirement: every faculty's "current students" section must deep-link Careers Online at least once. The eng/FBE pattern is proven — replicate it everywhere.

---

## Linked improvements from the register

| # | Improvement | Severity · Effort |
|---|---|---|
| 8 | Wire faculty + hub to central Careers Online at the apply-for-jobs moment | HIGH · medium |
| 3.8 | Give faculty placement/WIL pages real deep-links into careers + WIL spine | MEDIUM · medium |
| 4.2 | Decommission MBS's duplicate BCom careers tree (46 confirmed-duplicate tails) | HIGH · medium |
| 4.3 | Extract 7-faculty "Employability in X" template clone into one central component | MEDIUM · medium |

---

*Built from: cross-site-flow.csv (careers platform links), careers-pages.csv (1,150 pages), careers-employability-wil.md (existing deep-dive), improvements-register.md (items 8, 3.8, 4.2, 4.3), and the full-scrape link graph. June 2026.*
