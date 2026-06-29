#!/usr/bin/env python3
"""Wrap existing DEAG report HTMLs in UoM LHS nav framing."""
import os, re

BASE = '/Users/djmulholland/Documents/Claude/projects/unimelb-current-students-ia'
REPO = '/unimelb-current-students-ia'

# The 6 DEAG reports that need LHS nav
REPORTS = [
    ("Improvements-Register.html", "Improvements Register", "~75 actionable improvements with severity, effort, and evidence citations."),
    ("Lifecycle-Journeys.html", "Lifecycle Journeys & Moments", "Six persona traces and four high-stakes moments through the estate."),
    ("Course-Planning-Enrolment.html", "Course Planning & Enrolment", "The most fragmented single task — a seven-system obstacle course."),
    ("International-Student-Experience.html", "International Student Experience", "Nine stages — where a web fault costs a visa, not convenience."),
    ("Student-Services-Fragmentation.html", "Student Services Fragmentation", "Counselling branded \"Academic Skills Unit\" — the wellbeing audit."),
    ("Careers-Employability-WIL.html", "Careers, Employability & WIL", "1,058 careers pages across 18 domains — authored everywhere, connected nowhere."),
]

NAV_ITEMS = [
    ("Home", f"{REPO}/index.html", "🏠"),
    ("Project Summary", None, "📊"),
    ("Five Root Findings", None, "🎯"),
    ("---", None, ""),
    ("Key Reports", None, "📋"),
    ("  Improvements Register", f"{REPO}/report/Improvements-Register.html", ""),
    ("  Lifecycle Journeys", f"{REPO}/report/Lifecycle-Journeys.html", ""),
    ("  Course Planning", f"{REPO}/report/Course-Planning-Enrolment.html", ""),
    ("  International Student", f"{REPO}/report/International-Student-Experience.html", ""),
    ("  Services Fragmentation", f"{REPO}/report/Student-Services-Fragmentation.html", ""),
    ("  Careers & WIL", f"{REPO}/report/Careers-Employability-WIL.html", ""),
    ("---", None, ""),
    ("Structural Deep-Dives", None, "🔬"),
    ("  Graduation → Alumni", f"{REPO}/analysis/graduation-alumni-handoff.html", ""),
    ("  Careers Online Wiring", f"{REPO}/analysis/careers-online-wiring.html", ""),
    ("  Prospective → Current", f"{REPO}/analysis/prospective-current-handoff.html", ""),
    ("  Equity & Indigenous", f"{REPO}/analysis/equity-indigenous-journey.html", ""),
    ("  HDR Duplication", f"{REPO}/analysis/hdr-candidature-duplication.html", ""),
    ("  Forms & Microsites", f"{REPO}/analysis/forms-microsite-audit.html", ""),
    ("---", None, ""),
    ("Content Quality", None, "📝"),
    ("  The Handbook", f"{REPO}/analysis/the-handbook.html", ""),
    ("  Fees & Finance", f"{REPO}/analysis/fees-finance.html", ""),
    ("  Scholarships", f"{REPO}/analysis/scholarships.html", ""),
    ("  Mobile & Performance", f"{REPO}/analysis/mobile-performance-audit.html", ""),
    ("  Content Freshness", f"{REPO}/analysis/content-freshness-sandbox-leakage.html", ""),
    ("  Content Quality Audit", f"{REPO}/analysis/content-quality-deep-dive.html", ""),
    ("---", None, ""),
    ("Authenticated Core", None, "🔐"),
    ("  Auth Core Audit", f"{REPO}/analysis/authenticated-core-audit.html", ""),
    ("  Live Host Check", f"{REPO}/analysis/auth-hosts-live-check.html", ""),
    ("  Auth Core Findings", f"{REPO}/analysis/authenticated-core-findings.html", ""),
    ("---", None, ""),
    ("Crawl Analyses", None, "🌐"),
    ("  ask.unimelb", f"{REPO}/analysis/crawl-ask-unimelb.html", ""),
    ("  gradresearch", f"{REPO}/analysis/crawl-gradresearch.html", ""),
    ("  murrupbarak", f"{REPO}/analysis/crawl-murrupbarak.html", ""),
    ("  safercommunity", f"{REPO}/analysis/crawl-safercommunity.html", ""),
    ("  umsu", f"{REPO}/analysis/crawl-umsu.html", ""),
    ("  online.unimelb", f"{REPO}/analysis/crawl-online.html", ""),
    ("  sport", f"{REPO}/analysis/crawl-sport.html", ""),
    ("  library", f"{REPO}/analysis/crawl-library.html", ""),
    ("  studentit", f"{REPO}/analysis/crawl-studentit.html", ""),
    ("---", None, ""),
    ("Personas", None, "👤"),
    ("  Sam — Planning", f"{REPO}/personas/sam-planning-their-path.html", ""),
    ("  Alex — At-risk", f"{REPO}/personas/alex-at-risk-withdrawal.html", ""),
    ("  Priya — International", f"{REPO}/personas/priya-international-student.html", ""),
    ("  Jordan — Course Maze", f"{REPO}/personas/jordan-course-planning-maze.html", ""),
    ("  Taylor — Wellbeing", f"{REPO}/personas/taylor-wellbeing-mental-health.html", ""),
    ("---", None, ""),
    ("Deliverables", None, "📦"),
    ("  Governance Pack", f"{REPO}/analysis/governance-summary-pack.html", ""),
    ("  Quick Wins", f"{REPO}/analysis/quick-wins-checklist.html", ""),
    ("  Final Synthesis", f"{REPO}/analysis/final-synthesis.html", ""),
]

CSS = f"""@font-face{{font-family:'Fraunces';src:url('{REPO}/assets/fonts/Fraunces-VariableFont_SOFT_WONK_opsz_wght.ttf') format('truetype');font-weight:100 900;font-display:swap}}
@font-face{{font-family:'Source Sans 3';src:url('{REPO}/assets/fonts/SourceSans3-VariableFont_wght.ttf') format('truetype');font-weight:200 900;font-display:swap}}
@font-face{{font-family:'Source Code Pro';src:url('{REPO}/assets/fonts/SourceCodePro-VariableFont_wght.ttf') format('truetype');font-weight:200 900;font-display:swap}}
:root{{--navy:#000F46;--navy-light:#1B2D5C;--cyan:#46C8F0;--ink:#222;--ink-2:#555;--bg:#fff;--bg-nav:#000F46;--bg-subtle:#F3F3F6;--border:#DDDDE7;--red:#DB1927;--amber:#AC5907;--green:#31733B;--font-h:'Fraunces',Georgia,serif;--font-b:'Source Sans 3',system-ui,sans-serif;--font-m:'Source Code Pro',monospace;--nav-w:280px}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:var(--font-b);font-size:17px;line-height:1.65;color:var(--ink);background:var(--bg);display:flex;min-height:100vh;-webkit-font-smoothing:antialiased}}
a{{color:#004EAD;text-decoration:none}}a:hover{{text-decoration:underline}}
nav.lhs{{position:fixed;top:0;left:0;width:var(--nav-w);height:100vh;background:var(--bg-nav);color:#C9CDE6;overflow-y:auto;z-index:100;display:flex;flex-direction:column;font-size:14px;line-height:1.4}}
nav.lhs .logo{{padding:24px 20px 16px;border-bottom:1px solid rgba(255,255,255,.1)}}
nav.lhs .logo img{{height:26px}}
nav.lhs .logo a{{display:block;color:#fff;font-family:var(--font-h);font-size:16px;font-weight:600;text-decoration:none;margin-top:8px}}
nav.lhs .nav-scroll{{flex:1;overflow-y:auto;padding:8px 0 24px}}
nav.lhs .section{{font-family:var(--font-m);font-size:11px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--cyan);padding:16px 20px 6px}}
nav.lhs a.nav-link{{display:block;padding:5px 20px;color:#9BA3C4;text-decoration:none;transition:all .15s;border-left:3px solid transparent}}
nav.lhs a.nav-link:hover{{color:#fff;background:rgba(255,255,255,.05)}}
nav.lhs a.nav-link.active{{color:#fff;background:rgba(255,255,255,.08);border-left-color:var(--cyan)}}
nav.lhs .sep{{border:none;border-top:1px solid rgba(255,255,255,.08);margin:8px 16px}}
nav.lhs .footer{{padding:16px 20px;font-size:11px;color:#6B7394;border-top:1px solid rgba(255,255,255,.08)}}
main{{margin-left:var(--nav-w);flex:1;min-width:0;padding:40px 56px 80px;max-width:900px}}
main h1{{font-family:var(--font-h);font-size:42px;font-weight:700;color:var(--navy);line-height:1.07;letter-spacing:-.012em;margin:0 0 8px}}
main h2{{font-family:var(--font-h);font-size:28px;font-weight:600;color:var(--navy);margin:48px 0 16px;padding-bottom:8px;border-bottom:2px solid var(--border);line-height:1.15}}
main h3{{font-family:var(--font-h);font-size:20px;font-weight:600;color:var(--navy);margin:32px 0 10px;line-height:1.2}}
main h4{{font-size:18px;font-weight:700;color:var(--navy);margin:24px 0 8px}}
main p{{margin:12px 0}}
main .subtitle{{color:var(--ink-2);font-style:italic;font-size:18px;margin-bottom:32px}}
main blockquote{{border-left:3px solid var(--navy);padding:12px 20px;margin:20px 0;background:var(--bg-subtle);font-style:italic;color:var(--ink-2)}}
main table{{width:100%;border-collapse:collapse;margin:16px 0;font-size:15px}}
main th{{background:var(--navy);color:#fff;padding:10px 14px;text-align:left;font-weight:600}}
main td{{padding:8px 14px;border-bottom:1px solid var(--border)}}
main tr:nth-child(even) td{{background:var(--bg-subtle)}}
main ul,main ol{{margin:8px 0 8px 24px}}
main li{{margin:4px 0}}
main hr{{border:none;border-top:1px solid var(--border);margin:40px 0}}
main strong{{color:var(--navy)}}
.menu-toggle{{display:none;position:fixed;top:12px;left:12px;z-index:200;background:var(--navy);color:#fff;border:none;border-radius:6px;padding:8px 12px;font-size:20px;cursor:pointer}}
@media(max-width:960px){{nav.lhs{{transform:translateX(-100%);transition:transform .25s}}nav.lhs.open{{transform:translateX(0)}}main{{margin-left:0;padding:60px 24px 40px}}.menu-toggle{{display:block}}}}
"""

def build_nav(current_href):
    nav = '<nav class="lhs" id="lhsNav">\n'
    nav += f'  <div class="logo">\n    <img src="{REPO}/assets/UoM_Logo_Horiz_onDark.svg" alt="UoM">\n    <a href="{REPO}/index.html">Current Students IA</a>\n  </div>\n'
    nav += '  <div class="nav-scroll">\n'
    for label, href, icon in NAV_ITEMS:
        if label == '---': nav += '    <hr class="sep">\n'
        elif href is None: nav += f'    <div class="section">{icon} {label}</div>\n'
        else:
            cls = 'nav-link active' if href == current_href else 'nav-link'
            nav += f'    <a class="{cls}" href="{href}">{icon} {label.strip()}</a>\n'
    nav += '  </div>\n  <div class="footer">UoM · Student Experience &amp; Design<br>June 2026 · 41,533 pages · 31 domains</div>\n</nav>\n'
    return nav

os.chdir(BASE)
for filename, title, subtitle in REPORTS:
    src = os.path.join('report', filename)
    if not os.path.exists(src):
        print(f"SKIP: {src}")
        continue
    
    with open(src, 'r') as f:
        old = f.read()
    
    # Extract body content — everything between <body> and </body>, minus old nav/hero/footer
    body_match = re.search(r'<body[^>]*>(.*)</body>', old, re.DOTALL)
    if not body_match:
        print(f"SKIP: {src} — no body found")
        continue
    
    body = body_match.group(1)
    
    # Strip old topnav, hero, etc
    body = re.sub(r'<nav[^>]*>.*?</nav>', '', body, flags=re.DOTALL)
    body = re.sub(r'<header[^>]*>.*?</header>', '', body, flags=re.DOTALL)
    body = re.sub(r'<footer[^>]*>.*?</footer>', '', body, flags=re.DOTALL)
    body = re.sub(r'<div[^>]*class="[^"]*topnav[^"]*"[^>]*>.*?</div>', '', body, flags=re.DOTALL)
    body = re.sub(r'<div[^>]*class="[^"]*hero[^"]*"[^>]*>.*?</div>', '', body, flags=re.DOTALL)
    body = re.sub(r'<div[^>]*class="[^"]*statstrip[^"]*"[^>]*>.*?</div>', '', body, flags=re.DOTALL)
    body = re.sub(r'<div[^>]*class="[^"]*footer[^"]*"[^>]*>.*?</div>', '', body, flags=re.DOTALL)
    body = re.sub(r'<div[^>]*class="[^"]*footnote[^"]*"[^>]*>.*?</div>', '', body, flags=re.DOTALL)
    
    # Clean up: change old font-family declarations for headings to use our fonts, stick body text
    body = re.sub(r"font-family:['\"]?Fraunces['\"]?", "font-family:var(--font-h)", body)
    body = re.sub(r"font-family:['\"]?Source Sans 3['\"]?", "font-family:var(--font-b)", body)
    
    href = f"{REPO}/report/{filename}"
    nav_html = build_nav(href)
    
    new = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · UoM Current Students IA</title>
<style>{CSS}</style>
</head>
<body>
<button class="menu-toggle" onclick="document.getElementById('lhsNav').classList.toggle('open')">☰</button>
{nav_html}
<main>
<h1>{title}</h1>
<p class="subtitle">{subtitle}</p>
{body}
</main>
</body>
</html>"""
    
    with open(src, 'w') as f:
        f.write(new)
    
    print(f"✅ {filename}")

print("\nDone.")
