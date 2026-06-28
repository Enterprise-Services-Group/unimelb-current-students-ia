# ask.unimelb.edu.au — Crawl Analysis

*The legacy FAQ knowledge base — 515 pages, 393 FAQ articles. The hub's #1 outbound destination (444 links). Where the actual answers to enrolment, fees, census, and visa questions live. June 2026.*

---

## What we found

The ask.unimelb crawl confirms everything the link-graph analysis inferred. This is a legacy FAQ knowledge base with **515 pages**, overwhelmingly FAQ articles (393), served under **two inconsistent URL formats** — the root cause of the duplicate-link problem identified in the course-planning deep-dive.

### Structure

| Pattern | Count | Notes |
|---|---|---|
| FAQ articles (`/app/answers/detail/a_id/####` or `/faq/####`) | 393 | Two URL formats for the same content |
| Category pages | 15 | FAQ category indexes |
| "Page not found" | 10 | Dead FAQ articles still linked |
| Other (WAM, fee remission, enrolment) | ~12 | Standalone content pages |

### Content domains

Sampling 30 FAQ article titles reveals the topics the hub defers to:

| Topic | Sample titles |
|---|---|
| **Fees & finance** | Fee Account Statement, Fees-Statement of Liability, Fees Due Dates, Fee remission, How can I check my fees and payments? |
| **Enrolment** | Enrolling in subjects, Applying for an Extension |
| **Academic progress** | Academic progress, Weighted Average Mark |
| **Admin** | Accessing student email |
| **Visa** | (linked from services.unimelb, not ask directly) |

### The two-URL-format problem confirmed

The FAQ articles exist under BOTH:
- `/app/answers/detail/a_id/####` (79 pages in the crawl)
- `/faq/####/slug` (436 pages in the crawl)

This is the URL duplication the course-planning deep-dive identified: **the same content served under two inconsistent URL formats, with the hub linking both.** The index shows both formats exist and are crawled as separate pages.

### Link analysis

| Outbound destination | Links in 30-page sample | Role |
|---|---|---|
| www.unimelb.edu.au | 108 | Chrome/nav links |
| **students.unimelb.edu.au** | **100** | Hub — FAQ links back to the hub heavily |
| safety.unimelb.edu.au | 30 | Chrome links |
| services.unimelb.edu.au | 24 | Service delivery |
| about.unimelb.edu.au | 24 | Chrome links |
| my.unimelb.edu.au | 15 | SIS — "go do it in my.unimelb" |
| study.unimelb.edu.au | 15 | Prospective site |
| library.unimelb.edu.au | 9 | Library |
| forms.your.unimelb.edu.au | 8 | Transactional forms |

The FAQ links BACK to the hub 100 times in just 30 pages — confirming the tight hub↔FAQ coupling. The hub describes; the FAQ answers; the FAQ routes back to the hub. This is a working but fragile dependency.

### Page weight

Median 45KB — lightweight, text-dominant. The FAQ is built on a simple platform with minimal assets. This is actually one of the better-performing sites in the estate by weight.

---

## What this means

### 1. The FAQ IS the answers layer — and it's legacy

The hub's enrolment, fees, census, and visa pages describe the topic in 1-2 paragraphs, then link to ask.unimelb for the actual answer. The FAQ carries the operational detail: census dates with consequences, fee payment methods, enrolment variation procedures, academic progress rules. **The hub is the table of contents; the FAQ is the book.**

### 2. The two-URL-format problem is real and confirmed

Both `/app/answers/detail/a_id/####` and `/faq/####` serve the same FAQ articles. Links from the hub use both formats. This splits link equity, dilutes analytics, and creates canonical ambiguity. The fix recommended in the course-planning deep-dive (standardise to one format, 301 the other) is directly confirmed by the crawl.

### 3. 10 FAQ pages are dead

"Page not found" articles still exist and may still be linked. This is the same stale-content problem seen across the estate.

### 4. The FAQ platform is simple and fast

45KB median pages, text-heavy, minimal assets. If the plan is to migrate FAQ answers into the hub (as recommended by the improvements register), the content is well-structured and portable.

---

## Recommendations

1. **Standardise to ONE FAQ URL format.** 301 `/app/answers/detail/a_id/####` to `/faq/####` (or vice versa). Fix the 396 hub links to use the canonical format.

2. **Migrate high-traffic answers into the hub.** Census dates, fee payment methods, enrolment procedures — the operational core should live on students.unimelb, not a legacy FAQ. Keep the FAQ for long-tail questions.

3. **Remove the 10 dead FAQ pages** and fix any inbound links pointing to them.

4. **Add rel=canonical** to all FAQ articles pointing to the single canonical URL.

---

*Built from: ask.unimelb crawl (515 pages), links.json sampling (30 pages), index.json structural analysis. June 2026.*
