#!/usr/bin/env python3
"""Course planning & enrolment — deep-dive. The operational core of the
current-student experience, traced across its toolchain and the hub's parallel
trees. Composed from the deep evidence cut over the link graph + page HTML.
Run: python3 analysis/improvements/build_enrolment.py
"""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]

TOOLCHAIN = [
 {"system": "Hub guidance", "where": "students.unimelb · /course-admin + /your-course", "count": "313 pages", "wall": False,
  "role": "The advice on how to plan and enrol — but split across two parallel URL trees (212 + 101)."},
 {"system": "My Course Planner", "where": "studyos.students.unimelb (StudyOS)", "count": "~54 links · on ~830 pages", "wall": True,
  "role": "The subject-planning tool — on a separate subdomain, off the hub. A second study plan also lives in my.unimelb."},
 {"system": "The Handbook", "where": "handbook.unimelb", "count": "195 links", "wall": False,
  "role": "Course/subject structure, prerequisites, points — a different platform and visual standard."},
 {"system": "ask.unimelb FAQ", "where": "ask.unimelb (legacy KB)", "count": "396 links", "wall": False,
  "role": "Where the actual answers live (study load, census, HECS, prerequisites, unsatisfactory progress) — a legacy FAQ with mixed URL formats."},
 {"system": "my.unimelb (the SIS)", "where": "my.unimelb · /sone/STUDYPLN", "count": "187 links", "wall": True,
  "role": "The enrolment ACTION — enrol, study plan, vary — behind login. The hub describes it; my.unimelb does it."},
 {"system": "MyTimetable", "where": "mytimetable.students.unimelb", "count": "on 84 pages", "wall": True,
  "role": "Class timetabling / registration — yet another subdomain, behind its own login."},
 {"system": "Variation forms", "where": "forms.your + *.app.unimelb", "count": "161 links", "wall": True,
  "role": "Overload, leave of absence, withdrawal, advanced standing — each a different form on a different host."},
]

F = [
 {"title": "Planning and enrolling is a seven-system obstacle course", "severity": "high",
  "evidence": "To plan a course and enrol, a student crosses up to seven systems/platforms: the hub guidance (two parallel trees), My Course Planner (StudyOS, a separate subdomain), the Handbook (course structure), the ask.unimelb FAQ (the actual answers), my.unimelb (the enrolment action, behind login), MyTimetable (another subdomain), and the *.app variation forms. Course planning + enrolment is 343 of the hub's 833 pages (41%) — the operational core of the estate — and it is the most fragmented single task in it.",
  "recommendation": "Define ONE course-planning & enrolment home that unifies the toolchain — embed or consistently deep-link My Course Planner, the Handbook structure, MyTimetable and the my.unimelb action from one canonical guidance tree, so the student never has to assemble the journey themselves."},
 {"title": "The hub's own enrolment guidance is duplicated across two parallel trees", "severity": "high",
  "evidence": "students.unimelb serves the same guidance under /course-admin (212 pages, canonical) AND legacy /your-course (101 pages), with 19 core leaves duplicated byte-near — planning-your-course-and-subjects, study-load/overloading, study-periods, how-to-plan-your-course, subjects, class-timetable, key-dates, census. The legacy tree carries rel=canonical yet stays live and internally linked, so the most important operational content competes with itself.",
  "recommendation": "Finish the migration: keep /course-admin as the single tree, 301-redirect all 19 duplicated /your-course leaves, and add a no-live-inbound-on-two-trees check. This is the #1 enrolment fix and a prerequisite for everything else."},
 {"title": "My Course Planner is off the hub — and there are two planning surfaces", "severity": "high",
  "evidence": "'My Course Planner' is referenced on ~830 hub pages but the tool itself lives on a separate subdomain, studyos.students.unimelb.edu.au (StudyOS, ~54 links). A SECOND study-plan surface exists inside my.unimelb at /sone/STUDYPLN. So the single most important planning task points at two different tools on two different platforms, both off the guidance hub.",
  "recommendation": "Pick one canonical planning tool (or clearly delineate StudyOS-plan vs my.unimelb-plan), embed/deep-link it consistently from the planning guidance, and stop referencing 'My Course Planner' generically without a single resolved destination."},
 {"title": "The enrolment action is behind login; the public estate only describes it", "severity": "high",
  "evidence": "The 343 enrolment pages carry 187 links to my.unimelb.edu.au — the SIS where enrolment, study-plan and variations actually happen, behind login. The public hub is an instruction manual for a system it can't show; the find→act seam (read how → go do it in my.unimelb) is never closed on-site and is unverifiable from the outside.",
  "recommendation": "Map the public→authenticated seam per enrolment task and surface the my.unimelb action prominently and consistently (a single 'Enrol / manage in my.unimelb' control), and confirm the logged-in side guides the task the public page describes."},
 {"title": "The answers are outsourced to a legacy FAQ knowledge base", "severity": "high",
  "evidence": "The enrolment pages carry 396 links to ask.unimelb.edu.au — a legacy FAQ KB — across dozens of distinct a_id articles (study load, part-time, census, HECS-HELP, prerequisites, unsatisfactory progress, 'at risk', advanced standing, Commonwealth Supported Place, Statement of Liability), in TWO inconsistent URL formats (/app/answers/detail/a_id/#### and /faq/####). The hub page describes the topic; the actual answer is one hop away on a system at a different standard.",
  "recommendation": "Migrate the high-traffic enrolment answers off the legacy FAQ into the maintained hub pages (or embed them), and standardise/redirect the two ask.unimelb URL formats — stop describing-then-deferring on the operational core."},
 {"title": "Census dates and key dates — the highest-stakes content — are duplicated and mis-canonicalised", "severity": "high",
  "evidence": "Census dates and key dates appear under both hub trees (/course-admin/census-dates, /course-admin/key-dates AND /your-course/.../key-dates), and the census-dates page canonicalises to /page-not-found — the single most financially consequential date page tells search engines it does not exist. Census answers are also among the ask.unimelb FAQ deferrals.",
  "recommendation": "Make one canonical census/key-dates page, fix its canonical tag, and put the date + the fee/academic consequence + the my.unimelb withdraw action on it."},
 {"title": "Timetabling is yet another subdomain and login", "severity": "medium",
  "evidence": "Class timetabling runs on mytimetable.students.unimelb.edu.au — a separate subdomain behind its own login ('MyTimetable login') — referenced on 84 hub pages and reached via /course-admin/class-timetable (13 pages, itself duplicated under /your-course).",
  "recommendation": "Deep-link MyTimetable consistently from one canonical class-timetable page and collapse the duplicate timetable guidance trees."},
 {"title": "Course structure lives on the Handbook — a platform switch mid-plan", "severity": "medium",
  "evidence": "Planning which subjects to take requires the Handbook (195 links from the enrolment pages) — a different platform, visual standard and academic register. A student planning their enrolment bounces between the hub guidance, the Handbook structure, and the planner tool to assemble one decision.",
  "recommendation": "Surface the Handbook course-structure (subject list, prerequisites) inside the planning guidance / planner, reserving the deep Handbook link for full reference."},
 {"title": "Enrolment variations are scattered across forms and microsites", "severity": "medium",
  "evidence": "Overloading, leave of absence, intermission, withdrawal, course transfer and advanced standing each route to a different destination — forms.your.unimelb, *.app.unimelb microsites, and study.unimelb (advanced-standing application) — 161 form/app links from the enrolment pages, with no single 'change my enrolment' hub.",
  "recommendation": "Aggregate the variation actions behind one 'Change your enrolment' page that routes to the right form, with consistent naming."},
 {"title": "Faculties re-host the planning content", "severity": "medium",
  "evidence": "71 faculty course-planning pages (biomedical 32, MSD 24, arts 7, eng/law 3) parallel the central guidance — sample course plans and degree maps maintained per faculty rather than linking the centre, the same multi-owner pattern seen across the estate.",
  "recommendation": "Keep genuinely degree-specific sample plans with faculties but link the central how-to-plan/enrol guidance rather than re-hosting it; one canonical planning method."},
]

EXEC = """# Course Planning & Enrolment — Deep-Dive

*The operational core of the current-student experience — how a student plans their degree and enrols in subjects — traced exhaustively across its toolchain, the Handbook, the authenticated SIS, and the hub's mid-migration parallel trees. Course planning + enrolment is 343 of the central hub's 833 pages (41%); this is how that core is assembled. June 2026.*

---

## Executive summary

Everything else in the estate is downstream of this: if a student cannot plan their course and enrol, nothing else matters. It is also, by some distance, the **most fragmented single task in the estate**. To plan a degree and enrol in subjects, a student must cross **up to seven distinct systems and platforms** — the hub's guidance (itself split across two parallel URL trees), *My Course Planner* (on a separate StudyOS subdomain, with a *second* study-plan surface inside my.unimelb), the *Handbook* (course structure, a different platform), the legacy *ask.unimelb* FAQ (where the actual answers live, in two inconsistent URL formats), *my.unimelb* (the enrolment action itself, behind login), *MyTimetable* (another subdomain), and a scatter of *forms and `*.app` microsites* for every enrolment variation. No single page assembles this; the student assembles it themselves, under deadline, often for the first time.

The pattern is the estate's worst faults concentrated on its most important task: **the guidance describes but does not transact** (187 links out to the walled my.unimelb, 396 to a legacy FAQ for the real answers); **the hub competes with itself** (19 core leaves duplicated across `/course-admin` and `/your-course` mid-migration); and **the highest-stakes page is broken** (census-dates canonicalises to `/page-not-found`). The fix is correspondingly high-leverage: finish the migration to one tree, unify the toolchain behind one canonical planning-and-enrolment home, bring the answers back from the legacy FAQ, and make the my.unimelb action one prominent, consistent control. Get this right and the operational spine the whole lifecycle hangs on finally holds.
"""

def fmt(f):
    return (f"### {f['title']}  `[{f['severity'].upper()}]`\n\n"
            f"**Evidence.** {f['evidence']}\n\n**Recommendation.** {f['recommendation']}")

TOOL_MD = ("## The toolchain a student must traverse\n\n"
           "| System | Where | Role | Links from the hub |\n|---|---|---|--:|\n"
           + "\n".join(f"| {t['system']}{' 🔒' if t['wall'] else ''} | `{t['where']}` | {t['role']} | {t['count']} |" for t in TOOLCHAIN)
           + "\n\n🔒 = behind login or a separate platform. One task, seven systems — the student does the integration the estate does not.")

doc = "\n\n".join([EXEC, TOOL_MD, "## The findings\n"] + [fmt(f) for f in F]
                  + ["\n---\n\n*Source: deep link-graph cut over `crawl/students-full/` (the 343 enrolment/course-admin pages' links.json + page HTML), the enrolment service profile in `analysis/student-services-profiles.json`, and the improvements register. My Course Planner (StudyOS), my.unimelb, MyTimetable and the *.app forms are behind login / off the crawled estate — inferred from outbound links and on-page references.*"])

(ROOT / 'analysis/course-planning-enrolment.md').write_text(doc)
open(ROOT / 'report/research-report/enrolment.js', 'w').write(
    'window.ENROLMENT=' + json.dumps({'toolchain': TOOLCHAIN, 'findings': F}, ensure_ascii=False) + ';\n')
print(f"wrote analysis/course-planning-enrolment.md ({len(doc):,} chars) + enrolment.js ({len(F)} findings, {len(TOOLCHAIN)} systems)")
