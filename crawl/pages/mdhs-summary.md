# MDHS — Current Students crawl summary

- **Faculty:** Medicine, Dentistry & Health Sciences (MDHS)
- **Root:** https://mdhs.unimelb.edu.au/study/current-students
- **Scope (PRE):** `/study/current-students` on host `mdhs.unimelb.edu.au`
- **Crawl mode:** Live-browser navigate + in-page extractor BFS (Cloudflare blocked same-origin fetch; navigation passes the challenge)
- **Crawled:** 2026-06-15
- **Pages captured:** 112 (depth 0–6; 250-page cap NOT hit, depth-6 cap reached on 1 page)

## Counts

**By classification:**
- unique: 104
- mixed: 4
- link-farm: 1
- redirect/broken: 3

**Depth distribution:** d0=1, d1=4, d2=16, d3=26, d4=37, d5=27, d6=1

**By topic tag (pages carrying each tag):**
- placements-WIL: 96
- wellbeing-health: 44
- forms-admin: 36
- contacts-support: 35
- student-life: 25
- orientation: 14
- careers-employability: 13
- graduation: 11
- exams-results: 10
- inclusion-equity: 8
- clubs-events: 7
- subjects-timetable: 7
- international: 7
- scholarships: 6
- IT-systems: 4
- course-planning: 4
- research-candidature: 2
- academic-skills: 1
- enrolment: 1

## Key structural finding — placements-dominated faculty CS

Unlike the thin-hub picture from the Phase-1 probe, the MDHS *faculty* CS subtree is **substantial and almost entirely about Work-Integrated Learning / clinical placements**. The faculty root is a thin hub (4 cards), but `/placements` expands into a deep, content-rich operational system:

- **Pre-placement compliance** (`/placements/students/requirements`) is a full sub-site: immunisation pages (hepatitis B, influenza, MMR, pertussis, TB, varicella), non-immunisation checks (police AU/OS, WWCC, NDIS worker screening, mask-fit testing), and course-specific checks (AHPRA, COVID-19, first-aid/CPR, hand hygiene). Most are 400–1400 words of genuinely MDHS-specific, non-centralisable prose.
- **Per-department placement provider guides** (`/placements/org/<dept>`) each follow a before → day-one → during → conclusion lifecycle, for: MSPGH, MSPS (with clinical-psychology / clinical-neuropsychology / professional-psychology sub-streams), Melbourne Medical School, Melbourne Dental School, Clinical Audiology, Nursing, Optometry & Vision Sciences, Physiotherapy, Social Work, and Speech Pathology (DSP).
- **Student enrichment** (`/student-enrichment`) is the secondary cluster: MDHS Student Hub, Indigenous Student Success, Chat-Fest, clubs & societies, mentoring (Chancellor's Scholars profile pages), student leadership / Student Advisory Council, research-pathways advising.
- **Student Fitness to Practice** is a small but genuinely faculty-specific compliance/conduct cluster (examples of concerns, MDHS process, FAQs, links & resources).
- **Employability in MDHS** is a single substantive (~915w) hub page.

This is a faculty whose CS content **cannot be centralised** — it is clinical-placement regulatory content tied to AHPRA/health-sector requirements and per-discipline provider relationships.

## School fragmentation note

MDHS school-level CS sections live on **separate subdomains** (crawled separately / out of scope here). Outbound links from the faculty subtree to those school CS hosts:

- `medicine.unimelb.edu.au` — 3 link(s)
- `dental.unimelb.edu.au` — 1 link(s)
- `biomedicalsciences.unimelb.edu.au` — 1 link(s)

Note: within the in-scope faculty subtree, `mspgh`, `melbourne-medical-school`, `melbourne-dental-school` etc. ALSO appear as **path segments** under `/placements/org/` (e.g. `/placements/org/mspgh/before-placement`). Those are faculty-hosted placement-provider guides, NOT the school subdomains — they were crawled in-scope. The school *subdomains* (biomedicalsciences/dental/mspgh `.unimelb.edu.au`) remain separate and were only recorded as outbound.

## IA tree (in-scope, normalized paths)

```
/study/current-students
  /study/current-students/employability-in-mdhs
  /study/current-students/placements
    /study/current-students/placements/org
      /study/current-students/placements/org/DDS3 Year Level Coordinator
      /study/current-students/placements/org/clinicalaudiology
        /study/current-students/placements/org/clinicalaudiology/additional-questions
        /study/current-students/placements/org/clinicalaudiology/before
          /study/current-students/placements/org/clinicalaudiology/before/remote-placements-for-students
            /study/current-students/placements/org/clinicalaudiology/before/remote-placements-for-students/introduction
        /study/current-students/placements/org/clinicalaudiology/conclusion-of-placement
        /study/current-students/placements/org/clinicalaudiology/during-placement
        /study/current-students/placements/org/clinicalaudiology/eoi
        /study/current-students/placements/org/clinicalaudiology/frequently-asked-questions
      /study/current-students/placements/org/department-of-nursing
        /study/current-students/placements/org/department-of-nursing/before-placement
        /study/current-students/placements/org/department-of-nursing/conclusion-of-placement
        /study/current-students/placements/org/department-of-nursing/during-placement
      /study/current-students/placements/org/department-of-optometry-and-vision-sciences
      /study/current-students/placements/org/department-of-physiotherapy-resources
      /study/current-students/placements/org/department-of-social-work-resources
        /study/current-students/placements/org/department-of-social-work-resources/before-placement
        /study/current-students/placements/org/department-of-social-work-resources/conclusion-of-placement
        /study/current-students/placements/org/department-of-social-work-resources/during-placement
      /study/current-students/placements/org/dsp
        /study/current-students/placements/org/dsp/before-placement
        /study/current-students/placements/org/dsp/conclusion-of-placement
        /study/current-students/placements/org/dsp/day-one-of-placement
        /study/current-students/placements/org/dsp/during-placement
      /study/current-students/placements/org/melbourne-dental-school
        /study/current-students/placements/org/melbourne-dental-school/DDS3 Year Level Coordinator
        /study/current-students/placements/org/melbourne-dental-school/before-placement
        /study/current-students/placements/org/melbourne-dental-school/conclusion-of-placement
        /study/current-students/placements/org/melbourne-dental-school/during-placement
      /study/current-students/placements/org/melbourne-medical-school
      /study/current-students/placements/org/mspgh
        /study/current-students/placements/org/mspgh/before-placement
        /study/current-students/placements/org/mspgh/conclusion-of-placement
        /study/current-students/placements/org/mspgh/day-one-of-placement
        /study/current-students/placements/org/mspgh/during-placement
      /study/current-students/placements/org/msps
        /study/current-students/placements/org/msps/clinical-neuropsychology
          /study/current-students/placements/org/msps/clinical-neuropsychology/before-placement
          /study/current-students/placements/org/msps/clinical-neuropsychology/conclusion-of-placement
          /study/current-students/placements/org/msps/clinical-neuropsychology/during-placement
        /study/current-students/placements/org/msps/clinical-psychology
          /study/current-students/placements/org/msps/clinical-psychology/before-placement
          /study/current-students/placements/org/msps/clinical-psychology/conclusion-of-placement
          /study/current-students/placements/org/msps/clinical-psychology/during-placement
        /study/current-students/placements/org/msps/professional-psychology
          /study/current-students/placements/org/msps/professional-psychology/before-placement
          /study/current-students/placements/org/msps/professional-psychology/conclusion-of-placement
          /study/current-students/placements/org/msps/professional-psychology/during-placement
    /study/current-students/placements/prospective-orgs
      /study/current-students/placements/prospective-orgs/how-is-the-placement-arranged
      /study/current-students/placements/prospective-orgs/what-happens-after-the-placement
      /study/current-students/placements/prospective-orgs/why-should-your-ogranisation-place-student
    /study/current-students/placements/student-testimonials
    /study/current-students/placements/students
      /study/current-students/placements/students/feedback,-reporting-concerns-and-complains
      /study/current-students/placements/students/getting-help
      /study/current-students/placements/students/info
      /study/current-students/placements/students/insurance
      /study/current-students/placements/students/key-contacts
      /study/current-students/placements/students/obligations,-rights-and-responsibilities
      /study/current-students/placements/students/overseas-placements
      /study/current-students/placements/students/personal-information-and-intellectual-property
      /study/current-students/placements/students/requirements
        /study/current-students/placements/students/requirements/additional-info
          /study/current-students/placements/students/requirements/additional-info/additional-information-and-resources
        /study/current-students/placements/students/requirements/checklist
        /study/current-students/placements/students/requirements/course-specific-checks
          /study/current-students/placements/students/requirements/course-specific-checks/additional
          /study/current-students/placements/students/requirements/course-specific-checks/ahpra
          /study/current-students/placements/students/requirements/course-specific-checks/covid-19
          /study/current-students/placements/students/requirements/course-specific-checks/first-aid-and-cpr
          /study/current-students/placements/students/requirements/course-specific-checks/hand-hygiene
        /study/current-students/placements/students/requirements/handbook
          /study/current-students/placements/students/requirements/infection/flu
          /study/current-students/placements/students/requirements/infection/hepatitis-b
          /study/current-students/placements/students/requirements/infection/measles,-mumps-and-rubella-mmr
          /study/current-students/placements/students/requirements/infection/pertussis
          /study/current-students/placements/students/requirements/infection/tb
          /study/current-students/placements/students/requirements/infection/varicella
        /study/current-students/placements/students/requirements/non-immunisation-checks
          /study/current-students/placements/students/requirements/non-immunisation-checks/mask-fit-testing
          /study/current-students/placements/students/requirements/non-immunisation-checks/ndis-worker-screening-check
          /study/current-students/placements/students/requirements/non-immunisation-checks/police-au
          /study/current-students/placements/students/requirements/non-immunisation-checks/police-os
          /study/current-students/placements/students/requirements/non-immunisation-checks/wwcc
        /study/current-students/placements/students/requirements/sonia
      /study/current-students/placements/students/travel
      /study/current-students/placements/students/visas
  /study/current-students/student-enrichment
    /study/current-students/student-enrichment/chat-fest
    /study/current-students/student-enrichment/clubs-and-societies
    /study/current-students/student-enrichment/indigenous-student-success
    /study/current-students/student-enrichment/mdhs-student-hub
    /study/current-students/student-enrichment/mentoring-programs
      /study/current-students/student-enrichment/mentoring-programs/chancellors-scholars
        /study/current-students/student-enrichment/mentoring-programs/chancellors-scholars/emily-sun
        /study/current-students/student-enrichment/mentoring-programs/chancellors-scholars/garry-zhu
        /study/current-students/student-enrichment/mentoring-programs/chancellors-scholars/zahra-ataie
        /study/current-students/student-enrichment/older-site-versions/Student-Advisory-Council/student-support
    /study/current-students/student-enrichment/research-pathways-advising
    /study/current-students/student-enrichment/student-leadership
      /study/current-students/student-enrichment/student-leadership/Student-Advisory-Council
  /study/current-students/student-fitness-to-practice
    /study/current-students/student-fitness-to-practice/examples-of-concerns
    /study/current-students/student-fitness-to-practice/frequently-asked-questions
    /study/current-students/student-fitness-to-practice/links-and-resources
    /study/current-students/student-fitness-to-practice/mdhs-process
```

## Notable unique / substantive pages

- `~/placements/students/requirements/course-specific-checks/ahpra` — AHPRA Registration (1382w, unique; placements-WIL, wellbeing-health, forms-admin, course-planning)
- `~/placements/org/msps/clinical-neuropsychology/during-placement` — During placement (1166w, unique; placements-WIL)
- `~/placements/students/requirements/non-immunisation-checks/mask-fit-testing` — Mask Fit Testing (967w, unique; contacts-support, wellbeing-health, placements-WIL, forms-admin)
- `~/employability-in-mdhs` — Employability in MDHS (925w, mixed; careers-employability, placements-WIL, subjects-timetable, exams-results)
- `~/placements/org/clinicalaudiology/frequently-asked-questions` — Frequently asked questions (903w, unique; placements-WIL)
- `~/placements/students/travel` — Travel (900w, unique; placements-WIL, international, wellbeing-health)
- `~/placements/org/melbourne-dental-school/during-placement` — During placement (864w, unique; placements-WIL, forms-admin)
- `~/placements/students/requirements` — MDHS Pre-Placement Requirements (753w, unique; placements-WIL, wellbeing-health, forms-admin, contacts-support)
- `~/placements/students/requirements/non-immunisation-checks/wwcc` — Working with Children Check (740w, unique; placements-WIL, forms-admin, wellbeing-health, exams-results)
- `~/placements/student-testimonials` — Student Testimonials (735w, unique; placements-WIL, student-life)
- `~/placements/students/requirements/non-immunisation-checks/police-au` — Australian Police Check (731w, unique; placements-WIL, forms-admin, wellbeing-health)
- `~/placements/org/department-of-nursing/during-placement` — During placement (668w, unique; placements-WIL, graduation)
- `~/placements/org/melbourne-dental-school/before-placement` — Before placement (662w, unique; placements-WIL, contacts-support, orientation)
- `~/placements/students/requirements/sonia` — Sonia (645w, unique; placements-WIL, forms-admin)
- `~/placements/students/requirements/additional-info/additional-information-and-resources` — Additional Information and Resources (624w, unique; placements-WIL, forms-admin, wellbeing-health)
- `~/student-enrichment/student-leadership` — Student Leadership (605w, unique; careers-employability, student-life, contacts-support, wellbeing-health)
- `~/placements/students/getting-help` — Getting help (593w, mixed; placements-WIL, contacts-support, wellbeing-health)
- `~/placements/students/obligations,-rights-and-responsibilities` — Obligations, Rights & Responsibilities (578w, unique; placements-WIL)

## Top outbound destinations (host → link count, aggregated)

- `www.unimelb.edu.au` — 892 [central hub]
- `about.unimelb.edu.au` — 481 [central hub]
- `www.facebook.com` — 258
- `www.instagram.com` — 256
- `www.linkedin.com` — 222
- `safety.unimelb.edu.au` — 114
- `www.youtube.com` — 111
- `students.unimelb.edu.au` — 70 [central hub]
- `study.unimelb.edu.au` — 47 [central hub]
- `research.unimelb.edu.au` — 28
- `library.unimelb.edu.au` — 28
- `staff.unimelb.edu.au` — 28
- `unimelb.sonialive.com` — 23
- `q.surveys.unimelb.edu.au` — 15
- `forms.your.unimelb.edu.au` — 12
- `immunisationhandbook.health.gov.au` — 12
- `policy.unimelb.edu.au` — 11
- `www.ahpra.gov.au` — 11

## Auth-gated / outbound-only hosts

- `services.unimelb.edu.au` — 8 link(s) (recorded as outbound only; not crawled)
- `my.unimelb.edu.au` — 6 link(s) (recorded as outbound only; not crawled)
- `canvas.lms.unimelb.edu.au` — 2 link(s) (recorded as outbound only; not crawled)

## Broken / redirect pages

- `~/placements/org/DDS3 Year Level Coordinator` — Page not found (404 / Page not found)
- `~/placements/org/melbourne-dental-school/DDS3 Year Level Coordinator` — Page not found (404 / Page not found)
- `~/student-enrichment/older-site-versions/Student-Advisory-Council/student-support` — Student support (empty redirect (wc=0))

## Method notes

- **Cloudflare:** `mdhs.unimelb.edu.au` challenges programmatic same-origin `fetch()` (returns 403 'Just a moment…'), so the proven in-page fetch-BFS failed here. Fell back to **live-browser `navigate` + in-page DOM extractor**, POSTing each full record to a localhost receiver on port 8115 (MCP truncates tool output ~1KB and redacts localStorage).
- **Dedup:** normalized by stripping query/hash/trailing slash; redirect aliases collapsed to canonical (e.g. `/Student-Advisory-Council` → `/student-enrichment/student-leadership/Student-Advisory-Council`).
- **Excluded as non-pages:** `.pdf` assets and mailto-mangled `…@unimelb.edu.au` links (the CMS absolutises some `mailto:` hrefs into in-path URLs).
