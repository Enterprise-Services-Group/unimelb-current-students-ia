# Quick Wins Checklist

*Actionable one-line fixes from the improvements register. No analysis needed — ready to execute. Each item has the register reference, the fix, and the impact. June 2026.*

---

## Immediate (do today)

| # | Fix | Register § | Impact |
|---|---|---|---|
| Q1 | Fix census-dates canonical: change `<link rel="canonical" href="/page-not-found">` to actual page URL | 8a.2 | One line. Highest financial-stakes page fixed. |
| Q2 | Unpublish /sandbox/2026-uplifts/student-visas/ and /sandbox/content-models/ | 9.1, 8b.2 | 90 real inbound links to draft visa content removed. |
| Q3 | Unpublish / 301 the 2025 English language requirements page | Discover (international) | No applicant applies against superseded IELTS thresholds. |
| Q4 | Configure Cookiebot to use CSS `::after` instead of per-link `<img>` for external-link arrow | 7.2 | 4 law pages drop from 5MB to <200KB instantly. |
| Q5 | Remove `user-scalable=no` + `maximum-scale=1` from medicine template | 7.6 | One line. WCAG mobile-accessibility fix. |

---

## Template (one change, thousands of pages)

| # | Fix | Register § | Impact |
|---|---|---|---|
| Q6 | Give each scholarship detail page its own `<title>`: "[Name] — Scholarship \| UoM" | 6.2 | 2,038 pages fixed. One template change. |
| Q7 | Fix scholarship template heading-skip: insert `<h2>` between h1 and h3 | 6.1 | 2,065 pages fixed. One template change. |
| Q8 | Add "Stay connected — join your alumni network" CTA to all 35 completion/conferral pages | 3.1 | 35 pages, one CTA. Zero migration cost. |
| Q9 | Add "Enrol in this subject → my.unimelb" action to every Handbook subject page | 6.7 | Thousands of subject pages. One template change. |
| Q10 | Replace graduation-day page social media links (FB/IG/Twitter/TikTok) with alumni.unimelb | 3.1 | One page. Highest-traffic completion moment. |

---

## Redirects (fix link-breaks in bulk)

| # | Fix | Register § | Impact |
|---|---|---|---|
| Q11 | 301-redirect the 33 byte-identical HDR candidature pairs (education+mdhs) to gradresearch.unimelb | 4.1, 9b.1 | 33 pages deduplicated. Canonical owner exists. |
| Q12 | 301-redirect the 46 BCom careers duplicates (MBS→fbe) scoring Jaccard ≥0.85 | 4.2, 9b.2 | 46 pages deduplicated. Includes 35 cross-branded FBE URLs on MBS. |
| Q13 | 301-redirect /find-an-overseas-representative to /authorised-education-agent (byte-identical) | Discover (international) | One compliance-critical page, one URL. |
| Q14 | Resolve the 28 www-vs-bare duplicate hosts; set canonical-host rule | 5.4 | Fixes murrupbarak/www.murrupbarak, alumni/www.alumni, and 26 others. |
| Q15 | 301-redirect all /sandbox/ inbound links to canonical destinations | 9.1, 8b.2 | Don't break the 90 links editors already created. |

---

## Labels & metadata (fix findability)

| # | Fix | Register § | Impact |
|---|---|---|---|
| Q16 | Label the three fee-remission SID form links in plain language: "Waiver" / "Review" / "Enquiry" | 8a.6 | 143 instances of form 4747166. |
| Q17 | Fix financial-aid page title from "Support and wellbeing" to "Financial aid and emergency support" | 8a.2 | One page. Students can find it. |
| Q18 | Strip _nocache query-string variants from internal links (15 known instances) | 9.1 | 15 pages fixed. |
| Q19 | Add rel=canonical to all 120 dual-served hub leaves | 1.1 | Prerequisite for the full migration. Can be done today. |
| Q20 | Add "Already enrolled? Go to students.unimelb" to every study.unimelb fee page | 8a.4 | Stops the reverse-funnel. Template change. |

---

## Accessibility (quick template fixes)

| # | Fix | Register § | Impact |
|---|---|---|---|
| Q21 | Add alt text in the Funnelback/Squiz search-result card template | 6.4 | One template. All search results across all Squiz domains. |
| Q22 | Replace generic "Show more" / "Find out more" link text across templates | 6.8 | Multiple templates. |
| Q23 | Add `rel="noopener"` and visible "opens in new window" cue to external links | 6.5 | Template-level. |
| Q24 | Fix the analytics privacy-consent radios: uncomment `<label>`, fix `{{opt_in}}` rendering | 6.9 | One template. GDPR/privacy compliance. |

---

## Link hygiene (prevent breakage)

| # | Fix | Register § | Impact |
|---|---|---|---|
| Q25 | Fix the `?a=` query-string artifact manufacturing ~3,359 phantom 404s on live pages | 2.3 | 3,359 dead-appearing links resolved. |
| Q26 | Sweep the ~414 genuinely-dead destinations (957 links) after the `?a=` fix | 2.4 | Post-Q25 cleanup. |
| Q27 | Fix malformed double-hash in-page anchors on the agent page (`##navigation-find-an-agent`) | Discover (international) | One page. Agent page section links work. |
| Q28 | Repoint the 1,648 old Stop 1 links to the new canonical path | 1.1 | Largest single fan-in fix. |

---

## Implementation notes

- **Items Q1–Q5** can be done today. No dependencies. No stakeholder approvals needed for bug fixes.
- **Items Q6–Q10** are template changes. One CMS edit touches thousands of pages. Highest leverage.
- **Items Q11–Q15** are redirects. Require server/config access. Test before deploying.
- **Items Q16–Q20** are label/metadata changes. Content edits, not structural.
- **Items Q21–Q24** are accessibility fixes. Low effort, high compliance value.
- **Items Q25–Q28** are link hygiene. Q25 must be done before Q26 (the `?a=` artifact inflates the dead-link count).

All items are documented with full evidence citations in the improvements register (`analysis/improvements-register.md`).
