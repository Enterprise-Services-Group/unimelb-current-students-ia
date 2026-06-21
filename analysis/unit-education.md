# Education — CS Profile

- **Unit:** Faculty of Education
- **CS URL:** `education.unimelb.edu.au/study/current-students` (pattern: `/study/current-students` — unique among faculties)
- **Pages:** ~30-45 estimated (root + IA capture)
- **Crawl mode:** Root capture via web_extract

## IA Structure
```
/study/current-students
  Admissions & Getting Started
    /timetable, /academic-skills-module, /lantite, /icas, /itea
  Course Planning & Structure
    /course-enrolment, /subject-enrolment
  Managing Your Course
    /extension-assessment-information-and-policies
  Placements & WIL (professional experience)
  Support
```

## Service Model Position
**Content-rich for program-specific items; central-dependent for transactions.** Education is the best example of the central-and-spoke balance: it holds genuinely unique content (LANTITE, ICAS, iTEA, academic skills module, timetable) that cannot exist on students.unimelb.edu.au, while appropriately redirecting transactional tasks (course planning tools, special consideration, leave of absence, withdrawal, results, graduation) to students.unimelb.edu.au.

## Content Profile
- **Unique faculty content:** LANTITE (national literacy/numeracy test — legally required for teaching students), ICAS (Introduction to Contemporary Australian Schooling), iTEA (Initial Teacher Education Assessment), Academic Skills Module (education-specific), Timetable (faculty-specific), Extensions (faculty-specific guidelines), Professional Experience/Placements (teaching practicums), Secondary Learning Areas requirements
- **Central-redirect areas:** Course planning tools, special consideration, leave of absence, course/subject withdrawal, results, graduation, health & wellbeing

## Structural Issues
- URL pattern `/study/current-students` is unique — no other faculty uses this convention
- Extensions page sits alongside assessment policies — could be consolidated with students.unimelb.edu.au special consideration

## Recommendation Notes
- **Keep:** LANTITE, ICAS, iTEA, Academic Skills Module, timetable, placements, extensions, secondary learning areas
- **Redirect to students.unimelb.edu.au:** Course planning tools (My Course Planner), special consideration, leave, withdrawal, graduation
- **Standardise URL:** Redirect `/study/current-students` → `/students`
- **Good model:** Education's balance of unique program content + central-redirect for transactions is closest to the recommended central-and-spoke model. Use as a reference for other faculties.
