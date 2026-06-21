# Unification Strategy — Recommendations for University of Melbourne Current Students IA

*Evidence-based recommendations from the full crawl of all 12 current-students sections (9 faculties + 3 schools) + students.unimelb.edu.au — 1,173 pages. June 2026.*

---

## Executive Summary

The University of Melbourne runs a fragmented current-students ecosystem: **9 faculty CS sections + 3 school CS sections (MBS, Biomedical Sciences, Dental) + students.unimelb.edu.au — 1,173 pages crawled (1,161 after de-duplication).** The decisive finding from the full crawl is that **85% of pages (997) carry substantive, unique content** — only ~4% are pure link-farms, ~7% mixed, ~4% broken/redirect. Every faculty hosts a substantial, genuinely discipline-specific estate; even faculties earlier assumed to be thin "link directories" are content-rich (ABP runs 240 unique pages; MDHS 104). What faculties delegate to students.unimelb.edu.au is **transactional admin, not their discipline content.** students.unimelb.edu.au covers transactional admin comprehensively but has no presence in course planning, placements, or discipline-specific skills.

This document presents **four options** for addressing the fragmentation, with detailed trade-offs for each, and a recommendation. The options are not binary — each can be tuned along dimensions of centralisation depth, personalisation, and implementation speed.

**Recommended approach:** Central-and-spoke with clear boundaries. students.unimelb.edu.au owns transactional and cross-cutting services. Faculties retain discipline-specific content under a standardised template. Total migration over 12 months in three phases.

> **Evidence update (full crawl).** The option tables below were first drafted on a partial crawl (4 faculties). The completed crawl of all 12 units confirms the *direction* (central-and-spoke) but revises the *figures*: the unique, discipline-specific estate is far larger (~997 pages, 85%) and the removable duplication is thinner than the "~200 duplicative / ~400–450 unique" estimates in the tables below imply. Read the per-option page counts as indicative. The strategic implication is *stronger*, not weaker — full centralisation is even less viable, and the prize is connecting the seams (signposting, careers cross-linking, URL standardisation) and trimming a thin duplicative layer, not relocating ~1,000 pages of unique faculty content. Measured split: see Evidence Base (and the DEAG findings pack).

> **Context update (full faculty domains).** A subsequent full-domain crawl of all 9 faculty marketing sites (2,363 pages) supplies the denominator the current-students slice never had: current-student content is only **~7% sign-posted** of each faculty's actual web estate — the rest is research, news, about, and prospective `/study/`. Two facts sharpen the recommendation. (1) **There is no shared faculty IA to centralise into** — the dominant section differs in every faculty (eng is 76% a magazine; FFAM 86% "about-us"; education is research-centre-led). (2) **Most "faculty student content" is entangled with non-student content** (Law/FEIT explicitly section only 9/18 student pages despite ~195/204 tagged), so it is not a portable estate. Both make full centralisation *less* viable and the standardised template + URL convention the primary levers. Evidence: [`analysis/full-faculty-context.md`](../analysis/full-faculty-context.md).

---

## The Decision: Four Options

Four approaches to unifying the current-students experience, ranging from full centralisation to minimal intervention. Each is detailed below with scope, what changes, what stays, costs, risks, and decision criteria.

---

## Option A: Full Centralisation

All current-students content moves to `students.unimelb.edu.au`. Faculty CS sections become redirects or thin gateway pages. Faculty sites no longer host current-students content.

This option has **three sub-variants** depending on how content is handled:

### Variant A1: Full Consolidation

Move every existing faculty CS page to students.unimelb.edu.au, organised under `/your-faculty/<slug>/`.

| Dimension | Detail |
|-----------|--------|
| **Pages created on students.unimelb.edu.au** | ~600-700 (all faculty CS pages, re-hosted) |
| **Pages removed from faculties** | ~600-700 (redirected to students.unimelb.edu.au equivalents) |
| **students.unimelb.edu.au IA impact** | Adds a `/your-faculty/` section with 9 sub-sections mirroring current faculty IA |
| **Content changes** | Minimal — lift and shift. URLs change, content stays. |
| **Timeline** | 6-12 months (content migration + redirect mapping + QA) |
| **Central team burden** | Medium — central team manages students.unimelb.edu.au platform, templates, and governance. Faculty web officers retain authorship of their section's pages via distributed CMS permissions. Requires a RACI and governance framework to define who can publish what. |

**What this fixes:**
- Students have one place to search: `students.unimelb.edu.au`
- No URL convention problem (everything is on students.unimelb.edu.au)
- Search across all CS content becomes possible (single domain)

**What this requires:**
- A **distributed authorship model** — faculty web officers retain control of their section's pages on students.unimelb.edu.au. This requires CMS permissions, a RACI matrix defining who can create, edit, approve, and publish, and workflow governance.
- 600 pages of redirect mapping — every old faculty URL needs a 301 redirect to its new students.unimelb.edu.au location
- students.unimelb.edu.au IA becomes deep — students still navigate to "their faculty" section, which replicates the current problem at a different URL
- The central team's role shifts from "do everything" to "manage the platform and enforce governance"

**Decision criteria for choosing A1:**
- You believe a single URL namespace is the overriding priority
- You're willing to invest in the distributed authorship model (RACI, CMS permissions, workflow governance)
- Faculties are willing to author their content on students.unimelb.edu.au rather than on their own domains

### Variant A2: Harmonise-Then-Centralize

First, standardise faculty CS content to remove duplication. Then, migrate only what remains to students.unimelb.edu.au. Duplicative content is deleted, not moved.

| Dimension | Detail |
|-----------|--------|
| **Step 1 — Harmonisation** | All 9 faculties adopt the standardised CS template and remove central-duplicative pages (enrolment, fees, exams, graduation, health, key dates). Estimated ~200 pages removed across faculties. Remaining: ~400-450 pages of genuinely unique content. |
| **Step 2 — Centralisation** | Move the ~400-450 remaining unique pages to students.unimelb.edu.au under `/your-faculty/<slug>/`. |
| **Pages created on students.unimelb.edu.au** | ~400-450 (only unique content) |
| **Pages removed from faculties** | ~600-700 total (~200 duplicative deleted in Step 1 + ~400-450 moved in Step 2) |
| **Timeline** | 12-18 months (harmonisation first, then migration) |
| **Central team burden** | Medium — same distributed authorship model as A1. Fewer pages to manage (~400 vs ~600) because duplication was eliminated in Step 1. |

**What this fixes (beyond A1):**
- Duplication is eliminated before migration, so students.unimelb.edu.au doesn't inherit redundant content
- The standardised template means all faculty content follows the same structure
- students.unimelb.edu.au search is cleaner — no duplicate results for the same service

**What this requires (beyond A1):**
- The same distributed authorship model as A1 (RACI, CMS permissions, governance)
- The harmonisation step requires faculty buy-in before centralisation — two rounds of change management
- Standardising templates and removing duplication before migration is more work upfront but produces a cleaner result

**Decision criteria for choosing A2:**
- You want the benefits of a single namespace but recognise that 200 pages of duplication shouldn't be migrated
- You're willing to invest in a two-phase process (harmonise, then centralise) — the upfront work pays off in a cleaner students.unimelb.edu.au
- The standardisation work of Phase 1 is independently valuable regardless of whether Phase 2 proceeds

### Variant A3: Harmonised central site with CDP Personalisation

First, harmonise faculty CS content (same as A2 Step 1). Then, instead of migrating pages to students.unimelb.edu.au, use **Optimizely and Tealium CDP** to personalise students.unimelb.edu.au experience based on known student attributes. If the university knows a student's faculty and program (via SSO or Tealium audience segments), students.unimelb.edu.au dynamically surfaces the right faculty-specific content alongside central services — without moving any pages.

| Dimension | Detail |
|-----------|--------|
| **Step 1 — Harmonisation** | Same as A2: all 9 faculties adopt the standardised CS template and remove central-duplicative pages. ~200 pages removed. |
| **Step 2 — CDP Personalisation** | Deploy Optimizely for experience targeting and Tealium CDP for audience segmentation. When a student logs in or self-identifies their faculty, students.unimelb.edu.au personalises: course planning links point to their faculty's course plans, career links surface their faculty's mentoring program, placement info shows their discipline's WIL options. |
| **Technical model** | students.unimelb.edu.au remains the entry point. Tealium CDP holds student-faculty mappings and audience segments. Optimizely serves personalised content widgets (faculty-specific links, contacts, news) within students.unimelb.edu.au's existing pages. Content stays on faculty sites — students.unimelb.edu.au links intelligently. |
| **Pages created on students.unimelb.edu.au** | ~20-30 (personalisation widgets, faculty content connectors, audience logic) |
| **Pages removed from faculties** | ~200 (duplicative pages removed in Step 1) |
| **Pages moved** | 0 — faculty-unique content stays on faculty sites |
| **Timeline** | 12-18 months (harmonisation first, then CDP integration + Optimizely configuration) |
| **Central team burden** | Medium — ~14 students.unimelb.edu.au gateway pages + CDP/Optimizely configuration. Faculties maintain their own content. |

**What this fixes:**
- Students get a personalised single entry point without content migration
- Duplication is eliminated (Step 1 harmonisation)
- students.unimelb.edu.au feels like it knows the student — "You're in the Bachelor of Science. Here are your course guides. Here's your faculty's career mentor program. Here's where to book lab time."
- Faculties retain full ownership of their discipline-specific content
- No API federation needed — CDP + Optimizely handle the personalisation layer

**What this requires:**
- Optimizely and Tealium CDP already in use or procured at UoM
- Student-faculty mappings available in the CDP (via SSO attributes or SIS data feed)
- Optimizely configured for students.unimelb.edu.au's pages (audience-based widget visibility)
- Content governance to keep faculty links current in the CDP-driven widgets
- A personalisation strategy: what surfaces for whom, and what the fallback experience is for unknown/anonymous visitors

**Decision criteria for choosing A3:**
- Optimizely and Tealium CDP are already in the university's martech stack (or procurement is planned)
- You want a modern, personalised student experience without forcing content migration
- Faculty autonomy is a hard constraint — no unique content can move
- You're willing to invest in CDP/personalisation configuration as an ongoing capability
- The 12-18 month timeline is acceptable

### Option A summary: when to choose full centralisation

| Variant | Choose if... |
|---------|-------------|
| **A1: Full Consolidation** | Single namespace is the overriding priority; you'll invest in distributed authorship governance |
| **A2: Harmonise-then-centralise** | You want a clean students.unimelb.edu.au but recognise duplication must be killed first; same distributed authorship as A1 |
| **A3: CDP Personalisation** | Optimizely + Tealium are in your stack; you want personalisation without content migration |

---

## Option B: Federated Standards (Status Quo + Governance)

Keep the current model — faculties run their own CS sections — but enforce standards through governance.

| Dimension | Detail |
|-----------|--------|
| **What changes** | URL conventions, template standards, "where to go" cross-linking, broken link fixes |
| **What stays** | Faculty CS sections remain on faculty domains. students.unimelb.edu.au remains as-is. Content ownership unchanged. |
| **Pages created** | ~10-15 (students.unimelb.edu.au gateway pages for course planning, placements, faculty programs) |
| **Pages removed** | ~200 (duplicative pages on faculty sites — replaced with students.unimelb.edu.au links) |
| **Pages moved** | 0 |
| **Timeline** | 3-6 months |
| **Central team burden** | Low — governance and audit, not content maintenance |

**What this fixes:**
- URL inconsistency (all faculties move to `/students`)
- No "where to go" guidance (standardised sidebar added to every faculty CS page)
- Broken links (all identified issues fixed)
- Career silos (mandatory cross-linking between students.unimelb.edu.au and faculty careers)

**What this doesn't fix:**
- Students still navigate 9+ different CS sections — they just have better signposting
- Duplication persists — the same service is still explained on multiple sites, just with links to the canonical version
- The central team has no enforcement power over faculty web officers — governance is advisory unless backed by an executive mandate

**What makes this option succeed:**
- An executive mandate that all faculty CS pages must follow the standardised template
- Quarterly cross-linking audits with consequences for non-compliance
- A designated central owner with authority to enforce URL conventions and content standards

**What makes this option fail:**
- Governance without teeth — if faculties can ignore the standards, nothing changes
- The template is treated as a suggestion rather than a requirement
- No one is accountable for the cross-linking audits

**Decision criteria for choosing B:**
- You want the fastest possible improvement with minimal disruption
- Faculty autonomy is politically non-negotiable
- You believe better signposting solves 80% of the student navigation problem
- You're willing to accept that duplication won't be eliminated, only signposted

---

## Option C: Central-and-spoke with Clear Boundaries (RECOMMENDED)

students.unimelb.edu.au becomes the definitive source for all transactional and cross-cutting services. Faculties retain genuinely discipline-specific content but adopt a standardised template. Content is split by service type, not by organizational unit.

| Dimension | Detail |
|-----------|--------|
| **students.unimelb.edu.au owns** | Enrolment, fees, exams, graduation, special consideration, leave of absence, key dates, health & wellbeing, careers platform, student life framework, IT, international support, study overseas |
| **Faculty owns** | Course plans, placements/WIL, forms, discipline-specific academic skills, program regulatory requirements, faculty scholarships, faculty clubs/events/newsletters, faculty contacts |
| **Both share** | Course planning (students.unimelb.edu.au: general + My Course Planner; faculty: degree-specific plans), careers (students.unimelb.edu.au: platform + tools; faculty: discipline mentoring + pathways), academic skills (students.unimelb.edu.au: PASS + general; faculty: discipline-specific) |
| **Pages created on students.unimelb.edu.au** | ~14 (course planning gateway, placements gateway, careers-faculty bridge, 9 faculty landing pages, academic skills by discipline, "where to go" tool) |
| **Pages removed from faculties** | ~120–180 (the thin duplicative layer — pure link-farm pages + faculty restatements of enrolment, fees, exams, graduation, health, key dates, general career advice) |
| **Pages retained on faculties** | ~950+ (the measured unique, discipline-specific estate — course plans, placements/WIL, forms, faculty life, discipline skills, program requirements) |
| **Pages moved** | 0 — content is removed or retained, not migrated |
| **Timeline** | 12 months in 3 phases (quick wins → content consolidation → template standardisation) |
| **Central team burden** | Medium — ~14 new students.unimelb.edu.au pages + quarterly audits. Faculty content owners maintain their own pages. |

**What this fixes:**
- Single source of truth per service — no more "which page is the right one?"
- Students navigate students.unimelb.edu.au for transactional needs, faculty for discipline-specific needs — with explicit signposting
- Careers cross-linking breaks the silos
- URL conventions are standardised
- Duplication is removed at the source (pages deleted, not just linked past)

**What this doesn't fix:**
- Students still visit two domains (students.unimelb.edu.au + faculty) for different needs — but now they know which is which
- Requires faculty content owners to delete pages and maintain their remaining content to standard
- The boundary between "general career advice" and "discipline-specific mentoring" needs judgment calls per faculty

**Decision criteria for choosing C:**
- You want to eliminate duplication without centralizing everything
- You recognise that placements, course plans, and program requirements genuinely cannot be centralized
- You're willing to invest in governance to maintain the boundaries over time
- You want measurable improvement within 12 months

**Why this option is recommended:**

1. **It matches the evidence.** The full crawl shows ~85% of faculty pages (≈997) are genuinely unique, discipline-specific content; the duplicative layer is thin (the ~50 pure link-farm pages plus faculty restatements of students.unimelb.edu.au transactional content — on the order of 120–180 pages). Consolidating that thin layer is high-impact and low-risk; the ~950+ unique pages must stay with faculties. The measured split makes full centralisation untenable and central-and-spoke the only fit.

2. **It's realistic.** Full centralisation (Option A) requires either migrating 600 pages of faculty content to a central team that can't maintain it (A1/A2), or building a federated personalisation platform across 3+ CMS platforms (A3). Central-and-spoke works with the existing infrastructure.

3. **It preserves what works.** The four fully-crawled faculties (Law, FEIT, Arts, Science) have invested years in building genuinely useful faculty-specific content. Option C preserves this investment while removing the duplication that confuses students.

4. **It has a clear migration path.** Three phases over 12 months: quick wins first (URLs, sidebars, broken links), then content consolidation, then template standardisation. Each phase delivers independent value.

---

## Option D: Status Quo + Minimal Fixes

Fix the most egregious problems without any structural change.

| Dimension | Detail |
|-----------|--------|
| **What changes** | Fix broken links. Add "where to go" sidebar to a few faculty pages. Standardise URL conventions with redirects. |
| **What stays** | Everything else. No content removed. No templates enforced. No governance. |
| **Pages created** | 0-5 |
| **Pages removed** | 0 |
| **Timeline** | 1-2 months |
| **Central team burden** | Very low — one-off fixes |

**What this fixes:**
- Broken links (FEIT 17, Arts 3, FBE 404, MDHS circular)
- URL inconsistency (redirects added)
- A few faculties get "where to go" sidebars (voluntary adoption)

**What this doesn't fix:**
- Duplication — all 9 faculties still run parallel career services, course planning, wellbeing pages
- Students still don't know which system handles what (except on the few pages that adopt the sidebar)
- No structural change to the fragmented experience
- The audit's core findings remain unaddressed

**Decision criteria for choosing D:**
- You need to show some action in the next 1-2 months
- You lack the political capital for a structural change
- You're using this as a first step before committing to a larger option

---

## Decision Matrix

| Dimension | A1: Full Consolidation | A2: Harmonise-Centralise | A3: CDP Personalisation | B: Federated Standards | C: Central-and-spoke | D: Minimal Fixes |
|-----------|:--:|:--:|:--:|:--:|:--:|:--:|
| **Duplication eliminated?** | Partial (moved, not killed) | Yes | Yes (Step 1 harmonisation) | No (signposted, not killed) | Yes (duplicative pages deleted) | No |
| **Single entry point?** | Yes | Yes | Yes (personalised) | No | Partial (students.unimelb.edu.au for transactions) | No |
| **Faculty authorship retained?** | Yes (distributed authorship on students.unimelb.edu.au) | Yes (distributed authorship on students.unimelb.edu.au) | Yes (content stays on faculty sites) | Yes | Partial (discipline content stays on faculty sites) | Yes |
| **Central team burden** | Medium (platform + governance) | Medium (platform + governance) | Medium (CDP/Optimizely config) | Low | Medium | Very Low |
| **Timeline** | 6-12 mo | 12-18 mo | 12-18 mo | 3-6 mo | 12 mo | 1-2 mo |
| **Technical complexity** | Low | Low | Medium (CDP integration) | Low | Low | Very Low |
| **Governance required** | High (RACI + distributed authorship) | High (RACI + distributed authorship) | High | High | Medium | Minimal |
| **Risk of faculty non-compliance** | Medium (distributed authorship needs enforcement) | Medium (distributed authorship needs enforcement) | Low (content stays; standards enforced in Step 1) | High (voluntary standards) | Medium (template mandate) | N/A |
| **Student experience improvement** | High | High | High (personalised) | Medium | High | Low |
| **Ongoing sustainability** | Medium (governance-dependent) | Medium (governance-dependent) | Medium (CDP/Optimizely maintenance) | Medium (audit-dependent) | High (clear boundaries) | Low (problems return) |

---

## 4a. Recommended Model in Detail: Central-and-spoke

### The model

```
┌─────────────────────────────────────────────────────┐
│           students.unimelb.edu.au (students.unimelb.edu.au)              │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌────────┐ │
│  │Course    │ │Support & │ │Student   │ │Careers │ │
│  │Admin     │ │Wellbeing │ │Life      │ │        │ │
│  └──────────┘ └──────────┘ └──────────┘ └────────┘ │
│                                                     │
│  NEW: Faculty landing pages (1 per faculty)         │
│  NEW: Placements gateway                            │
│  NEW: Course planning gateway                       │
│  NEW: Faculty career programs gateway               │
└─────────────────────────────────────────────────────┘
         ↑                    ↑
         │ "For X, go to students.unimelb.edu.au" │ "For Y, see your faculty"
         │                    │
┌────────┴────────────────────┴───────────────────────┐
│           Faculty CS pages (standardised)            │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌────────┐ │
│  │Course    │ │Placements│ │Faculty   │ │Forms   │ │
│  │Plans     │ │& WIL     │ │Life      │ │        │ │
│  └──────────┘ └──────────┘ └──────────┘ └────────┘ │
│                                                     │
│  REMOVED: enrolment, fees, exams, graduation,       │
│  special consideration, key dates, health, careers  │
│  (→ redirect to students.unimelb.edu.au with "For X, go to..." notice)  │
└─────────────────────────────────────────────────────┘
```

### Service boundaries

| Service | Owner | Rationale |
|---------|-------|-----------|
| Enrolment, re-enrolment, course withdrawal | **students.unimelb.edu.au only** | Single source of truth |
| Fees, census dates | **students.unimelb.edu.au only** | University-wide |
| Exams, results, academic progress | **students.unimelb.edu.au only** | University-wide |
| Graduation | **students.unimelb.edu.au only** | University-wide |
| Special consideration | **students.unimelb.edu.au only** | University-wide process |
| Leave of absence | **students.unimelb.edu.au only** | University-wide process |
| Key dates | **students.unimelb.edu.au only** | students.unimelb.edu.au is definitive |
| Timetable (MyTimetable) | **students.unimelb.edu.au** + faculty context | students.unimelb.edu.au: tool. Faculty: timetable quirks |
| Course planning | **students.unimelb.edu.au (general) + Faculty (specific)** | students.unimelb.edu.au: My Course Planner + advice. Faculty: sample plans, degree guides |
| Health & wellbeing | **students.unimelb.edu.au only** | CAPS, medical, SEDS — central services |
| Academic skills | **students.unimelb.edu.au (general) + Faculty (discipline)** | students.unimelb.edu.au: PASS. Faculty: legal writing, lab skills |
| Careers & employability | **students.unimelb.edu.au (platform) + Faculty (pathways)** | students.unimelb.edu.au: tools + jobs. Faculty: mentoring + industry |
| Placements & WIL | **Faculty only** | Cannot be centralized — fundamentally different per discipline |
| Scholarships | **students.unimelb.edu.au (search) + Faculty (awards)** | students.unimelb.edu.au: search engine. Faculty: prizes |
| Student life & clubs | **students.unimelb.edu.au (framework) + Faculty (local)** | students.unimelb.edu.au: UMSU/GSA/Melbourne Plus. Faculty: local events |
| Forms | **Faculty only** | Operational — each discipline's forms are different |
| IT & systems | **students.unimelb.edu.au only** | University-wide |
| International support | **students.unimelb.edu.au only** | Visas, OSHC — university-wide |
| Study overseas | **students.unimelb.edu.au only** | Central exchange program |
| Indigenous students | **students.unimelb.edu.au (Murrup Barak) + Faculty (local)** | students.unimelb.edu.au is primary |

---

## 4c. Other Fixes Regardless of Option Chosen

These five fixes should be implemented regardless of which option is selected:

1. **Standardise the URL convention.** All faculty CS sections at `faculty.unimelb.edu.au/students`. Redirect `/current-students`, `/study/current-students`, `/study/student-resources`, `/study/current-student-information`.

2. **Add "Where do I go for X?" component.** Every faculty CS page must include a standardised sidebar mapping common needs to the correct system. This alone would substantially reduce student confusion and is the single highest-impact quick win.

3. **Consolidate school-level CS sections.** Biomedical Sciences, Dental School, and MBS CS sections must either redirect to their faculty CS page or follow the same template and URL convention as the faculty. No separate CS ecosystems at the school level.

4. **Fix broken links.** FEIT (17 broken/duplicate URLs), Arts (3 broken pages), FBE (`/current-students` → 404), and MDHS (circular school resource links) — fix regardless.

5. **Cross-link careers content.** Every faculty careers page must prominently link to the central Careers students.unimelb.edu.au, and students.unimelb.edu.au must link to every faculty's career programs. The current complete separation is the clearest failure in the ecosystem.

---

## 4d. Key-Topic Treatment

### Course Planning
- **students.unimelb.edu.au:** Add `/your-course/faculty-course-planning` — a single page linking to every faculty's sample plans and degree guides. Retain My Course Planner and general advice.
- **Faculty:** Retain sample course plans, degree guides, major selection advice. Standardise: each faculty produces a Course Planning page with subsections per degree program.
- **Remove:** General "how to plan your course" advice on faculty pages — redirect to students.unimelb.edu.au.

### Careers & Employability
- **students.unimelb.edu.au:** Becomes the primary careers platform (Careers Online, Smart Resume, Career Checklist, general workshops). Add `/careers/faculty-career-programs` linking to every faculty's discipline-specific programs.
- **Faculty:** Retain discipline-specific mentoring, industry connections, career pathway pages. **Must** embed or prominently link to students.unimelb.edu.au careers tools.
- **MBS Career Elevation:** Integrate with (not compete with) the central Careers students.unimelb.edu.au. At minimum, cross-link.

### Placements & WIL
- **students.unimelb.edu.au:** Create `/your-course/placements-and-wil` — a landing page explaining WIL and linking to each faculty's placement program. students.unimelb.edu.au currently has zero placement content.
- **Faculty:** Retain full ownership of placement management. Standardise structure: Overview → Eligibility → How to Apply → Contacts.

### Student Life & Wellbeing
- **students.unimelb.edu.au:** Retain primary ownership of health, counselling, SEDS, food, transport, clubs (via UMSU/GSA).
- **Faculty:** Retain faculty-specific events, newsletters, clubs. Faculty wellbeing pages should redirect to students.unimelb.edu.au, with faculty-specific contacts only (e.g., "FEIT wellbeing officer: [contact]").

---

## 4g. New Pages Required on students.unimelb.edu.au

| New page | Content | Priority |
|----------|---------|----------|
| `/your-course/faculty-course-planning` | Links to every faculty's course plans/sample plans/degree guides | High |
| `/your-course/placements-and-wil` | What WIL is, link to each faculty's placement program | High |
| `/careers/faculty-career-programs` | Links to each faculty's career mentoring, industry programs, internship infrastructure | High |
| 9× Faculty landing pages | `/your-faculty/<slug>` — one per faculty: contacts, link to CS page, key dates, course planning link, placement link | Medium |
| `/student-support/academic-skills-by-discipline` | Links to each faculty's discipline-specific academic skills resources | Medium |
| "Where do I go for..." tool | Maps common student needs to the correct system | Medium |

**Total: ~14 new pages on students.unimelb.edu.au.** All are thin gateway/landing pages. No heavy content migration.

---

## 4h. Faculty Site Updates

### Standardised CS template

Every faculty CS page should adopt this structure:

```
1. KEY CONTACTS
   - Stop 1 link (always present)
   - Faculty student centre contact

2. COURSE PLANNING (faculty-owned)
   - Sample course plans by degree
   - Degree guides / subject selection advice
   - Link to My Course Planner (students.unimelb.edu.au)

3. PLACEMENTS & WIL (faculty-owned)
   - Placement programs
   - Eligibility & how to apply
   - Contacts

4. FACULTY LIFE (faculty-owned)
   - Clubs & societies
   - Events & newsletters
   - Mentoring programs
   - Ambassador/leadership opportunities

5. FORMS (faculty-owned)
   - Faculty-specific forms

6. WHERE TO GO FOR EVERYTHING ELSE (standardised sidebar)
   - Enrolment → students.unimelb.edu.au/your-course
   - Fees → students.unimelb.edu.au/your-course/fees
   - Exams & results → students.unimelb.edu.au/your-course/exams
   - Health & wellbeing → students.unimelb.edu.au/student-support
   - Careers → students.unimelb.edu.au/careers
   - IT help → studentit.unimelb.edu.au
   - Study overseas → students.unimelb.edu.au/your-course/study-overseas
```

### Content to remove from faculty sites

| Remove | Redirect to |
|--------|-------------|
| Enrolment how-to pages | `students.unimelb.edu.au/your-course` |
| Special consideration explanation | `students.unimelb.edu.au/your-course/exams/special-consideration` |
| Leave of absence explanation | `students.unimelb.edu.au/your-course/leave-of-absence` |
| Fees explanation | `students.unimelb.edu.au/your-course/fees` |
| Graduation information | `students.unimelb.edu.au/your-course/graduation` |
| Key dates | `students.unimelb.edu.au/your-course/key-dates` |
| Health & counselling info | `students.unimelb.edu.au/student-support` |
| General career advice (not faculty-specific) | `students.unimelb.edu.au/careers` |

### Content to keep on faculty sites

| Keep | Because |
|------|---------|
| Sample course plans | Degree-specific — cannot be centralized |
| Placement/practicum management | Discipline-specific — clinical ≠ teaching ≠ legal |
| Faculty-specific forms | Operational requirement — each discipline's forms are different |
| Faculty scholarships & prizes | Faculty-funded and faculty-administered |
| Faculty clubs, events, newsletters | Local community — cannot be centralized |
| Discipline-specific academic skills | Legal writing ≠ lab skills ≠ studio practice |
| Program regulatory requirements | LANTITE, Fitness to Practice — legally required |
| Faculty contacts | Students need to know who to email |

---

## 4i. Design Principles & Governance

### Design principles

1. **Students should never have to know which system handles what.** students.unimelb.edu.au is always the first stop.

2. **One source of truth per service.** No service explained on both a faculty page and students.unimelb.edu.au.

3. **Consistent URL conventions.** `faculty.unimelb.edu.au/students` for every faculty. No exceptions.

4. **Standard navigation labels.** "Current students" — not "Students" / "Student resources" / "Current student information" / "Study".

5. **Faculty pages link out; students.unimelb.edu.au pages link down.** Faculty → students.unimelb.edu.au for transactional. students.unimelb.edu.au → faculty for discipline-specific.

6. **"Where to go" is always explicit.** Every page states where to go for related needs.

### Governance model

| Role | Who | Responsibility |
|------|-----|----------------|
| students.unimelb.edu.au content owner | Central web team / Student Services | All students.unimelb.edu.au pages. Faculty landing pages. Cross-faculty gateway pages. |
| Faculty content owner | Faculty web officer / student centre | Faculty CS pages — course plans, placements, forms, faculty life. |
| Template enforcement | Central web team | All faculty CS pages use standardised template. Annual audit. |
| Cross-linking audit | Central web team (quarterly) | Verify students.unimelb.edu.au↔faculty links. Fix broken links. |
| URL convention enforcement | Central web team | Redirect old patterns. Annual broken-link scan. |
| Content review cycle | Faculty content owners (6-monthly) | Course plans, placement info, contacts are current. |

### Migration phases

**Phase 1 — Quick Wins (3 months)**
- Standardise URL conventions with redirects
- Add "Where to go for everything else" sidebar to all faculty CS pages
- Fix all broken links discovered in this audit
- Cross-link students.unimelb.edu.au careers ↔ faculty careers
- *Decision gate: confirm which option (A/B/C/D) before Phase 2*

**Phase 2 — Content Consolidation (6 months)**
- Remove duplicative content from faculty sites (enrolment, fees, exams, graduation, health, key dates)
- Replace with students.unimelb.edu.au links
- Build students.unimelb.edu.au placements gateway page
- Build students.unimelb.edu.au course planning gateway page
- Build students.unimelb.edu.au careers-faculty bridge page

**Phase 3 — Template Standardisation (12 months)**
- Migrate all faculty CS pages to standardised template
- Consolidate school-level CS sections (Biomedical Sciences, Dental, MBS)
- Build students.unimelb.edu.au faculty landing pages
- Annual governance cycle begins

---

## Evidence Base

| Evidence | Source |
|----------|--------|
| 1,173 crawled pages across 12 units — 85% unique (Law 195, FEIT 204, ABP 250, MDHS 112, Science 94, Arts 91, MBS 61, Education 47, Biomedical 42, FFAM 37, FBE 36, Dental 4) | `crawl/pages/*.json` |
| Full faculty-domain crawl (9 domains, 2,363 pages) — current-students = 7.2% sign-posted; no shared faculty IA | `crawl/full-faculty/*.json`, `analysis/full-faculty-context.md`, `data/clean/full_faculty_stats.py` |
| 9 faculty summaries + students.unimelb.edu.au IA | `crawl/pages/*-summary.md`, `hub-summary.md` |
| Unit registry (43 units) | `data/unit-registry.csv` |
| Cross-faculty service model matrix | `analysis/service-model-matrix.md` |
| **Structural findings report (27 findings)** | `analysis/structural-findings.md` |
| Measurement cleanup & count corrections (cleaned dataset) | `analysis/data-and-synthesis-issues.md`, `data/clean/` |
| 11 unit profiles | `analysis/unit-*.md` |
| 20 topic deep-dives | `analysis/topic-deepdives/` |
| Cross-site overlap (study.unimelb, alumni) | `analysis/cross-site-overlap.md` |
| Structured data (inventory, IA, classification) | `data/url-inventory.csv`, `data/pages-by-topic.csv`, `data/clean/` |

Every recommendation above can be traced to specific pages and links in the crawl corpus.
