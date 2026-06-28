# online.unimelb.edu.au — Crawl Analysis

*The online learning portal — 87 pages. 45 pages are RFI (Request for Information) forms. The rest is marketing for online courses. Confirms the lifecycle deep-dive: online learners are courted by marketing but have no current-student home. June 2026.*

---

## What we found

The lifecycle deep-dive identified online/micro-credential learners as an orphaned cohort — courted by study.unimelb/study-with-us but with no current-student home once enrolled. The online.unimelb.edu.au crawl confirms this: the site is a **prospective marketing funnel, not a current-learner portal.**

### Structure

| Section | Pages | Content |
|---|---|---|
| `/form/rfi-form-modal` | **45** | Request for Information forms — 52% of the site |
| `/news/category` | 5 | News categories |
| `/news` | 4 | News listing |
| `/online-courses/` | ~13 | Course pages: Master of HRM, Grad Cert HRM, Master of Education, Master of Public Health, etc. |
| `/` | 1 | Homepage |
| `/contact` | 1 | Contact page |

**52% of the site is lead-capture forms.** The remaining content is course marketing pages and news. There is no current-student section, no learning portal, no "already enrolled" path.

### Content profile

- 45 RFI forms — all identical template, different courses
- 5 Graduate Certificate pages
- 2 Master's pages
- Topics: "Online learning experience," "How to become..." — marketing, not service
- "Resources" section — but these are prospective resources (how online learning works), not enrolled-student resources

### Link analysis

| Outbound destination | Links in 30-page sample | Role |
|---|---|---|
| www.unimelb.edu.au | 90 | Heavy chrome |
| study.unimelb.edu.au | 33 | Strong connection to the prospective estate |
| policy.unimelb.edu.au | 1 | Minimal |
| about.unimelb.edu.au | 1 | Minimal |
| students.unimelb.edu.au | **1** | Near-zero connection to the student hub |

The site is tightly coupled to study.unimelb (33 links) but sends **exactly 1 link to students.unimelb.** Once a student enrols, the marketing funnel drops them — there's no path to the enrolled-student experience.

### Page weight

Median 199KB — moderate. Consistent template (182-344KB range). Lighter than the study.unimelb course pages (304KB median).

---

## What this means

### 1. The orphaned cohort gap is confirmed

The lifecycle deep-dive said online learners have no current-student home. The crawl confirms: online.unimelb.edu.au is a marketing site that hands off to study.unimelb and Canvas, with **zero current-student infrastructure.** The "already enrolled" student is invisible to this site.

### 2. 52% of the site is lead capture

45 RFI forms dominate the crawl. This is a recruitment engine, not a service portal. The site's purpose is to convert prospects, not support enrolled learners.

### 3. The Canvas handoff is invisible

online.unimelb.edu.au does not link to lms.unimelb.edu.au or canvas.lms.unimelb.edu.au. The journey from "enrol in an online course" to "start learning in Canvas" has no public bridge. This is the same find→act gap that defines the rest of the estate.

### 4. The opportunity: a current-learner overlay

The fix recommended in the lifecycle deep-dive — give online learners a defined current-learner home — could live here or on students.unimelb. Either way, the gap between "you're enrolled" and "here's how to study" needs a bridge.

---

## Recommendations

1. **Add an "Already enrolled? Access your course →" bridge.** On every course page and the homepage, link to students.unimelb (or directly to Canvas/LMS). Stop dropping students after enrolment.

2. **Create an "Online learner" section on students.unimelb.** The hub is built for award-course students. Online/micro-credential learners need a home there — or a dedicated section on online.unimelb with current-student content.

3. **Wire the RFI forms to the current experience.** When a prospect submits an RFI, the confirmation page should include "If you enrol, here's what your learning experience looks like" — bridging the marketing→reality gap.

---

*Built from: online crawl (87 pages), links.json sampling (30 pages), index.json structural analysis, lifecycle-journeys.md deep-dive. June 2026.*
