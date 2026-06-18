# Crawl spec (for crawl sub-agents)

One sub-agent crawls ONE faculty Current-Students subtree (or the hub) and writes a durable corpus.

## Browser access
1. `ToolSearch` query `"Claude in Chrome browser navigate read page text"` to load the `mcp__Claude_in_Chrome__*` tools.
2. `mcp__Claude_in_Chrome__select_browser` with `deviceId: "8b10bba5-c057-466c-b520-90acb4633e9c"`.
3. `mcp__Claude_in_Chrome__tabs_create_mcp` to make your OWN tab(s); never reuse another agent's tab. You may create up to 4 tabs and crawl 4-wide in parallel via `browser_batch`.

## Efficient technique (proven on the Law crawl — use this)
UniMelb CS pages are **server-rendered and same-origin** under the faculty host. So instead of `navigate`-ing every URL (slow), open ONE tab on the faculty origin and run an **in-page `fetch()`-based BFS** inside `javascript_tool`: fetch each in-scope URL, parse with `DOMParser`, extract the same fields as the extractor below, keep a visited set in page memory (or `localStorage` for resumability). Because the MCP truncates tool output (~1KB), don't return the corpus through the tool result — instead POST the accumulated JSON to a throwaway local receiver (`http://127.0.0.1:<PORT>` is exempt from mixed-content blocking; run it with a quick Bash python one-liner on YOUR unique port) and write it to disk, or chunk it. Clean up tabs/localStorage when done; only touch tabs you created.

## Scope rules (BFS)
- **In-scope** = same host as the root AND pathname === PRE or starts with PRE + "/", where PRE is the faculty's CS path (e.g. `/students`, `/current-students`, `/study/current-students`).
- Enqueue only in-scope, not-yet-visited URLs. Normalize by stripping query/hash/trailing slash.
- **Do NOT crawl** auth-gated hosts: `my.unimelb.edu.au`, `lms.unimelb.edu.au`, `canvas.lms.unimelb.edu.au`, `sis*`, `studentit`, `services.unimelb.edu.au` login flows. Record them as `outboundHosts` only.
- Cap depth at 6 and total pages at 250 per faculty (log if hit).
- Be polite: rely on the natural latency of sequential navigation; no artificial hammering.

## Per-page extractor (run via javascript_tool after navigate; replace __PRE__)
```js
(()=>{const PRE='__PRE__';const n=s=>(s||'').replace(/\s+/g,' ').trim();const dl=r=>{let o=[];r.querySelectorAll('*').forEach(e=>{if(e.shadowRoot)o=o.concat(dl(e.shadowRoot));});r.querySelectorAll('a[href]').forEach(a=>o.push(a));return o;};const A=dl(document);const host=location.host;const main=document.querySelector('main')||document.body;const text=n(main?main.innerText:'');const wc=text?text.split(' ').length:0;const links=A.map(a=>a.href).filter(h=>h&&h.indexOf('javascript')!==0);const sset=new Set();for(const h of links){try{const u=new URL(h);if(u.host===host&&(u.pathname===PRE||u.pathname.indexOf(PRE+'/')===0)){sset.add(u.origin+u.pathname);}}catch(e){}}const inSec=[...sset];const dest={};for(const h of links){try{const u=new URL(h);if(u.host!==host||!(u.pathname===PRE||u.pathname.indexOf(PRE+'/')===0)){dest[u.host]=(dest[u.host]||0)+1;}}catch(e){}}const is404=/page not found|404|cannot be found/i.test(document.title+' '+text.slice(0,200));return JSON.stringify({url:location.href,title:document.title,is404,wordCount:wc,inSection:inSec,outboundHosts:dest,excerpt:text.slice(0,600)});})()
```

## Classification (per page, from signals)
- `redirect/broken` — is404 true.
- `link-farm` — wordCount < 160 AND it mostly points elsewhere (sum of outboundHosts counts ≥ ~10, or hub links present) with little unique prose.
- `unique` — wordCount ≥ 160 with substantive prose not obviously duplicated from the hub.
- `mixed` — has unique prose AND heavy redirection (esp. many `students.unimelb.edu.au` links).
Record the signals so Phase 3 can re-judge.

## Topic tags (assign 1-4 from this controlled list)
`enrolment, course-planning, subjects-timetable, exams-results, special-consideration, fees-finance, scholarships, placements-WIL, careers-employability, academic-skills, student-life, clubs-events, wellbeing-health, IT-systems, library, graduation, forms-admin, contacts-support, research-candidature, international, inclusion-equity, orientation`

## Output (write to disk)
- `crawl/pages/<faculty>.json` — JSON array of per-page records: `{url, normalizedUrl, faculty, unitLevel:"faculty", title, depth, wordCount, classification, topicTags[], outboundHosts{}, hubLinks, inSectionCount, excerpt}`.
- `crawl/pages/<faculty>-summary.md` — counts (pages, by classification, by topic), the section IA (tree of in-scope URLs), top outbound destinations, notable unique pages, and anything auth-gated.
- Append any newly discovered in-scope program subdomains to `crawl/pages/<faculty>-discovered.txt`.

## Return value (final message = compact summary, NOT the raw corpus)
`{faculty, pagesCaptured, byClassification:{unique,link-farm,mixed,redirect}, topTopics[], iaDepth, notableUniquePages[], authGatedHosts[], notes}`
