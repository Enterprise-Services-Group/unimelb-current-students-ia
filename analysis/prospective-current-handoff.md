# Prospective → Current Student Handoff — Deep-Dive

*The seam every student crosses exactly once — from applicant to enrolled student. 373 contextual links from study.unimelb to students.unimelb. 19 domains link the hub. But the most important transition in the lifecycle rides on fewer links than MSD sends to the hub from a single faculty. June 2026.*

---

## Executive summary

The prospective→current handoff is the transition every student makes: from course discovery on study.unimelb.edu.au to the enrolled-student hub at students.unimelb.edu.au. It is the single most important seam in the lifecycle — get it wrong and a new student starts lost. Yet it rides on **373 contextual links** — fewer than the 8,069 links MSD alone sends to the hub, and barely more than the 396 links the hub sends to a legacy FAQ.

The handoff works for one cohort: domestic VTAC undergraduates, who receive a guided "Get Started at Melbourne" sequence. For everyone else — international postgraduates, HDR candidates, online learners, non-award students — the seam is a cold link buried in an offer email or a my.unimelb notification. The public estate doesn't own this transition; it outsources it to the authenticated SIS.

The fix: a bidirectional, intentional handoff from every applicant-facing page to the enrolled-student equivalent, and a consistent "Already enrolled? Go here" bridge in the other direction.

---

## The seam by the numbers

| Metric | Value |
|---|---|
| Contextual links study→hub | 373 |
| Total hub inbound (all domains) | 11,186 |
| MSD→hub (comparison) | 8,069 |
| Handbook→hub | 1,193 |
| Hub→study (reverse) | 125 |
| Domains linking the hub | 19 |
| Domains sending <100 links to hub | 9 (law 99, science 64, finearts 63, medicine 21, mbs 26, www 24, scholarships 16, dental 6, research 30) |

---

## Who links the hub — and who doesn't

| Source | Contextual links | Verdict |
|---|---|---|
| msd.unimelb.edu.au | **8,069** | ⚠ All on deprecated paths — link-break risk |
| handbook.unimelb.edu.au | 1,193 | ✅ Strong — course structure → student hub |
| study.unimelb.edu.au | **373** | ⚠ The prospective→current seam — thin |
| education.unimelb.edu.au | 275 | ⚠ Below floor |
| eng.unimelb.edu.au | 224 | ⚠ Below floor |
| arts.unimelb.edu.au | 191 | ⚠ Below floor |
| mdhs.unimelb.edu.au | 175 | ⚠ Below floor |
| fbe.unimelb.edu.au | 131 | ⚠ Below floor |
| biomedicalsciences.unimelb.edu.au | 130 | ⚠ Below floor |
| law.unimelb.edu.au | 99 | ❌ Below 100 |
| science.unimelb.edu.au | 64 | ❌ Near-zero |
| finearts-music.unimelb.edu.au | 63 | ❌ Near-zero |
| medicine.unimelb.edu.au | 21 | ❌ Near-zero |
| mbs.unimelb.edu.au | 26 | ❌ Near-zero |
| dental.unimelb.edu.au | 6 | ❌ Effectively zero |
| research.unimelb.edu.au | 30 | ❌ Research→student seam broken |
| scholarships.unimelb.edu.au | 16 | ❌ Hub barely reaches scholarships |
| services.unimelb.edu.au | 76 | ⚠ Service pages should route to hub |
| www.unimelb.edu.au | 24 | ❌ Corporate site barely links student hub |

**9 of 19 domains send fewer than 100 contextual links to the student hub.** The University's own corporate site (www.unimelb.edu.au) sends 24. The scholarships catalogue — a core student service — sends 16. Dental sends 6.

---

## The study→hub seam: what the 373 links actually are

The 373 contextual links from study.unimelb to students.unimelb are the sum of every in-content reference from the applicant-facing site to the enrolled-student hub. They are not a single "You're in — here's next" bridge. They're scattered across:

- Per-course "How to apply" pages (the dominant entry path)
- International student pages (visa, CoE, OSHC guidance)
- "Get Started at Melbourne" pages (domestic VTAC UG only)
- General "current students" footer/nav links (stripped as chrome)
- Offer-acceptance pages

The 373 figure is the total after stripping navigation chrome — genuine in-content links. But they're not concentrated at the transition point. A student who has just accepted an offer is not met with a prominent "Now go here → students.unimelb" CTA; they're expected to already know the hub exists.

---

## The reverse seam: hub→study

The hub sends only 125 contextual links back to study.unimelb. These are mostly "how to apply" references for prospective students who've landed on the enrolled hub by mistake. The reverse handoff is:
- Not a consistent "Already enrolled? Go here" bridge from study pages
- Not a persistent "Not enrolled yet? Find your course" bridge from hub pages
- Not bidirectional — a student who lands on the wrong side has no clear path to the right one

---

## Which cohorts get a guided handoff?

| Cohort | Handoff experience | Verdict |
|---|---|---|
| Domestic VTAC undergraduate | "Get Started at Melbourne" sequence — guided | ✅ Good |
| International postgraduate | Offer email → my.unimelb → find hub yourself | ❌ Cold |
| HDR candidate | Faculty/gradresearch → my.unimelb → find hub yourself | ❌ Cold |
| Online / micro-credential | study-with-us → Canvas → no hub at all | ❌ Orphaned |
| Non-award / single subject | study-with-us → enrol → no hub home | ❌ Orphaned |
| Domestic graduate coursework | VTAC/direct → my.unimelb → find hub yourself | ❌ Cold |

Only one cohort gets a guided handoff. The majority of commencing students are expected to discover the hub on their own.

---

## The authenticated core dependency

The my.unimelb SIS (187 links from the hub) sits between the two public estates. The offer→accept→enrol flow happens in my.unimelb behind login. The public study.unimelb and students.unimelb can only describe what happens inside it. This means:

- The handoff is invisible to link-graph analysis — it happens in emails, offer letters, and portal notifications
- The public estate can't confirm the handoff works
- The authenticated flow may already be excellent — we can't see it
- But the public bridges (study→hub, hub→study) should still be bidirectional and intentional regardless

---

## Recommendations

### 1. Add a prominent "Now go here → students.unimelb" CTA to every offer-acceptance page on study.unimelb `[HIGH · quick-win]`
One template change. Every student who accepts an offer should be handed to the hub with a clear, consistent "You're in — here's your next step" bridge.

### 2. Build "Already enrolled?" and "Not enrolled yet?" bidirectional bridges `[MEDIUM · medium]`
Every study.unimelb page that serves enrolled students (fees, census, enrol) should carry "Already enrolled? Go to students.unimelb." Every students.unimelb page should carry "Not enrolled yet? Find your course on study.unimelb." Persistent, consistent, template-level.

### 3. Give every commencing cohort a guided "Get Started" sequence `[MEDIUM · medium]`
The domestic VTAC UG sequence works. Replicate it for international postgraduates, HDR candidates, graduate coursework, and online learners. One sequence per audience, linked from the offer-acceptance page.

### 4. Lift faculty→hub links to a floor of 200 per faculty `[MEDIUM · medium]`
9 faculties send fewer than 200 links to the hub. The eng/FBE pattern (~200-275) is proven — replicate it everywhere. Ensure links point to the canonical hub paths, not deprecated trees.

---

## Linked improvements from the register

| § | Improvement | Severity · Effort |
|---|---|---|
| 3.7 | Make the prospective↔current handoff bidirectional and intentional at apply→enrol | MEDIUM · medium |
| 3.4 | Replicate the MSD central-hub model — 12 faculties under-route students | MEDIUM · large |
| 1.2 | One URL convention for the current-students entry — top-level `/students` | HIGH · medium |

---

*Built from: cross-site-flow.csv (study→hub 373 links, full hub inbound audit, hub outbound audit), lifecycle-journeys.md (seam map), and improvements-register.md (§3.7, §3.4). June 2026.*
