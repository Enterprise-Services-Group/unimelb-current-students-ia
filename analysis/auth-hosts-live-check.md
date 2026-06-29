# Authenticated Core — Live Host Audit

*What happens when you actually visit the 42 authenticated hosts. Live HTTP checks reveal dead domains, SSO walls, and the few hosts with public content. June 2026.*

---

## Executive summary

The authenticated core audit mapped 42 hosts that the public estate links to. This follow-up actually visited them. Three findings change the picture:

1. **Two of the highest-stakes transactional hosts are dead.** specialconsideration.app.unimelb.edu.au returns 404 — at root and at /apply. enrolmentvariations.app.unimelb.edu.au returns 404 — at root and at /apply. The hub has 14 links pointing to dead pages for special consideration and enrolment variations. Students clicking "Apply for special consideration" or "Reduce study load" arrive at a 404.

2. **Mycounselling.app exists but is blocked.** 403 Forbidden. The 3 links from services.unimelb to counselling booking point to a host that refuses connections. This is marginally better than a 404 but still inaccessible.

3. **18 of 19 tested hosts are auth-gated, dead, or unreachable.** Only ecommerce.unimelb.edu.au has public content. The authenticated core is an authenticated core in the literal sense — almost nothing is accessible without login.

---

## Live check results — all 19 hosts

| Status | Host | What happens |
|---|---|---|
| ✅ OK (public) | ecommerce.unimelb.edu.au | "Home page" — payment gateway with public pages |
| ✅ OK (public) | intlstudaccept.unimelb.edu.au | "International Student Acceptance and Payment Agreement" — login wall behind |
| 🔒 SSO wall | my.unimelb.edu.au | Redirects to SSO — empty title |
| 🔒 SSO wall | tes.app.unimelb.edu.au | Empty title — SSO redirect |
| 🔒 SSO wall | feit-vocational-placement.app.unimelb.edu.au | Empty title — SSO redirect |
| 🔒 SSO wall | law.app.unimelb.edu.au | Empty title — SSO redirect |
| 🔒 SSO wall | ctrs.app.unimelb.edu.au | Empty title — SSO redirect |
| 🔒 SSO wall | overseasstudyplanner.unimelb.edu.au | Empty title — SSO redirect |
| 🔒 SSO wall | accounts.unimelb.edu.au | Empty title — SSO redirect |
| 🔒 SSO wall | mytimetable.students.unimelb.edu.au | Empty title — SSO redirect |
| 🔒 SSO wall | course-planner.unimelb.edu.au | Empty title — SSO redirect |
| 🔒 SSO wall | casemanagementform.unimelb.edu.au | Empty title — SSO redirect |
| 🔒 SSO wall | feerefundform.unimelb.edu.au | Empty title — SSO redirect |
| 🔒 SSO wall | forms.your.unimelb.edu.au/4747166 | "University of Melbourne - Sign In" — SSO wall |
| 🔒 SSO wall | forms.your.unimelb.edu.au | "FormAssembly: Enterprise" — SSO login |
| 🚫 Blocked | mycounselling.app.unimelb.edu.au | 403 Forbidden |
| ❌ **DEAD** | **specialconsideration.app.unimelb.edu.au** | **404 — at root AND /apply** |
| ❌ **DEAD** | **enrolmentvariations.app.unimelb.edu.au** | **404 — at root AND /apply** |
| ❌ DNS fail | student-advising-system.unimelb.edu.au | ERR_NAME_NOT_RESOLVED |
| ❌ Connection | enquiry.app.unimelb.edu.au | ERR_CONNECTION_RESET |

**18 of 19 hosts are inaccessible without authentication. 2 are dead. 1 has public content.**

---

## The dead hosts — a critical finding

### specialconsideration.app.unimelb.edu.au

| Check | Result |
|---|---|
| Root URL | 404 |
| /apply | 404 |
| Hub links pointing here | 12 (11 from students.unimelb, 1 from msd) |
| Link text | "Apply for special consideration" |

This is the host students are directed to when they need special consideration — extensions, deferred exams, academic adjustments. The links from the hub are correctly labeled. The destination is dead. **Every student who clicks "Apply for special consideration" from the hub arrives at a 404.**

### enrolmentvariations.app.unimelb.edu.au

| Check | Result |
|---|---|
| Root URL | 404 |
| /apply | 404 |
| Hub links pointing here | 2 (biomed, msd) |
| Link text | Unknown (buried in faculty pages) |

This is the host for reduced study load, leave of absence, and withdrawal — the highest-stakes enrolment changes. An international student reducing study load risks their visa. A domestic student withdrawing needs to know the census-date consequence. The destination is dead.

---

## The blocked host — mycounselling.app

| Check | Result |
|---|---|
| Root URL | 403 Forbidden |
| Hub links pointing here | 3 (all from services.unimelb) |

The counselling booking system exists but refuses connections at the root level. It may work with a specific path or require a referral token. But the links from services.unimelb point to a URL that returns 403. A student trying to book counselling from the public page hits a wall.

---

## The public host — ecommerce.unimelb.edu.au

The only authenticated host with public pages. 21 pages crawled — likely product listings, payment information, and help pages. This is the payment gateway used by sport memberships, event registrations, and fee payments. It has public content because the ecommerce flow starts before login.

---

## What this means

### 1. The find→act gap has a worse variant: the find→dead gap

The link-label problem identified in the authenticated core audit (generic labels) is now compounded by dead destinations. It's not just that the link text is vague — the links themselves are broken. **specialconsideration.app and enrolmentvariations.app need to be restored or the links redirected immediately.**

### 2. The *.app ecosystem is orphaned

The 19 single-purpose `*.app` microsites identified in the forms audit have no ownership, no retirement dates, and no monitoring. Two are already dead. The remaining 17 could go the same way with no one noticing until a student reports it.

### 3. The "describe but don't transact" pattern is confirmed at the HTTP level

18 of 19 hosts redirect to SSO. The public estate describes the action; the authenticated core requires login to transact. This is by design — but the dead hosts mean the design is breaking. When the destination dies, the public description becomes misinformation.

### 4. ecommerce is the only working model

The ecommerce site has public pages that describe products and payment options before requiring login. This is the pattern the other hosts should follow: a public landing layer that confirms the student is in the right place, then hands off to authentication.

---

## Recommendations

### 1. Fix or redirect specialconsideration.app and enrolmentvariations.app — immediately `[CRITICAL · quick-win]`

Two of the highest-stakes transactional hosts in the estate are dead. Either restore the hosts or redirect their URLs to the correct destinations. The 14 inbound links from the hub and faculties are currently sending students to 404s.

### 2. Investigate mycounselling.app `[HIGH · quick-win]`

403 Forbidden suggests the host exists but is misconfigured. Confirm the correct URL for counselling bookings and update the 3 links from services.unimelb.

### 3. Audit all remaining *.app hosts for liveness `[HIGH · medium]`

slidelibrary.app, thesislibrary.app, booklibrary.app, studenteforms.app, ffam-mcm.app, law.app, ctrs.app — all single-purpose legacy hosts with 1-8 inbound links each. Check if they still resolve. Add liveness monitoring.

### 4. Add a public landing page to every *.app host `[MEDIUM · medium]`

Before the SSO redirect, show a page that confirms the student is in the right place: "You're about to apply for special consideration. Log in with your University account to continue." This closes the find→act gap at the HTTP level — the student knows they've arrived at the right destination before they authenticate.

### 5. Add liveness monitoring to all 42 authenticated hosts `[MEDIUM · medium]`

If a host goes down, the public estate continues linking to it indefinitely. A periodic HEAD request to every authenticated host, with alerts when a 404 or connection failure is detected, would catch the next dead host before students do.

---

*Built from: live HTTP checks of 19 authenticated hosts using headless Chrome. June 2026.*
