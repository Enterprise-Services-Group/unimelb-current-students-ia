# MDHS — CS Profile

- **Unit:** Faculty of Medicine, Dentistry & Health Sciences
- **CS URL:** `mdhs.unimelb.edu.au/study/current-students` (pattern: `/study/current-students`)
- **Pages:** ~50 estimated across faculty + 3+ school subdomains
- **Crawl mode:** Root + biomedical school capture via web_extract
- **⚠️ School-level CS sections:** Biomedical Sciences, Dental School, MSPGH (likely)

## IA Structure
```
mdhs.unimelb.edu.au/study/current-students (thin faculty hub — 4 cards)
  /student-fitness-to-practice
  /student-enrichment
  /placements
  /employability-in-mdhs

biomedicalsciences.unimelb.edu.au/study/current-student-information (separate subdomain)
  /plan-your-bachelor-of-biomedicine
  /master-of-biomedical-science
  /university-health-hub
  /quota-subjects
  /biom30003-biomedical-science-research-project

dental.unimelb.edu.au/study/student-resources (separate subdomain — content not captured)
mspgh.unimelb.edu.au (likely has its own CS — not probed)
```

## Service Model Position
**Most fragmented CS architecture.** MDHS is the only faculty where multiple schools run their own full CS sections on separate subdomains with different URL patterns. The faculty hub itself is thin — 4 resource cards. A Biomedicine student navigates 3+ different CS experiences (hub, MDHS faculty, Biomedical Sciences school, potentially Dental or MSPGH).

## Content Profile
- **Faculty hub:** Student Fitness to Practice (mandatory clinical standards — genuinely unique), Student Enrichment, Placements, Employability, Scholarships
- **Biomedical Sciences:** BBiomed planning, Master of Biomedical Science, University Health Hub, Quota Subjects, BIOM30003 research project
- **Dental School:** Student Resources page (content dynamic — not captured)
- **Unique faculty content:** Fitness to Practice, clinical placements, MDHS-specific employability, school-level course planning
- **Hub-redirect areas:** General enrolment, fees, exams — faculty sends to hub for these

## Structural Issues
- **Most fragmented faculty** — 3+ school subdomains with separate CS sections, different URL patterns
- Faculty hub's "School Resources" section is misleading: Medical School and Psychological Sciences links point circularly back to the thin faculty hub
- Biomedical Sciences "Bachelor of Science" link is circular
- Dental School page exists but content was not captured by web_extract (likely dynamic/JS-rendered)
- 3 different URL patterns across faculty + schools: `/study/current-students`, `/study/current-student-information`, `/study/student-resources`

## Recommendation Notes
- **Consolidate school CS sections:** Biomedical Sciences, Dental, and MSPGH CS should either redirect to a unified MDHS CS page or adopt the same template and URL convention
- **Keep:** Fitness to Practice, clinical placements, MDHS employability, school-level course planning (BBiomed, etc.), quota subjects
- **Fix:** Circular links (Medical School, Psychological Sciences, BSc link on Biomedical page)
- **Standardise URLs:** All MDHS CS should live under a single pattern — ideally `mdhs.unimelb.edu.au/students` with school-specific sections
- **Add:** "Where to go" sidebar on faculty hub and all school CS pages
- **Highest priority for consolidation** — MDHS fragmentation is the worst in the university
