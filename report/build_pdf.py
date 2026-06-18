#!/usr/bin/env python3
"""Render a markdown file to a UoM-branded A4 PDF via pandoc + headless Chrome.
Usage: build_pdf.py <md> <out_html> <out_pdf> <eyebrow> <title> <subtitle>
Run from the report/ folder (references deag-assets/ for fonts + logo)."""
import sys, subprocess, re, os

md_path, out_html, out_pdf, eyebrow, title, subtitle = sys.argv[1:7]
md = open(md_path, encoding='utf-8').read()
# drop the first H1 line — the cover carries the title; keep the rest
md = re.sub(r'(?m)\A\s*#\s+.*\n', '', md, count=1)
# drop a leading italic provenance line if present (cover carries provenance)
frag = subprocess.run(['pandoc','--from=gfm','--to=html5','--wrap=none'],
                      input=md, capture_output=True, text=True, check=True).stdout

CSS = """
@font-face{font-family:'Fraunces';src:url('deag-assets/fonts/Fraunces.ttf') format('truetype');font-weight:100 900}
@font-face{font-family:'Fraunces';src:url('deag-assets/fonts/Fraunces-Italic.ttf') format('truetype');font-weight:100 900;font-style:italic}
@font-face{font-family:'Source Sans 3';src:url('deag-assets/fonts/SourceSans3.ttf') format('truetype');font-weight:200 900}
@font-face{font-family:'Source Sans 3';src:url('deag-assets/fonts/SourceSans3-Italic.ttf') format('truetype');font-weight:200 900;font-style:italic}
@font-face{font-family:'Source Code Pro';src:url('deag-assets/fonts/SourceCodePro.ttf') format('truetype');font-weight:200 900}
:root{--navy:#000F46;--navy2:#000B34;--cyan:#46C8F0;--cyanh:#2F95B7;--light:#F4F4F4;--tint:#F3F3F6;--border:#DDDDE7;--ink:#1c1c28;--muted:#5b5b6b}
*{box-sizing:border-box}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{font-family:'Source Sans 3',sans-serif;color:var(--ink);font-size:10.3pt;line-height:1.5;margin:0}
@page{size:A4;margin:16mm 15mm 17mm}
h1,h2,h3,h4{font-family:'Fraunces',serif;color:var(--navy);font-weight:600;line-height:1.16;letter-spacing:-0.006em}
h1{font-size:19pt;margin:0 0 .5em;padding-top:.2em;page-break-before:always;border-top:3px solid var(--cyan);padding-top:10px}
h2{font-size:14pt;margin:1.25em 0 .4em;padding-bottom:.18em;border-bottom:2px solid var(--cyan)}
h3{font-size:11.5pt;color:var(--navy2);margin:1em 0 .35em}
h4{font-size:10.5pt;color:var(--navy2);margin:.9em 0 .3em}
p{margin:0 0 .6em}
strong{color:var(--navy2)}
a{color:var(--cyanh);text-decoration:none}
ul,ol{margin:.3em 0 .8em;padding-left:1.3em}
li{margin:.2em 0}
code{font-family:'Source Code Pro',monospace;font-size:8.6pt;background:var(--light);padding:0 3px;border-radius:2px}
table{width:100%;border-collapse:collapse;margin:.55em 0 1.1em;font-size:9pt}
th,td{border:1px solid var(--border);padding:5px 8px;text-align:left;vertical-align:top}
thead th{background:var(--navy);color:#fff;font-weight:600}
tbody tr:nth-child(even){background:var(--light)}
blockquote{background:var(--tint);border-left:5px solid var(--cyan);margin:.8em 0;padding:9px 15px;color:var(--navy2)}
hr{border:0;border-top:1px solid var(--border);margin:1.2em 0}
em{color:var(--muted)}
.cover{background:var(--navy);color:#fff;min-height:262mm;margin:-16mm -15mm 0;padding:24mm 22mm;break-after:page;display:flex;flex-direction:column}
.cover img{width:58mm;margin-bottom:auto}
.cover .eyebrow{font-family:'Source Code Pro',monospace;color:var(--cyan);font-size:10pt;letter-spacing:.15em;text-transform:uppercase;margin-bottom:13px}
.cover h1.t{color:#fff;font-size:38pt;line-height:1.05;max-width:15em;margin:0 0 16px;border:0;padding:0;page-break-before:auto}
.cover .rule{width:60px;height:5px;background:var(--cyan);margin:18px 0}
.cover .sub{font-size:13pt;color:#c9cde4;max-width:32em}
.cover .meta{margin-top:24px;font-size:10.5pt;color:#aab0d4}
.cover .aoc{margin-top:auto;font-style:italic;font-size:9pt;color:#8f96c2;max-width:40em;padding-top:22px}
/* first real heading after cover shouldn't force a second blank page */
.body > h1:first-child{page-break-before:avoid}
"""

HTML = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{title}</title>
<style>{CSS}</style></head><body>
<section class="cover">
  <img src="deag-assets/logos/onDark.svg" alt="University of Melbourne">
  <div class="eyebrow">{eyebrow}</div>
  <h1 class="t">{title}</h1>
  <div class="rule"></div>
  <div class="sub">{subtitle}</div>
  <div class="meta">University of Melbourne &nbsp;·&nbsp; June 2026</div>
  <div class="aoc">The University of Melbourne acknowledges the Traditional Owners of the unceded land on which we work, learn and live, and pays respect to their Elders, past and present, and to Indigenous Australians today.</div>
</section>
<div class="body">
{frag}
</div></body></html>"""

open(out_html,'w',encoding='utf-8').write(HTML)
chrome="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
subprocess.run([chrome,"--headless=new","--disable-gpu","--no-pdf-header-footer",
  "--virtual-time-budget=15000",f"--print-to-pdf={out_pdf}",
  "file://"+os.path.abspath(out_html)], capture_output=True)
print("wrote",out_html,"and",out_pdf)
