# Melbourne Law School — CS Profile

- **Unit:** Law (single-department faculty)
- **CS URL:** `law.unimelb.edu.au/students` (pattern: `/students`)
- **Pages:** 195 (162 unique, 23 link-farm, 10 mixed)
- **Crawl:** Full BFS, max depth 4
- **students.unimelb.edu.au links:** 184 (0.94/page)

## IA Structure
```
/students
  /jd (JD program)
    /studies (course planning, enrolment, subjects, grading)
    /enrichment (clinics, global learning, mooting, orientation)
  /masters (MLM program)
    /studies (course planning, enrolment, subjects, advising)
    /enrichment (global, internships, orientation)
  /grd (graduate research)
    /degree-requirements, /supervision, /enrichment, /scholarships
  /career-services (pathways, consultations, ELLIS program)
  /legal-academic-skills (writing, resources, study groups)
  /study-overseas-program (exchanges, partnerships)
  /orientation, /student-life-and-societies
  /forms + /professional-behaviour-guidelines
```

## Service Model Position
**Self-contained ecosystem.** Law runs its own parallel systems for course planning, careers, academic skills, forms, and research candidature. Minimal students.unimelb.edu.au dependency — only 184 students.unimelb.edu.au links across 195 pages (vs FEIT's 265 across 204). Key central-redirect areas: enrolment transactions, special consideration.

## Content Profile
- **Heaviest topics:** research-candidature (86), forms-admin (66), international (55), student-life (49)
- **Richest pages:** Legal Research (5,424w), Professional Behaviour Guidelines (3,169w), PhD milestones (2,912w)
- **Unique faculty content:** JD/MLM course plans, MLS Clinics (12 clinics), degree partnerships (8 international), career pathways (7), legal academic skills, steps to practising law

## Structural Issues
- 3 `_recache` URL duplicates (CMS cache endpoints exposed)
- Heavy reliance on handbook.unimelb.edu.au (801 links) for subject detail
- Career services run completely separately from students.unimelb.edu.au

## Recommendation Notes
- **Keep:** Course plans, clinics, degree partnerships, legal academic skills, career pathways, forms
- **Redirect to students.unimelb.edu.au:** Enrolment how-to, special consideration, leave of absence
- **Cross-link:** Career services should link to central Careers service
