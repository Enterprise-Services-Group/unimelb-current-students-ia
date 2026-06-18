# Dental — Student Resources crawl summary

- **Unit:** Melbourne Dental School (MDS) — a *school* under the Faculty of Medicine, Dentistry & Health Sciences (MDHS)
- **Parent faculty:** MDHS
- **Root:** https://dental.unimelb.edu.au/study/student-resources
- **Scope prefix (PRE):** `/study/student-resources` (host `dental.unimelb.edu.au`)
- **Crawled:** 2026-06-15T06:05:13.016Z
- **Pages captured:** 4
- **Max depth reached:** 1 (cap 6)
- **Caps hit:** pages=False, depth=False
- **Fetch errors:** 0 — queue drained to 0 (exhaustive)
- **Technique:** in-page same-origin `fetch()` BFS over server-rendered HTML; `<script>/<style>/nav/footer` stripped before text extraction so word counts reflect real prose; corpus POSTed to a localhost receiver on port 8118 and written to disk.

> [!IMPORTANT] Fragmentation finding
> Melbourne Dental School runs its **own** current-students area — branded "Student Resources" — on its **own subdomain** `dental.unimelb.edu.au`, entirely separate from the MDHS faculty-level current-students section at `mdhs.unimelb.edu.au/study/current-students`. This documents **school-level fragmentation within a single faculty (MDHS)**: a student at this school must consult at least three different current-students surfaces (school 'Student Resources', MDHS faculty current-students, and the central `students.unimelb.edu.au` hub).

> [!NOTE] Why the subtree is tiny (and a nav quirk)
> The section is a thin, **outbound-routing shell**: it owns only 4 pages and pushes almost everything to central hubs, Formstack/MS-Forms form hosts, and the graduate-research portal. Its scope is narrow — essentially **research students' grants/awards/scholarships + an admin Forms catalogue** — rather than a full student-lifecycle resource set. NOTE: the section nav exposes "Research" and "Forms" as **same-page anchors** (href back to the root `#`), so a naïve link-following BFS finds only the root + one grants page. The real landing pages exist at **case-sensitive** paths `/study/student-resources/Research` and `/study/student-resources/Forms` (200), while `/research` and `/forms` 404. These were recovered by path-probing and seeded into the BFS.

## Breakdown by classification

- **unique:** 3
- **mixed:** 1

## Depth distribution

- depth 0: 1
- depth 1: 3

## Breakdown by topic tag

- **research-candidature:** 3
- **scholarships:** 3
- **forms-admin:** 3
- **fees-finance:** 3
- **contacts-support:** 2
- **enrolment:** 1

## Section IA tree (in-scope URLs)

```
/study/student-resources   (root — research grants/awards/scholarships overview)
├── Research                              (research-degrees + grants landing)
│   └── Research/mds-internal-grants      (MDS internal research grants — reimbursement/application forms)
└── Forms                                 (MDS admin forms catalogue — reimbursement, absence, financial)
```

*("Research" and "Forms" are real pages at case-sensitive paths; the nav presents them as in-page anchors.)*

## Top outbound destinations (host: total link count across all pages)

- `dental.unimelb.edu.au`: 39  ← school site (self)
- `www.unimelb.edu.au`: 28  ← central university site
- `about.unimelb.edu.au`: 16  ← central 'about' / governance
- `uomdental.formstack.com`: 8  ← ← Formstack — MDS-specific student forms host
- `www.facebook.com`: 8  (social (footer))
- `www.linkedin.com`: 8  (social (footer))
- `www.instagram.com`: 8  (social (footer))
- `forms.office.com`: 7  ← ← MS Forms — MDS form/application host
- `students.unimelb.edu.au`: 4  ← ← central student hub
- `www.youtube.com`: 4  (social (footer))
- `safety.unimelb.edu.au`: 4  ← central health & safety
- `futurestudents.unimelb.edu.au`: 2  ← central scholarships/admissions
- `gradresearch.unimelb.edu.au`: 2  ← central graduate research hub
- `staff.unimelb.edu.au`: 1  ← staff site

## Auth-gated hosts seen (recorded outbound-only, never crawled)

- **None.** This subtree links to no auth-gated hosts (`my.`, `lms.`, `canvas.lms.`, `studentit.`, `services.`) — it routes to public central hubs (`students.`, `futurestudents.`, `gradresearch.`) and external form hosts instead.

## Notable unique pages (substantive prose)

- **Student Resources | Melbourne Dental School** — `/study/student-resources (root)` (wc 1669, d0, mixed, tags: research-candidature, scholarships, forms-admin, contacts-support)
- **Forms** — `/Forms` (wc 1013, d1, unique, tags: forms-admin, fees-finance, enrolment, contacts-support)
- **Research** — `/Research` (wc 660, d1, unique, tags: research-candidature, scholarships, fees-finance)
- **Melbourne Dental School Internal Grants** — `/Research/mds-internal-grants` (wc 571, d1, unique, tags: scholarships, research-candidature, forms-admin, fees-finance)

## Broken / redirect pages

- none

## Notes on form-host fragmentation

- MDS routes student forms across **two distinct external/MS form platforms**: `uomdental.formstack.com` (8 refs) and `forms.office.com` (7 refs) — i.e. the school's own forms are not consolidated onto a single university system, compounding the school-vs-faculty-vs-central fragmentation.
