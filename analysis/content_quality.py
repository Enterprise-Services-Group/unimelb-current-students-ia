#!/usr/bin/env python3
"""Content quality analysis pipeline for crawled pages."""
import json, os, re, sys, ssl
from collections import Counter
from html.parser import HTMLParser
from urllib.parse import urlparse

# Disable SSL verification for NLTK data download
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

import textstat

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.skip = False
    def handle_starttag(self, tag, attrs):
        if tag in ('script','style','noscript','nav','footer','header'):
            self.skip = True
    def handle_endtag(self, tag):
        if tag in ('script','style','noscript','nav','footer','header'):
            self.skip = False
    def handle_data(self, data):
        if not self.skip:
            t = data.strip()
            if t: self.text.append(t)

def extract_text(html):
    parser = TextExtractor()
    try:
        parser.feed(html)
        return ' '.join(parser.text)
    except:
        return ''

# Action CTA patterns
ACTION_PATTERNS = [
    r'\benrol', r'\bapply', r'\bbook\b', r'\bregister', r'\bpay\b', r'\bsubmit\b',
    r'\bsign up\b', r'\bget started\b', r'\bmake an? (appointment|enquiry)\b',
    r'\bcontact us\b', r'\bfind out more\b', r'\blearn more\b',
]

# Find→act gap indicators: describe but don't link
GAP_INDICATORS = [
    r'you (can|must|need to|should)',
    r'visit my\.unimelb', r'log in to my\.unimelb', r'via my\.unimelb',
    r'through the portal', r'in eStudent', r'on Canvas',
    r'fill (out|in) the form', r'complete the form',
]

# Freshness signals
FRESHNESS = [
    (r'\b2025\b', 'stale_year'),
    (r'\b2024\b', 'stale_year'),
    (r'\b2023\b', 'very_stale'),
    (r'last updated', 'has_date'),
    (r'published', 'has_date'),
    (r'_nocache', 'nocache_leak'),
]

CRAWL_BASE = '/Users/djmulholland/Documents/Claude/projects/unimelb-current-students-ia/crawl'

def analyze_page(domain, page_dir):
    """Analyze a single crawled page."""
    html_path = os.path.join(CRAWL_BASE, page_dir, 'page.html')
    meta_path = os.path.join(CRAWL_BASE, page_dir, 'meta.json')
    links_path = os.path.join(CRAWL_BASE, page_dir, 'links.json')
    
    if not os.path.exists(html_path):
        return None
    
    # Read data
    with open(html_path, 'r', errors='ignore') as f:
        html = f.read()
    
    meta = {}
    if os.path.exists(meta_path):
        with open(meta_path) as f:
            meta = json.load(f)
    
    links = {'total': 0, 'internal': 0, 'unimelb': 0, 'external': 0}
    action_links = Counter()
    if os.path.exists(links_path):
        with open(links_path) as f:
            links_data = json.load(f)
        links = {k: links_data.get(k, 0) for k in ['total','internal','unimelb','external']}
        for link in links_data.get('links', []):
            text = (link.get('text') or '').lower().strip()
            for pattern in ACTION_PATTERNS:
                if re.search(pattern, text[:100]):
                    action_links[pattern.replace('\\b','')] += 1
    
    # Extract text
    text = extract_text(html)
    words = text.split()
    word_count = len(words)
    
    if word_count < 50:
        return {'url': meta.get('url',''), 'title': meta.get('title',''), 'word_count': word_count, 'skip': 'too_short'}
    
    # Readability
    try:
        flesch = textstat.flesch_reading_ease(text)
        grade = textstat.flesch_kincaid_grade(text)
    except:
        flesch, grade = None, None
    
    # Sentences
    sentences = textstat.sentence_count(text)
    avg_sentence_length = word_count / max(sentences, 1)
    
    # Action CTAs in body text
    body_actions = {}
    for pattern in ACTION_PATTERNS:
        matches = len(re.findall(pattern, text[:5000], re.I))
        if matches > 0:
            body_actions[pattern.replace('\\b','')] = matches
    
    # Find→act gap
    gap_signals = {}
    for pattern in GAP_INDICATORS:
        matches = len(re.findall(pattern, text[:5000], re.I))
        if matches > 0:
            gap_signals[pattern] = matches
    
    # Freshness
    freshness = []
    for pattern, tag in FRESHNESS:
        if re.search(pattern, text, re.I):
            freshness.append(tag)
    
    return {
        'url': meta.get('url', ''),
        'title': meta.get('title', ''),
        'domain': domain,
        'word_count': word_count,
        'sentence_count': sentences,
        'avg_sentence_length': round(avg_sentence_length, 1),
        'flesch_ease': round(flesch, 1) if flesch else None,
        'flesch_grade': round(grade, 1) if grade else None,
        'link_count': links['total'],
        'unimelb_links': links['unimelb'],
        'body_actions': body_actions,
        'action_link_count': sum(action_links.values()),
        'gap_signals': gap_signals,
        'freshness_flags': freshness,
        'find_act_gap': bool(gap_signals) and sum(action_links.values()) == 0,
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 content_quality.py <domain-dir> [sample-size]")
        sys.exit(1)
    
    domain_dir = sys.argv[1]
    sample_size = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    
    domain_name = os.path.basename(domain_dir).replace('-', '.')
    pages_dir = os.path.join(domain_dir, 'pages')
    
    if not os.path.exists(pages_dir):
        print(json.dumps({'error': 'no pages dir'}))
        return
    
    all_pages = sorted(os.listdir(pages_dir))
    sample = all_pages[:sample_size] if len(all_pages) > sample_size else all_pages
    
    results = []
    for page_id in sample:
        result = analyze_page(domain_name, os.path.join(os.path.basename(domain_dir), 'pages', page_id))
        if result:
            results.append(result)
    
    # Summary stats
    wc = [r['word_count'] for r in results if r.get('word_count', 0) >= 50]
    flesch_scores = [r['flesch_ease'] for r in results if r.get('flesch_ease')]
    grade_scores = [r['flesch_grade'] for r in results if r.get('flesch_grade')]
    gaps = [r for r in results if r.get('find_act_gap')]
    stale = [r for r in results if r.get('freshness_flags')]
    action_pages = [r for r in results if r.get('action_link_count', 0) > 0]
    
    print(json.dumps({
        'domain': domain_name,
        'sampled': len(sample),
        'analyzed': len(results),
        'short_pages': len([r for r in results if r.get('skip')]),
        'stats': {
            'median_words': sorted(wc)[len(wc)//2] if wc else 0,
            'median_flesch': sorted(flesch_scores)[len(flesch_scores)//2] if flesch_scores else None,
            'median_grade': sorted(grade_scores)[len(grade_scores)//2] if grade_scores else None,
            'avg_sentence_len': round(sum(r['avg_sentence_length'] for r in results if r.get('avg_sentence_length')) / max(len([r for r in results if r.get('avg_sentence_length')]), 1), 1),
        },
        'find_act_gaps': len(gaps),
        'stale_content': len(stale),
        'pages_with_actions': len(action_pages),
        'top_actions': Counter({k: v for r in results for k, v in r.get('body_actions', {}).items()}).most_common(10),
        'gap_examples': [{'url': r['url'], 'title': r['title'][:80], 'signals': r['gap_signals']} for r in gaps[:5]],
        'stale_examples': [{'url': r['url'], 'title': r['title'][:80], 'flags': r['freshness_flags']} for r in stale[:5]],
        'results': results,
    }, indent=2))

if __name__ == '__main__':
    main()
