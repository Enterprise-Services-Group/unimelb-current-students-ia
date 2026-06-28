import json, glob, os, re
from collections import Counter, defaultdict

ROOT = 'crawl'
DOMAINS = {
  'students':'students-full','study':'study-unimelb-edu-au','services':'services-unimelb-edu-au',
  'scholarships':'scholarships-unimelb-edu-au','handbook':'handbook-unimelb-edu-au',
  'msd':'msd-unimelb-edu-au','eng':'eng-unimelb-edu-au','arts':'arts-unimelb-edu-au',
  'fbe':'fbe-unimelb-edu-au','mdhs':'mdhs-unimelb-edu-au','science':'science-unimelb-edu-au',
  'law':'law-unimelb-edu-au','education':'education-unimelb-edu-au','medicine':'medicine-unimelb-edu-au',
  'finearts':'finearts-music-unimelb-edu-au','biomed':'biomedicalsciences-unimelb-edu-au',
  'dental':'dental-unimelb-edu-au','mbs':'mbs-unimelb-edu-au','research':'research-full',
  'alumni':'www-unimelb-edu-au-alumni',
}

def iter_pages(domkey):
    d = os.path.join(ROOT, DOMAINS[domkey], 'pages')
    if not os.path.isdir(d):
        # try alternate layout
        idx = os.path.join(ROOT, DOMAINS[domkey], 'index.json')
        return
    for h in os.listdir(d):
        pdir = os.path.join(d, h)
        mp = os.path.join(pdir, 'meta.json'); lp = os.path.join(pdir, 'links.json')
        if os.path.exists(mp) and os.path.exists(lp):
            try:
                meta = json.load(open(mp)); links = json.load(open(lp))
                yield meta, links, pdir
            except: pass

# Check what page dirs exist
for k in DOMAINS:
    d = os.path.join(ROOT, DOMAINS[k], 'pages')
    n = len(os.listdir(d)) if os.path.isdir(d) else 0
    print(f"{k:12s} pages_dir={'Y' if os.path.isdir(d) else 'N':2s} count={n}")
