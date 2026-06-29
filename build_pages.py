#!/usr/bin/env python3
"""Convert markdown analysis files to UoM-styled HTML with LHS navigation framing."""
import sys, re, os

BASE_PATH = '/unimelb-current-students-ia'

NAV_ITEMS = [
    ("Home", BASE_PATH + "/index.html", "🏠"),
    ("Project Summary", None, "📊"),
    ("Five Root Findings", None, "🎯"),
    ("---", None, ""),
    ("Key Reports", None, "📋"),
    ("  Improvements Register", BASE_PATH + "/report/Improvements-Register.html", ""),
    ("  Lifecycle Journeys", BASE_PATH + "/report/Lifecycle-Journeys.html", ""),
    ("  Course Planning", BASE_PATH + "/report/Course-Planning-Enrolment.html", ""),
    ("  International Student", BASE_PATH + "/report/International-Student-Experience.html", ""),
    ("  Services Fragmentation", BASE_PATH + "/report/Student-Services-Fragmentation.html", ""),
    ("  Careers & WIL", BASE_PATH + "/report/Careers-Employability-WIL.html", ""),
    ("---", None, ""),
    ("Structural Deep-Dives", None, "🔬"),
    ("  Graduation → Alumni", BASE_PATH + "/analysis/graduation-alumni-handoff.html", ""),
    ("  Careers Online Wiring", BASE_PATH + "/analysis/careers-online-wiring.html", ""),
    ("  Prospective → Current", BASE_PATH + "/analysis/prospective-current-handoff.html", ""),
    ("  Equity & Indigenous", BASE_PATH + "/analysis/equity-indigenous-journey.html", ""),
    ("  HDR Duplication", BASE_PATH + "/analysis/hdr-candidature-duplication.html", ""),
    ("  Forms & Microsites", BASE_PATH + "/analysis/forms-microsite-audit.html", ""),
    ("---", None, ""),
    ("Content Quality", None, "📝"),
    ("  The Handbook", BASE_PATH + "/analysis/the-handbook.html", ""),
    ("  Fees & Finance", BASE_PATH + "/analysis/fees-finance.html", ""),
    ("  Scholarships", BASE_PATH + "/analysis/scholarships.html", ""),
    ("  Mobile & Performance", BASE_PATH + "/analysis/mobile-performance-audit.html", ""),
    ("  Content Freshness", BASE_PATH + "/analysis/content-freshness-sandbox-leakage.html", ""),
    ("  Content Quality Audit", BASE_PATH + "/analysis/content-quality-deep-dive.html", ""),
    ("---", None, ""),
    ("Authenticated Core", None, "🔐"),
    ("  Auth Core Audit", BASE_PATH + "/analysis/authenticated-core-audit.html", ""),
    ("  Live Host Check", BASE_PATH + "/analysis/auth-hosts-live-check.html", ""),
    ("  Auth Core Findings", BASE_PATH + "/analysis/authenticated-core-findings.html", ""),
    ("---", None, ""),
    ("Crawl Analyses", None, "🌐"),
    ("  ask.unimelb", BASE_PATH + "/analysis/crawl-ask-unimelb.html", ""),
    ("  gradresearch", BASE_PATH + "/analysis/crawl-gradresearch.html", ""),
    ("  murrupbarak", BASE_PATH + "/analysis/crawl-murrupbarak.html", ""),
    ("  safercommunity", BASE_PATH + "/analysis/crawl-safercommunity.html", ""),
    ("  umsu", BASE_PATH + "/analysis/crawl-umsu.html", ""),
    ("  online.unimelb", BASE_PATH + "/analysis/crawl-online.html", ""),
    ("  sport", BASE_PATH + "/analysis/crawl-sport.html", ""),
    ("  library", BASE_PATH + "/analysis/crawl-library.html", ""),
    ("  studentit", BASE_PATH + "/analysis/crawl-studentit.html", ""),
    ("---", None, ""),
    ("Personas", None, "👤"),
    ("  Sam — Planning", BASE_PATH + "/personas/sam-planning-their-path.html", ""),
    ("  Alex — At-risk", BASE_PATH + "/personas/alex-at-risk-withdrawal.html", ""),
    ("  Priya — International", BASE_PATH + "/personas/priya-international-student.html", ""),
    ("  Jordan — Course Maze", BASE_PATH + "/personas/jordan-course-planning-maze.html", ""),
    ("  Taylor — Wellbeing", BASE_PATH + "/personas/taylor-wellbeing-mental-health.html", ""),
    ("---", None, ""),
    ("Deliverables", None, "📦"),
    ("  Governance Pack", BASE_PATH + "/analysis/governance-summary-pack.html", ""),
    ("  Quick Wins", BASE_PATH + "/analysis/quick-wins-checklist.html", ""),
    ("  Final Synthesis", BASE_PATH + "/analysis/final-synthesis.html", ""),
]

CSS = """@font-face{font-family:'Fraunces';src:url('''' + BASE_PATH + '''/assets/fonts/Fraunces-VariableFont_SOFT_WONK_opsz_wght.ttf') format('truetype');font-weight:100 900;font-display:swap}
@font-face{font-family:'Source Sans 3';src:url('''' + BASE_PATH + '''/assets/fonts/SourceSans3-VariableFont_wght.ttf') format('truetype');font-weight:200 900;font-display:swap}
@font-face{font-family:'Source Code Pro';src:url('''' + BASE_PATH + '''/assets/fonts/SourceCodePro-VariableFont_wght.ttf') format('truetype');font-weight:200 900;font-display:swap}
:root{--navy:#000F46;--navy-light:#1B2D5C;--cyan:#46C8F0;--ink:#222;--ink-2:#555;--bg:#fff;--bg-nav:#000F46;--bg-subtle:#F3F3F6;--border:#DDDDE7;--red:#DB1927;--amber:#AC5907;--green:#31733B;--font-h:'Fraunces',Georgia,serif;--font-b:'Source Sans 3',system-ui,sans-serif;--font-m:'Source Code Pro',monospace;--nav-w:280px}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:var(--font-b);font-size:17px;line-height:1.65;color:var(--ink);background:var(--bg);display:flex;min-height:100vh;-webkit-font-smoothing:antialiased}
a{color:#004EAD;text-decoration:none}a:hover{text-decoration:underline}

/* ── LHS Navigation ── */
nav.lhs{position:fixed;top:0;left:0;width:var(--nav-w);height:100vh;background:var(--bg-nav);color:#C9CDE6;overflow-y:auto;z-index:100;display:flex;flex-direction:column;font-size:14px;line-height:1.4}
nav.lhs .logo{padding:24px 20px 16px;border-bottom:1px solid rgba(255,255,255,.1)}
nav.lhs .logo img{height:26px}
nav.lhs .logo a{display:block;color:#fff;font-family:var(--font-h);font-size:16px;font-weight:600;text-decoration:none;margin-top:8px}
nav.lhs .nav-scroll{flex:1;overflow-y:auto;padding:8px 0 24px}
nav.lhs .section{font-family:var(--font-m);font-size:11px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--cyan);padding:16px 20px 6px}
nav.lhs a.nav-link{display:block;padding:5px 20px;color:#9BA3C4;text-decoration:none;transition:all .15s;border-left:3px solid transparent}
nav.lhs a.nav-link:hover{color:#fff;background:rgba(255,255,255,.05)}
nav.lhs a.nav-link.active{color:#fff;background:rgba(255,255,255,.08);border-left-color:var(--cyan)}
nav.lhs .sep{border:none;border-top:1px solid rgba(255,255,255,.08);margin:8px 16px}
nav.lhs .footer{padding:16px 20px;font-size:11px;color:#6B7394;border-top:1px solid rgba(255,255,255,.08)}

/* ── Main content ── */
main{margin-left:var(--nav-w);flex:1;min-width:0;padding:40px 56px 80px;max-width:900px}
main h1{font-family:var(--font-h);font-size:42px;font-weight:700;color:var(--navy);line-height:1.07;letter-spacing:-.012em;margin:0 0 8px}
main h2{font-family:var(--font-h);font-size:28px;font-weight:600;color:var(--navy);margin:48px 0 16px;padding-bottom:8px;border-bottom:2px solid var(--border);line-height:1.15}
main h3{font-family:var(--font-h);font-size:20px;font-weight:600;color:var(--navy);margin:32px 0 10px;line-height:1.2}
main h4{font-size:18px;font-weight:700;color:var(--navy);margin:24px 0 8px}
main p{margin:12px 0}
main .subtitle{color:var(--ink-2);font-style:italic;font-size:18px;margin-bottom:32px}
main blockquote{border-left:3px solid var(--navy);padding:12px 20px;margin:20px 0;background:var(--bg-subtle);font-style:italic;color:var(--ink-2)}
main code{font-family:var(--font-m);font-size:14px;background:var(--bg-subtle);padding:2px 6px;border-radius:3px}
main table{width:100%;border-collapse:collapse;margin:16px 0;font-size:15px}
main th{background:var(--navy);color:#fff;padding:10px 14px;text-align:left;font-weight:600}
main td{padding:8px 14px;border-bottom:1px solid var(--border)}
main tr:nth-child(even) td{background:var(--bg-subtle)}
main ul,main ol{margin:8px 0 8px 24px}
main li{margin:4px 0}
main hr{border:none;border-top:1px solid var(--border);margin:40px 0}
main strong{color:var(--navy)}
.severity-high{display:inline-block;padding:1px 8px;border-radius:3px;font-size:12px;font-weight:700;background:#FFEBEE;color:var(--red)}
.severity-medium{display:inline-block;padding:1px 8px;border-radius:3px;font-size:12px;font-weight:700;background:#FFF8E1;color:var(--amber)}
.effort{display:inline-block;padding:1px 8px;border-radius:3px;font-size:12px;font-weight:700;background:#E8F5E9;color:var(--green)}
.footer-note{color:var(--ink-2);font-size:13px;font-style:italic;margin-top:48px;padding-top:16px;border-top:1px solid var(--border)}

/* ── Mobile ── */
.menu-toggle{display:none;position:fixed;top:12px;left:12px;z-index:200;background:var(--navy);color:#fff;border:none;border-radius:6px;padding:8px 12px;font-size:20px;cursor:pointer}
@media(max-width:960px){
  nav.lhs{transform:translateX(-100%);transition:transform .25s}
  nav.lhs.open{transform:translateX(0)}
  main{margin-left:0;padding:60px 24px 40px}
  .menu-toggle{display:block}
}
"""

def md_to_html(text):
    """Simple markdown to HTML converter"""
    lines = text.split('\n')
    out = []
    in_table = False
    in_code = False
    in_list = False
    in_quote = False
    
    for line in lines:
        # Code blocks
        if line.startswith('```'):
            if in_code:
                out.append('</pre>')
                in_code = False
            else:
                out.append('<pre><code>')
                in_code = True
            continue
        if in_code:
            out.append(line)
            continue
        
        # Tables
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                in_table = True
                out.append('<table>')
            cells = [c.strip() for c in line.split('|')[1:-1]]
            if all(c.replace('-','').replace(':','').strip()=='' for c in cells):
                continue  # separator row
            tag = 'th' if in_table and out[-1] == '<table>' else 'td'
            out.append('<tr>' + ''.join(f'<{tag}>{c}</{tag}>' for c in cells) + '</tr>')
            continue
        elif in_table:
            out.append('</table>')
            in_table = False
        
        # Blockquotes
        if line.startswith('> '):
            if not in_quote:
                out.append('<blockquote>')
                in_quote = True
            out.append(line[2:])
            continue
        elif in_quote:
            out.append('</blockquote>')
            in_quote = False
        
        # Headings
        if line.startswith('### '): out.append(f'<h3>{line[4:]}</h3>'); continue
        if line.startswith('## '): out.append(f'<h2>{line[3:]}</h2>'); continue
        if line.startswith('# '): out.append(f'<h1>{line[2:]}</h1>'); continue
        
        # Lists
        if line.strip().startswith('- ') or line.strip().startswith('* '):
            if not in_list: out.append('<ul>'); in_list = True
            content = line.strip()[2:]
            out.append(f'<li>{content}</li>')
            continue
        elif line.strip() and re.match(r'^\d+\.', line.strip()):
            if not in_list: out.append('<ol>'); in_list = True
            content = re.sub(r'^\d+\.\s*', '', line.strip())
            out.append(f'<li>{content}</li>')
            continue
        elif in_list and not line.strip():
            out.append('</ul>' if in_list else '</ol>')
            in_list = False
        
        # Horizontal rules
        if line.strip() == '---':
            out.append('<hr>')
            continue
        
        # Inline formatting
        line = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', line)
        line = re.sub(r'\*(.+?)\*', r'<em>\1</em>', line)
        line = re.sub(r'`([^`]+)`', r'<code>\1</code>', line)
        line = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', line)
        
        # Severity/effort tags
        line = re.sub(r'`\[HIGH · quick-win\]`', '<span class="severity-high">HIGH</span> <span class="effort">quick-win</span>', line)
        line = re.sub(r'`\[HIGH · medium\]`', '<span class="severity-high">HIGH</span> <span class="effort">medium</span>', line)
        line = re.sub(r'`\[HIGH · large\]`', '<span class="severity-high">HIGH</span> <span class="effort">large</span>', line)
        line = re.sub(r'`\[MEDIUM · medium\]`', '<span class="severity-medium">MEDIUM</span> <span class="effort">medium</span>', line)
        line = re.sub(r'`\[MEDIUM · quick-win\]`', '<span class="severity-medium">MEDIUM</span> <span class="effort">quick-win</span>', line)
        line = re.sub(r'`\[CRITICAL · quick-win\]`', '<span class="severity-high" style="background:#B71C1C;color:#fff">CRITICAL</span> <span class="effort">quick-win</span>', line)
        
        if line.strip(): out.append(f'<p>{line}</p>')
        else: out.append('')
    
    if in_table: out.append('</table>')
    if in_list: out.append('</ul>')
    if in_quote: out.append('</blockquote>')
    if in_code: out.append('</pre></code>')
    
    return '\n'.join(out)


def build_nav(current_page):
    """Build LHS nav HTML with current page highlighted"""
    nav_html = '<nav class="lhs" id="lhsNav">\n'
    nav_html += '  <div class="logo">\n'
    nav_html += '    <img src="' + BASE_PATH + '/assets/UoM_Logo_Horiz_onDark.svg" alt="UoM">\n'
    nav_html += '    <a href="' + BASE_PATH + '/index.html">Current Students IA</a>\n'
    nav_html += '  </div>\n'
    nav_html += '  <div class="nav-scroll">\n'
    
    for item in NAV_ITEMS:
        label, href, icon = item
        if label == '---':
            nav_html += '    <hr class="sep">\n'
        elif href is None:
            nav_html += f'    <div class="section">{icon} {label}</div>\n'
        else:
            is_current = current_page and (current_page == href or current_page.endswith(href.split('/')[-1]))
            cls = 'nav-link active' if is_current else 'nav-link'
            nav_html += f'    <a class="{cls}" href="{href}">{icon} {label.strip()}</a>\n'
    
    nav_html += '  </div>\n'
    nav_html += '  <div class="footer">UoM · Student Experience &amp; Design<br>June 2026 · 41,533 pages · 31 domains</div>\n'
    nav_html += '</nav>\n'
    return nav_html


def build_page(title, subtitle, body_html, current_page):
    """Build complete HTML page with UoM design and LHS nav"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · UoM Current Students IA</title>
<style>{CSS}</style>
</head>
<body>
<button class="menu-toggle" onclick="document.getElementById('lhsNav').classList.toggle('open')">☰</button>
{build_nav(current_page)}
<main>
<h1>{title}</h1>
<p class="subtitle">{subtitle}</p>
{body_html}
</main>
</body>
</html>"""


def convert_file(md_path, title, subtitle, output_path, current_page=None):
    """Convert a markdown file to a UoM-styled HTML page"""
    if not os.path.exists(md_path):
        print(f"  SKIP: {md_path} not found")
        return False
    
    with open(md_path, 'r') as f:
        md_text = f.read()
    
    # Skip YAML frontmatter if present
    if md_text.startswith('---'):
        end = md_text.find('---', 3)
        if end > 0:
            md_text = md_text[end+3:]
    
    body_html = md_to_html(md_text)
    html = build_page(title, subtitle, body_html, current_page or output_path)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(html)
    print(f"  ✅ {output_path}")
    return True


if __name__ == '__main__':
    base = '/Users/djmulholland/Documents/Claude/projects/unimelb-current-students-ia'
    os.chdir(base)
    
    files = [
        # Key deep-dives
        ("analysis/graduation-alumni-handoff.md", "Graduation → Alumni Handoff", "35 completion pages, 0 alumni links. The most severed transition in the student lifecycle."),
        ("analysis/the-handbook.md", "The Handbook", "The #1 dependency in the estate — 7,819 inbound links, SPA-only, blank titles."),
        ("analysis/equity-indigenous-journey.md", "Equity & Indigenous Journey", "SEDS wizard on 1 of 3 trees. Zero Indigenous pages on the hub."),
        ("analysis/fees-finance.md", "Fees & Finance", "Triple-tree duplication, census→404, 8:1 applicant-to-enrolled ratio."),
        ("analysis/scholarships.md", "Scholarships", "2,038 identical titles, 96% heading-skip. One template fix."),
        ("analysis/mobile-performance-audit.md", "Mobile & Performance", "304KB median study pages. Cookiebot duplicates = 5MB pages."),
        ("analysis/content-freshness-sandbox-leakage.md", "Content Freshness & Sandbox Leakage", "Live sandbox visa draft with 90 real inbound links."),
        ("analysis/content-quality-deep-dive.md", "Content Quality Audit", "Readability, actionability, freshness across 10 domains."),
        ("analysis/forms-microsite-audit.md", "Forms & Microsite Audit", "14 *.app hosts mapped — counselling gets 3 links, enrolment variation gets 2."),
        ("analysis/careers-online-wiring.md", "Careers Online Wiring", "Faculty-by-faculty audit — 5 faculties send zero links."),
        ("analysis/prospective-current-handoff.md", "Prospective → Current Handoff", "373 study→hub links. Only one cohort gets a guided transition."),
        ("analysis/hdr-candidature-duplication.md", "HDR Candidature Duplication", "33 byte-identical pairs across education + mdhs."),
        # Auth core
        ("analysis/authenticated-core-audit.md", "Authenticated Core Audit", "42 auth hosts, 3,641 links, link-label analysis."),
        ("analysis/auth-hosts-live-check.md", "Auth Hosts Live Check", "19 hosts tested — 2 dead, 18/19 auth-gated."),
        ("analysis/authenticated-core-findings.md", "Authenticated Core Findings", "363 pages crawled behind login — what students actually see."),
        # Crawl analyses
        ("analysis/crawl-ask-unimelb.md", "ask.unimelb.edu.au", "515 pages — 393 FAQ articles, two URL formats confirmed."),
        ("analysis/crawl-gradresearch.md", "gradresearch.unimelb.edu.au", "302 pages — 40% are 404s. Canonical HDR owner."),
        ("analysis/crawl-murrupbarak.md", "murrupbarak.unimelb.edu.au", "37 pages — comprehensive Indigenous support, unlinked from hub."),
        ("analysis/crawl-safercommunity.md", "safercommunity.unimelb.edu.au", "17 pages — crisis support, healthy hub connection."),
        ("analysis/crawl-umsu.md", "umsu.unimelb.edu.au", "800 pages — 720KB median, 6.4MB max, extremely insular."),
        ("analysis/crawl-online.md", "online.unimelb.edu.au", "87 pages — 52% lead-capture forms, no current-learner home."),
        ("analysis/crawl-sport.md", "sport.unimelb.edu.au", "444 pages — best page weight in estate (67KB median)."),
        ("analysis/crawl-library.md", "library.unimelb.edu.au", "1,000 pages — 370 referencing style pages."),
        ("analysis/crawl-studentit.md", "studentit.unimelb.edu.au", "74 pages — task-focused IT support, 95% stale."),
        # Deliverables
        ("analysis/governance-summary-pack.md", "Governance Summary Pack", "10 stakeholder-ready one-pagers for COO/Provost briefing."),
        ("analysis/quick-wins-checklist.md", "Quick Wins Checklist", "28 actionable fixes across 5 categories."),
        ("analysis/final-synthesis.md", "Final Synthesis", "The complete project narrative — five root findings, all evidence."),
        # Personas
        ("personas/sam-planning-their-path.md", "Sam — Planning their path", "First-year domestic undergraduate. 7 systems to plan one semester."),
        ("personas/alex-at-risk-withdrawal.md", "Alex — At-risk & withdrawal", "Second-year hitting academic difficulty."),
        ("personas/priya-international-student.md", "Priya — International student", "Postgraduate on subclass-500 visa. 9 stages."),
        ("personas/jordan-course-planning-maze.md", "Jordan — Course planning maze", "Second-year BSc. 41% of hub pages for one task."),
        ("personas/taylor-wellbeing-mental-health.md", "Taylor — Wellbeing & crisis", "Third-year seeking help. 3-4 hosts to reach counselling."),
    ]
    
    count = 0
    for args in files:
        md_path = args[0]
        title = args[1]
        subtitle = args[2]
        html_path = md_path.replace('.md', '.html')
        if convert_file(md_path, title, subtitle, html_path):
            count += 1
    
    print(f"\nConverted {count}/{len(files)} files")
