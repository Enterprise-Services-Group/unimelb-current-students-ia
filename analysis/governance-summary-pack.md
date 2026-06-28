# Governance Summary Pack — Stakeholder-Ready Recommendations

*Condensed from 14 deep-dives, ~75 improvements, and 38,331 crawled pages. One page per structural recommendation, ready for COO/Provost briefing. June 2026.*

---

## 1. Finish the Hub Migration

**The problem.** The central student hub (students.unimelb.edu.au) is mid-migration, serving 120 leaf pages under two parallel URL trees. 12 domains link the deprecated trees. MSD has ~8,000 links pointed at legacy paths about to break. The hub is 833 pages, not the "74" the deck asserts.

**The fix.** Pick one canonical root per concept, 301-redirect all 120 legacy leaves, add rel=canonical, update high-fan-in links. Repoint the 12 external domains.

**Impact.** Every student, every journey. This is the prerequisite for everything else. Faculties cannot standardise their hub links until the hub's own URLs are stable.

**Effort.** Medium. No new content — redirects + external link repointing.

**From.** §1.1, Top 12 #1.

---

## 2. Mandate a Thin Student Overlay on Squiz

**The problem.** Every faculty already runs Squiz/Matrix (~11–13 markers/page), but no two share a top-level taxonomy. The student entry is at 5 different URL depths depending on which faculty you land on. Current students are only ~4–7% of faculty estates built for reputation, research, and recruitment.

**The fix.** A thin, consistent student overlay every faculty exposes identically: a fixed `/students` path, a fixed set of section labels, and a fixed "what's here vs what's on students.unimelb" block. No CMS migration — overlay only.

**Impact.** Every faculty, every student. A student moving between faculties sees the same IA. Depends on the hub migration landing first (the overlay must link stable URLs).

**Effort.** Medium. Template change × 12 faculties.

**From.** §1.3, §5.2, Top 12 #3.

---

## 3. Stand Up a Subdomain Registry

**The problem.** 415 distinct `*.unimelb.edu.au` hosts appear in the contextual graph — Fine-Arts cohort-year microsites, single-lab subdomains, 19 single-purpose `*.app` hosts — with no registry tying any host to an owner or retirement date. 28 hosts are linked as both www.X and X, splitting inbound equity.

**The fix.** A registry of every `*.unimelb.edu.au` host: owner, purpose, creation date, planned retirement date. A provisioning gate so no new subdomain appears without registration. A www-vs-bare canonical-host rule with 301 redirects.

**Impact.** Prevents re-fragmentation. The structural fix for the sandbox leakage, stale content, and duplicate-host problems.

**Effort.** Medium (process + config). The registry itself is a spreadsheet → governance process, not a technology build.

**From.** §5.1, §5.4, Top 12 #2.

---

## 4. Bring the Handbook Up to Baseline

**The problem.** The Handbook is the #1 dependency in the estate (7,819 contextual inbound links from 15+ domains). But it's SPA-only with no server-rendered fallback, has blank `<title>` tags on every subject and course page, no "Enrol in this subject" action, and ~1,470 of 2,134 pages are Imperva bot-block shells invisible to search engines.

**The fix.** SSR fallback for every subject/course page. Descriptive `<title>` template. One "Enrol in this subject → my.unimelb" action. Browsable A-Z indexes.

**Impact.** Every student who plans a degree, every search engine, every screen reader, every link preview. 7,819 inbound links currently point at broken pages.

**Effort.** Large. Requires platform work (SSR). Title/action/index changes are template-level (medium).

**From.** §2.2, §5.3, §6.6, §6.7. Handbook deep-dive.

---

## 5. Build the Graduate→Alumni Bridge

**The problem.** 35 completion/conferral pages. 0 alumni links. The graduation-day page links Facebook, Instagram, Twitter, and TikTok — but not alumni.unimelb. Total contextual links estate-wide to any alumni host: ~97.

**The fix.** One "Stay connected — join your alumni network" CTA on all 35 completion pages. Replace social media links on the graduation-day page with alumni. Bridge faculty student-mentoring to alumni mentoring.

**Impact.** Every graduating student. The only purely additive fix in the register — nothing to unpick, nothing to migrate.

**Effort.** Quick-win. Content insertion only.

**From.** §3.1, Top 12 #7. Graduation→Alumni deep-dive.

---

## 6. Wire Careers Online

**The problem.** 1,150 careers pages across 18 domains. Only 115 contextual links reach the careers platforms. 5 faculties send zero. The central hub's own 36-page careers section sends only 32 links to Careers Online.

**The fix.** One "Find jobs & book a careers adviser → Careers Online" CTA on every faculty landing page. Template change × 13 faculties. Target floor of 18 links per faculty (the eng/FBE pattern).

**Impact.** Every student seeking employment. The lifecycle's most cross-cutting service is its least connected.

**Effort.** Medium. Template change.

**From.** §3.2, Top 12 #8. Careers Online Wiring deep-dive.

---

## 7. Collapse the SEDS Fork and Build an Indigenous Hub Presence

**The problem.** The disability registration wizard exists on 1 of 3 equity trees — but 12 domains link students to the 2 without it. Indigenous students have zero pages on the hub. Murrup Barak is on a separate domain. The hub links it 19 times; MSD links it 614.

**The fix.** Canonicalize SEDS to one tree carrying the wizard. Repoint 12 external links. Create one Indigenous-students landing page on the hub. Standardise anchors and resolve the www-twin.

**Impact.** The highest-equity-stakes gap in the estate. Cohorts with the least margin to hunt across systems.

**Effort.** Medium. Redirects + one new page.

**From.** §8b. Equity & Indigenous deep-dive.

---

## 8. Fix the Census-Date Page — Day One

**The problem.** `/course-admin/census-dates` carries `<link rel="canonical" href="/page-not-found">`. The single most financially consequential page in the estate tells search engines it doesn't exist.

**The fix.** Change the canonical tag to the actual page URL. One line.

**Impact.** Every student who needs to know the census date. Withdrawing before vs after census determines whether they pay for the subject.

**Effort.** Quick-win. One-line fix. Should have been done on day one.

**From.** §8a.2. Course Planning & Enrolment deep-dive. Fees & Finance deep-dive.

---

## 9. Fix the 2,038 Identical Scholarship Titles

**The problem.** 94.7% of scholarship pages (2,038/2,151) emit identical `<title>`: "Find a scholarship | University of Melbourne." Every scholarship is indistinguishable in search results, bookmarks, and screen-reader navigation. 96% of pages skip a heading level.

**The fix.** Per-scholarship `<title>` template: "[Name] — [Faculty/Level] Scholarship | University of Melbourne." Fix heading-skip at template layer. One template change touches all 2,138 pages.

**Impact.** The highest-leverage findability + accessibility fix by volume in the entire estate.

**Effort.** Quick-win. Template change only.

**From.** §6.2, Top 12 #9. Scholarships deep-dive.

---

## 10. Fix the Cookiebot Duplicate-Icon Pathology

**The problem.** 4 law staff profile pages are 5MB each — 1,926 identical Cookiebot "opens in new window" arrow icons inlined per page instead of referenced once. mdhs has the same pathology (1,924 copies, 4,730KB).

**The fix.** Configure Cookiebot to use CSS `::after` background for the external-link arrow instead of injecting per-link `<img>` tags. One config change.

**Impact.** Drops 4 law pages from ~5MB to well under 200KB instantly. The cheapest high-impact performance win in the estate.

**Effort.** Quick-win. Cookiebot configuration change.

**From.** §7.2. Mobile & Performance deep-dive.

---

## Summary

| # | Fix | Severity | Effort | Type |
|---|---|---|---|---|
| 1 | Finish hub migration | HIGH | Medium | Structural |
| 2 | Student overlay on Squiz | HIGH | Medium | Structural |
| 3 | Subdomain registry | HIGH | Medium | Governance |
| 4 | Handbook baseline | HIGH | Large | Platform |
| 5 | Graduate→alumni bridge | HIGH | Quick-win | Content |
| 6 | Wire Careers Online | HIGH | Medium | Template |
| 7 | SEDS + Indigenous hub | HIGH | Medium | Content + redirects |
| 8 | Fix census-date canonical | HIGH | Quick-win | One-line |
| 9 | Fix scholarship titles | HIGH | Quick-win | Template |
| 10 | Fix Cookiebot icons | HIGH | Quick-win | Config |
