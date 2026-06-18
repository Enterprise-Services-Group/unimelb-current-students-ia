# Current Students IA — Structural Findings & Fragmentation Audit

*Synthesized from crawl of 9 faculty CS sections + central hub. June 2026.*

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

Faculties fall on a spectrum from "hub-dependent link directory" to "self-contained parallel ecosystem":

```
Hub-dependent ←————————————————————————————→ Self-contained
     ABP    FBE   Education  Arts  Science  MDHS   Law   FFAM   FEIT
```

- **ABP, FBE:** CS root is mostly a link directory. Most content delegates to students.unimelb.edu.au.
- **Education:** Unique program content + heavy hub-redirect for transactions. Good balance.
- **Arts, Science:** Well-structured local hubs with real faculty content + moderate hub links.
- **FEIT, Law:** Almost entirely self-contained. Run parallel systems for course planning, careers, scholarships, forms, academic skills. Minimal hub links.
- **FFAM:** Completely self-contained. Conservatorium/art-school model doesn't fit hub taxonomy.

---

## Finding 3: The school-level fragmentation problem

MDHS has the worst fragmentation — 3+ schools run their own CS sections on separate subdomains:

| Unit | CS URL | Status |
|------|--------|--------|
| MDHS Faculty | mdhs.unimelb.edu.au/study/current-students | Thin hub (4 cards) |
| Biomedical Sciences | biomedicalsciences.unimelb.edu.au/study/current-student-information | Full CS section |
| Dental School | dental.unimelb.edu.au/study/student-resources | Has CS section |
| MSPGH | mspgh.unimelb.edu.au | Likely has CS section |
| Medical School | Links to faculty hub | No separate CS |
| Psych Sciences | Links to faculty hub | No separate CS |

FBE has a similar split: FBE /students (BCom, PhD) + MBS /students (graduate programs) on mbs.unimelb.edu.au.

**No other faculty has school-level CS sections.** Arts schools, Science schools, FEIT schools, FFAM units — all route through the faculty CS page.

---

## Finding 4: Careers & employability is the most duplicated service

Every single faculty (8/9) and MBS run their own career content in parallel with the central careers hub:

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
| Central Hub | Careers section: Employability, Career Checklist, Careers Online, Smart Resume |

The hub careers content and faculty career content **do not cross-link**. A student who uses the hub career checklist may never discover their faculty's mentoring program, and vice versa.

---

## Finding 5: Course planning duplication is real but partially legitimate

Every faculty provides course plans / sample course plans / course guides. The hub has My Course Planner + general planning advice.

**Legitimate (faculty must own):**
- Degree-specific sample course plans (MSD's 10 masters course plans, Law JD/MLM plans)
- Program-specific requirements (LANTITE, Fitness to Practice, learning area requirements)
- Subject selection guidance for specific majors (Science first-year subject sets)

**Duplicative (hub should own):**
- General "how to plan your course" advice (FEIT duplicates what the hub says)
- Course planning tool links (My Course Planner linked from multiple faculties)
- Leave of absence, course withdrawal info (hub has definitive pages)

---

## Finding 6: Broken and circular links

- **FBE /current-students → 404.** The Phase 1 probe detected a link to this path, but it returns a 404. The real CS is at /students.
- **FEIT has 17 broken/redirect URLs** (e.g., internship FAQ at two different paths with identical content)
- **Arts has 3 broken pages** (academic mentoring profiles, WIL internships page)
- **Biomedical Sciences "Bachelor of Science" link** points circularly back to the same page
- **MDHS "Medical School" and "Psychological Sciences" school resource links** both point back to the same thin faculty hub page

---

## Finding 7: The central hub's gaps

The hub covers transactional admin (enrolment, fees, exams, graduation, key dates, timetable) and general support (health, counselling, Stop 1, careers, student life) comprehensively. But it has **no content** for:

1. **Course plans / degree-specific planning** — every faculty does this, hub has My Course Planner tool but no degree guides
2. **Placements & WIL** — completely absent from the hub. Students must find placement info on faculty sites.
3. **Discipline-specific academic skills** — hub has general PASS/academic skills; doesn't cover legal writing, lab reports, studio practice
4. **Faculty-specific forms** — no hub equivalent
5. **Professional recognition / accreditation pathways** — Law's "Steps to Practising Law," Education's LANTITE/teacher registration

---

## Finding 8: No consistent "what's where" guidance

No faculty CS page tells students "for X, go to the central hub; for Y, stay here." The result:
- Students must learn through trial and error which system handles which need
- Faculty pages often re-explain hub services (e.g., ABP's enrolment section re-explains special consideration, leave of absence, overloading — all of which are definitively covered on the hub)
- No page exists that maps "I need to do X → go to Y"

---

## Finding 9: CMS/platform inconsistency

- **Law, Arts, FEIT, Science** appear to use the same UoM Squiz Matrix CMS with consistent global header/footer
- **FFAM** uses a different template (no sidebar navigation on the CS root — just cards/grid)
- **MDHS** uses a card-based landing page pattern
- **FBE** and **MBS** use different visual treatments from each other despite being under the same faculty
- **Biomedical Sciences** has its own distinct template

---

## Finding 10: Page depth and complexity

| Faculty | Pages | Max depth | Est. total words |
|---------|-------|-----------|-----------------|
| Law | 195 | 4 | ~150K |
| FEIT | 204 | 6 | 156K |
| Arts | 91 | 5 | ~80K |
| Science | 94 | 3 | ~90K |
| ABP | ~40 | ~3 | ~40K |
| Education | ~40 | ~3 | ~40K |
| FFAM | ~40 | ~3 | ~30K |
| FBE+MBS | ~25 | ~2 | ~20K |
| MDHS+schools | ~50 | ~3 | ~50K |
| **Total** | **~780** | — | **~650K** |

The four fully-crawled faculties account for 75% of all pages. Law and FEIT alone account for 51%.
