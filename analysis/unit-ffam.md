# FFAM — CS Profile

- **Unit:** Faculty of Fine Arts & Music (VCA + MCM)
- **CS URL:** `finearts-music.unimelb.edu.au/current-students` (pattern: `/current-students`)
- **Pages:** ~30-50 estimated (root capture only)
- **Crawl mode:** Root capture via web_extract

## IA Structure
```
/current-students (thin hub — 8 sections)
  Starting out
  Room Bookings and Timetables
  Facilities and Amenities
  Student Experience
  Ensembles
  Forms
  Exams and Assessment
  Information for research students
```

## Service Model Position
**Most self-contained; least hub-dependent of all faculties.** FFAM operates almost entirely outside the central hub framework. The root page does not push students to Stop 1 or students.unimelb.edu.au — its fallback is "Check out our FAQs or search ask.unimelb." The conservatorium/art-school model (ensembles, practice rooms, performances, studio practice, exhibitions) doesn't map to the hub's service taxonomy.

## Content Profile
- **Thinnest root page:** ~100 words of unique content — essentially a jump-off menu
- **Unique faculty content (inferred from section labels):** Ensemble registration and management, Practice room booking, Performance timetables and examinations, VCA/MCM-specific forms, Studio/workshop facilities, Professional development for artists/musicians
- **Hub links:** Very few — FFAM does not redirect to the central hub for any services
- **Fallback:** "Can't find what you are looking for? Check FAQs or search ask.unimelb" — not "Go to students.unimelb.edu.au"

## Structural Issues
- Root page is too thin — no substantive content, just 8 labelled links
- No "Where to go" guidance at all
- URL pattern `/current-students` differs from the `/students` convention
- Sub-units (VCA, MCM, Wilin Centre) are path-based and don't have separate CS sections — this is actually good

## Recommendation Notes
- **Keep:** Ensembles, practice rooms, performance timetables, VCA/MCM forms, studio facilities — these are genuinely unique and cannot be centralized
- **Add:** "Where to go" sidebar that links to hub for health, counselling, careers, academic skills
- **Strengthen root page:** Add real content instead of just 8 link labels
- **Standardise URL:** Redirect `/current-students` → `/students`
- **FFAM is the strongest case for faculty autonomy** — its conservatorium model is fundamentally different from other faculties. The hub-and-spoke model should preserve this autonomy while adding cross-links.
