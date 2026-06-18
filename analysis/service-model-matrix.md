# Service-Model Matrix — Who Provides What

*Evidence from crawl of 9 faculty CS sections + central hub (584 fully crawled pages + ~200 IA-captured). June 2026.*

**Legend:**
- **H** = Hub provides (students.unimelb.edu.au is the primary/definitive source)
- **F** = Faculty provides (faculty CS section is the primary source)
- **B** = Both provide (faculty and hub both have content — potential duplication)
- **—** = Not applicable / not observed
- **S** = School-level provides (below faculty, on school subdomain — fragmentation risk)

---

## Service Category × Faculty Matrix

| Service | Hub | Law | FEIT | Arts | Science | ABP | FBE | Education | FFAM | MDHS |
|---------|-----|-----|------|-------|---------|-----|-----|-----------|------|------|
| **Enrolment & course admin** | H | B | B | B | B | H→ | H→ | B | F | H→ |
| **Exams, assessment & results** | H | B | F | H→ | H→ | H→ | H→ | B | F | H→ |
| **Fees & finance** | H | H→ | — | H→ | — | H→ | H→ | H→ | — | H→ |
| **Graduation** | H | B | F | B | — | H→ | H→ | H→ | — | — |
| **Key dates** | H | — | — | — | — | — | — | — | — | — |
| **Timetable** | H | B | F | B | — | H→ | H→ | F | F | — |
| **Course planning** | H | F | F | F | F | F | F | F | F | F+S |
| **Health & wellbeing** | H | F | F | F | F | H→ | F | H→ | F | F |
| **Careers & employability** | H | F | F | F | F | F | F | F | F | F |
| **Student life & clubs** | H | F | F | F | F | F | F | F | F | F |
| **Academic skills** | H | F | F | F | F | H→ | — | F | — | — |
| **Study overseas** | H | F | F | F | — | H→ | — | — | — | — |
| **Placements & WIL** | — | F | F | F | F | F | — | F | — | F |
| **Scholarships** | H | F | F | F | F | F | F | F | — | F+S |
| **International student support** | H | F | F | — | — | — | — | — | — | — |
| **IT & systems** | H | F | F | F | — | F | — | — | — | — |
| **Indigenous students** | H | — | — | — | F | H→ | — | — | — | — |
| **Forms & admin** | — | F | F | F | F | F | — | F | F | F |
| **Research candidature** | — | F | F | F | F | — | F | F | F | — |

---

## Key Patterns in the Matrix

### 1. The Hub is definitive for transactional admin
Enrolment, fees, key dates, graduation, special consideration, results — the hub is the single source of truth. Faculties that provide parallel content for these (FEIT, Law, Arts) are duplicating.

### 2. Faculty-specific content is concentrated in 4 areas
Every faculty runs its own content for:
- **Course planning** (sample plans, degree guides, subject selection advice)
- **Careers & employability** (faculty-specific career services, mentoring, internships)
- **Placements & WIL** (clinical placements, teaching practicums, legal clinics, engineering internships)
- **Student life & clubs** (faculty-specific clubs, societies, events, newsletters)

### 3. Three schools have their own CS sections — breaking the faculty model
- **Melbourne Business School** (mbs.unimelb.edu.au/students) — separate from FBE
- **School of Biomedical Sciences** (biomedicalsciences.unimelb.edu.au/study/current-student-information) — separate from MDHS
- **Melbourne Dental School** (dental.unimelb.edu.au/study/student-resources) — separate from MDHS
- Potentially MSPGH as well (not confirmed)

### 4. URL convention fragmentation
Four different URL patterns for the same "Current Students" concept:
- `/students` — Law, Arts, FEIT, Science, FBE
- `/current-students` — ABP/MSD, FFAM
- `/study/current-students` — Education, MDHS
- No consistent pattern for school-level CS

### 5. Hub dependency varies dramatically
- **FEIT, Law, Science** — low hub dependency, self-contained ecosystems
- **ABP, FBE** — high hub dependency, mostly a link directory
- **FFAM** — lowest hub dependency, entirely self-contained for conservatorium needs
- **Education** — mixed: unique program content + heavy hub redirect for transactions

### 6. Careers & employability is the most duplicated service
Every faculty runs career content (mentoring, internships, career pathways) in parallel with the central careers hub. MBS has its own branded career service (mbs.unimelb.edu.au/career). This is the clearest case for unification.

### 7. Forms are faculty-specific and legitimate
Every faculty has its own forms (placement applications, ensemble registration, special permission, clinic enrolment). These cannot be centralized — they're operational requirements of each discipline.

### 8. MDHS is the most fragmented
Content scattered across faculty hub + 3+ school subdomains with different URL patterns. A Biomedicine student potentially navigates 3 different CS experiences (hub, MDHS faculty, Biomedical Sciences school).

---

## Duplication Heatmap

| Service | Faculties duplicating hub | Duplication severity |
|---------|--------------------------|---------------------|
| Careers & employability | 8/9 | 🔴 High — every faculty runs career content |
| Course planning | 9/9 + schools | 🔴 High — but mostly legitimate (degree-specific) |
| Student life & clubs | 8/9 | 🟡 Medium — faculty newsletters, events, clubs |
| Academic skills | 5/9 | 🟡 Medium — faculty-specific tutoring |
| Scholarships | 7/9 | 🟡 Medium — faculty prizes vs hub search |
| Health & wellbeing | 6/9 | 🟡 Medium — faculty wellbeing pages |
| Enrolment & course admin | 4/9 | 🟢 Low — mostly hub-redirect |
| Exams & assessment | 3/9 | 🟢 Low — mostly hub-redirect |
| Placements & WIL | 7/9 | 🟢 Low — legitimate faculty-specific |

---

## What the Hub Does NOT Cover (Genuine Gaps)

These services exist **only** on faculty sites — the hub has no equivalent:
1. **Course plans / sample course plans** — every faculty, no hub equivalent
2. **Placement/practicum management** — clinical, teaching, legal, engineering
3. **Discipline-specific academic skills** — legal writing, lab skills, performance
4. **Faculty forms** — ensemble registration, clinic enrolment, placement applications
5. **Program-specific regulatory requirements** — LANTITE (Education), Fitness to Practice (MDHS)
6. **Faculty-specific enrichment** — MSD mentoring, Science ambassadors, FEIT hackathons
7. **Performance/practice management** — FFAM ensembles, practice rooms, performances
8. **School-level course planning** — BBiomed planning, MBS course planning
