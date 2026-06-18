const pptxgen = require("pptxgenjs");
const ASSETS = __dirname + "/assets";

const C = { navy:"000F46", navy2:"000B34", cyan:"46C8F0", cyandk:"2F95B7",
  ink:"1C1C28", light:"F4F4F4", tint:"EAF6FB", muted:"5B5B6B", white:"FFFFFF",
  ice:"C9CDE6", faint:"8F96C2", dim:"AAB0D4", linelt:"DDDDE7" };
const HEAD="Fraunces", BODY="Source Sans 3", MONO="Source Code Pro";
const LOGO_W=ASSETS+"/logo-white.png", LOGO_R=2600/818;

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.author = "University of Melbourne";
pres.title = "Current Students — End-to-End Experience (discussion)";

let PG = 0;
function footer(s){
  s.addText("Current Students: End-to-End Experience — alignment discussion · for discussion",
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
s1.addText("CURRENT STUDENTS · SERVICE EXPERIENCE",{x:1.08,y:2.48,w:10,h:0.38,fontFace:MONO,fontSize:12,color:C.cyan,bold:true,charSpacing:3,valign:"middle",margin:0});
s1.addText("The end-to-end student experience",{x:0.6,y:3.0,w:12,h:1.2,fontFace:HEAD,fontSize:44,color:C.white,bold:true,margin:0});
s1.addText("An alignment discussion on overlaps across our current-students websites",{x:0.63,y:4.35,w:10.6,h:0.7,fontFace:BODY,fontSize:18,color:C.ice,margin:0});
s1.addText("For discussion · June 2026",{x:0.63,y:5.1,w:8,h:0.4,fontFace:MONO,fontSize:12,color:C.dim,margin:0});
s1.addText("The University of Melbourne acknowledges the Traditional Owners of the unceded land on which we work, learn and live, and pays respect to their Elders, past and present, and to Indigenous Australians today.",
  {x:0.63,y:6.7,w:11.6,h:0.6,fontFace:BODY,fontSize:9.5,italic:true,color:"C9CDE6",margin:0});
s1.addNotes("Welcome. This is a discussion, not a decision meeting (~45 min). Frame: we're aligning on where the current-students experience overlaps across our websites, what's already underway, and what we might explore together. Make clear up front: no recommendations today — the data is a guide, the questions are the work.");

/* ============ 2 — About ============ */
const s2=content("About this session");
s2.addText([
 {text:"Our current-students content lives across many websites — the central hub, nine faculties and three schools. Students move between them, end to end.",options:{breakLine:true,paraSpaceAfter:14}},
 {text:"This is an alignment conversation: where do these experiences overlap, what is already underway to address them, and what might we do together.",options:{breakLine:true,paraSpaceAfter:14}},
 {text:"This pack is a discussion guide — not a set of recommendations. The data sets the scene; the questions are ours to work through.",options:{}}
],{x:0.62,y:1.5,w:11.9,h:2.4,fontFace:BODY,fontSize:17,color:C.ink,valign:"top",margin:0,lineSpacingMultiple:1.12});
s2.addText("TODAY'S TOPICS",{x:0.62,y:4.45,w:6,h:0.3,fontFace:MONO,fontSize:11,bold:true,color:C.cyandk,charSpacing:2,margin:0});
["Course planning","Employability","Faculty service requests","Applications for further study"].forEach((t,i)=>{
  const x=0.62+i*3.0;
  s2.addShape(pres.shapes.RECTANGLE,{x,y:4.95,w:2.78,h:0.78,fill:{color:C.navy}});
  s2.addShape(pres.shapes.RECTANGLE,{x,y:4.95,w:2.78,h:0.09,fill:{color:C.cyan}});
  s2.addText(t,{x:x+0.1,y:4.95,w:2.58,h:0.78,fontFace:BODY,fontSize:12.5,bold:true,color:C.white,align:"center",valign:"middle",margin:0});
});
s2.addNotes("Set expectations (~3 min): the data describes what exists and where — it is not a judgement. The four topics are our agenda. Invite people to hold their 'what should we do' ideas for the discussion prompts and the capture board near the end. Confirm everyone can see the four topics.");

/* ============ 3 — Journey ============ */
const s3=content("What students are trying to do");
s3.addText("Students don't experience our websites as 'central' or 'faculty' — they have needs that run across the whole year, and they cross between sites as they go.",
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
s3.addShape(pres.shapes.RECTANGLE,{x:0.62,y:5.05,w:11.9,h:1.05,fill:{color:C.tint}});
s3.addShape(pres.shapes.RECTANGLE,{x:0.62,y:5.05,w:0.1,h:1.05,fill:{color:C.cyan}});
s3.addText([{text:"To discuss:  ",options:{bold:true,color:C.navy}},
  {text:"Where in this journey do students cross between websites most — and where does that help or hinder them?",options:{color:C.navy2}}],
  {x:0.95,y:5.05,w:11.3,h:1.05,fontFace:BODY,fontSize:15,valign:"middle",margin:0});
s3.addNotes("Ground the room in the student's view (~4 min). The journey is illustrative, not a process map. Ask the opening question and capture early themes about where students hop between sites. Today's four topics each sit somewhere on this journey — flag that we'll go deep on those.");

/* ============ 4 — Landscape ============ */
const s4=content("The shared landscape");
s4.addText("A full content scan of the current-students estate — the central hub plus nine faculties and three schools. The same student need is often served in more than one place; some content is genuinely discipline-specific, and some is shared.",
  {x:0.62,y:1.45,w:11.9,h:1.0,fontFace:BODY,fontSize:15.5,color:C.ink,margin:0,lineSpacingMultiple:1.12});
[["1,161","pages of current-students content"],["13","separate websites"],["6","different web-address patterns"]].forEach(([n,l],i)=>{
  const x=0.62+i*4.12;
  s4.addShape(pres.shapes.RECTANGLE,{x,y:2.85,w:3.86,h:2.0,fill:{color:C.light}});
  s4.addShape(pres.shapes.RECTANGLE,{x,y:2.85,w:3.86,h:0.1,fill:{color:C.cyan}});
  s4.addText(n,{x,y:3.1,w:3.86,h:1.0,fontFace:HEAD,fontSize:52,bold:true,color:C.navy,align:"center",valign:"middle",margin:0});
  s4.addText(l,{x:x+0.25,y:4.1,w:3.36,h:0.6,fontFace:BODY,fontSize:13,color:C.muted,align:"center",margin:0});
});
s4.addText("Central hub · Architecture, Building & Planning · Arts · Business & Economics · Education · Engineering & IT · Fine Arts & Music · Law · Medicine, Dentistry & Health Sciences · Science  —  plus separate Business School, Biomedical Sciences and Dental school sites.",
  {x:0.62,y:5.2,w:11.9,h:0.9,fontFace:BODY,fontSize:12.5,italic:true,color:C.navy2,margin:0,lineSpacingMultiple:1.18});
s4.addText("Descriptive only — a scan of what exists and where, not an assessment.",
  {x:0.62,y:6.25,w:11.9,h:0.3,fontFace:MONO,fontSize:9.5,color:C.muted,margin:0});
s4.addNotes("Scale-setting (~2 min), don't dwell. The point is breadth: 13 sites, 6 address patterns. Reinforce the 'descriptive, not an assessment' note — we're not grading anyone's site today.");

/* ============ 5 — Overlap lens ============ */
const s5=content("A lens for today: overlap");
s5.addText("Overlap isn't automatically a problem. Sometimes it is helpful local context; sometimes it is duplicated effort or mixed messages. For each topic today, we will look at where the content sits — then ask whether the overlap is intentional, and whether it helps or hinders the student.",
  {x:0.62,y:1.55,w:6.3,h:4.0,fontFace:BODY,fontSize:17,color:C.ink,margin:0,valign:"top",lineSpacingMultiple:1.22});
s5.addShape(pres.shapes.OVAL,{x:7.55,y:2.1,w:3.1,h:3.1,fill:{color:C.navy,transparency:86},line:{color:C.navy,width:1.5}});
s5.addShape(pres.shapes.OVAL,{x:9.35,y:2.1,w:3.1,h:3.1,fill:{color:C.cyan,transparency:72},line:{color:C.cyandk,width:1.5}});
s5.addText("Central hub",{x:7.5,y:3.35,w:1.85,h:0.5,fontFace:BODY,fontSize:13,bold:true,color:C.navy,align:"center",valign:"middle",margin:0});
s5.addText([{text:"Faculty /",options:{breakLine:true}},{text:"school sites"}],{x:10.6,y:3.2,w:1.95,h:0.85,fontFace:BODY,fontSize:13,bold:true,color:C.navy,align:"center",valign:"middle",margin:0});
s5.addText("overlap",{x:9.43,y:4.08,w:1.15,h:0.35,fontFace:MONO,fontSize:11,bold:true,color:C.navy2,align:"center",margin:0});
s5.addNotes("Define overlap neutrally (~2 min): not inherently good or bad. This is the lens for every topic that follows — 'is the overlap intentional, and does it help or hinder the student?' Keep the room out of solution mode for now.");

/* ============ 6 — Overlap matrix ============ */
const s6=content("Overlap at a glance");
s6.addText("Where each topic is provided today, across the estate. The same need often appears in several places.",
  {x:0.62,y:1.4,w:11.9,h:0.5,fontFace:BODY,fontSize:15,color:C.ink,margin:0});
const hd=(t)=>({text:t,options:{fill:{color:C.navy},color:C.white,bold:true,fontSize:12,align:"left",valign:"middle"}});
const cl=(t)=>({text:t,options:{color:C.ink,fontSize:11.5,valign:"middle"}});
s6.addTable([
 [hd("Topic"),hd("Central hub"),hd("Faculties"),hd("Schools"),hd("Cross-linked?")],
 [cl("Course planning"),cl("Planner + Handbook"),cl("Every faculty"),cl("MBS, Biomedical"),cl("Partly")],
 [cl("Careers"),cl("Central platform"),cl("8 of 9"),cl("MBS"),cl("Rarely")],
 [cl("Placements / WIL"),cl("—"),cl("Every faculty"),cl("Some"),cl("—")],
 [cl("Service requests"),cl("Stop 1 + processes"),cl("Student centres + forms"),cl("Some"),cl("Mixed")],
 [cl("Further study"),cl("Some"),cl("Faculties"),cl("Some"),cl("Mixed")],
],{x:0.62,y:2.05,w:12.1,colW:[2.9,2.7,2.7,2.0,1.8],rowH:0.62,border:{type:"solid",pt:1,color:C.linelt},fontFace:BODY,valign:"middle",margin:[3,6,3,6],fill:{color:C.white}});
s6.addShape(pres.shapes.RECTANGLE,{x:0.62,y:6.05,w:11.9,h:0.7,fill:{color:C.tint}});
s6.addShape(pres.shapes.RECTANGLE,{x:0.62,y:6.05,w:0.1,h:0.7,fill:{color:C.cyan}});
s6.addText([{text:"To discuss:  ",options:{bold:true,color:C.navy}},
  {text:"Is this the right picture? Where is the overlap intentional and helpful — and where is it accidental?",options:{color:C.navy2}}],
  {x:0.95,y:6.05,w:11.3,h:0.7,fontFace:BODY,fontSize:14.5,valign:"middle",margin:0});
s6.addNotes("Walk the rows quickly (~5 min). Don't defend the marks — invite corrections and mark them live. 'Cross-linked?' means: do the central and faculty versions point to each other. The goal is a shared picture before we go topic by topic.");

/* ============ Topic helper ============ */
function topic(title, dataPts, questions, notes){
  const s=content(title);
  s.addText("WHAT THE DATA SHOWS",{x:0.62,y:1.4,w:6.6,h:0.3,fontFace:MONO,fontSize:11,bold:true,color:C.cyandk,charSpacing:2,margin:0});
  s.addText(dataPts.map(t=>({text:t,options:{bullet:{indent:16},breakLine:true,paraSpaceAfter:10}})),
    {x:0.62,y:1.8,w:6.65,h:5.0,fontFace:BODY,fontSize:13.5,color:C.ink,valign:"top",margin:0});
  s.addShape(pres.shapes.RECTANGLE,{x:7.62,y:1.4,w:5.11,h:5.3,fill:{color:C.tint}});
  s.addShape(pres.shapes.RECTANGLE,{x:7.62,y:1.4,w:0.1,h:5.3,fill:{color:C.cyan}});
  s.addText("TO DISCUSS",{x:7.95,y:1.62,w:4.6,h:0.3,fontFace:MONO,fontSize:11,bold:true,color:C.navy,charSpacing:2,margin:0});
  s.addText(questions.map(q=>({text:q,options:{bullet:{indent:16},breakLine:true,paraSpaceAfter:12}})),
    {x:7.95,y:2.06,w:4.55,h:4.5,fontFace:BODY,fontSize:14,color:C.navy2,valign:"top",margin:0});
  s.addNotes(notes);
}

topic("Course planning",
[
 "Around 207 pages relate to course planning — across the central hub (My Course Planner, the Handbook) and every faculty.",
 "Two schools — Business (MBS) and Biomedical Sciences — hold about 46% of it, a level below their faculty.",
 "It spans many forms: degree sample plans, subject-selection guides, breadth and diploma options, prerequisites and quotas, honours and research-project planning.",
 "The central planning tool is sometimes re-presented on faculty sites, and the section is reached through several different web addresses.",
],
[
 "Where do students actually start when planning their course?",
 "Which parts are genuinely degree-specific, and which are shared?",
 "What is already underway to align course planning?",
 "What would make course planning feel seamless to a student?",
],
"~6 min. Course planning is mostly degree-specific (legitimately faculty-owned), with a thin shared layer on top. Pull in faculty course-planning owners. Listen for: where the hub tool and faculty plans should connect, and whether labels/locations differ confusingly. Hold solutions for the capture board.");

topic("Employability",
[
 "Around 351 pages relate to employability — roughly 144 on careers and 207 on work-integrated learning (placements, internships).",
 "Careers content appears in 8 of 9 faculties, plus Melbourne Business School, alongside the central careers platform.",
 "Today the central and faculty careers content largely do not link to each other; several near-identical 'Employability in [discipline]' pages exist.",
 "Work-integrated learning sits entirely with faculties; there is no central placements page.",
],
[
 "How does a student discover careers and placement support — central, faculty, or both?",
 "Where does the current split serve students well, and where does it confuse?",
 "What is already in flight here (for example, the Employability Service Integration work)?",
 "What would a joined-up employability journey feel like?",
],
"~6 min. The richest topic. Note the Employability Service Integration (ESI) work is already in flight — invite that team to speak to it. Listen for: the careers central/faculty disconnect, and that WIL has no central front door. Keep neutral — surface, don't solve.");

topic("Faculty service requests",
[
 "Students request help — special consideration, forms, advising, enrolment changes — through several channels: Stop 1 centrally, faculty student centres, and around 210 faculty forms and admin pages.",
 "Some requests are university-wide processes (special consideration, leave of absence, fees); others are specific to a faculty or school.",
 "Across the estate, about 227 pages touch enrolment, exams, fees and special consideration — and the same process is often described in more than one place.",
 "Where a student starts (central or faculty) often differs from where the request is actually handled.",
],
[
 "When a student needs to request something, where do they go first — and where do they end up?",
 "Which service requests are genuinely faculty-specific, and which are university-wide?",
 "What is underway to streamline how students request service?",
 "Where are the hand-offs that frustrate students or duplicate effort?",
],
"~6 min. This is the service-model question. Bring in Stop 1 / faculty student-centre voices. Listen for: the hand-offs between central and faculty, and where students start vs where requests are resolved. Distinguish genuinely faculty-specific requests from university-wide ones.");

topic("Applications for further study",
[
 "'What next' content spans honours, graduate and coursework pathways, course transfers, concurrent diplomas, and research candidature.",
 "It sits across faculties and schools — for example faculty honours pages and graduate-pathway guides.",
 "It overlaps with admissions / future-students messaging, and with course-planning content.",
 "Research candidature alone is around 240 pages, largely held by faculties.",
],
[
 "How does a current student find out about further study options?",
 "Where should 'current student' stop and 'future student / admissions' begin?",
 "What is already underway to support student progression?",
 "How do we make the path to further study clear for current students?",
],
"~6 min. The trickiest boundary — current-student vs admissions/future-student content. Listen for: where the 'apply for further study' path lives and who owns it, and the overlap with course planning. Note any progression-support work already underway.");

/* ============ Worked example ============ */
const sw=content("One student, four topics");
sw.addShape(pres.shapes.RECTANGLE,{x:0.62,y:1.4,w:11.9,h:0.62,fill:{color:C.navy}});
sw.addText([{text:"Maya  ",options:{bold:true,color:C.white,fontSize:15}},{text:"· second-year Science undergraduate · one semester",options:{color:C.ice,fontSize:13}}],
  {x:0.85,y:1.4,w:11.5,h:0.62,fontFace:BODY,valign:"middle",margin:0});
const steps=[
 ["1","Course planning","Plans her second-year subjects","Hub planner + Science course guides"],
 ["2","Employability","Looks for a summer internship","Science WIL pages — nothing central"],
 ["3","Service request","Applies for special consideration","Starts at Stop 1 → handled by the faculty"],
 ["4","Further study","Starts weighing up Honours","Science Honours info (would compare faculties)"],
];
steps.forEach((st,i)=>{
  const y=2.25+i*0.86;
  sw.addShape(pres.shapes.OVAL,{x:0.7,y:y+0.04,w:0.5,h:0.5,fill:{color:C.cyan}});
  sw.addText(st[0],{x:0.7,y:y+0.04,w:0.5,h:0.5,fontFace:HEAD,fontSize:16,bold:true,color:C.navy,align:"center",valign:"middle",margin:0});
  sw.addText([{text:st[1]+"  —  ",options:{bold:true,color:C.navy}},{text:st[2],options:{color:C.ink}}],
    {x:1.4,y:y,w:7.7,h:0.6,fontFace:BODY,fontSize:14,valign:"middle",margin:0});
  sw.addShape(pres.shapes.RECTANGLE,{x:9.25,y:y+0.06,w:3.45,h:0.46,fill:{color:C.tint}});
  sw.addText(st[3],{x:9.35,y:y+0.06,w:3.3,h:0.46,fontFace:BODY,fontSize:10.5,color:C.navy2,valign:"middle",margin:0});
});
sw.addText([{text:"In one semester Maya crosses the central hub, her faculty site and a school site several times — with no single thread tying it together.    ",options:{italic:true,color:C.ink}},
  {text:"To discuss: where in this one journey would small changes make the biggest difference?",options:{bold:true,color:C.navy}}],
  {x:0.7,y:5.95,w:12.0,h:0.7,fontFace:BODY,fontSize:13.5,valign:"top",margin:0,lineSpacingMultiple:1.1});
sw.addNotes("~5 min. Make it concrete — one student, four topics, one semester. The right-hand tags show which site(s) she touches. The point is the experience is a single thread for her, even though our content isn't. Ask where small changes in her journey would help most.");

/* ============ Capture canvas ============ */
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

/* ============ Closing ============ */
const s9=pres.addSlide(); PG++; s9.background={color:C.navy};
s9.addShape(pres.shapes.RECTANGLE,{x:0.62,y:0.72,w:0.3,h:0.3,fill:{color:C.cyan}});
s9.addText("Where to from here — together",{x:1.06,y:0.6,w:11,h:0.7,fontFace:HEAD,fontSize:32,bold:true,color:C.white,valign:"middle",margin:0});
s9.addText("Not conclusions — questions to take forward.",{x:0.64,y:1.65,w:11,h:0.5,fontFace:BODY,fontSize:17,italic:true,color:C.cyan,margin:0});
s9.addText([
 "Across the four topics, what did we agree are the real overlaps?",
 "What is already in flight that we could connect or build on?",
 "For each topic — what is one thing we'd like to explore next, and who is involved?",
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

/* ============ Appendix — per-faculty matrix ============ */
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
sm.addText("* school-level site (runs its own current-students section below its faculty).  Page counts are descriptive — they show where content sits, not its quality. Source: full crawl, June 2026.",
  {x:0.62,y:6.55,w:11.9,h:0.4,fontFace:BODY,fontSize:10,italic:true,color:C.muted,margin:0});
sm.addNotes("Reference only. Per-faculty page counts by topic, from the full crawl. Schools (*) run their own sites. Use to answer 'how much does faculty X have for topic Y?' Bigger numbers = more content there, not better or worse.");

pres.writeFile({ fileName: __dirname + "/Current-Students-EndToEnd-Discussion.pptx" })
  .then(f=>console.log("WROTE", f, "·", PG, "slides"));
