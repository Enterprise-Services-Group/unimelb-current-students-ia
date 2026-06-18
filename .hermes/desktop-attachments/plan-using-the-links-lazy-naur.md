# Plan — University of Melbourne "Current Students" IA Audit & Unification Strategy

## Context

The University of Melbourne runs a **central current-students hub** (`students.unimelb.edu.au`) **plus 9 faculty sites** that each maintain their own "Current Students" section on separate subdomains (e.g. `arts.unimelb.edu.au/students`, `fbe.unimelb.edu.au/current-students`, `finearts-music.unimelb.edu.au/current-students`). The result is a **fragmented student experience**: some faculty pages hold genuinely unique content (placements, course-planning advice, faculty-specific services), while many are **"link farms"** that just redirect students back to the central hub — with inconsistent IA, duplication, and gaps that differ faculty-to-faculty.

You (a UoM staff member) want an **evidence-based audit** of this fragmentation and a **strategy to unify** faculty current-students content into `students.unimelb.edu.au`, including the service-model nuances, the new pages the hub would need, how faculty sites should be standardised, and the governance/design principles to keep it consistent over time.

**Goal:** produce (1) a complete crawled inventory + IA/content/topic logs of all faculty current-students sections and the central hub, (2) a multi-faculty service-model comparison, and (3) a full recommendations brief — delivered as working docs+data, a UoM-branded PDF, and an executive deck.

**Scope = the full academic-unit tree** (confirmed from the seed page): the **9 faculties**, **every school / department / institute / centre beneath them** (≈35 units), **and any nested program/school subdomains those link to that expose their own current-students section** (e.g. a degree-program site under a school). The 9 faculties: Architecture, Building & Planning · Arts · Business & Economics · Education · Engineering & IT · Fine Arts & Music · Melbourne Law School · Medicine, Dentistry & Health Sciences · Science. See the **Academic-unit registry** below for the captured unit→site map.

---

## Key constraints discovered (these shape the whole approach)

| Constraint | Consequence |
|---|---|
| `WebFetch` → **403 Forbidden** (UoM WAF blocks the bot UA) | Cannot use WebFetch for any unimelb page. |
| Apify `rag-web-browser` → **monthly hard limit exceeded** | No Apify crawling available. |
| **Claude-in-Chrome works** (verified — pulled the full seed page) via your connected "Browser 1" | This is the **only** viable fetch path. It uses your single, session-bound browser → crawling is **sequential**, page-by-page, and **must be resumable / multi-session** for an exhaustive run. |
| Workflow subagents share session MCP but would **contend over the one browser tab group** | **Crawl in the main thread → write a local file corpus → the analysis Workflow reads the FILES, not the live site.** Clean separation, parallelisable, resumable. |
| `students.unimelb.edu.au` is very large (potentially 1000s of leaf pages) | "Exhaustive" = full BFS of each **unit current-students subtree**; for the hub, the **complete IA tree + section/landing pages + a logged leaf inventory by topic** (flag and checkpoint if leaf count explodes). |
| Scope is the **whole academic-unit tree** (≈44 known units) **+ recursively-discovered** program/school subdomains | Crawl is **unit-aware**: each faculty / school / dept / institute / centre is a unit. Any `*.unimelb.edu.au` host reachable from a unit site that exposes a current-students section is added to the registry and crawled. Scope growth is logged + checkpointed. |

**Politeness/ethics:** public pages only, sane pacing, **skip anything behind student login** (`my.unimelb`, LMS/Canvas, SIS) and only record that those gateways exist.

---

## Academic-unit registry (Phase 1 seed set — captured live from the seed page)

The unit→site map below is the real starting set. Note the **mixed pattern** — some units own a **dedicated subdomain**, others live as **paths inside the faculty domain** — which itself is a finding for the audit:

- **Architecture, Building & Planning** — `msd.unimelb.edu.au` (Melbourne School of Design *is* the faculty site)
- **Arts** — `arts.unimelb.edu.au`; schools as **paths**: `/asia-institute`, `/graduate` (Grad School of Humanities & Social Sciences), `/school-of-culture-and-communication`, `/school-of-historical-and-philosophical-studies`, `/school-of-languages-and-linguistics`, `/school-of-social-and-political-sciences`
- **Business & Economics** — `fbe.unimelb.edu.au`; departments as **paths**: `/accounting`, `/economics`, `/finance`, `/managementmarketing`; **separate entities**: `mbs.unimelb.edu.au` (Melbourne Business School), `melbourneinstitute.unimelb.edu.au`
- **Education** — `education.unimelb.edu.au` (to confirm); `melbourne-cshe.unimelb.edu.au` (Centre for the Study of Higher Education)
- **Engineering & IT** — `eng.unimelb.edu.au`; `cis.unimelb.edu.au` (Computing & Information Systems); two schools as **paths** under `eng.unimelb.edu.au/about/departments/…`
- **Fine Arts & Music** — `finearts-music.unimelb.edu.au`; units as **paths**: `/about-us/mcm` (Conservatorium), `/about-us/vca` (VCA), `/about-us/wilin` (Wilin Centre)
- **Melbourne Law School** — `law.unimelb.edu.au` (single-department faculty)
- **Medicine, Dentistry & Health Sciences** — `medicine.unimelb.edu.au` (faculty); **school subdomains**: `dental`, `healthsciences`, `psychologicalsciences`, `biomedicalsciences`, `mspgh` (Population & Global Health)
- **Science** — `science.unimelb.edu.au` (to confirm); **school subdomains**: `safes`, `biosciences`, `chemistry`, `sgeas`, `ms` (Maths & Stats), `physics`, `mvs` (Melbourne Veterinary School)

**≈44 known units before recursive discovery.** Faculty "Visit" links route through `about.unimelb.edu.au` structure pages, so Phase 1 resolves each faculty's canonical site + CS entry by visiting those. After the registry is built I'll report the **unit count + estimated page-scale** and checkpoint with you before the full BFS (recursive subdomain discovery — e.g. a Bachelor of Design program site — can grow the set).

---

## Output location & structure

New sibling folder (keeps this out of the `mydo` product repo):
`/Users/djmulholland/Documents/Claude/projects/unimelb-current-students-ia/`

```
unimelb-current-students-ia/
├── README.md                       # what this is + how to resume the crawl
├── state/
│   ├── frontier.json               # per-unit URL queue (resume point)
│   ├── visited.json                # normalized URLs already captured
│   └── progress.md                 # human checkpoint log (counts per unit)
├── crawl/
│   ├── pages.jsonl                 # one record per page (schema below)
│   └── raw/<sha1>.txt              # raw extracted text per page
├── data/                           # the deliverable "logs" (CSV/JSON)
│   ├── url-inventory.csv           # (brief 1) every URL + unit + faculty + section
│   ├── unit-registry.csv           # every academic unit → site host → has-CS-section?
│   ├── top-ia.json                 # (2a) per-unit top nav (faculty + schools)
│   ├── current-students-ia.json    # (2b) per-unit CS-section IA tree
│   ├── pages-by-topic.csv          # (2e) page → topic tags
│   ├── unique-vs-linkfarm.csv      # (2d) page → class + where it sends students
│   └── students-unimelb-ia.json    # (3a) hub IA + topic taxonomy
├── analysis/
│   ├── unit-<slug>.md              # (2c) per-unit content/service profile (rolled up by faculty)
│   ├── service-model-matrix.csv/md # (4e) who-provides-what across units & faculties
│   └── topic-deepdives/*.md        # (4d) course planning, faculty services, employability, student life
├── report/
│   ├── recommendations.md          # (4a–i) full strategy
│   ├── report.html → report.pdf    # branded PDF
└── deck/
    └── unimelb-cs-ia.pptx          # executive deck
```

**Per-page record (`pages.jsonl`):**
```json
{ "url","normalizedUrl","unitName","unitLevel":"faculty|school|department|institute|centre|program","faculty","subdomain","domain","section","breadcrumb":[],
  "title","depth","navItems":[],"wordCountUnique",
  "outboundLinks":[{"text","href"}],
  "destinationsSummary":{"students.unimelb.edu.au":N,"ask.unimelb":N,"handbook":N,"my.unimelb":N},
  "classification":"unique|link-farm|mixed|redirect",
  "topicTags":[], "rawTextFile":"raw/<sha1>.txt", "capturedAt" }
```

**Classification heuristic (at crawl time, refined by agents in Phase 3):**
- **link-farm/hub** — high outbound-link density (esp. → `students.unimelb.edu.au`), low unique prose (≲150 unique words), page is mostly a list of links.
- **unique** — substantive content not available on the hub (faculty placements, discipline advice, local forms/contacts).
- **mixed** — some unique content + significant redirection.
- **redirect** — pass-through (meta-refresh / "go to students.unimelb").

---

## Execution phases

### Phase 0 — Setup
Create the folder tree + empty `state/` files + `README.md` with resume instructions. Model state handling on the repo's existing `.research_state` resumable pattern.

### Phase 1 — Unit registry, URL inventory & seed frontier (brief step 1)
- **Build the academic-unit registry** from the captured seed-page map (above): every faculty + school/dept/institute/centre, each with `unitName`, `unitLevel`, `faculty`, and site host/path. Write `data/unit-registry.csv`.
- **Probe each unit** by visiting its site once: capture its **top nav (2a top IA)** and detect whether it has its own **"Current Students" / "Students"** section (label varies: `/students`, `/current-students`, `/study/current-students`, in-nav "Current students"). Record `hasCSSection` + the CS entry URL in the registry.
- **Recursive discovery:** flag any further `*.unimelb.edu.au` host linked from a unit site that itself exposes a CS section (e.g. a Bachelor of Design program site) and add it to the registry as a `program` unit.
- Seed `frontier.json` with every discovered CS entry point + `students.unimelb.edu.au`.
- **Scale checkpoint:** report unit count + rough page estimate before the full BFS; proceed unless you want to trim.
- Write initial `url-inventory.csv`.

### Phase 2 — Exhaustive resumable crawl (brief steps 2 & 3)
Done by me in the main thread, **unit-by-unit (grouped by faculty)**, via Claude-in-Chrome (`navigate` + `get_page_text` + `read_page`/`javascript_tool` to extract hrefs), batching with `browser_batch`.

- **Pilot first** on one faculty + one of its schools (e.g. Arts + School of Culture and Communication) to validate the schema, classification heuristic, unit-tagging, and pacing; then scale to all units.
- BFS each unit's CS subtree: extract in-section links → enqueue unvisited (same host/path scope for that unit); record **all outbound destinations** (for 2d) and tag each page with its `unitName`/`unitLevel`. Compute the per-page record + classification; append to `pages.jsonl`; save raw text to `raw/`.
- **Recursive subdomain discovery during crawl:** if a unit's CS section links to another `*.unimelb.edu.au` host with its own CS content, register it and crawl it too (logged in `progress.md`).
- **Checkpoint after each unit**: flush `frontier/visited/progress`, update the `data/*.csv|json` logs. Crawl **spans multiple sessions** — you resume by saying "continue the crawl"; I reload state and continue from the frontier.
- Map `students.unimelb.edu.au`: full IA tree + section landing pages + topic-tagged leaf inventory (→ `students-unimelb-ia.json`, with a checkpoint if the leaf set is huge).
- Output of this phase: complete `url-inventory.csv` (1), `top-ia.json` (2a), `current-students-ia.json` (2b), raw corpus (2c), `unique-vs-linkfarm.csv` (2d), `pages-by-topic.csv` (2e), `students-unimelb-ia.json` (3a).

### Phase 3 — Multi-agent analysis Workflow (brief step 4 evidence)
Authored with the **`workflow-patterns`** skill. Subagents read the **local corpus** (not the live site). Pipeline/parallel stages:
1. **Classify + topic-tag refine** — pipeline over `pages.jsonl`; second-pass verify edge-case link-farm vs unique calls.
2. **Per-unit profile** — one agent per unit (faculty + each school/dept/institute/centre) → `analysis/unit-<slug>.md` (content held, services offered, topic coverage, unique vs redirected; rolled up by faculty). *(Route through the `UX Process` agent for IA/service-design framing.)*
3. **Hub IA + topic map** — agent maps `students.unimelb` IA & taxonomy.
4. **Cross-unit service-model matrix** (barrier — needs all profiles together) → `service-model-matrix` (4e): which services/topics each **faculty and school** provides vs not, **where schools duplicate / extend / diverge from their faculty and the hub**, and the nuances.
5. **Topic deep-dives** (4d): course planning · faculty services · employability · student life — each as a cross-faculty note.

### Phase 4 — Recommendations synthesis + deliverables (brief step 4 output)
- **Synthesis with adversarial pressure-test** (workflow-patterns archetype): generate the unification recommendation + alternatives, then a judge/critic pass to stress-test feasibility and surface risks. Produces `report/recommendations.md` covering:
  - **4a** Unify faculty content into `students.unimelb` — recommended model + *how* (content migration map, what collapses, what stays faculty-owned).
  - **4b** Alternative approaches (e.g. federated standards vs full centralisation vs hybrid hub-and-spoke).
  - **4c** Other fixes for the fragmented experience.
  - **4d** Key-topic treatment (course planning, faculty services, employability, student life).
  - **4f** How to improve the service model.
  - **4g** New pages required on `students.unimelb.edu.au` (content model).
  - **4h** How faculty sites should be updated consistently (a faculty CS template + content standards).
  - **4i** Design principles + governance to maintain it ongoing.
- **Deliverables:**
  - **Working docs + data** — the `data/`, `analysis/`, and `recommendations.md` artifacts.
  - **Branded PDF** — `uom-design-system` skill (official navy `#000F46` / cyan `#46C8F0`, Fraunces/Source Sans) + `designed-deliverable` (HTML+SVG → headless-Chromium PDF → render→inspect-pixels→fix visual-QA loop).
  - **Executive deck** — `anthropic-skills:pptx` (UoM-branded), findings + recommendations for steering audiences.

---

## Brief-point → artifact traceability

| Brief | Artifact |
|---|---|
| 1 URL list | `data/url-inventory.csv` |
| 2a top IA | `data/top-ia.json` + `data/unit-registry.csv` + unit profiles |
| 2b Current Students IA | `data/current-students-ia.json` |
| 2c CS content | `crawl/raw/*` + `analysis/unit-*.md` |
| 2d unique vs link-farm + destinations | `data/unique-vs-linkfarm.csv` |
| 2e pages by topic | `data/pages-by-topic.csv` |
| 3a hub IA + topics | `data/students-unimelb-ia.json` |
| 4a–4i recommendations | `report/recommendations.md` → PDF + deck |
| 4e service model | `analysis/service-model-matrix.*` |
| 4d topic deep-dives | `analysis/topic-deepdives/*` |

---

## Verification

- **Coverage:** per-unit page counts in `progress.md`; confirm every unit's frontier is drained and every registry unit was probed for a CS section; list any URLs skipped (auth-gated) and why.
- **Classification audit:** spot-check several pages per class (unique / link-farm / mixed) against the live page.
- **Evidence-grounded recs:** every recommendation cites specific `url-inventory`/`pages.jsonl` rows.
- **Deliverable QA:** visual-QA loop (render → inspect pixels → fix) on the PDF and deck; check brand tokens applied.

## Risks & handling
- **Scale / multi-session** → resumable state + per-unit checkpoints; scale checkpoint after Phase 1; honest progress reporting; you can pause/resume anytime.
- **WAF / single browser** → all fetches via Claude-in-Chrome with sane pacing; corpus cached locally so analysis never re-hits the site.
- **Auth-gated content** (LMS/SIS/my.unimelb) → recorded as gateways, not crawled.
- **Hub vastness** → IA-complete + section-level + topic-tagged leaf inventory, with a checkpoint before any deep leaf sweep.

## Resumability
State lives in `state/frontier.json` + `visited.json` + `progress.md`. To resume: reload state, continue BFS from the frontier. Same pattern lets the analysis Workflow re-run cheaply (it reads the static corpus).
