# Arts — CS Profile

- **Unit:** Faculty of Arts
- **CS URL:** `arts.unimelb.edu.au/students` (pattern: `/students`)
- **Pages:** 91 (51 unique, 13 link-farm, 24 mixed, 3 broken)
- **Crawl:** Full BFS, max depth 5
- **Hub links:** 133 (1.46/page)

## IA Structure
```
/students
  /undergraduate (BA orientation, enrichment, resources)
  /graduate-coursework (census dates, timetable, enrichment, course management)
  /graduate-research (commencement, FAQs, manage program, plan program)
  /experiential-learning (internships, industry projects, job-ready)
  /career-mentoring
  /employability-in-arts
  /overseas-experience (funding, travel grants)
  /arts-student-advisory-council, /arts-student-ambassadors
```

## Service Model Position
**Well-balanced local hub.** Arts has genuine unique content (experiential learning, career mentoring, overseas travel grants, language placement tests) while appropriately redirecting transactional tasks to the hub. Moderate hub dependency: 133 links to students.unimelb.edu.au.

## Content Profile
- **Heaviest topics:** graduation (66), contacts-support (55), research-candidature (30), careers-employability (25), subjects-timetable (25)
- **Richest pages:** Experiential Learning (1,770w), Milestone Reviews (1,517w), Arts Student Advisory Council (1,489w), Cross-institutional study (1,418w)
- **Unique faculty content:** Experiential learning/internship subjects, Arts Career Mentoring, Faculty overseas travel grants, Language placement tests, Arts Student Ambassadors, Diploma in Languages, Video edit suites

## Structural Issues
- 3 broken pages (academic mentoring profiles, WIL internships page)
- `_nocache` URL variants exposed in graduate research section
- `eStudent%20login` URL with unencoded space — broken
- Significant duplication: Overview of Course Structure appears at 4 different URLs

## Recommendation Notes
- **Keep:** Experiential learning, career mentoring, travel grants, language placement tests, student ambassador program
- **Redirect to hub:** General enrolment/timetable/exams info
- **Fix:** 3 broken pages, 4× duplicate course structure pages, URL encoding issues
- **Good model:** Arts' balance of faculty-specific content + hub-redirect is closest to the recommended hub-and-spoke pattern
