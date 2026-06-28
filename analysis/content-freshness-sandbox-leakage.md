# Content Freshness & Sandbox Leakage — Deep-Dive

*Draft content is live, indexed, and accumulating production inbound links. A published sandbox carries 19,000+ chars of real visa/CoE/OSHC text with 90 real inbound links. A 2025 English requirements page is still live in 2026. _nocache variants leak into the link graph. There is no content ownership registry. June 2026.*

---

## Executive summary

The University's web estate has no mechanism to prevent draft, staging, or stale content from being published, indexed, and linked from production pages. Three acute failures define the gap:

1. **A live /sandbox/2026-uplifts/student-visas draft tree** — 812KB, 19,000+ chars of real immigration-critical content, accumulating **90 real inbound links** from production pages. One URL resolves to a UoM Sign-In wall — confirming it's a live staging surface, not a content model.

2. **Year-stamped stale content** — a "2025 English language requirements" page still live and linked from the 2026 hub. An applicant can apply against superseded IELTS thresholds.

3. **_nocache URL variants leaking into the link graph** — 15 production pages link to _nocache versions of fee/eligibility pages.

Underneath all three: **there is no content ownership registry.** No one knows who owns which page, when it should be reviewed, or when it should be retired. The estate silently degrades because nobody is watching.

---

## The sandbox leakage

### What's live

The freshness-signals.csv crawl found **13 students.unimelb /sandbox URLs**. 12 are under `/sandbox/2026-uplifts/student-visas/`. These are not empty stubs — the page.html for `/sandbox/2026-uplifts/student-visas/support-with-student-visas` is **812,250 bytes with 19,493 characters of real visible text** covering:

- Overseas Student Health Cover (OSHC)
- Confirmation of Enrolment (CoE)
- Study load requirements
- Department of Home Affairs links
- Visa renewal information
- Working on a student visa

This is a fully-authored, publication-ready page on the single most immigration-critical topic in the estate — and it's served from a `/sandbox/` URL.

### What links to it

**90 real inbound links** from production students.unimelb pages point to sandbox URLs:

| Sandbox destination | Inbound links | Anchor text |
|---|---|---|
| .../arrange-your-overseas-student-health-cover-oshc | 8 | Correct anchor text from students.unimelb itself |
| Other visa/CoE/OSHC sandbox pages | 82 | Various |

Editors are already linking to staging content. The sandbox is functioning as a parallel production tree for visa/immigration content — without any of the governance, redirects, or canonical tags that protect the rest of the estate.

### The Sign-In wall

One sandbox URL (`.../renew-your-student-visa/_nocache`) resolves to a **"University of Melbourne - Sign In"** wall — confirming this is a live staging surface connected to the University's authentication system, not a static content model.

### The SEDS sandbox

A parallel `/sandbox/content-models/student-equity-and-disability-services` tree also leaks — its SEDS-privacy page has **10 inbound links** from production pages. The equity/disability service, already forked across three production trees, now has a fourth: a sandbox draft accumulating real traffic.

---

## Stale content: 2025 in 2026

### English language requirements

A "2025 English language requirements" page is still live on study.unimelb as of June 2026. It is **still linked from the current 2026 hub** (verified in links.json). The page mentions "2025" 6 times and "2026" only once. It carries 3,441 words of real content — IELTS thresholds, country equivalency tables, test provider links.

An international applicant can land on this page and apply against **superseded IELTS thresholds**. A 0.5-band miss means no offer and no visa. This is a direct immigration-compliance risk from stale content.

### _nocache URL leakage

15 pages across students.unimelb link to _nocache versions of fee, eligibility, and HELP-loan pages. These are cache-bust artifacts — URL variants that bypass the CDN. They leak into the link graph because editors linked the _nocache URL instead of the canonical one. A student who bookmarks a _nocache URL gets a URL that:
- May break when the CDN configuration changes
- Creates duplicate analytics entries
- Splits link equity across two URLs

---

## No content ownership registry

Underneath all three failures is the same governance gap: **there is no content ownership registry.** No system tracks:

- Who owns each page
- When it was last reviewed
- When it should next be reviewed
- Whether it's live, draft, or deprecated
- What its retirement date is

The 415 distinct `*.unimelb.edu.au` hosts in the contextual graph have no owner register. The 19 single-purpose transaction `*.app` hosts have no retirement date. The sandbox trees have no publication gate. The 2025 English page has no expiry flag. The _nocache variants have no redirect.

The estate cannot self-govern because it doesn't know what it contains.

---

## Recommendations

### 1. Unpublish all /sandbox/ content — immediately `[HIGH · quick-win]`
Take down `/sandbox/2026-uplifts/student-visas/` and `/sandbox/content-models/student-equity-and-disability-services/`. If the content is ready for production, publish it to the canonical URL tree with proper redirects. If it's not ready, remove it from the public web. A live published draft on immigration-critical content is a compliance hazard.

### 2. Redirect all sandbox inbound links to canonical destinations `[HIGH · quick-win]`
The 90 real inbound links to sandbox visa pages need 301-redirects to the canonical `/support-and-wellbeing/international-student-support/visas/` tree. Don't break the links editors already created — redirect them.

### 3. Unpublish / 301 the 2025 English requirements page `[HIGH · quick-win]`
Remove the 2025 page and redirect its inbound links to the current 2026 English requirements page. Never expose year-forked eligibility thresholds.

### 4. Add a publication gate: no /sandbox/ content accessible without authentication `[MEDIUM · medium]`
Sandbox/staging environments should require login. Public sandbox URLs should 404 or redirect. This is a server-config change, not a content change.

### 5. Strip _nocache query strings from internal links `[MEDIUM · quick-win]`
Audit and fix the 15 known _nocache inbound links. Add a CMS guard that prevents editors from linking to _nocache URLs.

### 6. Stand up a content ownership registry `[MEDIUM · medium]`
Every published page needs: owner, last-review date, next-review date, and status (live/draft/deprecated). Every subdomain needs a registered owner and a retirement date. This is the structural fix that prevents all three failures from recurring.

---

## Linked improvements from the register

| § | Improvement | Severity · Effort |
|---|---|---|
| 9.1 | Draft / sandbox content is live and indexed in production | HIGH · quick-win |
| 8b.2 | A draft /sandbox/2026-uplifts/student-visas tree is live, indexed, and accumulating production links on immigration-critical content | HIGH · quick-win |
| 9.2 | Governance actions have no addressee — there is no current-state ownership map | MEDIUM · medium |
| Discover (international) | Unpublish / 301 the live 2025 English language requirements page | HIGH · quick-win |
| 5.1 | Stand up a subdomain registry + provisioning gate | HIGH · medium |

---

*Built from: freshness-signals.csv (13 sandbox URLs), improvements-register.md (§9 Content freshness, §8b International compliance & equity), crawl/ sandbox page captures, international-student-experience.md (2025 English page finding), and cross-site-flow.csv (sandbox inbound link audit). June 2026.*
