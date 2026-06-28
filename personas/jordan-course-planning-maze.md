# Jordan — Course planning maze

> *"I've got the Course Planner open in one tab, the Handbook in another, a faculty sample plan PDF in a third, and the FAQ article about prerequisites in a fourth. Four tabs to answer one question: which subjects do I enrol in this semester?"*

## Bio
Jordan is a second-year Bachelor of Science student trying to plan their major sequence. They need to: check prerequisites for third-year subjects, ensure they meet the 50-points-at-each-level rule, timetable around lab sessions, and confirm their study load keeps them on track for the course duration. This single task — "what should I enrol in?" — sends Jordan across the hub's two parallel guidance trees, My Course Planner on StudyOS, the Handbook on a different platform, a legacy FAQ where the actual rules live, and the my.unimelb enrolment screen where the action happens. 343 hub pages exist for course planning and enrolment — 41% of the hub's total footprint — and it's the most fragmented single task in the entire estate.

## Journey pain points

| Pain point | Crawl evidence | Severity |
|---|---|---|
| **Seven-system obstacle course** | Hub guidance (2 trees) + My Course Planner (StudyOS) + Handbook + ask.unimelb + my.unimelb + MyTimetable + *.app forms | HIGH |
| **Two parallel guidance trees compete** | `/course-admin` (212 pages) vs legacy `/your-course` (101 pages); 19 core leaves byte-near duplicates | HIGH |
| **Two planning tools, no delineation** | StudyOS My Course Planner vs my.unimelb /sone/STUDYPLN — referenced on ~830 pages but resolved to two different tools | HIGH |
| **Every answer is a FAQ hop away** | 396 links to ask.unimelb across two URL formats; the hub describes, the FAQ answers | HIGH |
| **Census dates page is broken** | Canonicalises to `/page-not-found` — the highest-stakes operational page in the estate | HIGH |
| **Handbook switch mid-plan** | 195 links to handbook.unimelb — different platform, different visual standard, different navigation | MEDIUM |
| **Enrolment variations scattered** | 161 links to forms.your + *.app microsites for overload, leave, withdrawal — no single "change my enrolment" hub | MEDIUM |
| **Timetabling is yet another subdomain + login** | MyTimetable on mytimetable.students.unimelb — separate system behind its own authentication | MEDIUM |
| **Faculties re-host planning content** | 71 faculty course-planning pages parallel the central guidance — 46% on school subdomains beneath faculties | MEDIUM |

## Top frustrations
1. **No single source of truth.** The hub, the Handbook, the FAQ, and the faculty sample plan each claim to own part of the answer.
2. **The guidance describes but doesn't transact.** Every page tells Jordan *about* enrolment; none of them let Jordan *do* enrolment — that's behind a my.unimelb login.
3. **The two parallel trees create confusion.** Jordan lands on `/your-course/census-dates` from a faculty link but the real page is at `/course-admin/census-dates` — and the canonical tag points to a 404.
4. **Timetabling requires yet another login.** After planning subjects and enrolling, Jordan must go to a completely separate system (MyTimetable) to register for classes.

## The toolchain Jordan must traverse
| System | Role | Links from hub |
|---|---|---|
| Hub guidance (2 trees) | How-to advice — split across `/course-admin` + `/your-course` | 313 pages |
| My Course Planner 🔒 | Subject planning tool — on a separate subdomain | ~54 links · on ~830 pages |
| The Handbook | Course/subject structure, prerequisites, points | 195 links |
| ask.unimelb FAQ | The actual answers (study load, census, HECS, prerequisites) | 396 links |
| my.unimelb 🔒 | The enrolment ACTION — enrol, study plan, vary | 187 links |
| MyTimetable 🔒 | Class registration — another subdomain, another login | on 84 pages |
| Variation forms 🔒 | Overload, leave, withdrawal — each a different form/host | 161 links |

## Systems traversed
~7: students.unimelb (2 trees) → studyos.students.unimelb → handbook.unimelb → ask.unimelb → my.unimelb (auth) → mytimetable.students.unimelb → forms.your / *.app

## Linked improvements from the register
| # | Improvement | Severity · Effort |
|---|---|---|
| 1 | Finish the stalled hub migration & collapse parallel URL trees | HIGH · medium |
| 3 | Mandate a thin standardised student overlay on Squiz | HIGH · medium |
| 4 | Fix the `?a=` query-string artifact manufacturing ~3,359 phantom 404s | HIGH · quick-win |
| 5 | Guarantee 301s for MSD's ~8,000 deep-links into legacy hub paths | HIGH · quick-win |

## Related deep-dives
- `analysis/course-planning-enrolment.md` — full toolchain audit
- `analysis/lifecycle-journeys.md` — Domestic undergraduate + enrolment moment traces
- `report/Course-Planning-Enrolment.html` — formatted report

---

*Built from: course-planning-enrolment.md deep-dive, lifecycle-journeys.md, improvements-register.md, and the full-scrape link graph (students-full crawl, cross-site-flow.csv). June 2026.*
