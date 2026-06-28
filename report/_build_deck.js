const pptxgen = require("pptxgenjs");
const pptx = new pptxgen();

// Theme — Navy + Ice Blue (matching UoM feel, not using official brand)
const NAVY = "1B3A5C";
const ICE = "CADCFC";
const WHITE = "FFFFFF";
const DARK = "0F1F33";
const MUTED = "6B8299";

pptx.defineLayout({ name: "CUSTOM", width: 13.33, height: 7.5 });
pptx.layout = "CUSTOM";

// Master slide
pptx.defineSlideMaster({
  title: "MASTER",
  background: { color: WHITE },
  objects: [
    { rect: { x: 0, y: 7.2, w: 13.33, h: 0.3, fill: { color: NAVY } } },
  ]
});

// Helper: dark slide
function darkSlide(title, subtitle) {
  const slide = pptx.addSlide();
  slide.background = { color: DARK };
  if (title) slide.addText(title, { x: 0.8, y: 1.5, w: 11.7, h: 1.2, fontSize: 36, bold: true, color: WHITE, fontFace: "Calibri" });
  if (subtitle) slide.addText(subtitle, { x: 0.8, y: 2.8, w: 11.7, h: 1.0, fontSize: 16, color: ICE, fontFace: "Calibri" });
  return slide;
}

// Helper: content slide
function contentSlide(title) {
  const slide = pptx.addSlide();
  slide.background = { color: WHITE };
  slide.addText("FRAGMENTED EXPERIENCES", { x: 0.5, y: 0.2, w: 5, h: 0.4, fontSize: 8, color: MUTED, fontFace: "Calibri", bold: true });
  slide.addText(title, { x: 0.5, y: 0.5, w: 12, h: 0.7, fontSize: 28, bold: true, color: DARK, fontFace: "Calibri" });
  return slide;
}

// Helper: stat callout
function statBox(slide, number, label, x, y, w, h) {
  slide.addShape(pptx.ShapeType.rect, { x, y, w, h, fill: { color: "F2F5FA" }, rectRadius: 0.05 });
  slide.addText(number, { x, y: y + 0.1, w, h: h * 0.55, fontSize: 28, bold: true, color: NAVY, fontFace: "Calibri", align: "center" });
  slide.addText(label, { x, y: y + h * 0.55, w, h: h * 0.45, fontSize: 9, color: MUTED, fontFace: "Calibri", align: "center" });
}

// SLIDE 1 — Title
let s = darkSlide("Fragmented Experiences", "How the University of Melbourne's Web Estate Works Against Students");
s.addText("Evidence-based audit of 33,500+ pages across 18 domains · June 2026", { x: 0.8, y: 4.0, w: 11.7, h: 0.5, fontSize: 12, color: MUTED, fontFace: "Calibri" });

// SLIDE 2 — The core finding
s = contentSlide("A Student's Journey — Four Sites, No Map");
s.addText([
  { text: "One student. Three lifecycle stages. Four different websites — on four different domains, with four different information architectures and vocabularies.", options: { fontSize: 14, color: DARK } },
], { x: 0.5, y: 1.5, w: 7.5, h: 1.5, valign: "top" });

const domains = [
  ["study.unimelb.edu.au", "Prospective", "Course finder, how to apply"],
  ["students.unimelb.edu.au", "Current (central)", "Enrolment, support, admin"],
  ["{faculty}.unimelb.edu.au", "Current (faculty)", "Course plans, placements"],
  ["www.unimelb.edu.au/alumni", "Alumni", "Career tools, benefits"],
];
domains.forEach((d, i) => {
  const y = 3.3 + i * 0.95;
  s.addShape(pptx.ShapeType.rect, { x: 0.5, y, w: 0.08, h: 0.7, fill: { color: NAVY } });
  s.addText(d[0], { x: 0.8, y, w: 3.5, h: 0.4, fontSize: 11, bold: true, color: DARK, fontFace: "Calibri" });
  s.addText(d[2], { x: 4.5, y, w: 4, h: 0.4, fontSize: 10, color: MUTED, fontFace: "Calibri" });
  s.addText(d[1], { x: 8.5, y, w: 2, h: 0.4, fontSize: 9, color: NAVY, fontFace: "Calibri", bold: true, align: "right" });
});

statBox(s, "0", "links from current\nstudent pages to alumni", 9.0, 3.3, 3.8, 1.5);
s.addText("The graduation → alumni handoff is structurally absent", { x: 9.0, y: 5.2, w: 3.8, h: 0.6, fontSize: 10, color: NAVY, fontFace: "Calibri", bold: true });

// SLIDE 3 — Fragmentation spectrum
s = contentSlide("How Nine Faculties Diverged");
s.addText("Faculties fall on a spectrum from central-dependent to self-contained parallel ecosystems:", { x: 0.5, y: 1.5, w: 12, h: 0.5, fontSize: 13, color: DARK, fontFace: "Calibri" });

const spectrum = [
  ["ABP/MSD", "FBE", "Education", "Arts", "Science", "MDHS", "Law", "FFAM", "FEIT"],
  ["Central-dependent", "", "", "", "", "", "", "", "Self-contained"]
];
const sx = 0.5, sw = 1.35;
spectrum[0].forEach((name, i) => {
  const x = sx + i * sw;
  const shade = i < 3 ? "A8C4DD" : i < 6 ? NAVY : DARK;
  s.addShape(pptx.ShapeType.rect, { x, y: 2.4, w: sw - 0.05, h: 0.6, fill: { color: shade }, rectRadius: 0.03 });
  s.addText(name, { x, y: 2.45, w: sw - 0.05, h: 0.5, fontSize: 9, bold: true, color: i >= 3 ? WHITE : DARK, fontFace: "Calibri", align: "center" });
});

s.addText([
  { text: "FEIT & Law run entirely parallel systems — a student could complete their degree without discovering central services.", options: { fontSize: 11 } },
], { x: 0.5, y: 3.3, w: 12, h: 0.8, color: DARK, fontFace: "Calibri" });

statBox(s, "5", "different URL patterns\nfor 'current students'", 0.5, 4.3, 3.8, 1.3);
statBox(s, "5", "different names for\nthe same careers function", 4.8, 4.3, 3.8, 1.3);
statBox(s, "66", "items under a single\nLaw nav heading", 9.0, 4.3, 3.8, 1.3);

s.addText("Root cause: no content ownership governance + a template that manufactures duplication + accountability at faculty level with no counter-incentive.", { x: 0.5, y: 6.0, w: 12, h: 0.6, fontSize: 10, color: MUTED, fontFace: "Calibri", italic: true });

// SLIDE 4 — Topic duplication
s = contentSlide("Where the Duplication Hurts Most");
s.addText([
  { text: "Consolidation targets — central already owns these:", options: { bold: true, fontSize: 14, color: NAVY } },
], { x: 0.5, y: 1.5, w: 12, h: 0.5 });

const dupes = [
  ["Transactional admin", "6 of 227 pages on central hub", "25 pages restate one policy (special consideration)"],
  ["Scholarships", "0 pages on students.unimelb", "FEIT built 71-page shadow sub-site"],
  ["\"Employability in X\"", "7 identical gateway pages", "Same structure, different faculty name"],
  ["Special consideration", "25 faculty pages", "One policy (MPF1326), already centralised"],
  ["Wellbeing gateways", "6 near-identical pages", "\"Wellbeing + Ambassadors\" × 6"],
];
dupes.forEach((d, i) => {
  const y = 2.2 + i * 0.85;
  s.addShape(pptx.ShapeType.rect, { x: 0.5, y, w: 0.06, h: 0.7, fill: { color: NAVY } });
  s.addText(d[0], { x: 0.8, y, w: 3.5, h: 0.4, fontSize: 12, bold: true, color: DARK, fontFace: "Calibri" });
  s.addText(d[1], { x: 4.5, y, w: 3.5, h: 0.35, fontSize: 10, color: MUTED, fontFace: "Calibri" });
  s.addText(d[2], { x: 8.0, y, w: 5, h: 0.35, fontSize: 10, color: DARK, fontFace: "Calibri" });
});

// SLIDE 5 — What to keep
s = contentSlide("Where Faculty Ownership is Legitimate");
s.addText("Not all duplication is wrong — these topics genuinely belong with faculties:", { x: 0.5, y: 1.5, w: 12, h: 0.5, fontSize: 14, color: NAVY, bold: true, fontFace: "Calibri" });

const keep = [
  ["Placements & WIL", "207 pages, every faculty", "Clinical compliance, legal internships, teaching placements — discipline-bound by definition"],
  ["Course plans", "207 pages", "Degree-specific sample plans, program requirements (LANTITE, Fitness to Practice)"],
  ["Clubs & societies", "Faculty-owned", "Named clubs, ensembles, hackathons, mooting — requires discipline knowledge"],
  ["Academic skills", "Discipline methods", "Legal writing, lab reports, studio critique — not centralisable"],
];
keep.forEach((k, i) => {
  const y = 2.3 + i * 1.1;
  s.addShape(pptx.ShapeType.rect, { x: 0.5, y, w: 0.06, h: 0.9, fill: { color: "4CAF50" } });
  s.addText(k[0], { x: 0.8, y, w: 3.5, h: 0.4, fontSize: 12, bold: true, color: DARK, fontFace: "Calibri" });
  s.addText(k[1], { x: 4.5, y, w: 2.5, h: 0.35, fontSize: 10, color: MUTED, fontFace: "Calibri" });
  s.addText(k[2], { x: 7.2, y, w: 5.5, h: 0.8, fontSize: 10, color: DARK, fontFace: "Calibri" });
});

s.addText("\"Connect, don't centralise\" — centralise discovery, leave ownership with faculties.", { x: 0.5, y: 6.5, w: 12, h: 0.5, fontSize: 11, color: NAVY, fontFace: "Calibri", italic: true, bold: true });

// SLIDE 6 — Lifecycle
s = contentSlide("The Lifecycle Problem — Services Authored Three Times");
s.addText("Every cross-cutting service is independently written for prospective, current, and alumni stages:", { x: 0.5, y: 1.5, w: 12, h: 0.5, fontSize: 13, color: DARK, fontFace: "Calibri" });

const svc = [
  ["Careers & employability", "37", "80", "38", "Authored ~10 times across 4 domains"],
  ["Student life & community", "156", "108", "21", "Three framings, no narrative thread"],
  ["International support", "121", "100", "20", "Prospective + current + alumni, unlinked"],
  ["Wellbeing & health", "17", "46", "17", "Pastoral care × 3, no handoff"],
  ["Scholarships", "75", "113", "1", "Central catalogue exists, not surfaced"],
];
// Header
s.addText("Service", { x: 0.5, y: 2.2, w: 3.5, h: 0.4, fontSize: 10, bold: true, color: MUTED, fontFace: "Calibri" });
s.addText("Prosp.", { x: 4.3, y: 2.2, w: 1, h: 0.4, fontSize: 10, bold: true, color: MUTED, fontFace: "Calibri", align: "center" });
s.addText("Current", { x: 5.5, y: 2.2, w: 1, h: 0.4, fontSize: 10, bold: true, color: MUTED, fontFace: "Calibri", align: "center" });
s.addText("Alumni", { x: 6.7, y: 2.2, w: 1, h: 0.4, fontSize: 10, bold: true, color: MUTED, fontFace: "Calibri", align: "center" });
s.addText("Pattern", { x: 8.0, y: 2.2, w: 5, h: 0.4, fontSize: 10, bold: true, color: MUTED, fontFace: "Calibri" });

svc.forEach((r, i) => {
  const y = 2.7 + i * 0.65;
  s.addShape(pptx.ShapeType.rect, { x: 0.5, y, w: 0.04, h: 0.5, fill: { color: ICE } });
  s.addText(r[0], { x: 0.7, y, w: 3.5, h: 0.5, fontSize: 11, color: DARK, fontFace: "Calibri" });
  s.addText(r[1], { x: 4.3, y, w: 1, h: 0.5, fontSize: 14, bold: true, color: NAVY, fontFace: "Calibri", align: "center" });
  s.addText(r[2], { x: 5.5, y, w: 1, h: 0.5, fontSize: 14, bold: true, color: NAVY, fontFace: "Calibri", align: "center" });
  s.addText(r[3], { x: 6.7, y, w: 1, h: 0.5, fontSize: 14, bold: true, color: NAVY, fontFace: "Calibri", align: "center" });
  s.addText(r[4], { x: 8.0, y, w: 5, h: 0.5, fontSize: 10, color: MUTED, fontFace: "Calibri" });
});

// SLIDE 7 — Central gaps
s = contentSlide("What the Central Hub is Missing");
s.addText("Gaps in students.unimelb.edu.au that drive faculty duplication:", { x: 0.5, y: 1.5, w: 12, h: 0.5, fontSize: 14, color: NAVY, bold: true, fontFace: "Calibri" });

const gaps = [
  ["Placements & WIL", "Zero content — the largest faculty-owned topic has no central discovery page"],
  ["Scholarships for enrolled students", "Zero pages — an enrolled student looking for scholarships finds nothing"],
  ["Graduation spine", "Missing — no 'apply to graduate' or ceremony information on central hub"],
  ["Inbound international support", "Absent — visas, OSHC, ESOS compliance not covered centrally"],
  ["Course planning gateway", "My Course Planner tool exists but no guiding degree content surrounds it"],
];
gaps.forEach((g, i) => {
  const y = 2.3 + i * 0.85;
  s.addShape(pptx.ShapeType.rect, { x: 0.5, y, w: 0.06, h: 0.7, fill: { color: "E74C3C" } });
  s.addText(g[0], { x: 0.8, y, w: 3.5, h: 0.4, fontSize: 12, bold: true, color: DARK, fontFace: "Calibri" });
  s.addText(g[1], { x: 4.5, y, w: 8, h: 0.5, fontSize: 10, color: MUTED, fontFace: "Calibri" });
});

s.addText("Each gap has been filled — differently, inconsistently — by faculties acting independently.", { x: 0.5, y: 6.8, w: 12, h: 0.4, fontSize: 10, color: NAVY, fontFace: "Calibri", italic: true });

// SLIDE 8 — Research paradox
s = contentSlide("The Research Paradox");
s.addText("The faculties strongest in research support their research students the least:", { x: 0.5, y: 1.5, w: 12, h: 0.5, fontSize: 13, color: DARK, fontFace: "Calibri" });

const research = [
  ["MDHS", "63", "1"],
  ["Science", "60", "6"],
  ["Education", "44", "0"],
  ["Arts", "34", "27"],
  ["Law", "19", "79*"],
];
s.addText("Faculty", { x: 0.5, y: 2.3, w: 2.5, h: 0.4, fontSize: 10, bold: true, color: MUTED, fontFace: "Calibri" });
s.addText("Research pages", { x: 3.5, y: 2.3, w: 2.5, h: 0.4, fontSize: 10, bold: true, color: MUTED, fontFace: "Calibri", align: "center" });
s.addText("HDR student\nsupport pages", { x: 6.5, y: 2.2, w: 2.5, h: 0.6, fontSize: 10, bold: true, color: NAVY, fontFace: "Calibri", align: "center" });

research.forEach((r, i) => {
  const y = 3.0 + i * 0.65;
  s.addText(r[0], { x: 0.5, y, w: 2.5, h: 0.5, fontSize: 12, bold: true, color: DARK, fontFace: "Calibri" });
  s.addText(r[1], { x: 3.5, y, w: 2.5, h: 0.5, fontSize: 18, bold: true, color: NAVY, fontFace: "Calibri", align: "center" });
  s.addText(r[2], { x: 6.5, y, w: 2.5, h: 0.5, fontSize: 18, bold: true, color: "E74C3C", fontFace: "Calibri", align: "center" });
});

s.addText("* Law's 79 includes 61 researcher bios — only ~18 are genuine candidature support", { x: 0.5, y: 6.3, w: 10, h: 0.4, fontSize: 9, color: MUTED, fontFace: "Calibri", italic: true });
s.addText("Research is run as a reputation asset, decoupled from the student experience.", { x: 0.5, y: 6.7, w: 12, h: 0.4, fontSize: 11, color: NAVY, fontFace: "Calibri", bold: true });

// SLIDE 9 — Recommendations
s = contentSlide("Priority Recommendations");
s.addText("High priority — fix the seams", { x: 0.5, y: 1.5, w: 6, h: 0.5, fontSize: 14, bold: true, color: NAVY, fontFace: "Calibri" });

const recs = [
  ["1", "Graduation → alumni bridge", "Single page closing the most broken handoff"],
  ["2", "Connect faculty careers to alumni mentoring", "Cross-link existing content, no migration"],
  ["3", "Placements discovery page on hub", "Close the largest central gap"],
  ["4", "Decommission spec-con pages", "25 → 1 redirect; highest-impact lowest-effort"],
];
recs.forEach((r, i) => {
  const y = 2.2 + i * 0.7;
  s.addShape(pptx.ShapeType.ellipse, { x: 0.5, y: y + 0.05, w: 0.4, h: 0.4, fill: { color: NAVY } });
  s.addText(r[0], { x: 0.5, y: y + 0.05, w: 0.4, h: 0.4, fontSize: 14, bold: true, color: WHITE, fontFace: "Calibri", align: "center", valign: "middle" });
  s.addText(r[1], { x: 1.1, y, w: 5, h: 0.35, fontSize: 13, bold: true, color: DARK, fontFace: "Calibri" });
  s.addText(r[2], { x: 6.5, y, w: 6, h: 0.35, fontSize: 11, color: MUTED, fontFace: "Calibri" });
});

s.addText("High priority — standardise", { x: 0.5, y: 5.1, w: 5, h: 0.5, fontSize: 14, bold: true, color: NAVY, fontFace: "Calibri" });

const recs2 = [
  ["Standardise one URL convention", "/students across all faculties"],
  ["Establish shared vocabulary", "One label per function, enforced"],
  ["Mandate Education/Arts model", "Already works — issue as required template"],
];
recs2.forEach((r, i) => {
  const y = 5.7 + i * 0.45;
  s.addText(`→ ${r[0]}`, { x: 0.5, y, w: 6, h: 0.4, fontSize: 12, bold: true, color: DARK, fontFace: "Calibri" });
  s.addText(r[1], { x: 6.5, y, w: 6, h: 0.4, fontSize: 11, color: MUTED, fontFace: "Calibri" });
});

// SLIDE 10 — The fix
s = darkSlide("Connect, Don't Consolidate", "The majority of faculty content is legitimately faculty-owned.\nThe fix is to close the seams, fill the central gaps, and standardise the experience.");
s.addText([
  { text: "\"Connect, don't centralise\"", options: { italic: true, fontSize: 14, color: ICE } },
  { text: "\n\nCentralise discovery, leave ownership with faculties.\nClose the lifecycle handoffs students fall through.\nFill the central gaps that drive faculty duplication.\nStandardise the URL, the vocabulary, and the template.", options: { fontSize: 13, color: WHITE } },
], { x: 0.8, y: 4.8, w: 11.7, h: 2.5 });

// SLIDE 11 — By the numbers
s = contentSlide("The Estate by the Numbers");
const stats = [
  ["33,507", "pages crawled", "across 18 domains"],
  ["26,634", "with full HTML", "archived for analysis"],
  ["18", "domains", "15 complete"],
  ["5", "URL patterns", "for one concept"],
  ["0", "links", "current → alumni"],
];
stats.forEach((st, i) => {
  const x = 0.5 + i * 2.5;
  s.addShape(pptx.ShapeType.rect, { x, y: 1.8, w: 2.2, h: 2.5, fill: { color: "F2F5FA" }, rectRadius: 0.05 });
  s.addText(st[0], { x, y: 2.0, w: 2.2, h: 1.0, fontSize: 30, bold: true, color: NAVY, fontFace: "Calibri", align: "center" });
  s.addText(st[1], { x, y: 3.0, w: 2.2, h: 0.5, fontSize: 11, bold: true, color: DARK, fontFace: "Calibri", align: "center" });
  s.addText(st[2], { x, y: 3.5, w: 2.2, h: 0.5, fontSize: 9, color: MUTED, fontFace: "Calibri", align: "center" });
});

s.addText("Comprehensive crawl of the University of Melbourne's public web estate · June 2026 · Full technical audit available separately", { x: 0.5, y: 5.0, w: 12, h: 0.5, fontSize: 10, color: MUTED, fontFace: "Calibri", align: "center" });

// Domain list
const domainList = [
  "students.unimelb (833)  ·  msd (2,348)  ·  arts (2,446)  ·  fbe (2,241)  ·  education (852)",
  "eng (1,985)  ·  finearts-music (1,444)  ·  law (3,188)  ·  medicine (3,213)  ·  mdhs (6,072)",
  "science (420)  ·  mbs (83)  ·  biomed (1,584)  ·  dental (204)  ·  study (4,048)",
  "services (176)  ·  scholarships (2,226)  ·  alumni (137)"
];
domainList.forEach((line, i) => {
  s.addText(line, { x: 0.5, y: 5.7 + i * 0.35, w: 12, h: 0.35, fontSize: 9, color: MUTED, fontFace: "Calibri", align: "center" });
});

// Save
const outPath = "/Users/djmulholland/Documents/Claude/projects/unimelb-current-students-ia/report/insights-report.pptx";
pptx.writeFile({ fileName: outPath }).then(() => {
  console.log("PPTX saved:", outPath);
  const fs = require("fs");
  console.log("Size:", (fs.statSync(outPath).size / 1024).toFixed(1), "KB");
});
