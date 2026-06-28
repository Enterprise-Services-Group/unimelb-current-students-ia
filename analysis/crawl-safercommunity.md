# safercommunity.unimelb.edu.au — Crawl Analysis

*The crisis and safety service — 17 pages. Comprehensive, well-written, and strongly connected to the hub (53 outbound links in 17 pages). But every page is ~300KB. Confirms the wellbeing deep-dive: the service is real; the routing from the hub exists; the remaining gap is findability within the wellbeing ecosystem. June 2026.*

---

## What we found

Safer Community is the University's crisis, safety, and sexual misconduct support service. The wellbeing deep-dive identified it as living on a separate uncrawled domain with 144 inbound links from 12 domains. The crawl reveals a **compact but comprehensive 17-page site** covering every form of interpersonal harm a student might experience.

### Structure

| Section | Pages | Content |
|---|---|---|
| Sexual assault | 1 | Definition, support, reporting |
| Sexual harassment | 1 | Definition, support, reporting |
| Bullying | 1 | Definition, support, reporting |
| Discrimination | 1 | Definition, support, reporting |
| Family/intimate partner violence | 1 | Definition, support, reporting |
| Stalking | 1 | Definition, support, reporting |
| Child safety | 1 | Child safety obligations |
| Scam warning | 1 | Current scam alerts |
| Home/overview | 2 | Safer Community Program overview |
| Other | 7 | Additional pages |

Every page follows the same pattern: **definition → what it looks like → how to get support → how to report → further resources.** This is consistent, well-structured crisis content.

### Link analysis

| Outbound destination | Links in 17-page sample | Role |
|---|---|---|
| www.unimelb.edu.au | 164 | Heavy chrome |
| about.unimelb.edu.au | 70 | Chrome |
| **students.unimelb.edu.au** | **53** | Hub — strong connection |
| policy.unimelb.edu.au | 28 | University policies |
| services.unimelb.edu.au | 23 | Counselling/health services |
| staff.unimelb.edu.au | 18 | Staff resources |
| safety.unimelb.edu.au | 17 | General safety |
| library.unimelb.edu.au | 17 | Chrome |
| umsu.unimelb.edu.au | 8 | Student union — advocacy referral |
| ask.unimelb.edu.au | 3 | FAQ |

The site links BACK to students.unimelb 53 times — and the hub links to safercommunity 62 times. **This is a bidirectional, working connection — one of the few balanced link relationships in the estate.**

### Page weight

Consistently heavy: median 291KB, max 318KB, min 286KB. All 17 pages are within a 32KB range — uniform template. The weight is concerning for a crisis service where students may be on slow connections or using a friend's device.

---

## What this means

### 1. The service is real and the routing works

Unlike murrupbarak (19 hub links vs 614 MSD), safercommunity has a healthy bidirectional relationship with the hub: 62 hub→safercommunity, 53 safercommunity→hub. **This is one of the few seams in the estate that isn't broken.**

### 2. The gap is within the wellbeing ecosystem

The wellbeing deep-dive found counselling branded "Academic Skills Unit" on services.unimelb. Safer Community is a separate domain. A student in crisis might land on counselling when they need Safer Community, or vice versa. The gap is cross-service findability, not cross-domain routing.

### 3. Content quality is high

Every page covers the same structure: definition, what it looks like, support, reporting, resources. This is crisis-content best practice. No need to rewrite — just make it more findable.

### 4. Page weight is a concern for crisis access

~300KB per page on a service where students may be accessing from a library computer, a friend's phone, or a constrained connection. Trim the chrome overhead.

---

## Recommendations

1. **Add Safer Community to a unified "I need help now" front door on the hub.** Alongside counselling, health, and financial hardship. A student in crisis should not need to know which service is called "Safer Community."

2. **Cross-link counselling and Safer Community.** A student landing on the counselling page should see "If you need to report sexual assault, harassment, or discrimination → Safer Community." And vice versa.

3. **Trim page weight.** 300KB for crisis content is too heavy. Reduce chrome overhead from 164 www.unimelb + 70 about.unimelb links.

---

*Built from: safercommunity crawl (17 pages), links.json sampling (17 pages — full crawl), index.json structural analysis, student-services-fragmentation.md deep-dive. June 2026.*
