const pptxgen = require("pptxgenjs");
const ASSETS = __dirname + "/assets";

const C = { navy:"000F46", navy2:"000B34", cyan:"46C8F0", cyandk:"2F95B7",
  ink:"1C1C28", light:"F4F4F4", tint:"EAF6FB", muted:"5B5B6B", white:"FFFFFF",
  ice:"C9CDE6", faint:"8F96C2", dim:"AAB0D4", linelt:"DDDDE7" };
const HEAD="Fraunces", BODY="Source Sans 3", MONO="Source Code Pro";
const LOGO_W=ASSETS+"/logo-white.svg", LOGO_R=576/181;

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.author = "University of Melbourne";
pres.title = "University of Melbourne — Web Estate Alignment Discussion";

let PG = 0;
function footer(s){
  s.addText("University of Melbourne — web estate alignment discussion · for discussion",
    {x:0.6,y:7.04,w:10.5,h:0.3,fontFace:BODY,fontSize:9,color:C.muted,margin:0});
  s.addText(String(PG),{x:12.3,y:7.04,w:0.45,h:0.3,fontFace:BODY,fontSize:9,color:C.muted,align:"right",margin:0});
}
function head(s, title){
  s.background={color:C.white};
  s.addShape(pres.shapes.RECTANGLE,{x:0.6,y:0.62,w:0.28,h:0.28,fill:{color:C.cyan}});
  s.addText(title,{x:1.0,y:0.5,w:11.7,h:0.55,fontFace:HEAD,fontSize:29,color:C.navy,bold:true,valign:"middle",margin:0});
  footer(s);
}
function content(title){ const s=pres.addSlide(); PG++; head(s,title); return s; }

/* ============ 1 — Title ============ */
const s1=pres.addSlide(); PG++; s1.background={color:C.navy};
s1.addImage({path:LOGO_W,x:0.6,y:0.55,w:2.2,h:2.2/LOGO_R});
s1.addShape(pres.shapes.RECTANGLE,{x:0.62,y:2.5,w:0.32,h:0.32,fill:{color:C.cyan}});
s1.addText("DIGITAL EXPERIENCE · ALIGNMENT DISCUSSION",{x:1.08,y:2.48,w:10,h:0.38,fontFace:MONO,fontSize:12,color:C.cyan,bold:true,charSpacing:3,valign:"middle",margin:0});
s1.addText("The end-to-end student experience",{x:0.6,y:3.0,w:12,h:1.2,fontFace:HEAD,fontSize:44,color:C.white,bold:true,margin:0});
s1.addText("An alignment conversation about overlaps across the University's web estate",{x:0.63,y:4.35,w:10.6,h:0.7,fontFace:BODY,fontSize:18,color:C.ice,margin:0});
s1.addText("For discussion · June 2026",{x:0.63,y:5.1,w:8,h:0.4,fontFace:MONO,fontSize:12,color:C.dim,margin:0});
s1.addText("The University of Melbourne acknowledges the Traditional Owners of the unceded land on which we work, learn and live, and pays respect to their Elders, past and present, and to Indigenous Australians today.",
  {x:0.63,y:6.7,w:11.6,h:0.6,fontFace:BODY,fontSize:9.5,italic:true,color:"C9CDE6",margin:0});
s1.addNotes("Welcome. This is a discussion, not a decision meeting (~45 min). Frame: we're aligning on where the University's web experiences overlap across our sites, what's already underway, and what we might explore together. Make clear up front: no recommendations today — the data is a guide, the questions are the work.");

/* ============ 2 — Journey ============ */
const s3=content("How users move across our websites");
s3.addText("Our websites are experienced as one University — not as separate sites. Users cross between them as they try to do things, and the seams show.",
  {x:0.62,y:1.45,w:11.9,h:0.8,fontFace:BODY,fontSize:16,color:C.ink,margin:0,lineSpacingMultiple:1.12});
const stages=["Orientate","Plan my course","Manage study","Get experience","Build my career","Get support","Finish & graduate"];
const jx0=1.05, jx1=12.0, jy=3.35;
s3.addShape(pres.shapes.LINE,{x:jx0,y:jy,w:jx1-jx0,h:0,line:{color:C.cyan,width:2}});
stages.forEach((st,i)=>{
  const cx=jx0+(jx1-jx0)*i/(stages.length-1);
  s3.addShape(pres.shapes.OVAL,{x:cx-0.19,y:jy-0.19,w:0.38,h:0.38,fill:{color:C.navy},line:{color:C.white,width:1.5}});
  s3.addText(String(i+1),{x:cx-0.19,y:jy-0.19,w:0.38,h:0.38,fontFace:BODY,fontSize:11,bold:true,color:C.white,align:"center",valign:"middle",margin:0});
  s3.addText(st,{x:cx-0.95,y:jy+0.28,w:1.9,h:0.7,fontFace:BODY,fontSize:11,bold:true,color:C.navy2,align:"center",valign:"top",margin:0});
});
s3.addText("Shown for a current student — the same pattern of crossing between sites applies across further study, alumni and faculty experiences.",
  {x:0.62,y:4.48,w:11.9,h:0.42,fontFace:MONO,fontSize:10,italic:true,color:C.muted,margin:0,align:"center"});
s3.addShape(pres.shapes.RECTANGLE,{x:0.62,y:5.05,w:11.9,h:1.05,fill:{color:C.tint}});
s3.addShape(pres.shapes.RECTANGLE,{x:0.62,y:5.05,w:0.1,h:1.05,fill:{color:C.cyan}});
s3.addText([{text:"To discuss:  ",options:{bold:true,color:C.navy}},
  {text:"Where do users cross between websites most — and where does that crossing help or hinder them?",options:{color:C.navy2}}],
  {x:0.95,y:5.05,w:11.3,h:1.05,fontFace:BODY,fontSize:15,valign:"middle",margin:0});
s3.addNotes("Ground the room in the user's view (~4 min). The journey is illustrative — it shows the current-student view, but the same crossing-between-sites experience applies to anyone moving through University web content. Ask the opening question and capture early themes. We'll go deeper on specific areas shortly.");

/* ============ 3 — Landscape ============ */
const s4=content("The shared landscape");
s4.addText("In June 2026, an automated browser visited every publicly reachable page — following links the same way a user would. Each page was read, classified and tagged by topic. The crawl covered the 12 faculty & school current-student sections and both estate-adjacent sites. The central Current Students Website (students.unimelb.edu.au) is the hub all these link into and was not separately crawled in this round.",
  {x:0.62,y:1.45,w:11.9,h:0.82,fontFace:BODY,fontSize:13.5,color:C.ink,margin:0,lineSpacingMultiple:1.12});
[["1,173","pages across 12 faculty\n& school current-student sites"],["300","study.unimelb\nprospective students"],["116","alumni.unimelb\ngraduate community"],["1,589","total pages\nreviewed"]].forEach(([n,l],i)=>{
  const x=0.62+i*3.06;
  s4.addShape(pres.shapes.RECTANGLE,{x,y:2.28,w:2.9,h:1.72,fill:{color:C.light}});
  s4.addShape(pres.shapes.RECTANGLE,{x,y:2.28,w:2.9,h:0.1,fill:{color:C.cyan}});
  s4.addText(n,{x,y:2.42,w:2.9,h:0.88,fontFace:HEAD,fontSize:44,bold:true,color:C.navy,align:"center",valign:"middle",margin:0});
  s4.addText(l,{x:x+0.1,y:3.32,w:2.7,h:0.56,fontFace:BODY,fontSize:11.5,color:C.muted,align:"center",margin:0,lineSpacingMultiple:1.1});
});
const themes=[
  ["Careers","4 parallel presences — Current Students Website, 8 faculties, study.unimelb, alumni. No cross-links in any direction."],
  ["Mentoring","12 faculty alumni programs matching student programs on all faculties. Neither side links to the other."],
  ["Course info","Enrolled students follow 529 links back to the prospective site — for content missing from their own."],
  ["Alumni handoff","0 current-student pages link forward to alumni, including graduation pages. No web path at exit."],
];
themes.forEach(([title,desc],i)=>{
  const x=0.62+i*3.06;
  s4.addShape(pres.shapes.RECTANGLE,{x,y:4.12,w:2.9,h:0.07,fill:{color:C.cyan}});
  s4.addText(title,{x,y:4.22,w:2.9,h:0.3,fontFace:BODY,fontSize:12,bold:true,color:C.navy,margin:0});
  s4.addText(desc,{x,y:4.56,w:2.9,h:1.02,fontFace:BODY,fontSize:11,color:C.muted,margin:0,lineSpacingMultiple:1.14});
});
s4.addText("Current Students Website · Architecture, Building & Planning · Arts · Business & Economics · Education · Engineering & IT · Fine Arts & Music · Law · Medicine, Dentistry & Health Sciences · Science · Melbourne Business School · Biomedical Sciences · Dental School · study.unimelb.edu.au · alumni.unimelb.edu.au",
  {x:0.62,y:5.76,w:11.9,h:0.62,fontFace:BODY,fontSize:11,italic:true,color:C.navy2,margin:0,lineSpacingMultiple:1.12});
s4.addNotes("Scale-setting and method (~3 min). Explain the crawl in one sentence: an automated browser, every public page, tagged by topic. The four stat cards cover all four parts of the estate. The four themes below are the main overlaps the data surfaced. Don't dwell — the discussion slides go deeper. We're not grading anyone's site today.");

/* ============ 4 — Overlap lens ============ */
const s5=content("Three phases of one student journey");
s5.addText("Students experience one University — not separate websites. When they need careers help, scholarship info, or study planning, that need may exist in any phase of the estate. Today: where does content appear in more than one place, and where are the handoffs between phases broken?",
  {x:0.62,y:1.55,w:6.3,h:2.6,fontFace:BODY,fontSize:16.5,color:C.ink,margin:0,valign:"top",lineSpacingMultiple:1.22});

// Three lifecycle phase boxes
// x layout: 7.35 | 1.35 box | 0.45 gap | 2.0 box | 0.45 gap | 1.1 box | = 7.35+5.35=12.7
const phaseBoxes=[
  {x:7.35,w:1.35,fill:C.tint,lc:C.cyandk,tc:C.navy,phase:"BEFORE\nENROLMENT",site:"study.unimelb\n.edu.au"},
  {x:9.15,w:2.0,fill:C.navy,lc:C.navy,tc:C.white,phase:"DURING STUDY",site:"students.unimelb.edu.au\n+ 12 faculty sites"},
  {x:11.6,w:1.1,fill:C.light,lc:C.linelt,tc:C.navy,phase:"AFTER\nGRADUATION",site:"alumni\n.unimelb.edu.au"},
];
phaseBoxes.forEach(({x,w,fill,lc,tc,phase,site})=>{
  s5.addShape(pres.shapes.RECTANGLE,{x,y:2.1,w,h:2.75,fill:{color:fill},line:{color:lc,width:1.5}});
  s5.addText(phase,{x,y:2.18,w,h:0.58,fontFace:MONO,fontSize:9,bold:true,color:tc===C.white?C.ice:C.cyandk,align:"center",margin:0,lineSpacingMultiple:1.1,charSpacing:0.5});
  s5.addText(site,{x:x+0.06,y:2.86,w:w-0.12,h:0.72,fontFace:BODY,fontSize:10.5,bold:true,color:tc,align:"center",margin:0,lineSpacingMultiple:1.12});
});
// Connection labels in the gaps
s5.addText("↔ 529 links",{x:8.48,y:3.2,w:0.88,h:0.3,fontFace:MONO,fontSize:8,color:C.navy2,align:"center",margin:0});
s5.addText("(intentional?)",{x:8.48,y:3.5,w:0.88,h:0.26,fontFace:MONO,fontSize:7.5,italic:true,color:C.muted,align:"center",margin:0});
s5.addText("→ 0 links",{x:11.15,y:3.2,w:0.68,h:0.3,fontFace:MONO,fontSize:8,color:C.muted,align:"center",margin:0});
s5.addText("out",{x:11.15,y:3.5,w:0.68,h:0.26,fontFace:MONO,fontSize:7.5,italic:true,color:C.muted,align:"center",margin:0});

// Overlap chips: content appearing across multiple phases
s5.addShape(pres.shapes.RECTANGLE,{x:7.35,y:5.0,w:5.35,h:0.3,fill:{color:C.navy}});
s5.addText("CONTENT APPEARING ACROSS MULTIPLE PHASES",{x:7.35,y:5.0,w:5.35,h:0.3,fontFace:MONO,fontSize:8,bold:true,color:C.cyan,align:"center",margin:0,charSpacing:0.8});
[
  ["Careers","all 4 estates\nnone connected"],
  ["Mentoring","both ends\nno web link"],
  ["Course info","study → enrolled\nno handoff"],
  ["Scholarships","3 sites + 1\nunused entry point"],
].forEach(([t,d],i)=>{
  const x=7.35+i*1.3375;
  s5.addShape(pres.shapes.RECTANGLE,{x,y:5.34,w:1.3,h:0.88,fill:{color:C.tint},line:{color:C.cyandk,width:0.75}});
  s5.addText(t,{x,y:5.37,w:1.3,h:0.34,fontFace:BODY,fontSize:11,bold:true,color:C.navy,align:"center",margin:0});
  s5.addText(d,{x,y:5.72,w:1.3,h:0.46,fontFace:MONO,fontSize:8.5,color:C.muted,align:"center",margin:0,lineSpacingMultiple:1.05});
});

s5.addNotes("Reframed as a lifecycle: three phases — before enrolment, during study, after graduation — and two key handoffs. The 529 links back to study.unimelb were deliberate (study.unimelb holds the canonical prospectus). Prompt the room: 'is the enrolled-student experience on those journeys working as intended?' The 0 links to alumni = no graduation handoff. Bottom chips: where the same content appears across multiple phases — these are today's discussion territory. Keep the room out of solution mode.");

/* ============ 5 — Overlap matrix ============ */
const s6=content("Overlap at a glance");
s6.addText("Where each topic is provided today, across the estate. The same need often appears in several places.",
  {x:0.62,y:1.4,w:11.9,h:0.5,fontFace:BODY,fontSize:15,color:C.ink,margin:0});
const hd=(t)=>({text:t,options:{fill:{color:C.navy},color:C.white,bold:true,fontSize:12,align:"left",valign:"middle"}});
const cl=(t)=>({text:t,options:{color:C.ink,fontSize:11.5,valign:"middle"}});
const cm=(t)=>({text:t,options:{color:C.muted,fontSize:11,italic:true,valign:"middle"}});
s6.addTable([
 [hd("Topic"),hd("Current Students\nWebsite"),hd("Faculties"),hd("Schools"),hd("Cross-linked?")],
 [cl("Course planning"),cl("Planner + Handbook"),cl("Every faculty"),cl("MBS, Biomedical"),cl("Partly")],
 [cl("Careers"),cl("Careers service"),cl("8 of 9 (141 pp)"),cl("MBS"),cl("Rarely")],
 [cl("Placements / WIL"),cl("—"),cl("Every faculty"),cl("Some"),cl("—")],
 [cl("Service requests"),cl("Stop 1 + processes"),cl("Student centres + forms"),cl("Some"),cl("Mixed")],
 [cl("Further study"),cl("Some"),cl("Faculties"),cl("Some"),cl("Mixed")],
 [cl("Alumni engagement"),cl("—"),cl("Some faculties (patchy)"),cl("MBS"),cl("No — 0 links")],
 [cl("study.unimelb"),cl("Entry paths"),cl("529 links back"),cl("—"),cl("One-way only")],
],{x:0.62,y:2.05,w:12.1,colW:[2.9,2.7,2.7,2.0,1.8],rowH:[0.60,0.50,0.50,0.50,0.50,0.50,0.50,0.50],border:{type:"solid",pt:1,color:C.linelt},fontFace:BODY,valign:"middle",margin:[3,6,3,6],fill:{color:C.white}});
s6.addShape(pres.shapes.RECTANGLE,{x:0.62,y:6.15,w:11.9,h:0.68,fill:{color:C.tint}});
s6.addShape(pres.shapes.RECTANGLE,{x:0.62,y:6.15,w:0.1,h:0.68,fill:{color:C.cyan}});
s6.addText([{text:"To discuss:  ",options:{bold:true,color:C.navy}},
  {text:"Is this the right picture of where things live? Where is the overlap helpful — and where is it accidental or frustrating?",options:{color:C.navy2}}],
  {x:0.95,y:6.15,w:11.3,h:0.68,fontFace:BODY,fontSize:13.5,valign:"middle",margin:0});
s6.addNotes("Walk the rows quickly (~5 min). Don't defend the marks — invite corrections and mark them live. 'Cross-linked?' means: do the current-students-website and faculty versions point to each other. Alumni and study.unimelb rows are from the June 2026 crawl — 0 links from current-student pages to alumni is confirmed. The goal is a shared picture before we open the discussion.");

/* ============ 6 — Open discussion ============ */
const sd=content("Where overlap shows up — and where it matters");
sd.addText([
  {text:"For each finding — the same three questions:",options:{bold:true,breakLine:true,paraSpaceAfter:16}},
  {text:"1.  Is the overlap intentional, or accidental?",options:{breakLine:true,paraSpaceAfter:10}},
  {text:"2.  Does it help or hinder the user?",options:{breakLine:true,paraSpaceAfter:10}},
  {text:"3.  Is someone already working on it?",options:{breakLine:true,paraSpaceAfter:28}},
  {text:"Use the capture board to note what we agree on, what's already in flight, what's worth exploring, and who's involved.",options:{color:C.muted}},
],{x:0.62,y:1.45,w:6.3,h:4.8,fontFace:BODY,fontSize:15.5,color:C.ink,valign:"top",margin:0,lineSpacingMultiple:1.22});
sd.addShape(pres.shapes.RECTANGLE,{x:7.35,y:1.4,w:5.37,h:5.3,fill:{color:C.tint}});
sd.addShape(pres.shapes.RECTANGLE,{x:7.35,y:1.4,w:0.1,h:5.3,fill:{color:C.cyan}});
sd.addText("WHAT THE DATA SHOWS",{x:7.68,y:1.62,w:4.9,h:0.3,fontFace:MONO,fontSize:11,bold:true,color:C.cyandk,charSpacing:2,margin:0});
[
  "Mentoring: 12 faculty alumni programs + matching student programs on all faculties. Neither side links to the other.",
  "Careers: 4 parallel presences — Current Students Website, 8 faculties, study.unimelb, alumni. No cross-links in any direction.",
  "Graduation exit: 0 current-student pages link to alumni, including graduation pages. No web path forward.",
  "study.unimelb: 529 links from faculty pages back to the prospective site — deliberate when study.unimelb was set up. Is the enrolled-student experience on these journeys working as intended?",
  "Scholarships: 3 separate presences — 141 faculty pages, 75 on study.unimelb, 1 on alumni. scholarships.unimelb.edu.au exists as a dedicated single entry point for all of them, but none of the three sites link to it.",
].forEach((a,i)=>{
  const y=2.1+i*0.86;
  sd.addShape(pres.shapes.RECTANGLE,{x:7.68,y,w:4.8,h:0.72,fill:{color:C.white},line:{color:C.linelt,width:1}});
  sd.addText(a,{x:7.82,y,w:4.6,h:0.72,fontFace:BODY,fontSize:11.5,color:C.navy2,valign:"middle",margin:0,lineSpacingMultiple:1.1});
});
sd.addNotes("Data-driven discussion (~15 min). Each finding on the right is from the June 2026 crawl — use them as conversation starters, not a rigid sequence. For each: is this the right picture? What explains it? Is someone already working on it? Capture themes on the next slide. Keep out of solution mode — we're mapping the territory, not resolving it today.");

/* ============ 7 — What's in flight ============ */
const sf=content("What's already in flight");
sf.addText("Initiatives already underway — to build on rather than duplicate.",
  {x:0.62,y:1.45,w:11.9,h:0.5,fontFace:BODY,fontSize:15,color:C.ink,margin:0});
const ih=(t)=>({text:t,options:{fill:{color:C.navy},color:C.white,bold:true,fontSize:12,align:"left",valign:"middle"}});
const ic=(t)=>({text:t,options:{color:C.ink,fontSize:12,valign:"middle"}});
const ig=(t)=>({text:t,options:{color:C.muted,fontSize:11.5,italic:true,valign:"middle"}});
sf.addTable([
  [ih("Initiative"),ih("Owner area"),ih("Status")],
  [ic("Employability Service Integration"),ic("Central Careers / Faculties"),ic("In progress")],
  [ig(""),ig(""),ig("")],
  [ig(""),ig(""),ig("")],
  [ig(""),ig(""),ig("")],
  [ig(""),ig(""),ig("")],
  [ig(""),ig(""),ig("")],
],{x:0.62,y:2.1,w:12.1,colW:[6.8,3.2,2.1],rowH:0.62,border:{type:"solid",pt:1,color:C.linelt},fontFace:BODY,valign:"middle",margin:[3,6,3,8],fill:{color:C.white}});
sf.addText("Pre-populate any known initiatives before the session — or capture from the room.",
  {x:0.62,y:6.55,w:11.9,h:0.3,fontFace:MONO,fontSize:9.5,color:C.muted,margin:0});
sf.addNotes("Ask: 'what's already underway in your area that touches these overlaps?' Pre-populate any known initiatives before the session. Goal: we don't want to invent solutions to problems someone else is already solving — connect first.");

/* ============ 8 — Capture canvas ============ */
const sc=content("Capturing today's discussion");
sc.addText("We'll capture the conversation here — to revisit together, not to conclude today.",
  {x:0.62,y:1.4,w:11.9,h:0.5,fontFace:BODY,fontSize:15,italic:true,color:C.ink,margin:0});
["Overlaps to align","Already in flight","Worth exploring","Owners / next step"].forEach((t,i)=>{
  const x=0.62+i*3.03;
  sc.addShape(pres.shapes.RECTANGLE,{x,y:2.1,w:2.88,h:0.6,fill:{color:C.navy}});
  sc.addText(t,{x:x+0.12,y:2.1,w:2.64,h:0.6,fontFace:BODY,fontSize:12.5,bold:true,color:C.white,align:"left",valign:"middle",margin:0});
  sc.addShape(pres.shapes.RECTANGLE,{x,y:2.7,w:2.88,h:3.9,fill:{color:C.light},line:{color:C.linelt,width:1}});
});
sc.addNotes("~5 min, capture mode. Fill the four columns from everything raised: overlaps people agreed on, work already in flight, things worth exploring, and a name against each. This is the artefact we take away.");

/* ============ 9 — Closing ============ */
const s9=pres.addSlide(); PG++; s9.background={color:C.navy};
s9.addShape(pres.shapes.RECTANGLE,{x:0.62,y:0.72,w:0.3,h:0.3,fill:{color:C.cyan}});
s9.addText("Where to from here — together",{x:1.06,y:0.6,w:11,h:0.7,fontFace:HEAD,fontSize:32,bold:true,color:C.white,valign:"middle",margin:0});
s9.addText("Not conclusions — questions to take forward.",{x:0.64,y:1.65,w:11,h:0.5,fontFace:BODY,fontSize:17,italic:true,color:C.cyan,margin:0});
s9.addText([
 "Across all areas: what did we agree are the real overlaps?",
 "What is already in flight that we could connect or build on?",
 "For the biggest overlap — what is one next step, and who is involved?",
 "How will we keep aligned as this work continues?",
].map(q=>({text:q,options:{bullet:{indent:18},breakLine:true,paraSpaceAfter:16}})),
 {x:0.66,y:2.5,w:11.4,h:3.6,fontFace:BODY,fontSize:18,color:C.white,valign:"top",margin:0});
s9.addImage({path:LOGO_W,x:10.5,y:6.62,w:2.2,h:2.2/LOGO_R});
s9.addText("Thank you · discussion",{x:0.66,y:6.8,w:6,h:0.4,fontFace:MONO,fontSize:12,color:"C9CDE6",margin:0});
s9.addNotes("~3 min. Land next steps as questions, not conclusions. Confirm who picks up what from the capture board, and how we'll stay aligned (e.g. a follow-up). Thank the room.");

/* ============ Appendix divider ============ */
const sa=pres.addSlide(); PG++; sa.background={color:C.navy2};
sa.addShape(pres.shapes.RECTANGLE,{x:0.62,y:3.2,w:0.32,h:0.32,fill:{color:C.cyan}});
sa.addText("Appendix",{x:1.08,y:3.05,w:10,h:0.7,fontFace:HEAD,fontSize:34,bold:true,color:C.white,valign:"middle",margin:0});
sa.addText("Backup detail — per-faculty data, for reference if the discussion calls for specifics.",{x:0.64,y:3.95,w:10.5,h:0.5,fontFace:BODY,fontSize:15,color:C.ice,margin:0});
sa.addNotes("Backup. Pull up the next slide only if the room wants faculty-level specifics.");

/* ============ Appendix A — per-faculty matrix (current-students) ============ */
const sm=content("Who holds what — pages by faculty and topic");
const ah=(t,al)=>({text:t,options:{fill:{color:C.navy},color:C.white,bold:true,fontSize:11,align:al||"left",valign:"middle"}});
const an=(t)=>({text:String(t),options:{color:C.ink,fontSize:11,align:"right",valign:"middle"}});
const af=(t)=>({text:t,options:{color:C.navy2,fontSize:11,bold:true,valign:"middle"}});
const M=[
 ["Arts",6,22,13,16,28],["ABP / MSD",29,13,9,26,43],["Business & Economics",8,2,0,1,8],
 ["Education",20,23,24,4,1],["Engineering & IT",2,19,17,1,31],["Fine Arts & Music",6,4,5,22,12],
 ["Law",11,24,36,66,86],["Medicine, Dentistry & HS",4,13,96,36,2],["Science",26,4,2,2,10],
 ["Melbourne Business School *",58,0,0,1,13],["Biomedical Sciences *",37,17,4,34,4],["Dental School *",0,0,0,3,3],
];
const mrows=[[ah("Faculty / school"),ah("Course\nplanning","right"),ah("Careers","right"),ah("Placements\n/ WIL","right"),ah("Forms\n/ admin","right"),ah("Research\ncandidature","right")]];
M.forEach(r=>mrows.push([af(r[0]),an(r[1]),an(r[2]),an(r[3]),an(r[4]),an(r[5])]));
sm.addTable(mrows,{x:0.62,y:1.45,w:12.1,colW:[3.4,1.74,1.74,1.74,1.74,1.74],rowH:0.4,
  border:{type:"solid",pt:1,color:C.linelt},fontFace:BODY,valign:"middle",margin:[2,6,2,6],fill:{color:C.white}});
sm.addText("* school-level site (runs its own current-students section below its faculty).  Page counts are descriptive — they show where content sits, not its quality. Source: current-students crawl, June 2026.",
  {x:0.62,y:6.55,w:11.9,h:0.4,fontFace:BODY,fontSize:10,italic:true,color:C.muted,margin:0});
sm.addNotes("Reference only. Per-faculty page counts by topic, from the current-students crawl. Schools (*) run their own sites. Use to answer 'how much does faculty X have for topic Y?' Bigger numbers = more content there, not better or worse.");

/* ============ Appendix B — broader estate (June 2026 crawl data) ============ */
const sb=content("The broader estate — where each topic lives");
sb.addText("Across all four parts of the University's web estate. Source: June 2026 crawl — 1,173 pages (current-students), 300 pages (study.unimelb), 116 pages (alumni.unimelb).",
  {x:0.62,y:1.45,w:11.9,h:0.65,fontFace:BODY,fontSize:14,color:C.ink,margin:0,lineSpacingMultiple:1.12});
const bh=(t,al)=>({text:t,options:{fill:{color:C.navy},color:C.white,bold:true,fontSize:11,align:al||"left",valign:"middle"}});
const bc=(t)=>({text:t,options:{color:C.ink,fontSize:11,valign:"middle"}});
const brows=[
  [bh("Topic area"),bh("Current Students\nWebsite","center"),bh("Faculty sites","center"),bh("Further study\n(study.)","center"),bh("Alumni","center")],
  [bc("Course / degree info"),bc("Planner + Handbook"),bc("Every faculty"),bc("224 pages — full coverage"),bc("—")],
  [bc("Careers"),bc("Careers service"),bc("8 of 9 (141 pp)"),bc("37 pages — entry only"),bc("38 pp + mentoring")],
  [bc("Placements / WIL"),bc("—"),bc("Every faculty\n(207 pp)"),bc("10 pages — overview"),bc("—")],
  [bc("Scholarships"),bc("—"),bc("Some (141 pp)"),bc("75 pages"),bc("1 page")],
  [bc("Research candidature"),bc("Thin"),bc("Heavy"),bc("1 page — entry only"),bc("1 page")],
  [bc("Alumni engagement"),bc("—"),bc("Some (patchy)"),bc("—"),bc("116 pages — full")],
  [bc("Service requests"),bc("Stop 1 + processes"),bc("Student centres"),bc("—"),bc("—")],
];
sb.addTable(brows,{x:0.62,y:2.2,w:12.1,colW:[3.4,2.5,2.5,2.1,1.6],rowH:0.47,
  border:{type:"solid",pt:1,color:C.linelt},fontFace:BODY,valign:"middle",margin:[2,6,2,6],fill:{color:C.white}});
sb.addText("Source: analysis/cross-site-overlap.md · crawl/pages/study-unimelb.json (300 pp) · crawl/pages/alumni-unimelb.json (116 pp)",
  {x:0.62,y:6.2,w:11.9,h:0.3,fontFace:MONO,fontSize:9,italic:true,color:C.muted,margin:0});
sb.addNotes("Reference only — broader view of the estate across all four circles from the overlap diagram. All page counts are from the June 2026 crawl. See analysis/cross-site-overlap.md for full breakdown and verdicts.");

pres.writeFile({ fileName: __dirname + "/Current-Students-EndToEnd-Discussion.pptx" })
  .then(f=>console.log("WROTE", f, "·", PG, "slides"));
