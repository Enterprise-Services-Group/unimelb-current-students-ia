# FBE + MBS — CS Profile

- **Unit:** Faculty of Business & Economics + Melbourne Business School
- **CS URL:** `fbe.unimelb.edu.au/students` (pattern: `/students`; `/current-students` → 404)
- **Pages:** ~25 estimated across FBE + MBS (root capture)
- **Crawl mode:** Root + MBS subdomain via web_extract
- **⚠️ Separate MBS CS:** `mbs.unimelb.edu.au/students`

## IA Structure
```
fbe.unimelb.edu.au/students (thin gateway — 4 cards)
  /bcom — Bachelor of Commerce CS
  /phd — Graduate Research CS
  /wellbeing — shared wellbeing page
  /services — services and facilities

mbs.unimelb.edu.au/students (MBS graduate CS — separate subdomain)
  /orientation, /course-planning, /wellbeing
mbs.unimelb.edu.au/career (MBS Career Elevation — separate from hub careers)
```

## Service Model Position
**Split CS architecture.** FBE is unique among faculties: it splits students by cohort (BCom → FBE, graduate → MBS) with MBS operating on a completely separate subdomain with its own branding, CS section, and career service. The FBE /students page itself is a thin gateway.

## Content Profile
- **FBE unique:** BCom-specific resources, PhD candidature management, shared wellbeing
- **MBS unique:** Orientation, course planning, Career Elevation (mbs.unimelb.edu.au/career), wellbeing
- **Hub-redirect areas:** Most transactional admin likely links to hub
- **Duplication:** MBS Career Elevation runs parallel to central Careers hub — no cross-linking observed

## Structural Issues
- `/current-students` → 404 (Phase 1 probe detected this link but it's dead)
- MBS operates as a quasi-independent entity under the FBE umbrella — students in MBS programs have a completely different CS experience than BCom students
- MBS career services are fully separate from both FBE and central hub careers
- No apparent cross-linking between FBE BCom and MBS graduate CS

## Recommendation Notes
- **Consolidate:** MBS CS section should follow the standardised faculty template
- **Cross-link:** MBS Career Elevation must link to central Careers hub, and vice versa
- **Fix:** Redirect `/current-students` → `/students`
- **Gateway improvement:** The FBE /students page should include explicit "Where to go" guidance for each cohort
- **Consider:** Whether MBS needs a separate CS section at all, or whether it should be a section within a unified FBE CS page
