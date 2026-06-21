# Topic Deep-Dive: Subjects & Timetabling
*Cross-faculty analysis from the full crawl. June 2026.*

**319 subjects-timetable–tagged pages** make this the single largest content topic in the audit. But the volume is wildly skewed: one school (ABP/MSD) holds **64%** of it, almost entirely as design-studio subject pages and studio archives going back to 2008. Strip those out and the topic is small and split — a thin layer of genuinely transactional students.unimelb.edu.au content (MyTimetable, census dates, overloading) mis-attributed to faculties, plus legitimately discipline-specific subject catalogues (clinics, studios, internships, quota subjects). The duplication problem here is *archival bloat*, not cross-faculty redundancy.

## Distribution — who holds it

| Unit | Pages | What dominates |
|---|--:|---|
| Architecture, Building & Planning (MSD) | 204 | Design studios + travelling-studio archives (2008–2026) |
| Law | 30 | Daily-rebuilt subject listings, MLS clinic subjects, subject delivery |
| Education | 25 | Placement-bound subjects, extensions/assessment, timetabling |
| Arts | 21 | Experiential-learning/internship subjects + re-hosted students.unimelb.edu.au pages |
| Science | 15 | First-year subject sets, internship & research-project subjects, quota |
| MDHS | 7 | Placement subjects (during/conclusion of placement) |
| Engineering & IT (FEIT) | 6 | Internship subjects, MyTimetable/class-registration re-hosts |
| Fine Arts & Music | 6 | Timetable & room bookings, performance exam timetables |
| Business & Economics (FBE) | 2 | Intensives, Compulsory Quantitative Requirement |
| Biomedical Sciences (school · MDHS) | 2 | Quota subjects, first-year subject planning |
| Melbourne Business School (school · FBE) | 1 | Subject selection & advanced standing |
| **Total** | **319** | |

ABP/MSD alone is bigger than every other unit combined. The count is inflated by MSD treating each studio offering (and every past-year archive — "Semester 2 2017 Studio 24", "2014 Studio Archive") as a standalone subject page; this is one school's content-management habit, not a true measure of where subject information lives.

## Types of Subjects & Timetabling content

1. **Design-studio subject pages & studio archives** — the dominant category by raw count, and effectively unique to one school. *MSD* runs ~150+ pages under `subject-information/msd-studios` and `travelling-studios` — current offerings ("Open Studio: Worlding", "Threshold", "Wasteocene") plus a deep year-by-year archive ("Semester 1 2017 Thesis 5", "2009 Past Studios"). Discipline-specific and pedagogically real, but the historical archive drives most of the volume.

2. **students.unimelb.edu.au transactional spine (re-surfaced through faculties)** — the genuinely cross-cutting, transactional pages every student needs, owned by students.unimelb.edu.au but crawled under faculty tags because faculties link to them. central domain pages caught here: **"Class timetable"** ("MyTimetable is the system you use to create and view your class schedule"), **"Check your subject census dates"** ("Every subject offered by the University has a census date"), **"Overloading"** ("enrol in more subjects than the standard amount… you will need to apply to overload"), **"Cross-institutional study"**. *Arts* surfaces all four; *FEIT* re-hosts MyTimetable as "Graduate Coursework Students (Domestic/International)".

3. **Subject catalogues / "what subjects can I take" listings** — discipline-scoped lists of available subjects. *Law* "JD subjects" (2,103w) and "MLM subjects" (1,901w) are daily-rebuilt listings ("This page is updated daily… considered indicative at the time of last update") — Handbook-derived data restated locally. *Science* "First year subject sets" and the per-discipline "starting in the Bachelor of Science" guides.

4. **Quota & restricted-enrolment subjects** — subjects with capped places and selection rules. *Science* "Quota subjects" (1,774w); *MSD* "Quota Subjects"; *Biomedical* "Quota Subjects" (1,452w). Three faculties independently maintain near-identical-in-purpose quota pages.

5. **Clinic, internship & experiential-learning subjects** — credit-bearing placement/practice subjects, deeply discipline-specific. *Law* MLS clinics ("Legal Internship", "Stateless Legal Clinic", "Tax Clinic", "Public Interest Law Clinic"); *Arts* "Experiential Learning", "Journalism Internship", "EMA Internship Subject", "Industry Project (ARTS30001)"; *Science* "Internships in the Faculty of Science", "Undergraduate research projects"; *FEIT* "Internship subjects".

6. **Subject delivery, timetabling & room bookings** — how/when/where subjects run. *FFAM* "Timetable & Room Bookings" (1,598w), "Practical Music and Performance Timetable", "Conservatorium performance examinations"; *Education* "Student Timetabling"; *Law* "Subject delivery", "Acceleration Guidelines"; *MSD* "SM2 2017 Studio Key Dates".

7. **Assessment, extensions & special consideration (subject-level)** — rules attached to taking subjects. *Education* runs a cluster — "FoE Extensions", "FoE Assessment Penalties", "Attendance Hurdles", "Reassessment", "Special Consideration", "Unsatisfactory performance" — much of which restates central assessment policy in a faculty voice.

8. **Subject enrolment mechanics & requirements** — enrolling in / selecting subjects. *Education* "Course Enrolment", "Subject Enrolment", "Permission to Teach"; *FBE* "Compulsory Quantitative Requirement", "Summer & Winter Intensives"; *MBS* "Subject Selection and Advanced Standing"; *Biomedical* "Plan your First Year Subjects".

## Legitimate vs central-overlapping

| Faculty-owned (cannot be centralised) | Overlaps students.unimelb.edu.au (consolidation candidate) |
|---|---|
| Design-studio offerings & catalogues (MSD) | Re-hosted MyTimetable / class timetable (FEIT, Arts) |
| Clinic & internship subjects (Law, Arts, Science, FEIT) | Census-date / overloading restatements |
| Quota-subject rules (per discipline) | Cross-institutional study (Law restates students.unimelb.edu.au page verbatim) |
| Performance/room-booking timetables (FFAM) | Subject-level assessment/extension/special-consideration policy (Education) |
| Daily subject listings tied to a degree (Law JD/MLM) | Generic "how to enrol in subjects" advice |
| Subject delivery & acceleration rules (Law, Education) | Studio *archives* (internal record-keeping, not current-student need) |

The balance is unusual for this estate: most of the *raw volume* is legitimately faculty-owned (studios, clinics, catalogues), but it is heavily padded by MSD's historical archive, while the small set of pages students most need — the timetabling/census/overloading spine — is centrally-owned and merely echoed by faculties. The redundancy is vertical (faculty restates students.unimelb.edu.au) and archival (MSD keeps everything), not horizontal duplication across faculties.

## Recommendation
- **students.unimelb.edu.au owns the transactional spine, unambiguously:** MyTimetable/class timetable, census dates, overloading, and cross-institutional study are single-source-of-truth students.unimelb.edu.au pages. Faculties should *link*, never restate — retire Law's verbatim cross-institutional copy and FEIT's MyTimetable re-hosts.
- **Faculties keep the discipline-specific catalogue:** studios, clinics, internship/experiential subjects, performance timetables, and quota rules are genuinely theirs and cannot be centralised.
- **De-archive MSD:** move the studio archive (2008–2018 "Past Studios" / "Studio Archive" pages — well over half of ABP's 204) out of the current-students estate into a separate showcase/archive. This single move shrinks the topic's footprint by roughly a third and stops the audit being dominated by one school's record-keeping.
- **Add one students.unimelb.edu.au gateway + standard:** a students.unimelb.edu.au "Subjects & timetabling" page that links every faculty's subject catalogue and the MyTimetable tool, plus a standard that subject-level assessment/extension/special-consideration content (Education's cluster) defers to the central policy page rather than re-authoring it.
- **Highest-value fix:** **separate the live timetabling spine from archival subject bloat.** Students need MyTimetable, census dates and overloading to be one obvious students.unimelb.edu.au destination; the 130+ MSD archive pages should not sit in the same content class as the page that tells someone when their fees lock in.

## Appendix — all subjects-timetable pages (319)

### ABP/MSD — 204
- **2444w** — [2014 Past Studios | Travelling Studios | MSD](https://msd.unimelb.edu.au/current-students/subject-information/travelling-studios/past-studios/2014)
- **1641w** — [Information for clubs](https://msd.unimelb.edu.au/current-students/student-experience/clubs-and-societies/information-for-clubs)
- **1518w** — [Studio A](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-urban-design/ud-2023_sm2-studios/studio-a)
- **1505w** — [Open Studio: Future Civic](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/thesis_sm1_2026/future-civic)
- **1502w** — [2019 Past Studios | Travelling Studios | MSD](https://msd.unimelb.edu.au/current-students/subject-information/travelling-studios/past-studios/2019)
- **1489w** — [2013 Past Studios | Travelling Studios | MSD](https://msd.unimelb.edu.au/current-students/subject-information/travelling-studios/past-studios/2013)
- **1454w** — [Semester 2 2017 Studio 25](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-25)
- **1445w** — [2016 Past Studios | Travelling Studios | MSD](https://msd.unimelb.edu.au/current-students/subject-information/travelling-studios/past-studios/2016)
- **1423w** — [2012 Past Studios | Travelling Studios | MSD](https://msd.unimelb.edu.au/current-students/subject-information/travelling-studios/past-studios/2012)
- **1412w** — [The City as Design Project](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/d_sm2_2025/the-city-as-design)
- **1391w** — [2015 Past Studios | Travelling Studios | MSD](https://msd.unimelb.edu.au/current-students/subject-information/travelling-studios/past-studios/2015)
- **1347w** — [Threshold](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/c_sm1_2026/threshold)
- **1320w** — [Open Studio: Worlding](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/thesis_sm1_2026/open-worlding)
- **1289w** — [Self-sourced internships | ABPL90434](https://msd.unimelb.edu.au/current-students/subject-information/internships-vocational-placements/abpl90434-construction-management-internship/self-sourced)
- **1275w** — [DESIGNING RIPIARIAN SYSTEMS FOR RESILIENCE & CULTURAL MEANING](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-landscape-architecture/la_sm1_2026/darebin-resilience)
- **1271w** — [Internships and Vocational Placements](https://msd.unimelb.edu.au/current-students/subject-information/internships-vocational-placements)
- **1268w** — [Studio 10](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SM1-Studios/studio-10)
- **1239w** · _mixed_ — [Current Students | Melbourne School of Design](https://msd.unimelb.edu.au/current-students)
- **1228w** — [Studio 6](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SM1-Studios/studio-6)
- **1216w** — [Quota Subjects | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/subject-information/quota-subjects)
- **1199w** — [Wasteocene](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/e_sm1_2026/wasteocene)
- **1196w** — [2011 Past Studios | Travelling Studios | MSD](https://msd.unimelb.edu.au/current-students/subject-information/travelling-studios/past-studios/2011)
- **1193w** — [CHURCH Studio](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/d_sm1_2026/church-studio)
- **1183w** — [2017 Past Studios | Travelling Studios | MSD](https://msd.unimelb.edu.au/current-students/subject-information/travelling-studios/past-studios/2017)
- **1109w** — [2009 Past Studios | Travelling Studios | MSD](https://msd.unimelb.edu.au/current-students/subject-information/travelling-studios/past-studios/2009)
- **1100w** — [2023 and 2024](https://msd.unimelb.edu.au/current-students/subject-information/travelling-studios/past-studios/2023m-and-2024)
- **1087w** — [Semester 2 2017 Studio 35](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-35)
- **1076w** — [Go East Young Wo(Man)](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/d_sm2_2025/go-east-young-woman)
- **1071w** — [Semester 2 2017 Thesis 7](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/THE-2017_SM2-Studios/thesis-7)
- **1059w** — [Information for hosts | ABPL90434](https://msd.unimelb.edu.au/current-students/subject-information/internships-vocational-placements/abpl90434-construction-management-internship/information-for-hosts)
- **1043w** — [The Mansion and The Lagoon](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/c_sm1_2026/the-mansion-and-the-lagoon)
- **1035w** — [Healing the City](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/c_sm1_2026/healing-the-city)
- **1031w** — [Semester 1 2017 Studio 32](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-32)
- **1024w** — [Semester 2 2017 Studio 22](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-22)
- **1024w** — [Studio 4](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SM1-Studios/studio-4)
- **1012w** — [Summer 2018 Studio 5](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SUM-Studios/studio-5)
- **1011w** — [Semester 1 2017 Thesis 5](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/the_2017_SM1-studios/semester-1-2017-thesis-5)
- **1006w** — [Studio 17](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SM1-Studios/studio-17)
- **1001w** — [Semester 2 2017 Studio 26](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-26)
- **997w** — [Semester 1 2017 Studio 1](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-1)
- **991w** — [2018 Past Studios | Travelling Studios | MSD](https://msd.unimelb.edu.au/current-students/subject-information/travelling-studios/past-studios/2018)
- **987w** — [Thesis Studio](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-urban-design/ud-2023_sm2-studios/thesis-studio)
- **985w** — [Summer 2018 Studio 29](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SUM-Studios/studio-29)
- **984w** — [Semester 2 2017 Studio 15](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-15)
- **981w** — [Semester 1 2017 Studio 18](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-18)
- **977w** — [Semester 1 2017 Studio 6](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-6)
- **969w** — [Semester 1 2017 Studio 25](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-25)
- **958w** — [BARBICAN Independent London](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/d_sm1_2026/barbican)
- **950w** — [Semester 2 2017 Thesis 2](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/THE-2017_SM2-Studios/thesis-2)
- **946w** — [Bower Studio (Studio 30)](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-30)
- **942w** — [Studio 2](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SM1-Studios/studio-2)
- **942w** — [Studio 13](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SM1-Studios/studio-13)
- **941w** — [Five Mile Creek](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/c_sm1_2026/five-mile-creek)
- **940w** — [The Broken Box](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/c_sm1_2026/the-broken-box)
- **936w** — [Basin](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/d_sm1_2026/basin)
- **934w** — [Re-Up](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/thesis_sm1_2026/re-up)
- **934w** — [Semester 2 2017 Studio 24](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-24)
- **914w** — [Semester 1 2017 Studio 28](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-28)
- **913w** — [Sweating out the Toxins](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/d_sm1_2026/denatured-visions)
- **912w** — [Semester 2 2017 Studio 2](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-2)
- **910w** — [Nightingale Night School](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/thesis_sm1_2026/nightingale-night-school)
- **907w** — [Semester 1 2017 Studio 3](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-3)
- **889w** — [Semester 1 2017 Studio 2](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-2)
- **886w** — [Semester 1 2017 Studio 22](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-22)
- **884w** — [Semester 2 2017 Studio 6](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-6)
- **882w** — [Semester 2 2017 Studio 28](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-28)
- **876w** — [Studio 1](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SM1-Studios/studio-1)
- **873w** — [Semester 2 2017 Thesis 10](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/THE-2017_SM2-Studios/thesis-10)
- **851w** — [Studio 16](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SM1-Studios/studio-16)
- **848w** — [HTML](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/c_sm1_2026/html)
- **841w** — [Semester 2 2017 Thesis 1](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/THE-2017_SM2-Studios/thesis-1)
- **835w** — [Not Only But Also](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/e_sm1_2026/NotOnlyButAlso)
- **832w** — [Semester 1 2017 Studio 20](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-20)
- **831w** — [Travelling Studios | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/subject-information/travelling-studios)
- **827w** — [Semester 1 2017 Studio 26](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-26)
- **826w** — [Cenobio](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/e_sm1_2026/cenobio-endgame)
- **815w** — [MATERIAL TRACES](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-landscape-architecture/la_sm1_2026/material-traces)
- **811w** — [Yern-da-ville](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/c_sm1_2026/yern-da-ville)
- **811w** — [Nothing Special](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/d_sm1_2026/nothing-special)
- **807w** — [2010 Past Studios | Travelling Studios | MSD](https://msd.unimelb.edu.au/current-students/subject-information/travelling-studios/past-studios/2010)
- **806w** — [Semester 1 2017 Studio 10 (Urban Design C)](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-10)
- **804w** — [Semester 2 2017 Studio 16](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-16)
- **802w** — [Semester 2 2017 Studio 4](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-4)
- **799w** — [Future Casting](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/d_sm1_2026/future-casting)
- **799w** — [Semester 2 2017 Studio 3](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-3)
- **798w** — [Semester 2 2017 Studio 31](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-31)
- **792w** — [Semester 2 2017 Studio 23](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-23)
- **791w** — [Caretaker Studio](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/c_sm1_2026/caretaker-studio)
- **790w** — [Semester 1 2017 Studio 34](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-34)
- **789w** — [2019 Past Studios | Travelling Studios | MSD](https://msd.unimelb.edu.au/current-students/subject-information/travelling-studios/past-studios/2020)
- **789w** — [Housing Studio](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/thesis_sm1_2026/collective-housing)
- **786w** — [Open Studio: Rememory](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/thesis_sm1_2026/open-rememory)
- **780w** — [Southeast Asia Travelling Studio](https://msd.unimelb.edu.au/current-students/subject-information/travelling-studios/2026-subjects-with-international-travel/southeast-asia-travelling-studio)
- **773w** — [Living Island](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/c_sm1_2026/living-island)
- **773w** — [Light Industry](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/e_sm1_2026/space-for-hire)
- **772w** — [MSD Student Curator Group](https://msd.unimelb.edu.au/current-students/student-experience/msdx-and-student-exhibitions/msd-student-curator-group)
- **768w** — [Semester 2 2017 Studio 33](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-33)
- **767w** — [Master of Urban Planning Studio/Thesis](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-urban-planning)
- **766w** — [Studio 14](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SM1-Studios/studio-14)
- **761w** — [Semester 2 2017 Studio 1](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-1)
- **758w** — [Summer Design Studio 22](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SUM-studios/studio-22)
- **755w** — [Open Studio: Parts Unknown](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/thesis_sm1_2026/open-studio-parts-unknown)
- **753w** — [2017 Studio Archive | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017)
- **749w** — [Domesticity Inside Out](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/d_sm1_2026/domesticity-inside-out)
- **747w** — [Semester 2 2017 Studio 34](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-34)
- **743w** — [Semester 1 2017 Thesis 3](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/the_2017_SM1-studios/semester-1-2017-thesis-3)
- **743w** — [Semester 2 2017 Thesis 4](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/THE-2017_SM2-Studios/thesis-4)
- **740w** — [Narrating Ground](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/c_sm1_2026/narrating-ground)
- **736w** — [Semester 1 2017 Studio 19](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-19)
- **735w** — [Semester 1 2017 Studio 14](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-14)
- **734w** — [Bothy](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/e_sm1_2026/bothy)
- **729w** — [Unbounding Ground](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/c_sm1_2026/unbounding-ground)
- **729w** — [Studio 12](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SM1-Studios/studio-12)
- **728w** — [Vernacular Spectacular](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/e_sm1_2026/vernacular-spectacular)
- **721w** — [Semester 1 2017 Studio 12](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-12)
- **721w** — [Semester 1 2017 Studio 35 (MUP Studio T)](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-35)
- **719w** — [Semester 2 2017 Studio 17](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-17)
- **713w** — [Material Metaphors](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/e_sm1_2026/material-metaphors)
- **712w** — [Animal, Vegetable, Mineral : Architecture in the Anthropocene](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/thesis_sm1_2026/open-animal,-vegetable,-mineral)
- **711w** — [Install tips and equipment](https://msd.unimelb.edu.au/current-students/student-experience/msdx-and-student-exhibitions/installation-tips)
- **704w** — [Flats](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/d_sm1_2026/flats)
- **704w** — [Semester 2 2017 Studio 19](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-19)
- **701w** — [Studio 11](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SM1-Studios/studio-11)
- **699w** — [Semester 1 2017 Studio 16](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-16)
- **697w** — [ABPL90434 Construction Management Internship](https://msd.unimelb.edu.au/current-students/subject-information/internships-vocational-placements/abpl90434-construction-management-internship)
- **694w** — [Semester 1 2017 Thesis 7](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/the_2017_SM1-studios/semester-1-2017-thesis-7)
- **690w** — [Summer 2018 Studio 21](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SUM-Studios/studio-21)
- **688w** — [Semester 2 2017 Studio 12](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-12)
- **687w** — [Semester 1 2017 Studio 24](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-24)
- **685w** — [Semester 2 2017 Thesis 8](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/THE-2017_SM2-Studios/thesis-8)
- **680w** — [Semester 1 2017 Studio 13](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-13)
- **680w** — [Semester 1 2017 Thesis 4](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/the_2017_SM1-studios/semester-1-2017-thesis-4)
- **678w** — [Summer 2018 Studio 19](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SUM-Studios/studio-19)
- **677w** — [Semester 1 2017 Studio 11](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-11)
- **677w** — [Semester 2 2017 Studio 14](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-14)
- **674w** — [Semester 2 2017 Studio 10](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-10)
- **671w** — [Semester 1 2017 Thesis 2](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/the_2017_SM1-studios/semester-1-2017-thesis-2)
- **670w** — [Semester 2 2017 Studio 7](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-7)
- **668w** — [How to apply | ABPL90434](https://msd.unimelb.edu.au/current-students/subject-information/internships-vocational-placements/abpl90434-construction-management-internship/how-to-apply)
- **665w** — [Semester 1 2017 Studio 33](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-33)
- **662w** — [Inland](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture/c_sm1_2026/inland)
- **651w** — [Semester 1 2017 Studio 7](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-7)
- **649w** — [Summer Design Studio 21](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SUM-studios/studio-21)
- **647w** — [Semester 1 2017 Studio 29](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-29)
- **646w** — [Semester 2 2017 Studio 8](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-8)
- **645w** — [SM2 2017 Studio Key Dates](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/sm2-2017-studio-key-dates)
- **642w** — [Semester 2 2017 Studio 30](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-30)
- **641w** — [Semester 1 2017 Thesis 6](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/the_2017_SM1-studios/semester-1-2017-thesis-6)
- **641w** — [Semester 2 2017 Thesis 3](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/THE-2017_SM2-Studios/thesis-3)
- **640w** — [Semester 1 2017 Studio 23](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-23)
- **640w** — [Semester 2 2017 Studio 5](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-5)
- **639w** — [Semester 2 2017 Thesis 9](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/THE-2017_SM2-Studios/thesis-9)
- **638w** — [Semester 1 2017 Studio 9](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-9)
- **634w** — [Summer Design Studio 10](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SUM-studios/studio-10)
- **627w** — [2022 Studio Archive | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2022)
- **626w** — [Semester 2 2017 Studio 29](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-29)
- **622w** — [Studio S: Social Planning](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/mup-2017_SM2-studios/studio-s)
- **613w** — [Summer 2018 Studio 10](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SUM-Studios/studio-10)
- **610w** — [Summer Design Studio 4](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SUM-studios/studio-4)
- **609w** — [Semester 2 2017 Thesis 6](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/THE-2017_SM2-Studios/thesis-6)
- **605w** — [2021 Studio Archive | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2021)
- **603w** — [2023 Studio Archive | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2023)
- **601w** — [Summer 2018 Studio 14](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SUM-Studios/studio-14)
- **596w** — [Subject Information | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/subject-information)
- **593w** — [Studio 9](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SM1-Studios/studio-9)
- **591w** — [Semester 1 2017 Studio 31](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-31)
- **589w** — [2020 Studio Archive | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2020)
- **588w** — [2019 Studio Archive | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2019)
- **578w** — [2025](https://msd.unimelb.edu.au/current-students/subject-information/travelling-studios/past-studios/2025)
- **573w** — [Summer Design Studio 27](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SUM-studios/studio-27)
- **571w** — [Semester 2 2017 Thesis 5](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/THE-2017_SM2-Studios/thesis-5)
- **571w** — [Studio 5](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SM1-Studios/studio-5)
- **570w** — [Semester 1 2017 Thesis 1](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/the_2017_SM1-studios/semester-1-2017-thesis-1)
- **565w** — [MUP Studio](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-urban-planning/up-2023_sm2-studios/mup-studio)
- **561w** — [Studio E: Environment](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/mup-2017_SM1-studios/studio-e)
- **558w** — [Semester 2 2017 Studio 27](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-27)
- **557w** — [2018 Studio Archive | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018)
- **557w** — [Semester 2 2017 Studio 9](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/CDE-2017_SM2-Studios/studio-9)
- **554w** — [Semester 1 2017 Studio 27](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-27)
- **549w** — [Summer 2018 Studio 26](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SUM-Studios/studio-26)
- **530w** — [Studio P: Placemaking](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/mup-2017_SM2-studios/studio-p)
- **525w** — [2024](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2024)
- **521w** — [2025](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2026)
- **514w** · _mixed_ — [Enrolment | Current Students | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/enrolment)
- **509w** — [Studio 3](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SM1-Studios/studio-3)
- **495w** — [Semester 1 2017 Studio 5 (Urban Design C)](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/cde-2017_SM1-studios/semester-1-2017-studio-5)
- **494w** — [Studio H: Housing](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/mup-2017_SM1-studios/studio-h)
- **487w** — [Master of Architecture Studios](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-architecture)
- **471w** — [Studio 7](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2018/CDE-2018_SM1-Studios/studio-7)
- **465w** — [Studio T: Transport](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2017/mup-2017_SM1-studios/studio-t)
- **437w** — [2008 Past Studios | Travelling Studios | MSD](https://msd.unimelb.edu.au/current-students/subject-information/travelling-studios/past-studios/2008)
- **397w** — [Master of Urban Design Sample Course Plans](https://msd.unimelb.edu.au/current-students/course-planning/sample-course-plans/urban-design)
- **397w** — [Past Studios | Travelling Studios | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/subject-information/travelling-studios/past-studios)
- **377w** — [Master of Urban Design Studios](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-urban-design)
- **376w** — [Practical Experience](https://msd.unimelb.edu.au/current-students/subject-information/practical-experience)
- **373w** — [MSD Studios](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios)
- **356w** — [Subjects with a Travel Component](https://msd.unimelb.edu.au/current-students/subject-information/subjects-with-a-travel-component)
- **343w** — [Master of Landscape Architecture Studios](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/master-of-landscape-architecture)
- **300w** — [Course Planning | Current Students | MSD](https://msd.unimelb.edu.au/current-students/course-planning)
- **297w** — [MSD Studios Archive](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive)
- **291w** — [2014 Studio Archive | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2014)
- **291w** — [2015 Studio Archive | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2015)
- **291w** — [2016 Studio Archive | Melbourne School of Design](https://msd.unimelb.edu.au/current-students/subject-information/msd-studios/msd-studio-archive/2016)
- **0w** · _redirect_ — [Redirecting...](https://msd.unimelb.edu.au/current-students/subject-information/travelling-studios/d02-application-for-travelling-studio)

### Law — 30
- **2103w** — [JD subjects](https://law.unimelb.edu.au/students/jd/studies/enrolment/jd-subjects)
- **2103w** — [JD subjects](https://law.unimelb.edu.au/students/jd/studies/enrolment/jd-subjects/_recache)
- **1901w** — [MLM subjects](https://law.unimelb.edu.au/students/masters/studies/enrolment/mlm-subjects)
- **1901w** — [MLM subjects](https://law.unimelb.edu.au/students/masters/studies/enrolment/mlm-subjects/_recache)
- **1823w** · _mixed_ — [Accept Your Offer & Get Started | JD | University of Melbourne](https://law.unimelb.edu.au/students/jd/studies/accept-your-offer-and-get-started)
- **1379w** — [Melbourne Law Masters course planning](https://law.unimelb.edu.au/students/masters/studies/mlm-course-planning)
- **1356w** — [Legal Internship](https://law.unimelb.edu.au/students/jd/enrichment/mls-clinics/subjects/legal-internship)
- **1259w** — [Stateless Legal Clinic](https://law.unimelb.edu.au/students/jd/enrichment/mls-clinics/subjects/stateless-legal-clinic)
- **976w** — [Student Achievement and Grading](https://law.unimelb.edu.au/students/jd/studies/student-achievement-and-grading)
- **943w** — [Sustainability Business Clinic](https://law.unimelb.edu.au/students/jd/enrichment/mls-clinics/subjects/sustainability-business-clinic)
- **932w** — [Study Abroad at Oxford](https://law.unimelb.edu.au/students/masters/enrichment/global-learning-opportunities/study-abroad-at-oxford)
- **837w** — [JD course structure and plans](https://law.unimelb.edu.au/students/jd/studies/course-plans)
- **803w** — [Public Interest Law Clinic](https://law.unimelb.edu.au/students/jd/enrichment/mls-clinics/subjects/public-interest-law-clinic)
- **708w** — [Global and interstate subjects](https://law.unimelb.edu.au/students/jd/enrichment/global-learning-opportunities/global-subjects)
- **564w** — [Tax Clinic | Melbourne Law School | University of Melbourne](https://law.unimelb.edu.au/students/jd/enrichment/mls-clinics/subjects/mls-tax-clinic)
- **560w** — [Subject delivery](https://law.unimelb.edu.au/students/masters/studies/subject-delivery)
- **558w** — [Acceleration Guidelines](https://law.unimelb.edu.au/students/jd/studies/acceleration-guidelines)
- **537w** — [Law Apps](https://law.unimelb.edu.au/students/jd/enrichment/mls-clinics/subjects/law-apps)
- **475w** — [Street Law](https://law.unimelb.edu.au/students/jd/enrichment/mls-clinics/subjects/street-law)
- **453w** — [NDIS and Disability Benefits Clinic](https://law.unimelb.edu.au/students/jd/enrichment/mls-clinics/subjects/ndis-and-disability-benefits-clinic)
- **437w** — [Indigenous Legal Advocacy Clinic](https://law.unimelb.edu.au/students/jd/enrichment/mls-clinics/subjects/indigenous-legal-advocacy-clinic)
- **372w** · _mixed_ — [MLM student advising](https://law.unimelb.edu.au/students/masters/studies/student-advising)
- **286w** — [Global learning opportunities](https://law.unimelb.edu.au/students/jd/enrichment/global-learning-opportunities)
- **256w** — [Disability Human Rights Clinic](https://law.unimelb.edu.au/students/jd/enrichment/mls-clinics/subjects/disability-human-rights-clinic)
- **231w** — [MLS Feedback](https://law.unimelb.edu.au/students/mls-feedback)
- **205w** — [DHRC Research Outcomes](https://law.unimelb.edu.au/students/jd/enrichment/mls-clinics/subjects/disability-human-rights-clinic/research-outcomes)
- **203w** — [Early Academic Guidance for Legal Education](https://law.unimelb.edu.au/students/legal-academic-skills/facilitated-study-groups)
- **158w** · _link-farm_ — [Minor Thesis option](https://law.unimelb.edu.au/students/masters/studies/minor-thesis-option)
- **131w** · _link-farm_ — [Climate Resilience Clinic](https://law.unimelb.edu.au/students/jd/enrichment/mls-clinics/subjects/climate-resilience-clinic)
- **130w** · _link-farm_ — [Law and the Environment Lab](https://law.unimelb.edu.au/students/jd/enrichment/mls-clinics/subjects/law-and-the-environment-lab)

### Education — 25
- **5447w** — [FAQs](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/faqs)
- **1482w** — [Roles and responsibilities](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/placement-requirements/roles-and-responsibilities)
- **1457w** · _mixed_ — [Course Enrolment | Faculty of Education](https://education.unimelb.edu.au/study/current-students/course-enrolment)
- **1277w** · _mixed_ — [Academic Skills module](https://education.unimelb.edu.au/study/current-students/academic-skills-module)
- **1142w** — [Introduction to Contemporary Australian Schooling](https://education.unimelb.edu.au/study/current-students/icas)
- **1048w** · _mixed_ — [Student Timetabling | Faculty of Education](https://education.unimelb.edu.au/study/current-students/timetable)
- **961w** — [Assessment](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/placement-requirements/assessment)
- **881w** · _mixed_ — [Employability in Education](https://education.unimelb.edu.au/study/current-students/employability-in-education)
- **875w** — [Permission to Teach (PTT) Information](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/permission-to-teach-ptt-information)
- **795w** · _mixed_ — [Current Students | Faculty of Education](https://education.unimelb.edu.au/study/current-students)
- **708w** — [Placement Allocation Process](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/placement-allocation-process)
- **697w** — [Professional Conduct](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/placement-requirements/professional-conduct)
- **689w** — [Unsatisfactory performance](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/placement-requirements/unsatisfactory-performance)
- **524w** · _mixed_ — [Subject Enrolment](https://education.unimelb.edu.au/study/current-students/subject-enrolment)
- **512w** — [Master of Teaching](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching)
- **479w** — [Attendance and absences](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/placement-requirements/attendance-and-absences)
- **475w** — [Health and safety](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/placement-requirements/health-and-safety)
- **409w** · _mixed_ — [International Study | Faculty of Education](https://education.unimelb.edu.au/study/current-students/international-study-opportunities)
- **402w** — [FoE Assessment Penalties](https://education.unimelb.edu.au/study/current-students/extension-assessment-information-and-policies/main-page-links/foe-assessment-penalties)
- **391w** · _mixed_ — [Faculty of Education Scholarships](https://education.unimelb.edu.au/study/current-students/employability-in-education/faculty-of-education-scholarships)
- **369w** — [FoE Extensions](https://education.unimelb.edu.au/study/current-students/extension-assessment-information-and-policies/main-page-links/foe-extensions)
- **309w** — [Participation](https://education.unimelb.edu.au/study/current-students/employability-in-education/master-of-teaching/placement-requirements/participation)
- **300w** — [Attendance Hurdles](https://education.unimelb.edu.au/study/current-students/extension-assessment-information-and-policies/main-page-links/attendance-hurdles)
- **293w** — [Reassessment](https://education.unimelb.edu.au/study/current-students/extension-assessment-information-and-policies/main-page-links/reassessment)
- **225w** — [Special Consideration](https://education.unimelb.edu.au/study/current-students/extension-assessment-information-and-policies/main-page-links/special-consideration)

### Arts — 21
- **1770w** · _mixed_ — [Experiential Learning](https://arts.unimelb.edu.au/students/experiential-learning)
- **1418w** · _mixed_ — [Cross-institutional study](https://students.unimelb.edu.au/course-admin/cross-institutional-study)
- **987w** · _mixed_ — [Check your subject census dates : The University of Melbourne](https://students.unimelb.edu.au/course-admin/census-dates)
- **893w** · _mixed_ — [Overseas experience](https://arts.unimelb.edu.au/students/overseas-experience)
- **893w** · _mixed_ — [Overseas experience](https://arts.unimelb.edu.au/students/graduate-coursework/enrich-your-program/overseas-experience)
- **891w** — [Internship: Personal & Career Growth | UniMelb Arts](https://arts.unimelb.edu.au/students/experiential-learning/internship-personal-and-career-growth)
- **804w** — [Journalism Internship | Master of Journalism & International Journalism – UniMelb](https://arts.unimelb.edu.au/students/experiential-learning/journalism-internship-subject)
- **791w** — [EMA Internship Subject | Executive Master of Arts – UniMelb](https://arts.unimelb.edu.au/students/experiential-learning/ema-internship-subject)
- **718w** · _mixed_ — [Overloading | Current students | The University of Melbourne](https://students.unimelb.edu.au/course-admin/planning-your-course-and-subjects/study-load/overloading)
- **667w** — [Invitation to host an intern](https://arts.unimelb.edu.au/students/experiential-learning/internship-personal-and-career-growth/invitation-to-host-an-intern)
- **629w** · _mixed_ — [SCC Graduate Internship Subjects](https://arts.unimelb.edu.au/students/experiential-learning/scc-graduate-internship-subjects)
- **456w** · _mixed_ — [Diploma in Languages](https://arts.unimelb.edu.au/students/graduate-coursework/enrichment/diploma-in-languages)
- **426w** — [Dr Delia Lin](https://arts.unimelb.edu.au/students/undergraduate/enrich-your-bachelor-of-arts/academic-mentoring/dr-delia-lin)
- **344w** — [Video edit suites](https://arts.unimelb.edu.au/students/graduate-coursework/resources-and-support/video-edit-suites)
- **344w** — [Video edit suites](https://arts.unimelb.edu.au/students/graduate-coursework/enrich-your-program/video-edit-suites)
- **331w** — [Audio/Visual loan equipment](https://arts.unimelb.edu.au/students/audiovisual-loan-equipment)
- **316w** · _mixed_ — [Class timetable | Current students | The University of Melbourne](https://students.unimelb.edu.au/course-admin/class-timetable)
- **311w** — [GSHSS Academic Culture and English Tutorials](https://arts.unimelb.edu.au/students/graduate-coursework/enrichment/gshss-academic-culture-and-english-tutorials)
- **306w** — [Industry Project (ARTS30001)](https://arts.unimelb.edu.au/students/experiential-learning/industry-project)
- **194w** — [Faculty of Arts Travel Grant](https://arts.unimelb.edu.au/students/overseas-experience/funding/faculty-of-arts-overseas-subject-travel-grant)
- **194w** — [Faculty of Arts Travel Grant](https://arts.unimelb.edu.au/students/graduate-coursework/enrich-your-program/overseas-experience/funding/faculty-of-arts-overseas-subject-travel-grant)

### Science — 15
- **3185w** — [Research Project Subjects | Veterinary & Agricultural Sciences](https://science.unimelb.edu.au/students/course-guide-graduate-coursework-degrees/agriculture-food-science-research-projects)
- **2666w** — [Internships in the Faculty of Science](https://science.unimelb.edu.au/students/enrich-your-studies/internship-subjects)
- **1774w** — [Quota subjects](https://science.unimelb.edu.au/students/quota-subjects)
- **1271w** — [Undergraduate research projects](https://science.unimelb.edu.au/students/research-project-subjects)
- **1245w** — [Mathematics and Statistics: starting in the Bachelor of Science](https://science.unimelb.edu.au/students/course-guide-bachelor-of-science/first-year-subject-sets/mathematics-and-statistics)
- **1224w** — [Physical Sciences: starting in the Bachelor of Science](https://science.unimelb.edu.au/students/course-guide-bachelor-of-science/first-year-subject-sets/physical-sciences)
- **1047w** — [Geography: getting started in the Bachelor of Science](https://science.unimelb.edu.au/students/course-guide-bachelor-of-science/first-year-subject-sets/geography)
- **1034w** — [Earth Sciences: getting started in the Bachelor of Science](https://science.unimelb.edu.au/students/course-guide-bachelor-of-science/first-year-subject-sets/earth-sciences)
- **1006w** — [Chemical Sciences: getting started in the Bachelor of Science](https://science.unimelb.edu.au/students/course-guide-bachelor-of-science/first-year-subject-sets/chemical-sciences)
- **974w** — [Engineering Systems: starting in the Bachelor of Science](https://science.unimelb.edu.au/students/course-guide-bachelor-of-science/first-year-subject-sets/engineering-systems)
- **963w** — [Psychological Sciences: starting in the Bachelor of Science](https://science.unimelb.edu.au/students/course-guide-bachelor-of-science/first-year-subject-sets/psychological-sciences)
- **952w** — [Information Technology: starting in the Bachelor of Science](https://science.unimelb.edu.au/students/course-guide-bachelor-of-science/first-year-subject-sets/information-technology)
- **949w** — [Biological sciences: getting started in the Bachelor of Science](https://science.unimelb.edu.au/students/course-guide-bachelor-of-science/first-year-subject-sets/biological-sciences)
- **939w** — [First year subject sets](https://science.unimelb.edu.au/students/course-guide-bachelor-of-science/first-year-subject-sets)
- **841w** — [Breadth subjects in the Bachelor of Science](https://science.unimelb.edu.au/students/course-guide-bachelor-of-science/breadth)

### MDHS — 7
- **925w** · _mixed_ — [Employability in MDHS](https://mdhs.unimelb.edu.au/study/current-students/employability-in-mdhs)
- **445w** — [During Placement](https://mdhs.unimelb.edu.au/study/current-students/placements/org/dsp/during-placement)
- **419w** — [Information for students](https://mdhs.unimelb.edu.au/study/current-students/placements/students)
- **378w** — [Professional Psychology](https://mdhs.unimelb.edu.au/study/current-students/placements/org/msps/professional-psychology)
- **349w** — [Department of Nursing](https://mdhs.unimelb.edu.au/study/current-students/placements/org/department-of-nursing)
- **244w** — [Conclusion of Placement](https://mdhs.unimelb.edu.au/study/current-students/placements/org/mspgh/conclusion-of-placement)
- **206w** — [Conclusion of placement](https://mdhs.unimelb.edu.au/study/current-students/placements/org/department-of-social-work-resources/conclusion-of-placement)

### FEIT — 6
- **728w** · _redirect_ — [Internships - Students - Faculty of Engineering and Information Technology](https://eng.unimelb.edu.au/students/coursework/progress-your-career/internship/internship-subjects)
- **728w** — [Internships - Students - Faculty of Engineering and Information Technology](https://eng.unimelb.edu.au/students/coursework/student-experience/internship/internship-subjects)
- **667w** — [Academic English Tutorials](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/improve-your-english,-communication-and-academic-skills/academic-english-tutorials)
- **523w** · _mixed_ — [Graduate Coursework Students (International)](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/class-registration/mytimetable)
- **474w** · _mixed_ — [Graduate Coursework Students (Domestic)](https://eng.unimelb.edu.au/students/coursework/student-experience/orientation/before-orientation/class-registration/enrolling-in-subjects)
- **433w** — [Undergraduate Prizes](https://eng.unimelb.edu.au/students/scholarships-prizes-and-awards/undergraduate/subject-prizes-1)

### FFAM — 6
- **1598w** · _mixed_ — [Timetable & Room Bookings | Faculty of Fine Arts & Music](https://finearts-music.unimelb.edu.au/current-students/bookings-and-timetables/timetable-and-room-bookings)
- **1598w** · _mixed_ — [Timetable & Room Bookings | Faculty of Fine Arts & Music](https://finearts-music.unimelb.edu.au/current-students/bookings-and-timetables/timetable-and-room-bookings/_nocache)
- **721w** — [Quiet spaces at the Southbank Campus](https://finearts-music.unimelb.edu.au/current-students/bookings-and-timetables/quiet-spaces-at-the-southbank-campus)
- **307w** — [Conservatorium performance examinations](https://finearts-music.unimelb.edu.au/current-students/assessment-and-exams/conservatorium-performance-timetable-and-examinations)
- **275w** — [Information for current students at the Faculty of Fine Arts and Music](https://finearts-music.unimelb.edu.au/current-students)
- **43w** · _link-farm_ — [Practical Music and Performance Timetable](https://finearts-music.unimelb.edu.au/current-students/bookings-and-timetables/pcme-practical-music-timetable)

### FBE — 2
- **458w** — [Summer & Winter Intensives](https://fbe.unimelb.edu.au/students/bcom/current-students/intensives)
- **392w** — [Compulsory Quantitative Requirement](https://fbe.unimelb.edu.au/students/bcom/current-students/compulsory-quantitative-requirement)

### Biomedical (school) — 2
- **1452w** — [Quota Subjects](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/quota-subjects)
- **1184w** · _mixed_ — [Plan your First Year Subjects](https://biomedicalsciences.unimelb.edu.au/study/current-student-information/plan-your-bachelor-of-biomedicine/plan-your-first-year-subjects)

### MBS (school) — 1
- **1098w** — [Subject Selection and Advanced Standing](https://mbs.unimelb.edu.au/students/course-planning/subject-selection-and-advanced)
