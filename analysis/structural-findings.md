# Current Students IA — Structural Findings & Fragmentation Audit

*Synthesized from crawl of 9 faculty CS sections + students.unimelb.edu.au. June 2026.*

> **About this report.** The fragmentation, duplication, gap, and governance problems a current student actually hits, each with a recommended fix. The estate is **1,153 current-students pages (843 substantive content)**. Topic counts are cleaned content counts — raw crawl counts were inflated 40–94% by archives, profiles, and over-broad tagging, so several findings cite the *pattern* (every faculty runs its own) rather than a page tally. Findings 1–20 come from the structural crawl; findings 21–27 are cross-source insights (from triangulating the crawl, the student-journey research, the navigation structure, and the full-faculty-domain crawl together).

---

## Finding 1: Four URL conventions for the same thing

The single concept "information for current students" is served at four different URL patterns:

| Pattern | Faculties using it |
|---------|-------------------|
| `/students` | Law, Arts, FEIT, Science, FBE |
| `/current-students` | ABP/MSD, FFAM |
| `/study/current-students` | Education, MDHS |
| `/study/student-resources` | Dental School |
| `/study/current-student-information` | Biomedical Sciences School |

**Impact:** No discoverability by convention. A student cannot guess the URL of their faculty's CS section.

---

## Finding 2: The fragmentation spectrum

Faculties fall on a spectrum from "central-dependent link directory" to "self-contained parallel ecosystem":

```
Central-dependent ←————————————————————————————→ Self-contained
     ABP    FBE   Education  Arts  Science  MDHS   Law   FFAM   FEIT
```

- **ABP, FBE:** CS root is mostly a link directory. Most content delegates to students.unimelb.edu.au.
- **Education:** Unique program content + heavy central-redirect for transactions. Good balance.
- **Arts, Science:** Well-structured local central sites with real faculty content + moderate students.unimelb.edu.au links.
- **FEIT, Law:** Almost entirely self-contained. Run parallel systems for course planning, careers, scholarships, forms, academic skills. Minimal students.unimelb.edu.au links.
- **FFAM:** Completely self-contained. Conservatorium/art-school model doesn't fit students.unimelb.edu.au taxonomy.

---

## Finding 3: The school-level fragmentation problem

MDHS has the worst fragmentation — 3+ schools run their own CS sections on separate subdomains:

| Unit | CS URL | Status |
|------|--------|--------|
| MDHS Faculty | mdhs.unimelb.edu.au/study/current-students | Thin central landing (4 cards) |
| Biomedical Sciences | biomedicalsciences.unimelb.edu.au/study/current-student-information | Full CS section |
| Dental School | dental.unimelb.edu.au/study/student-resources | Has CS section |
| MSPGH | mspgh.unimelb.edu.au | Likely has CS section |
| Medical School | Links to faculty central page | No separate CS |
| Psych Sciences | Links to faculty central page | No separate CS |

FBE has a similar split: FBE /students (BCom, PhD) + MBS /students (graduate programs) on mbs.unimelb.edu.au.

**No other faculty has school-level CS sections.** Arts schools, Science schools, FEIT schools, FFAM units — all route through the faculty CS page.

---

## Finding 4: Careers & employability is the most duplicated service

Every single faculty (8/9) and MBS run their own career content in parallel with the central Careers service:

| Faculty/School | Career content observed |
|---------------|----------------------|
| Law | MLS Career Services (career pathways, steps to practising law, career consultations) |
| FEIT | Internship program (3 pages, ~14K words), Career Mentoring, Industry Series |
| Arts | Career Mentoring, Employability in Arts, Experiential Learning, Internship subjects |
| Science | Employability in Science, Career Enrichment Program, Internship subjects |
| ABP/MSD | ABP Industry Mentoring, Internships & Vocational Placements |
| FBE/MBS | MBS Career Elevation (mbs.unimelb.edu.au/career), BCom Career Launchpad |
| Education | Professional Experience (teaching placements) |
| MDHS | Student Employability Opportunities |
| students.unimelb.edu.au | Careers section: Employability, Career Checklist, Careers Online, Smart Resume |

students.unimelb.edu.au careers content and faculty career content **do not cross-link**. A student who uses students.unimelb.edu.au career checklist may never discover their faculty's mentoring program, and vice versa.

---

## Finding 5: Course planning duplication is real but partially legitimate

Every faculty provides course plans / sample course plans / course guides. students.unimelb.edu.au has My Course Planner + general planning advice.

**Legitimate (faculty must own):**
- Degree-specific sample course plans (MSD's 10 masters course plans, Law JD/MLM plans)
- Program-specific requirements (LANTITE, Fitness to Practice, learning area requirements)
- Subject selection guidance for specific majors (Science first-year subject sets)

**Duplicative (students.unimelb.edu.au should own):**
- General "how to plan your course" advice (FEIT duplicates what students.unimelb.edu.au says)
- Course planning tool links (My Course Planner linked from multiple faculties)
- Leave of absence, course withdrawal info (students.unimelb.edu.au has definitive pages)

---

## Finding 6: Broken and circular links

- **Arts has 3 broken pages** (academic mentoring profiles, WIL internships page)
- **Biomedical Sciences "Bachelor of Science" link** points circularly back to the same page
- **MDHS "Medical School" and "Psychological Sciences" school resource links** both point back to the same thin faculty central page

---

## Finding 7: students.unimelb.edu.au's gaps

students.unimelb.edu.au covers transactional admin (enrolment, fees, exams, graduation, key dates, timetable) and general support (health, counselling, Stop 1, careers, student life) comprehensively. But it has **no content** for:

1. **Course plans / degree-specific planning** — every faculty does this, students.unimelb.edu.au has My Course Planner tool but no degree guides
2. **Placements & WIL** — completely absent from students.unimelb.edu.au. Students must find placement info on faculty sites.
3. **Discipline-specific academic skills** — students.unimelb.edu.au has general PASS/academic skills; doesn't cover legal writing, lab reports, studio practice
4. **Faculty-specific forms** — no students.unimelb.edu.au equivalent
5. **Professional recognition / accreditation pathways** — Law's "Steps to Practising Law," Education's LANTITE/teacher registration

---

## Finding 8: No consistent "what's where" guidance

No faculty CS page tells students "for X, go to students.unimelb.edu.au; for Y, stay here." The result:
- Students must learn through trial and error which system handles which need
- Faculty pages often re-explain students.unimelb.edu.au services (e.g., ABP's enrolment section re-explains special consideration, leave of absence, overloading — all of which are definitively covered on students.unimelb.edu.au)
- No page exists that maps "I need to do X → go to Y"

---

## Finding 9: CMS/platform inconsistency

- **Law, Arts, FEIT, Science** appear to use the same UoM Squiz Matrix CMS with consistent global header/footer
- **FFAM** uses a different template (no sidebar navigation on the CS root — just cards/grid)
- **MDHS** uses a card-based landing page pattern
- **FBE** and **MBS** use different visual treatments from each other despite being under the same faculty
- **Biomedical Sciences** has its own distinct template

---

## Finding 10: Root cause for the gateway-page duplication pattern

Every faculty runs its own gateway page for services students.unimelb.edu.au already provides (Careers, Academic Skills, Wellbeing, Scholarships, Student Life). Five interlocking causes drive this:

**1. No content ownership governance.** No published policy states "Careers content is centrally-owned; faculties link, never restate." Without a rule, faculties apply their own judgment — and their judgment is "our students need to find this on our site." Absence of a content ownership framework is the deepest structural cause.

**2. The IA template drives completeness.** Faculty CS sections inherit a template IA with headings like "Support," "Careers," and "Wellbeing." Those headings don't say "link to students.unimelb.edu.au" — they say "fill in content." The template was designed around the full set of student needs rather than just faculty-specific ones. The template is the mechanism that manufactures duplicates.

**3. Accountability sits at the faculty level; authority to set content policy doesn't.** Faculty web managers are answerable to their dean for student satisfaction with information. If a student can't find careers support and complains, that complaint goes to the faculty — not to the central Careers service. Faculties have an accountability incentive to ensure every service is findable on their own site. students.unimelb.edu.au has no lever over faculty publishing decisions.

**4. students.unimelb.edu.au's content is sometimes genuinely too generic.** students.unimelb.edu.au's Employability page covers Careers Online and Smart Resume. The Faculty of Science's Employability in Science page covers the Science Career Enrichment Program, industry-specific pathways, and employer partnerships. The faculty page is more useful for a Science student. Gateway pages often started as legitimate "here's what students.unimelb.edu.au doesn't cover for us" pages and expanded to restating students.unimelb.edu.au content over time. The seed is legitimate; the overgrowth is the problem.

**5. Removal requires deliberate effort; addition is automatic.** A faculty adds an Academic Skills page in 2015 when students.unimelb.edu.au's offering is thin. students.unimelb.edu.au builds out its academic skills section in 2018. The faculty page persists because someone is listed as owner, it appears in their sitemap, and retiring it requires a decision-maker willing to own the consequence. Addition takes one person; retirement takes coordination. The estate accumulates.

**Structural diagnosis:** The University built a students.unimelb.edu.au alongside faculty sites rather than replacing them. students.unimelb.edu.au was designed as "the authoritative source" but was never operationalised as "the exclusive source." By the time students.unimelb.edu.au was comprehensive, every faculty had already built parallel infrastructure with no mechanism to wind it back.

---

## Finding 11: Research candidature — students.unimelb.edu.au vacuum, not students.unimelb.edu.au duplication

The service-model matrix shows research candidature as `—` (students.unimelb.edu.au) + `F` (faculty-owned) across every faculty. This is structurally different from careers or academic skills, where students.unimelb.edu.au has real content that faculties duplicate. For HDR, students.unimelb.edu.au never built the lifecycle content. Arts, FEIT, and FBE each built their own candidature spine (confirmation milestones, progress reviews, thesis submission) independently, with no model to converge on. The duplication is horizontal (three faculties did the same thing) rather than vertical (faculty copied students.unimelb.edu.au).

Three additional HDR-specific patterns:
- **HDR students sit in an IA no-man's land.** students.unimelb.edu.au is built around coursework. HDR students use different systems (Ethics, Research Gateway, milestone reporting), but no faculty CS section has a coherent HDR sub-section — candidature content is scattered across research, forms, course-planning, and academic-skills topics depending on which faculty tagged what.
- **Graduate research funding is the most genuinely fragmented area.** APA/MRS (central), faculty-specific stipends (Arts, Science, FEIT), discipline-specific grants, and `scholarships.unimelb.edu.au` all hold parts of the HDR funding picture. No single page in the estate gives an HDR student a complete view of what they can apply for.
- **The entry-to-candidature handoff is broken.** `study.unimelb.edu.au` has a single research-candidature page (entry info only). From there, the hop to actual faculty candidature information requires navigating from a prospective site to a faculty CS section with no students.unimelb.edu.au gateway in between.

---

## Finding 12: Every faculty independently reinvented its forms index

212 pages are tagged forms-admin. Every faculty built its own version with a different label and location:

| Faculty | Label / location |
|---------|-----------------|
| Law | "Student forms" under JD and Masters separately |
| FEIT | Forms scattered across placement, scholarship, and internship pages |
| Arts | "Student forms and resources" |
| MDHS | 36 near-identical per-checklist compliance pages across school subdomains |
| Science | Forms embedded in topic sections (no consolidated students.unimelb.edu.au) |

No consistent label exists across the estate.

students.unimelb.edu.au has no forms index. Students who don't know which form they need — and which site holds it — have no discovery path.

---

## Finding 13: Indigenous student experience is the most fragmented welfare area

No students.unimelb.edu.au coordination exists for Indigenous student support. Content is fragmented across:
- A general students.unimelb.edu.au mention (thin)
- Science's faculty-specific Indigenous student section (most substantial)
- ABP's Ngargee program (standalone)
- FEIT and Arts surface-level mentions

No faculty links to another faculty's Indigenous student offering. There is no cross-faculty "here's what the University offers Indigenous students" gateway anywhere in the estate. This is the welfare area with the highest cost of fragmentation for the students it affects.

---

## Finding 14 — "Employability in X" is the most templated gateway duplication in the estate

Seven faculties each publish a structurally identical "Employability in [Faculty Name]" landing page: Law, Arts, Science, FEIT, MDHS, FFAM, Education. The content shape is so consistent — an introduction to the faculty's careers culture, three to four service callout boxes, links to the central Careers platform — that it reads as a CMS template that was provisioned once and instantiated eight times. The legitimate content underneath (credit-bearing internship subjects, accreditation-pathway programs, regulated clinical career requirements) is a small subset of what's there and is genuinely faculty-owned. The landing pages themselves are not.

This is the clearest signal in the audit that the central Careers team and faculty web teams are not aligned on ownership boundaries. Each faculty believes it needs its own "front door" to Careers; none of them has agreed with the others on what content goes inside it.

**Recommendation:** Replace eight parallel landing pages with one students.unimelb.edu.au gateway (`students.unimelb.edu.au/careers/by-discipline`) that links to faculty-specific content where it genuinely exists (accreditation paths, credit-bearing subjects, named programs). The "Employability in X" wrapper pages can be decommissioned once students.unimelb.edu.au gateway is live.

---

## Finding 15 — Special consideration is the purest single-policy duplication in the estate

Twenty-five faculty pages across the estate describe the special consideration process. One central policy document (MPF1326) governs this process. students.unimelb.edu.au already holds the canonical procedure at `students.unimelb.edu.au/student-support/special-consideration`. There is no legitimate faculty-specific content in this topic beyond minor local-extension provisions (some faculties grant short extensions at their own discretion) — but those variants are not documented on the pages that exist; the pages simply restate students.unimelb.edu.au procedure in different words.

Special consideration is the clearest case in the audit where faculty content exists not because the faculty owns any of the underlying policy, but because no one removed the locally-authored page after students.unimelb.edu.au built the canonical one. Version drift is the real risk: when MPF1326 changes, 25 pages need to be updated simultaneously, and they won't be.

**Recommendation:** Decommission all faculty special-consideration pages and replace with a single inbound redirect to students.unimelb.edu.au canonical URL. The faculty pages add no information that students.unimelb.edu.au doesn't already cover more accurately.

---

## Finding 16 — The "reverse funnel": enrolled students are directed back to the prospective site

529 outbound links from current-student faculty pages point to `study.unimelb.edu.au` — a site framed for prospective students asking "should I come here?" Enrolled students follow these links because the content they need as current students (course information, degree requirement detail, program structures, Graduate Degree Package pathways) exists only on the prospective site and has no enrolled-student equivalent.

The most acute instance is the Graduate Degree Package (GDP): 14+ substantive pages on study.unimelb, averaging 2,000–4,700 words each, describing how enrolled students activate guaranteed pathway progression from bachelor's to master's degrees. These pages are framed at prospective students but are clearly being used — and linked from — enrolled-student contexts. An enrolled Year 2 student trying to activate their GDP pathway has nowhere to go in the enrolled estate.

The Glossary (6,294 words, 44 links to students.unimelb) and the Moving Guide (pre-arrival guide for international students — highest-stakes for the post-offer cohort) are further examples of enrolled-student utility content parked on the prospective site with no enrolled-student mirror.

**Recommendation:** Build enrolled-student mirrors for GDP pathway pages and the Moving Guide at minimum. These are not duplication targets — they are missing content. The enrolled mirrors should be framed for students already in and trying to do something, not for prospective students deciding whether to apply.

---

## Finding 17 — The alumni handoff is structurally absent at the web level

Zero links from any page in the current-students estate — students.unimelb.edu.au or faculty — point to `alumni.unimelb.edu.au`. The lifecycle progression (current student → graduate → alumnus) that the University communicates organisationally has no corresponding web pathway. The alumni site is invisible from the enrolled-student experience.

The costs are concrete:
- The **graduate benefits package** (library access post-graduation, alumni email, sports centre eligibility, career tools, language learning, journal access) is not disclosed to graduating students anywhere in the enrolled estate.
- The **"Welcome new alumni" page** (1,745 words) is the natural first destination for a graduate, but it has zero inbound links from the enrolled estate and is discoverable only from within the alumni site itself.
- The **alumni mentoring pipeline** — alumni offering mentorship to current students — is completely disconnected from the faculty careers and employability pages that would benefit from it.

**Recommendation:** Add "what comes next" signposting at the graduation milestone in the enrolled estate — a single students.unimelb.edu.au page or section at `students.unimelb.edu.au/graduating` that introduces graduate benefits, links the welcome-new-alumni page, and surfaces the alumni mentoring connection. This is a missing link, not a duplication problem.

---

## Finding 18 — Scholarship infrastructure exists centrally but isn't surfaced from students.unimelb.edu.au

`scholarships.unimelb.edu.au` operates as a functional centralised awards system. Arts already links directly into it, and the broader university estate links to it 515 times. Study.unimelb has 75 scholarship pages; faculties collectively hold 141. But the enrolled-student site — `students.unimelb.edu.au` — has **zero** scholarship pages. An enrolled student who goes to students.unimelb.edu.au looking for scholarships finds nothing.

FEIT's response to this students.unimelb.edu.au gap was to build a 71-page shadow scholarship sub-site from scratch: one page per application round, per-year Dean's Honours Lists (2022–2024), and per-year Community Awards galleries (2022–2025), served from two parallel URL trees. This is a faculty filling a students.unimelb.edu.au vacuum — the same root cause pattern as Finding 10.

**Recommendation:** Add a students.unimelb.edu.au scholarship gateway at `students.unimelb.edu.au/fees-scholarships/scholarships` that routes enrolled students to `scholarships.unimelb.edu.au` for the award catalogue. This single page would eliminate the primary motivation for faculty shadow scholarship sub-sites.

---

## Finding 19 — Annual content accretes without retirement, creating a structural maintenance liability

Three topics illustrate the same pattern: content is added on a cycle (per year, per award round, per cohort) with no corresponding retirement mechanism.

- **FEIT scholarships**: one page per application round, one page per year's Dean's Honours List (2022–2024), one gallery page per year's Community Awards (2022–2025). The estate grows by ~6–8 pages per year with no pages ever retired.
- **MSD studio archives**: one new "Past Studios" archive page per academic year since 2008 has produced 130+ pages of historical content in the live current-student estate.
- **Law GRD researcher profiles**: individual biography pages accumulate with no clear retirement trigger when a researcher leaves or completes their candidature.

An estate that only grows has no steady state, and it becomes increasingly expensive to audit, maintain, and navigate over time.

**Recommendation:** For annually-recurring content, establish an archive path outside the current-student estate (e.g. `/about/archives/`) with a redirect from the current-path URL. The current-student estate should expose only the current cycle; historical cycles should be accessible but not indexed in navigation.

---

## Finding 20 — Clubs, discipline community, and student identity content is the most legitimately faculty-owned category in the estate

In contrast to the duplication and fragmentation findings across most topics, clubs and discipline community content is a clear case where faculty ownership is structurally correct and centralisation would damage rather than improve the experience.

Named discipline societies (FEIT engineering clubs, MDHS student associations, Biomedical societies), conservatorium performance ensembles (FFAM Big Band, Symphonic Wind Ensemble, Chamber Music — each with audition mechanics and registration), flagship competitions (FEIT Hackathon Festival 2,177 words, Law Mooting circuit, Science Agriculture Discovery Week 2,235 words, MDHS Chat Fest), and graduate-researcher community events are discipline-bound by definition. students.unimelb.edu.au cannot meaningfully own the Hackathon Festival content because it requires knowledge of the discipline calendar, judging criteria, sponsor relationships, and participant community that only FEIT has.

The narrow consolidation target within this topic is the generic administrative layer: room-booking procedures, club-funding claims, event-promotion processes, and committee governance guidance. This administrative layer currently exists in both students.unimelb.edu.au (partially) and FEIT (fully, 5,000+ words). That is the duplication to resolve — not the named, discipline-specific content.

**Recommendation:** Do not attempt to centralise named club or competition content. Audit the generic administrative layer (room booking, funding, committee governance) and confirm whether students.unimelb.edu.au or FEIT holds the canonical version, then redirect from the duplicate. Leave all discipline-specific content in place.

**Connect, don't centralise — discovery is the real gap.** Faculty club and discipline-community content is owned in the right place, but it is currently invisible from students.unimelb.edu.au. The student-life section of students.unimelb.edu.au should carry a "find your community" directory that **links out** to each faculty's clubs, societies, and ensembles — centralising *discovery* while leaving *ownership* with the faculties. This is the same connect-not-consolidate pattern as the careers and alumni-mentoring recommendations.

---

## Finding 21 — There is no shared vocabulary across the estate

The same function is named differently everywhere, and different things share the same name — across three layers at once. "Orientation" is used as a page title on five different faculties; across the four faculty navigation menus, not one label is shared by all four; the careers function alone appears under five different names ("Employability in X", "Career Elevation", "Career Launchpad", and more). A student's learned vocabulary therefore doesn't transfer between faculties, and even a perfect site search returns a jumble of look-alike results. This sits underneath the URL-convention and "what's where" findings — it is the prerequisite none of them can be fixed without.

**Recommendation:** Agree one canonical label per function (one "Careers", one "Student forms", one "Orientation") and enforce it across page titles, navigation, and search facets — **before** any navigation redesign. Restructuring the menus first simply rebuilds the same confusion in a new shape.

---

## Finding 22 — The navigation is both too deep and too flat

Faculties have no shared rule for how deep or wide their navigation should be, and the failure runs in opposite directions at once. FEIT buries content up to ten levels deep; Law piles 66 items under a single top-level heading; one-off pages (a vaccination page, an equipment-loan page) sit at the top level beside major categories. Education and Arts sit in a sensible middle — so the spread is the absence of a standard, not a house style.

**Recommendation:** Add a depth-and-breadth rule to the standard faculty template — target two to three levels deep, cap the number of items in any one menu, and keep single-purpose pages out of the top level. Re-nest FEIT's deep branches and break up Law's overloaded top menu.

---

## Finding 23 — A good model already exists but was never issued as a standard

The University does not need to invent an information-architecture model; it needs to issue the one it already has. The Education and Arts sites already do the central-and-spoke pattern well — a lean set of top-level sections that link out to students.unimelb.edu.au for shared services. Today students.unimelb.edu.au exposes four top-level sections while faculties expose eight to seventeen, with no agreed target. The gap is purely that the working pattern was never mandated or distributed.

**Recommendation:** Turn the Education/Arts pattern into a published, mandated "standard faculty section" specification with an adoption deadline. This is a documentation-and-governance task, not a rebuild.

---

## Finding 24 — Careers is authored three times, in three voices

Careers content is written independently on the prospective site, the current-student estate, and the alumni site — each in a different register, with no editorial link between them. The alumni site even repeats the per-faculty fragmentation, with 13 near-identical faculty mentoring pages. A student moving through their degree and into graduate life meets three disconnected careers stories. This is the cross-lifecycle version of the careers-duplication finding.

**Recommendation:** Give careers content a single owner across the prospective, current-student, and alumni estates, with one shared structure and clear cross-links at each handoff.

---

## Finding 25 — Course planning depends on the Handbook but isn't designed around it

The Handbook is the single biggest external dependency in the estate — current-student pages link to it 3,380 times, far more than to any other site. Yet the planning experience is not built around it: students bounce between the central course planner, their faculty's sample plan, and the separately-built Handbook, and the journey research shows this step scoring poorly.

**Recommendation:** Integrate Handbook subject data directly into the course-planning step (inline, or via a clean embed) so a student can plan in one place instead of bouncing between three.

---

## Finding 26 — A few problems can't be fixed by editing a page

Some duplication lives in separate systems, not in content. MBS runs its own careers platform on a separate subdomain; placements run through a third-party system (SONIA). These won't be resolved by a content edit — they need a decision from the system's owner about whether to keep, merge, or retire the tool.

**Recommendation:** Inventory the genuinely separate tools and platforms and route each to its owner for a keep-or-migrate decision — distinct from the content-level fixes elsewhere in this report.

---

## Finding 27 — Current students are a minority tenant inside outward-facing faculty estates

Seen against the *whole* faculty domain (not just the current-students slice this report is built on), current-student content is a thin, often unsigned layer. A full-domain crawl of all 9 faculty marketing sites — 2,363 pages — finds only **7.2% (171 pages) explicitly sign-posted under a `/students/` path**; the rest is research, news, about, prospective `/study/`, and industry/engagement. By the site's own navigation a current student is a side-quest on a domain built for prospective students, media, industry, and donors.

Two structural consequences follow:
- **There is no shared faculty IA to standardise into.** The single biggest section differs in every faculty — eng is 76% a magazine (`/ingenium/`), FFAM is 86% `/about-us/`, education is led by a research centre (`/aerc/`), arts devolves to five named schools. The student-section inconsistency in Findings 1–3 is inherited from nine unrelated parent architectures.
- **Most "faculty student content" isn't a liftable estate.** Law and FEIT were tagged with ~195–204 student-relevant pages, but their domains explicitly section only 9 and 18 under `/students/`. The rest is general faculty content that happens to be student-relevant — entangled, not portable.

**Impact:** Strengthens the central-and-spoke direction rather than changing it. Full centralisation is *less* viable (nothing common to centralise into; student content is entangled with non-student content), and the case for a consistent student-facing overlay — URL convention, signposting, a standardised template — is sharper. A current student's tasks will always sit inside an outward-facing estate; the fix is to make that 7% layer findable and consistent, not to relocate it.

**Recommendation:** Treat the standardised CS template and URL convention as the primary levers — they are the only ones that touch all nine architectures without trying to unify the parent sites. Full evidence and per-faculty figures: [`full-faculty-context.md`](full-faculty-context.md).
