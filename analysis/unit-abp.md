# ABP / Melbourne School of Design — CS Profile

- **Unit:** Architecture, Building & Planning (MSD is the faculty site)
- **CS URL:** `msd.unimelb.edu.au/current-students` (pattern: `/current-students`)
- **Pages:** ~35-50 estimated (root + IA capture; Cloudflare blocked full BFS)
- **Crawl mode:** Root + section landing pages via web_extract

## IA Structure
```
/current-students
  /course-planning (sample course plans for 10 masters programs)
  /enrolment (mostly hub links; one unique: list-of-forms)
  /subject-information (studios, quota, travelling studios, internships, practical experience)
  /student-experience (maker spaces, access, IT, clubs, newsletters, mentoring, feedback)
```

## Service Model Position
**Hub-dependent link directory.** The CS root page serves primarily as a curated link list. All transactional tasks (enrolment, timetable, special consideration, leave, overloading, course withdrawal, exams) link to students.unimelb.edu.au. Genuine unique content is concentrated in course plans and subject information.

## Content Profile
- **Unique faculty content:** Sample course plans (10 MSD masters programs), MSD Studios (4 programs + archive), Travelling studios, Internships & vocational placements (SONIA platform, ABP-specific process), Maker Spaces (FabLab, Robotics, NExT Lab), ABP Industry Mentoring, Graduate Ambassador Program
- **Hub-redirect areas:** Enrolment, timetable, special consideration, leave of absence, advanced standing, overloading, course withdrawal, exams, cross-institutional study, study overseas, academic skills (→ services.unimelb), Indigenous students (→ Murrup Barak)
- **Well-structured 4-section IA** — one of the clearer CS layouts

## Structural Issues
- Enrolment section is almost entirely hub-redirect — re-explains hub services students could get directly from the source
- URL pattern `/current-students` differs from the `/students` convention (5/9 faculties use `/students`)

## Recommendation Notes
- **Keep:** Course plans, studios, travelling studios, internships, maker spaces, mentoring
- **Redirect to hub:** Enrolment section — replace with "Where to go" sidebar
- **Standardise URL:** Redirect `/current-students` → `/students`
- **Good structural model:** The 4-section layout (Course Planning, Subject Info, Student Experience, Enrolment) is a strong template for the standardised faculty CS page
