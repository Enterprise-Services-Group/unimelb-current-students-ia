#!/usr/bin/env python3
"""Use CDP (Chrome DevTools Protocol) via websockets to check faculty sites for alumni.unimelb.edu.au links."""
import asyncio
import json
import websockets

CDP_BASE = "http://localhost:9222"

FACULTIES = [
    ("Law", "law.unimelb.edu.au"),
    ("FEIT (Engineering & IT)", "eng.unimelb.edu.au"),
    ("Arts", "arts.unimelb.edu.au"),
    ("Science", "science.unimelb.edu.au"),
    ("Education", "education.unimelb.edu.au"),
    ("FBE (Business & Economics)", "fbe.unimelb.edu.au"),
    ("FFAM (Fine Arts & Music)", "finearts-music.unimelb.edu.au"),
    ("MDHS (Medicine, Dentistry & HS)", "mdhs.unimelb.edu.au"),
    ("MSD (Architecture, Building & Planning)", "msd.unimelb.edu.au"),
]

SUBPAGES = ["/alumni", "/engage", "/community", "/about/alumni"]

ALUMNI_JS = """
(() => {
    const results = {alumni_links: [], nav_alumni: [], footer_alumni: []};
    // All links to alumni.unimelb.edu.au
    document.querySelectorAll('a[href]').forEach(a => {
        const href = a.href || '';
        if (href.includes('alumni.unimelb.edu.au')) {
            const inNav = a.closest('nav, header, .uom-megamenu, .mega-menu, [role="navigation"]') !== null;
            const inFooter = a.closest('footer') !== null;
            results.alumni_links.push({
                text: (a.textContent || '').trim().slice(0, 100),
                href: href,
                in_nav: inNav,
                in_footer: inFooter,
            });
        }
    });
    // Any link with "alumni" text anywhere on page
    document.querySelectorAll('a[href]').forEach(a => {
        const text = (a.textContent || '').trim().toLowerCase();
        if (text.includes('alumni')) {
            const inNav = a.closest('nav, header, .uom-megamenu, .mega-menu, [role="navigation"]') !== null;
            const inFooter = a.closest('footer') !== null;
            const container = inNav ? 'nav_alumni' : inFooter ? 'footer_alumni' : null;
            if (container) {
                results[container].push({
                    text: (a.textContent || '').trim().slice(0, 100),
                    href: a.href || '',
                    links_to_alumni_site: (a.href || '').includes('alumni.unimelb.edu.au'),
                });
            }
        }
    });
    return JSON.stringify(results);
})
"""

async def check_page(ws_url, url):
    """Navigate to url and extract alumni link data."""
    async with websockets.connect(ws_url, max_size=10*1024*1024) as ws:
        # Enable Page domain
        await ws.send(json.dumps({"id": 1, "method": "Page.enable"}))
        await asyncio.wait_for(ws.recv(), timeout=5)
        
        # Navigate
        await ws.send(json.dumps({
            "id": 2, "method": "Page.navigate",
            "params": {"url": url}
        }))
        nav_result = await asyncio.wait_for(ws.recv(), timeout=5)
        nav_data = json.loads(nav_result)
        
        # Wait for page to load
        await asyncio.sleep(3)
        
        # Run JS to extract alumni links
        await ws.send(json.dumps({
            "id": 3, "method": "Runtime.evaluate",
            "params": {"expression": ALUMNI_JS, "returnByValue": True}
        }))
        eval_result = await asyncio.wait_for(ws.recv(), timeout=10)
        eval_data = json.loads(eval_result)
        
        result = eval_data.get("result", {}).get("result", {}).get("value", "{}")
        if isinstance(result, str):
            result = json.loads(result)
        
        # Also get page title and status
        await ws.send(json.dumps({
            "id": 4, "method": "Runtime.evaluate",
            "params": {"expression": "JSON.stringify({title: document.title, url: location.href})", "returnByValue": True}
        }))
        meta_result = await asyncio.wait_for(ws.recv(), timeout=5)
        meta_data = json.loads(meta_result)
        meta = json.loads(meta_data.get("result", {}).get("result", {}).get("value", "{}"))
        
        return {
            "url": meta.get("url", url),
            "title": meta.get("title", ""),
            **result
        }

async def main():
    # Create a new tab
    import urllib.request
    req = urllib.request.Request(f"{CDP_BASE}/json/new?url=about:blank", method="PUT")
    with urllib.request.urlopen(req) as resp:
        tab = json.loads(resp.read())
    ws_url = tab["webSocketDebuggerUrl"]
    print(f"Tab created: {tab['id']}")
    
    results = {}
    
    for name, domain in FACULTIES:
        print(f"\n{'='*60}")
        print(f"Checking: {name} ({domain})")
        
        try:
            homepage_result = await check_page(ws_url, f"https://{domain}/")
            results[domain] = {
                "name": name,
                "homepage": homepage_result,
            }
            
            alumni_count = len(homepage_result.get("alumni_links", []))
            nav_count = len(homepage_result.get("nav_alumni", []))
            footer_count = len(homepage_result.get("footer_alumni", []))
            
            print(f"  Alumni.unimelb links: {alumni_count}")
            for l in homepage_result.get("alumni_links", []):
                print(f"    [{('NAV' if l['in_nav'] else 'FOOTER' if l['in_footer'] else 'BODY')}] \"{l['text']}\" -> {l['href']}")
            print(f"  Nav alumni links: {nav_count}")
            for l in homepage_result.get("nav_alumni", []):
                target = " [ALUMNI SITE]" if l["links_to_alumni_site"] else ""
                print(f"    \"{l['text']}\" -> {l['href']}{target}")
            print(f"  Footer alumni links: {footer_count}")
            for l in homepage_result.get("footer_alumni", []):
                target = " [ALUMNI SITE]" if l["links_to_alumni_site"] else ""
                print(f"    \"{l['text']}\" -> {l['href']}{target}")
            
            # Check a couple of subpages
            for sub in ["/alumni"]:
                try:
                    sub_result = await check_page(ws_url, f"https://{domain}{sub}")
                    print(f"  {sub}: title=\"{sub_result.get('title','')}\", alumni_links={len(sub_result.get('alumni_links',[]))}")
                    results[domain][f"subpage{sub}"] = sub_result
                except Exception as e:
                    print(f"  {sub}: ERROR - {e}")
            
        except Exception as e:
            print(f"  ERROR: {e}")
            results[domain] = {"name": name, "error": str(e)}
        
        await asyncio.sleep(1)
    
    # Save
    out_path = "/Users/djmulholland/Documents/Claude/projects/unimelb-current-students-ia/crawl/faculty_alumni_cdp.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\n\nResults saved to: {out_path}")
    
    # Summary table
    print(f"\n{'='*80}")
    print(f"{'Faculty':<35} {'Alumni links':<15} {'Nav alumni':<15} {'Footer alumni':<15}")
    print("-"*80)
    for domain, data in results.items():
        name = data.get("name", "?")
        if "error" in data:
            print(f"{name:<35} ERROR: {data['error'][:40]}")
        else:
            hp = data.get("homepage", {})
            al = len(hp.get("alumni_links", []))
            na = len(hp.get("nav_alumni", []))
            fa = len(hp.get("footer_alumni", []))
            print(f"{name:<35} {al:<15} {na:<15} {fa:<15}")

if __name__ == "__main__":
    asyncio.run(main())
