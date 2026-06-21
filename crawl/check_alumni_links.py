#!/usr/bin/env python3
"""
Check all 9 University of Melbourne faculty homepages for links to alumni.unimelb.edu.au.
Also checks students.unimelb.edu.au.

For each faculty:
- Homepage nav/mega-menu for "Alumni" links
- Footer for alumni links
- /alumni, /engage, /community subpages
"""

import requests
import re
import json
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

FACULTIES = [
    {"name": "Law", "domain": "law.unimelb.edu.au"},
    {"name": "Engineering & IT", "domain": "feit.unimelb.edu.au"},
    {"name": "Arts", "domain": "arts.unimelb.edu.au"},
    {"name": "Science", "domain": "science.unimelb.edu.au"},
    {"name": "Education", "domain": "education.unimelb.edu.au"},
    {"name": "Business & Economics", "domain": "fbe.unimelb.edu.au"},
    {"name": "Fine Arts & Music", "domain": "finearts-music.unimelb.edu.au"},
    {"name": "MDHS (Medicine, Dentistry & Health Sciences)", "domain": "mdhs.unimelb.edu.au"},
    {"name": "MSD (Architecture, Building & Planning)", "domain": "msd.unimelb.edu.au"},
]

ALUMNI_HOSTS = ["alumni.unimelb.edu.au"]

def fetch_page(url, timeout=15):
    """Fetch a page and return (status_code, soup, raw_text)."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=timeout, allow_redirects=True)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        return resp.status_code, soup, resp.text
    except requests.exceptions.HTTPError as e:
        return e.response.status_code if e.response else 0, None, str(e)
    except requests.exceptions.RequestException as e:
        return 0, None, str(e)

def extract_links_to_alumni(soup, base_url):
    """Find all <a> tags that link to alumni.unimelb.edu.au."""
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        # Normalize
        full_url = urljoin(base_url, href)
        parsed = urlparse(full_url)
        if parsed.hostname and "alumni.unimelb.edu.au" in parsed.hostname:
            text = a.get_text(strip=True)
            links.append({
                "text": text[:100] if text else "(no text)",
                "href": href,
                "full_url": full_url,
                "parent_tag": a.parent.name if a.parent else "unknown",
                "in_nav": bool(a.find_parent(["nav", "header"])),
                "in_footer": bool(a.find_parent("footer")),
            })
    return links

def check_nav_for_alumni(soup, base_url):
    """Check navigation menus for Alumni links."""
    results = []
    # Check header nav, mega-menu
    nav_selectors = [
        "nav", "header", ".uom-megamenu", ".mega-menu", ".main-nav",
        ".primary-nav", ".site-nav", "[role='navigation']",
        ".navbar", ".nav", "#nav", "#navigation"
    ]
    for selector in nav_selectors:
        elements = soup.select(selector)
        for el in elements:
            for a in el.find_all("a", href=True):
                text = a.get_text(strip=True).lower()
                href = a["href"]
                full_url = urljoin(base_url, href)
                if "alumni" in text or "alumni" in href.lower():
                    parsed = urlparse(full_url)
                    is_alumni_site = parsed.hostname and "alumni.unimelb.edu.au" in parsed.hostname
                    results.append({
                        "text": a.get_text(strip=True)[:100],
                        "href": href,
                        "full_url": full_url,
                        "selector": selector,
                        "links_to_alumni_site": is_alumni_site,
                    })
    return results

def check_footer_for_alumni(soup, base_url):
    """Check footer for alumni links."""
    results = []
    footer = soup.find("footer")
    if not footer:
        footer_selectors = [".footer", "#footer", "[class*='footer']", ".site-footer"]
        for sel in footer_selectors:
            footer = soup.select_one(sel)
            if footer:
                break
    if footer:
        for a in footer.find_all("a", href=True):
            text = a.get_text(strip=True).lower()
            href = a["href"]
            full_url = urljoin(base_url, href)
            if "alumni" in text or "alumni" in href.lower():
                parsed = urlparse(full_url)
                is_alumni_site = parsed.hostname and "alumni.unimelb.edu.au" in parsed.hostname
                results.append({
                    "text": a.get_text(strip=True)[:100],
                    "href": href,
                    "full_url": full_url,
                    "links_to_alumni_site": is_alumni_site,
                })
    return results

def check_subpage(domain, path, timeout=15):
    """Check a subpage like /alumni or /engage."""
    url = f"https://{domain}{path}"
    status, soup, text = fetch_page(url, timeout)
    result = {
        "url": url,
        "status": status,
        "exists": status == 200,
    }
    if status == 200 and soup:
        result["alumni_links"] = extract_links_to_alumni(soup, url)
        result["all_alumni_links"] = []
        # Also search raw text
        alumni_pattern = re.compile(r'alumni\.unimelb\.edu\.au[^\s"\'<>]*', re.I)
        matches = alumni_pattern.findall(text)
        result["raw_text_matches"] = matches[:20]
    elif status != 200:
        result["error"] = text[:200] if isinstance(text, str) else str(text)
    return result

def analyze_faculty(fac):
    name = fac["name"]
    domain = fac["domain"]
    homepage = f"https://{domain}/"
    
    print(f"\n{'='*60}")
    print(f"Checking: {name} ({domain})")
    print(f"{'='*60}")
    
    result = {
        "faculty": name,
        "domain": domain,
        "homepage": homepage,
    }
    
    # 1. Fetch homepage
    print(f"  Fetching homepage: {homepage}")
    status, soup, raw = fetch_page(homepage)
    result["homepage_status"] = status
    
    if status != 200 or not soup:
        result["error"] = f"Homepage fetch failed: status={status}"
        print(f"  FAILED: status={status}")
        return result
    
    print(f"  OK: status={status}")
    
    # 2. Extract all links to alumni.unimelb.edu.au
    all_alumni_links = extract_links_to_alumni(soup, homepage)
    result["all_alumni_links_on_homepage"] = len(all_alumni_links)
    
    # 3. Check nav
    nav_alumni = check_nav_for_alumni(soup, homepage)
    result["nav_alumni_links"] = nav_alumni
    
    # 4. Check footer
    footer_alumni = check_footer_for_alumni(soup, homepage)
    result["footer_alumni_links"] = footer_alumni
    
    # 5. Check subpages
    for subpath in ["/alumni", "/engage", "/community"]:
        print(f"  Checking {subpath}...")
        sub_result = check_subpage(domain, subpath)
        result[f"subpage_{subpath.replace('/', '_')}"] = sub_result
        if sub_result["exists"]:
            print(f"    EXISTS (status={sub_result['status']}), alumni links: {len(sub_result.get('alumni_links', []))}")
        else:
            print(f"    Status: {sub_result['status']}")
    
    # Summary
    print(f"\n  --- SUMMARY for {name} ---")
    nav_has_alumni = any(l.get("links_to_alumni_site") for l in nav_alumni)
    footer_has_alumni = any(l.get("links_to_alumni_site") for l in footer_alumni)
    print(f"  Alumni in homepage nav: {'Yes' if nav_alumni else 'No'}")
    if nav_alumni:
        for l in nav_alumni:
            print(f"    - '{l['text']}' -> {l['full_url']} {'[alumni.unimelb.edu.au]' if l['links_to_alumni_site'] else ''}")
    print(f"  Alumni in footer: {'Yes' if footer_alumni else 'No'}")
    if footer_alumni:
        for l in footer_alumni:
            print(f"    - '{l['text']}' -> {l['full_url']} {'[alumni.unimelb.edu.au]' if l['links_to_alumni_site'] else ''}")
    print(f"  Total alumni.unimelb.edu.au links on homepage: {len(all_alumni_links)}")
    for link in all_alumni_links:
        print(f"    - '{link['text']}' -> {link['full_url']} (in_nav={link['in_nav']}, in_footer={link['in_footer']})")
    
    return result

def check_students_site():
    """Check students.unimelb.edu.au."""
    print(f"\n{'='*60}")
    print(f"Checking: students.unimelb.edu.au")
    print(f"{'='*60}")
    
    result = {"site": "students.unimelb.edu.au"}
    
    # Homepage
    print("  Fetching homepage...")
    status, soup, raw = fetch_page("https://students.unimelb.edu.au/")
    result["homepage_status"] = status
    
    if status == 200 and soup:
        all_links = extract_links_to_alumni(soup, "https://students.unimelb.edu.au/")
        nav_links = check_nav_for_alumni(soup, "https://students.unimelb.edu.au/")
        footer_links = check_footer_for_alumni(soup, "https://students.unimelb.edu.au/")
        
        result["homepage_alumni_links"] = len(all_links)
        result["nav_alumni"] = nav_links
        result["footer_alumni"] = footer_links
        
        print(f"  Nav alumni links: {len(nav_links)}")
        for l in nav_links:
            print(f"    - '{l['text']}' -> {l['full_url']}")
        print(f"  Footer alumni links: {len(footer_links)}")
        for l in footer_links:
            print(f"    - '{l['text']}' -> {l['full_url']}")
        print(f"  All alumni.unimelb.edu.au links: {len(all_links)}")
        for l in all_links:
            print(f"    - '{l['text']}' -> {l['full_url']}")
    
    # Also check a few subpages
    for subpath in ["/alumni", "/careers-employability", "/graduation"]:
        url = f"https://students.unimelb.edu.au{subpath}"
        status, soup, raw = fetch_page(url)
        alumni_links = []
        if status == 200 and soup:
            alumni_links = extract_links_to_alumni(soup, url)
        result[f"subpage_{subpath}"] = {
            "url": url,
            "status": status,
            "alumni_links": len(alumni_links),
            "links": [l["full_url"] for l in alumni_links],
        }
        print(f"  {subpath}: status={status}, alumni links={len(alumni_links)}")
    
    return result

def main():
    print("=" * 60)
    print("FACULTY ALUMNI LINK CHECK")
    print("Checking for links to alumni.unimelb.edu.au")
    print("=" * 60)
    
    all_results = []
    
    for fac in FACULTIES:
        result = analyze_faculty(fac)
        all_results.append(result)
        time.sleep(1)  # Be polite
    
    # Check students.unimelb.edu.au
    students_result = check_students_site()
    
    # Save results
    output = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "faculties": all_results,
        "students_site": students_result,
    }
    
    out_path = "/Users/djmulholland/Documents/Claude/projects/unimelb-current-students-ia/crawl/faculty_alumni_links.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=str)
    
    print(f"\n\nResults saved to: {out_path}")
    
    # Print final summary table
    print("\n" + "=" * 80)
    print("FINAL SUMMARY TABLE")
    print("=" * 80)
    print(f"{'Faculty':<40} {'Nav Alumni':<15} {'Footer Alumni':<15} {'HP Alumni Links':<15}")
    print("-" * 80)
    for r in all_results:
        name = r.get("faculty", "?")
        nav = "Yes" if any(l.get("links_to_alumni_site") for l in r.get("nav_alumni_links", [])) else "No"
        footer = "Yes" if any(l.get("links_to_alumni_site") for l in r.get("footer_alumni_links", [])) else "No"
        hp_links = r.get("all_alumni_links_on_homepage", 0)
        print(f"{name:<40} {nav:<15} {footer:<15} {hp_links:<15}")
    
    print(f"\n{'students.unimelb.edu.au':<40} {'N/A':<15} {'N/A':<15} {students_result.get('homepage_alumni_links', '?'):<15}")

if __name__ == "__main__":
    main()
