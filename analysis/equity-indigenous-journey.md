# Equity & Indigenous Student Journey — Deep-Dive

*The highest-equity-stakes journey in the estate: the cohorts least able to absorb fragmentation hit the most of it. A forked disability-registration wizard, an Indigenous support service with zero hub presence, and financial-hardship support spread across ~5 pages — all behind login walls. June 2026.*

---

## Executive summary

The equity and Indigenous student journey is where the estate's fragmentation costs the most. Three findings define it:

1. **The disability registration wizard exists on only 1 of 3 equity hubs.** 12 external domains link disabled students to the two hubs that lack it — so a student arriving from their faculty lands on an equity page with no visible "register for support" path.

2. **Indigenous students have zero presence on the current-students hub.** Murrup Barak — the University's Indigenous student support unit — lives on a separate, uncrawled domain. The hub that serves every other cohort sends only 19–35 contextual links to the Indigenous service. Meanwhile MSD alone sends 614 — a building-and-construction faculty links Indigenous support 30× more than the student hub.

3. **Financial hardship support is ~5 pages.** The fee-remission form funnels through opaque SID query parameters. "Bursary" appears on 2 pages. A student in genuine financial crisis meets one of the thinnest, hardest-to-find corners of the estate.

The fix is structural: one canonical equity hub with the wizard, one Indigenous-students landing page on the hub, one emergency/hardship front door. Prioritise because the equity cost is highest.

---

## The SEDS fork: one wizard, three trees

### The problem

Student Equity & Disability Services (SEDS) is the entry point for disability registration, academic adjustments, and ongoing support. It's forked across **three live, simultaneously-published URL trees** on students.unimelb:

| Tree | Inbound links | Has registration wizard? | Linked by faculties? |
|---|---|---|---|
| `/support-and-wellbeing/student-equity-and-disability-services` | 137 | ✅ Yes (4-step: prepare→register→create→action) | No |
| `/student-support/student-equity-and-disability-services` | 63 | ❌ No | Yes — 12 domains |
| `/student-support/student-equity-and-disability-support` | 31 | ❌ No | Yes — 12 domains |
| `/sandbox/content-models/student-equity-and-disability-services` | 10 | ❌ Draft | No |

The 4-step registration wizard (prepare-to-register → registration-for-ongoing-support → create-your-plan → action-your-plan, each ~10-16 inbound with "Step N" anchors) exists ONLY under the canonical `/support-and-wellbeing` tree.

But **12 external domains** (arts, biomedicalsciences, education, eng, fbe, handbook, law, mdhs, medicine, msd, services, study) link disabled students to the two `/student-support` hubs that **do not carry the wizard**. A student arriving from their faculty's "disability support" link lands on a page with no visible path to register.

### The equity/hardship gap

Beyond SEDS, the equity journey fragments further:
- Financial hardship appears on only 5 pages across all 833 students.unimelb pages
- "Bursary" appears on 2 pages
- The fee-remission/refund route funnels into a single forms.your.unimelb.edu.au/4747166 reached via three opaque SID query params
- 143 students.unimelb pages reference that form ID — a widely-linked opaque destination
- The financial-aid page is mis-titled "Support and wellbeing"
- _nocache URL variants of fee pages leak into the link graph (15 pages link a _nocache version of CSP/HELP-loans eligibility)

---

## Indigenous students: zero hub presence, fragmented destinations

### The hub gap

A scan of all 833 students.unimelb pages returns **zero Indigenous-specific pages**. Murrup Barak — Melbourne's Indigenous student support unit — is not in the current-students IA at all. It lives on a separate, uncrawled domain murrupbarak.unimelb.edu.au, reached only as an outbound destination.

### Who links Murrup Barak — and who doesn't

| Source | Contextual links to Murrup Barak |
|---|---|
| msd.unimelb.edu.au | **614** |
| study.unimelb.edu.au | 79 |
| mdhs.unimelb.edu.au | 49 |
| students.unimelb.edu.au | **19** |
| research.unimelb.edu.au | 9 |
| eng.unimelb.edu.au | 7 |
| scholarships.unimelb.edu.au | 7 |
| science.unimelb.edu.au | 4 |
| services.unimelb.edu.au | 4 |
| arts.unimelb.edu.au | 3 |
| education.unimelb.edu.au | 3 |

The central student hub — the front door for every enrolled student — links Murrup Barak **19 times**. MSD, a building-and-construction faculty, links it **614 times** — a 30:1 ratio. The hub that should be the primary entry point for Indigenous student support is the second-lowest linker among faculties.

### The destination fragmentation

Indigenous support is scattered across 4+ destinations with no single canonical path:

| Destination | What it is | Inbound links |
|---|---|---|
| murrupbarak.unimelb.edu.au | Indigenous student support unit | 614 (msd), 19 (students hub) |
| indigenousknowledge.unimelb.edu.au | Research institute | 90 (research) |
| Wilin Centre (vca/finearts) | Indigenous arts centre | 29-10 |
| indigenousscholarships.com.au | External scholarships site | Unknown |

Anchors drift: "Indigenous Students" appears 611×, "Murrup Barak" 47×, "Visit Murrup Barak website" 5×. The destination is www-split (murrupbarak vs www.murrupbarak — one of the 28 www-twins in the estate). A student asking "where do I go for Indigenous support?" gets 4+ different answers depending on which page they land on.

### The wider equity destinations

| Destination | Inbound links |
|---|---|
| socialequity.unimelb.edu.au | 236 (research), 7 (eng), 5 (arts), 5 (law), 4 (medicine) |
| disability.unimelb.edu.au | 24 (research), 4 (mdhs), 3 (fbe) |

Social equity and disability research institutes have more presence on the estate than the services meant for current students.

---

## The financial-hardship pathway

A student in genuine financial crisis — can't pay rent, fees, or eat — needs emergency grants, fee remission, hardship bursaries, emergency accommodation, or food relief. What they find:

| Resource | Coverage | Findability |
|---|---|---|
| Financial hardship pages | ~5 on students.unimelb | Thin; buried under wellbeing |
| Bursary pages | ~2 | Near-invisible |
| Fee remission form | 1 — forms.your.unimelb.edu.au/4747166 | Three opaque SID params; no plain-language labels |
| Emergency accommodation | Scattered across wellbeing, scholarships | No single entry point |
| Food relief | Unknown | No dedicated page found |

The request funnels into one form with indistinguishable SID links. The financial-aid page is mis-titled. A stressed student is the least able to hunt.

---

## The common pattern: every action is behind a wall

Like every other journey in the estate, equity actions terminate behind login:
- SEDS registration → my.unimelb / forms
- Disability adjustments → Academic Adjustment Plan (behind login)
- Fee remission → forms.your.unimelb.edu.au
- Hardship grants → forms / my.unimelb
- Murrup Barak appointments → separate uncrawled domain

The public estate describes the service; it never lets the student transact it.

---

## Recommendations

### 1. Collapse SEDS to one canonical tree carrying the wizard `[HIGH · medium]`
Canonicalize to `/support-and-wellbeing/student-equity-and-disability-services`. 301-redirect the two `/student-support` trees. Unpublish the sandbox draft. Repoint the 12 external faculty/service links. Every equity hub must surface the prepare→register→create→action steps above the fold.

### 2. Create an Indigenous-students landing page on the hub `[HIGH · medium]`
Mirroring the international-student-support hub pattern: one canonical Indigenous-students page within students.unimelb that introduces Murrup Barak, scholarships, cultural leave, and the Wilin Centre, then deep-links out — so Indigenous students enter through the same front door as every other cohort.

### 3. Standardise the Indigenous support anchor and resolve the www-twin `[MEDIUM · quick-win]`
Standardise the outbound anchor to one label ("Murrup Barak — Indigenous student support"). Resolve the murrupbarak/www.murrupbarak twin to one host. Have all faculties link the new students.unimelb Indigenous-students hub page rather than 4 different destinations.

### 4. Build one emergency/hardship front door `[HIGH · medium]`
Create a clearly-titled, findable "Financial difficulty / emergency support" page consolidating fee remission, payment extensions, hardship grants, emergency loans, and Stop 1 financial advice. Link prominently from the fees hub, the census page, and paying-your-fees. Label the three fee-remission form actions in plain language. Strip _nocache query-string variants from internal links.

### 5. Surface the SEDS wizard from the "I need help now" front door `[MEDIUM · medium]`
If recommendation 1 lands, ensure the consolidated SEDS hub is reachable from a single "I need help now" crisis entry (as described in the at-risk student journey). A panicking student shouldn't need to know the service is called "SEDS."

---

## Linked improvements from the register

| § | Improvement | Severity · Effort |
|---|---|---|
| 8b.1 | Collapse SEDS to one canonical tree; repoint 12 faculties to wizard-carrying hub | HIGH · medium |
| 8b.2 | Create Indigenous-students landing page on the hub; standardise anchors and resolve www-twin | HIGH · medium |
| 8a.1 | Build emergency/hardship front door; label fee-remission SID links in plain language | MEDIUM · medium |
| 8a.2 | Create one canonical enrolled fees hub; bridge from applicant fee pages | HIGH · medium |
| 8c | Wire highest-risk pages (reduced study load, enrolment changes) to action forms | HIGH · medium |

---

*Built from: cross-site-flow.csv (Murrup Barak + equity links), improvements-register.md (§8 High-stakes Journeys, 8b International compliance & equity), lifecycle-journeys.md (Equity/Indigenous persona trace), student-services-profiles.json, and the full-scrape link graph. June 2026.*
