# Faculty of Business & Economics — Current Students crawl summary

- **Faculty:** fbe (Business & Economics)
- **Root:** https://fbe.unimelb.edu.au/students  (NOTE: `/current-students` 404s — CS root is `/students`)
- **Scope prefix (PRE):** /students
- **Pages captured:** 36
- **Max IA depth:** 4
- **Fetch errors:** 0 (2 auth-gated SSO pages short-circuited, not fetched)
- **HTTP/parse 404s:** 2 (both are SSO-gated redirects)
- **Crawled:** 2026-06-15 (in-page fetch-BFS via connected Chrome)

## Headline finding — small, shallow CS section; cohort-routing top layer + a genuinely deep PhD/BCom core

The FBE `/students` subtree is **small and shallow: 36 pages, max depth 4**. The expectation going in was a pure "link-directory to the central hub" — that is **only half right**. The pattern is two-layered:

1. **The top layer is a set of thin cohort-routing gateways.** The root (367w), the BCom landing (360w), the Graduate Research landing (300w) and the FBE services page (328w) are short orienting pages whose job is to *split students into cohorts and push them onward*. They clear the 160-word `unique` threshold (so the classifier scores 0 strict link-farms) but they are functionally navigational shells, not content.
2. **Underneath, the BCom-assessment and especially the PhD subtrees ARE substantive** — `Your Candidature` (2,469w), the PhD scholarships/stipends cluster, `BCom First Semester Guide` (2,086w), and BCom `Assessment` (1,039w) are real, self-hosted content. So FBE is **not** a content-free farm like a pure directory.

Outbound is still heavily University-central: `www.unimelb.edu.au` **240** links, `about.unimelb.edu.au` **136**, and the central student hub `students.unimelb.edu.au` **38** — i.e. the faculty leans on central services for transactional/policy content while keeping a thin but real layer of cohort-specific guidance. The two structurally important findings are the **subdomain split to Melbourne Business School** and the **SSO-gated student-life app** (both below).

### The cohort-split gateway pattern

The `/students` root routes to four distinct cohorts, two of which leave the FBE host entirely:

| Cohort | Destination | CS type |
|--------|-------------|---------|
| Bachelor of Commerce | `fbe.unimelb.edu.au/students/bcom` | FBE sub-path (the bulk of in-scope content) |
| Graduate Research (PhD/MPhil) | `fbe.unimelb.edu.au/students/phd` | FBE sub-path |
| Melbourne Business School (graduate coursework) | `mbs.unimelb.edu.au/students` | **Separate subdomain — out of scope** |
| Wellbeing / services | `fbe.unimelb.edu.au/students/wellbeing`, `/services` | Shared FBE pages |

MBS graduate students navigate a **completely separate CS subdomain** (mbs.unimelb.edu.au/students, with its own career service at mbs.unimelb.edu.au/career) — a significant fragmentation vector under one faculty.

## Breakdown by classification

- **unique:** 31
- **link-farm:** 0
- **mixed:** 3
- **redirect:** 2

## Breakdown by topic tag

- research-candidature: 8
- course-planning: 8
- IT-systems: 8
- scholarships: 5
- student-life: 3
- wellbeing-health: 2
- orientation: 2
- academic-skills: 2
- exams-results: 2
- subjects-timetable: 2
- graduation: 2
- fees-finance: 2
- careers-employability: 2
- contacts-support: 1
- forms-admin: 1

## Depth distribution

- depth 0: 1 pages
- depth 1: 4 pages
- depth 2: 10 pages
- depth 3: 14 pages
- depth 4: 7 pages

## Top outbound destinations (where it sends students)

Other unimelb / external hosts linked from the /students subtree, by total link count:

- `www.unimelb.edu.au`: 240
- `about.unimelb.edu.au`: 136
- `fbe.unimelb.edu.au`: 98
- `www.facebook.com`: 68
- `www.instagram.com`: 68
- `www.linkedin.com`: 68
- `students.unimelb.edu.au`: 38
- `safety.unimelb.edu.au`: 34
- `handbook.unimelb.edu.au`: 28
- `gradresearch.unimelb.edu.au`: 23
- `scholarships.unimelb.edu.au`: 10
- `library.unimelb.edu.au`: 8
- `services.unimelb.edu.au`: 7  ⚠ auth-gated
- `findanexpert.unimelb.edu.au`: 6
- `ask.unimelb.edu.au`: 6
- `study.unimelb.edu.au`: 4
- `policy.unimelb.edu.au`: 4
- `studentit.unimelb.edu.au`: 3  ⚠ auth-gated
- `umsu.unimelb.edu.au`: 3
- `eng.unimelb.edu.au`: 3
- `mbs.unimelb.edu.au`: 2
- `www.beyondblue.org.au`: 2
- `canvas.lms.unimelb.edu.au`: 2  ⚠ auth-gated
- `gateway.research.unimelb.edu.au`: 2
- `tes.app.unimelb.edu.au`: 2

## Auth-gated / login hosts seen (recorded as outbound only, not crawled)

- `services.unimelb.edu.au`: 7 links
- `studentit.unimelb.edu.au`: 3 links
- `canvas.lms.unimelb.edu.au`: 2 links
- `sso.unimelb.edu.au`: 2 links
- `lms.unimelb.edu.au`: 1 links

Additionally, **2 in-scope BCom pages 302-redirect to `sso.unimelb.edu.au` (SAML SSO) → `studentlifeapp` (a Salesforce-backed authenticated student-life app)** and could not be fetched cross-origin. Recorded as `redirect`/auth-gated, outbound-only:

- `/students/bcom/first-semester-guide/week-1/connect-with-your-peer-mentor`
- `/students/bcom/first-semester-guide/week-2-3/fbe-engagement-planner`

## Notable unique pages (richest substantive content)

- **Your Candidature** (2469w, d2, research-candidature) — `/students/phd/your-candidature`
- **BCom First Semester Guide** (2086w, d3, student-life) — `/students/bcom/first-semester-guide`
- **Research training and development scholarships** (1383w, d3, research-candidature/scholarships) — `/students/phd/scholarships-and-grants/research-training-and-development`
- **Assessment** (1039w, d3, exams-results) — `/students/bcom/current-students/assessment`
- **Graduate researcher prizes and awards** (873w, d3, research-candidature/scholarships/graduation) — `/students/phd/scholarships-and-grants/prizes-and-awards`
- **Wellbeing** (850w, d1, wellbeing-health) — `/students/wellbeing`
- **Exam Viewing FAQ** (735w, d4, exams-results) — `/students/bcom/current-students/assessment/exam-viewing-faq`
- **FBE Doctoral Program Stipend and Tuition (Fee Remission) Scholarships** (732w, d4, research-candidature/scholarships/fees-finance) — `/students/phd/scholarships-and-grants/stipends-and-fee-remissions/fbe-doctoral-program-stipend-and-tuition-fee-remission-scholarships`
- **Honours Entry & Application** (664w, d3, course-planning/forms-admin) — `/students/bcom/honours/entry-requirements-and-how-to-apply`
- **Stipends and fee remissions** (642w, d3, scholarships/fees-finance/research-candidature) — `/students/phd/scholarships-and-grants/stipends-and-fee-remissions`
- **Dean's Honours List 2024** (627w, d3, graduation/course-planning) — `/students/bcom/current-students/deans-honours-list-2020`
- **Studies in Engineering** (614w, d3, course-planning) — `/students/bcom/current-students/studies-in-engineering`
- **Resources and Support** (607w, d2, contacts-support/research-candidature) — `/students/phd/resources-and-support`
- **Orientation** (576w, d2, orientation) — `/students/bcom/orientation`
- **Student Computing Spaces** (553w, d4, IT-systems) — `/students/bcom/current-students/services/computing-spaces`

## Section IA tree (in-scope URLs)

```
/students
  bcom
    current-students
      academic-success
      assessment
        exam-viewing-faq
      compulsory-quantitative-requirement
      deans-honours-list-2020
      intensives
      services
        computing-spaces
        rules
        virtual-lab
      studies-in-engineering
    first-semester-guide
      week-1
        connect-with-your-peer-mentor
      week-2-3
        fbe-engagement-planner
    honours
      convenors
      entry-requirements-and-how-to-apply
      what-is-honours
    orientation
  phd
    resources-and-support
    scholarships-and-grants
      prizes-and-awards
      research-training-and-development
      stipends-and-fee-remissions
        fbe-doctoral-program-stipend-and-tuition-fee-remission-scholarships
    your-candidature
  services
    computing-spaces
    rules
    virtual-lab
  wellbeing
    ambassadors
```