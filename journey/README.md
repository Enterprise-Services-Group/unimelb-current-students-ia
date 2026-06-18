# Current Student Experience — Journey Map

A self-contained, UoM-branded journey map of how a current student moves through the
fragmented current-students web estate. **The entire map is generated from one
`JOURNEY` data object** in the HTML — edit the data, reload, the visual regenerates.

## Files
- `current-student-journey-map.html` — open in any browser.
- `logo.svg` — the UoM logo (referenced by the HTML; keep it alongside).

## How to edit (this is the point)
Open the HTML and find the `const JOURNEY = { … }` block. Everything is data:
- **`persona`** — who the journey is for. Swap it (e.g. a coursework-masters or HDR student) or add detail.
- **`lanes`** — the rows down the left. Each is `{ key, label, icon, style }`. Add/remove/reorder rows; `key` must match a field on each stage; `style` is one of `action · touch · system · pain · opp · sol` (controls colour).
- **`stages`** — the columns across the top. Each stage carries:
  - the lane fields (`doing`, `touchpoints`, `systems`, `pains`, `hmw`, `solutions`) — arrays of strings (`hmw` = How-Might-We opportunity questions; `solutions` = concrete solution examples; together they form the insight → opportunity → solution ladder),
  - `emotion` (−2 … +2) — plots the experience curve,
  - `feeling` — the short label shown on the curve.

To add a stage, copy a stage block and edit it. To add a lane (e.g. "Channels" or
"Moments of truth"), add a `lanes` entry and the matching field on each stage. No build
step, no framework — just edit and refresh.

### Drill-down detail (modals)
Pain points, opportunities (HMW) and systems are **clickable** (look for the `+`) — they open a
modal that expands on the point. That content lives in the `details` object at the bottom of the
`JOURNEY` block, keyed by the exact item text:
- pain points & opportunities → a `body` paragraph,
- systems → a `note` plus example `urls` (rendered as links).

Items with no `details` entry simply aren't clickable. You can deep-link a modal with
`current-student-journey-map.html#open=N` (N = its order among clickable items).

### Editing with AI
Because the map *is* the data, an AI can edit it directly: paste the `JOURNEY` object,
ask for changes ("add a 'Channels' lane", "make the WIL stage emotion −1", "add an
international-student persona"), and drop the returned object back in.

## Rendering to PDF / PNG
```
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# PNG
"$CHROME" --headless=new --window-size=1640,1180 --screenshot=journey.png current-student-journey-map.html
# PDF (landscape reads best — set @page in the <style> or print to PDF from the browser)
"$CHROME" --headless=new --print-to-pdf=journey.pdf current-student-journey-map.html
```

## Notes
- Fonts (Fraunces, Source Sans 3, Source Code Pro) load from Google Fonts — online for
  the exact brand type; it falls back to system serif/sans offline.
- The map shows the **current** (fragmented) experience the audit found; the
  **Opportunities** row is the hub-and-spoke target state.
- Evidence base: the sibling `unimelb-current-students-ia/` audit (crawl corpus, topic
  deep-dives, recommendations).
