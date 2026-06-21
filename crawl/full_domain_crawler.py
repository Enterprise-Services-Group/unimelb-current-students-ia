#!/usr/bin/env python3
"""
Full-domain BFS crawler via CDP (Chrome DevTools Protocol).
Crawls every reachable page on a domain, extracts text + links,
saves raw corpus and structured JSON.
Pattern: same approach as the original CS crawl, but for the full domain.
"""
import asyncio
import json
import time
import os
import hashlib
import re
import urllib.request
import websockets
from urllib.parse import urljoin, urlparse

CDP_BASE = "http://localhost:9222"
OUT_DIR = os.path.expanduser("~/Documents/Claude/projects/unimelb-current-students-ia/crawl/full-faculty")

# 9 faculties (corrected FEIT domain)
FACULTIES = [
    ("law", "law.unimelb.edu.au"),
    ("feit", "eng.unimelb.edu.au"),
    ("arts", "arts.unimelb.edu.au"),
    ("science", "science.unimelb.edu.au"),
    ("education", "education.unimelb.edu.au"),
    ("fbe", "fbe.unimelb.edu.au"),
    ("ffam", "finearts-music.unimelb.edu.au"),
    ("mdhs", "mdhs.unimelb.edu.au"),
    ("msd", "msd.unimelb.edu.au"),
]

MAX_PAGES_PER_DOMAIN = 500  # Safety cap
PAGE_TIMEOUT = 15

os.makedirs(OUT_DIR, exist_ok=True)

EXTRACT_LINKS_JS = """
(() => {
    const links = [];
    const base = location.origin;
    document.querySelectorAll('a[href]').forEach(a => {
        let href = a.href;
        if (!href) return;
        // Normalize: resolve relative, strip hash
        try {
            const u = new URL(href, base);
            u.hash = '';
            href = u.href;
        } catch(e) { return; }
        // Only same-domain links
        if (href.startsWith(base + '/') || href === base + '/' || href === base) {
            links.push(href);
        }
    });
    return JSON.stringify([...new Set(links)]);
})
"""

EXTRACT_CONTENT_JS = """
(() => {
    // Get main content: prefer main/article, fall back to body
    const main = document.querySelector('main') || document.querySelector('article') || document.body;
    if (!main) return JSON.stringify({title: document.title, text: '', wordCount: 0});
    
    // Remove scripts, styles, nav, footer
    const clone = main.cloneNode(true);
    clone.querySelectorAll('script, style, nav, footer, header, .uom-megamenu, .site-nav, .breadcrumb').forEach(el => el.remove());
    
    const text = clone.innerText || clone.textContent || '';
    const words = text.trim().split(/\\s+/).filter(w => w.length > 0);
    
    return JSON.stringify({
        title: document.title || '',
        url: location.href,
        text: text.trim().slice(0, 50000),
        wordCount: words.length,
    });
})
"""

def page_fingerprint(url):
    return hashlib.sha1(url.encode()).hexdigest()[:16]

class CDPCrawler:
    def __init__(self, ws_url, domain, slug):
        self.ws_url = ws_url
        self.domain = domain
        self.slug = slug
        self.base = f"https://{domain}"
        self.visited = set()
        self.frontier = [f"{self.base}/"]
        self.pages = []
        self.raw_dir = os.path.join(OUT_DIR, f"raw_{slug}")
        os.makedirs(self.raw_dir, exist_ok=True)
        self.ws = None
        
    async def connect(self):
        self.ws = await websockets.connect(self.ws_url, max_size=20*1024*1024,
            ping_interval=None, close_timeout=10)
        await self.send_recv({"id": 1, "method": "Page.enable"})
    
    async def send_recv(self, msg, expect_id=None):
        await self.ws.send(json.dumps(msg))
        # For commands with an id, wait for the response
        # For events-only (no id), return immediately
        cmd_id = msg.get("id")
        
    async def navigate_and_wait(self, url):
        """Navigate and wait for DOM content loaded."""
        await self.ws.send(json.dumps({"id": 100, "method": "Page.navigate", "params": {"url": url}}))
        
        # Drain messages until domContentEventFired or timeout
        for _ in range(50):
            raw = await asyncio.wait_for(self.ws.recv(), timeout=PAGE_TIMEOUT)
            data = json.loads(raw)
            method = data.get("method", "")
            if method == "Page.domContentEventFired":
                return True
            elif method == "Page.loadEventFired":
                pass  # Keep waiting for domContentEventFired
            # else: ignore other events
        return False
    
    async def eval_js(self, expression):
        """Evaluate JS and return the result value."""
        await self.ws.send(json.dumps({
            "id": 200, "method": "Runtime.evaluate",
            "params": {"expression": expression, "returnByValue": True}
        }))
        raw = await asyncio.wait_for(self.ws.recv(), timeout=10)
        data = json.loads(raw)
        result = data.get("result", {}).get("result", {})
        if result.get("type") == "string":
            return result["value"]
        return None
    
    async def crawl_page(self, url):
        """Crawl a single page: navigate, extract content + links, save raw."""
        fp = page_fingerprint(url)
        print(f"  [{len(self.pages)+1}] {url[:100]}")
        
        # Navigate
        ok = await self.navigate_and_wait(url)
        if not ok:
            print(f"    WARN: navigation timeout")
        
        # Wait for JS rendering
        await asyncio.sleep(2)
        
        # Extract content
        content_raw = await self.eval_js(EXTRACT_CONTENT_JS)
        content = json.loads(content_raw) if content_raw else {}
        
        if not content or content.get("wordCount", 0) == 0:
            print(f"    EMPTY page (wordCount=0) — likely WAF block or JS render failure")
            # Save raw HTML as fallback
            try:
                html = await self.eval_js("document.documentElement.outerHTML.slice(0, 10000)")
                if html:
                    raw_path = os.path.join(self.raw_dir, f"{fp}.html")
                    with open(raw_path, "w") as f:
                        f.write(html)
            except:
                pass
            return None, []
        
        # Extract links
        links_raw = await self.eval_js(EXTRACT_LINKS_JS)
        links = json.loads(links_raw) if links_raw else []
        links = [l for l in links if l not in self.visited]  # Filter visited
        
        # Save raw text
        raw_path = os.path.join(self.raw_dir, f"{fp}.txt")
        with open(raw_path, "w") as f:
            f.write(f"URL: {url}\nTITLE: {content.get('title','')}\nWORD_COUNT: {content.get('wordCount',0)}\n\n")
            f.write(content.get("text", ""))
        
        # Build page record
        page = {
            "url": url,
            "normalizedUrl": url,
            "title": content.get("title", ""),
            "wordCount": content.get("wordCount", 0),
            "outboundLinks": links,
            "fingerprint": fp,
        }
        
        return page, links
    
    async def crawl(self):
        """Main BFS crawl loop."""
        print(f"\n{'='*60}")
        print(f"CRAWLING: {self.slug} ({self.domain})")
        print(f"Frontier start: {len(self.frontier)} URLs")
        print(f"{'='*60}")
        
        await self.connect()
        
        page_count = 0
        while self.frontier and page_count < MAX_PAGES_PER_DOMAIN:
            url = self.frontier.pop(0)
            if url in self.visited:
                continue
            
            self.visited.add(url)
            
            try:
                page, links = await self.crawl_page(url)
            except Exception as e:
                print(f"    ERROR: {e}")
                continue
            
            if page:
                self.pages.append(page)
                page_count += 1
                
                # Add new links to frontier
                new_links = [l for l in links if l not in self.visited and l not in self.frontier]
                self.frontier.extend(new_links)
            
            # Small delay between pages
            await asyncio.sleep(1)
        
        # Save structured data
        out_path = os.path.join(OUT_DIR, f"{self.slug}.json")
        output = {
            "domain": self.domain,
            "slug": self.slug,
            "pages_crawled": len(self.pages),
            "urls_visited": len(self.visited),
            "frontier_remaining": len(self.frontier),
            "pages": self.pages,
        }
        with open(out_path, "w") as f:
            json.dump(output, f, indent=2)
        
        print(f"\n  DONE: {len(self.pages)} pages saved to {out_path}")
        print(f"  Visited: {len(self.visited)}, Frontier remaining: {len(self.frontier)}")
        return output
    
    async def close(self):
        if self.ws:
            await self.ws.close()


async def main():
    # Create a fresh Chrome tab
    req = urllib.request.Request(f"{CDP_BASE}/json/new?url=about:blank", method="PUT")
    with urllib.request.urlopen(req) as resp:
        tab = json.loads(resp.read())
    ws_url = tab["webSocketDebuggerUrl"]
    print(f"Tab created: {tab['id']}")
    
    all_results = {}
    
    for slug, domain in FACULTIES:
        crawler = CDPCrawler(ws_url, domain, slug)
        try:
            result = await crawler.crawl()
            all_results[slug] = result
        except Exception as e:
            print(f"\n  FATAL for {slug}: {e}")
            all_results[slug] = {"error": str(e), "domain": domain}
        finally:
            await crawler.close()
        
        # Create a new tab for each faculty
        req = urllib.request.Request(f"{CDP_BASE}/json/new?url=about:blank", method="PUT")
        with urllib.request.urlopen(req) as resp:
            tab = json.loads(resp.read())
        ws_url = tab["webSocketDebuggerUrl"]
        print(f"\nNew tab: {tab['id']}")
    
    # Save master summary
    summary_path = os.path.join(OUT_DIR, "_summary.json")
    with open(summary_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)
    
    print(f"\n\n{'='*60}")
    print(f"FULL CRAWL COMPLETE")
    print(f"{'='*60}")
    for slug, data in all_results.items():
        if "error" in data:
            print(f"  {slug}: ERROR - {data['error']}")
        else:
            print(f"  {slug}: {data['pages_crawled']} pages, {data['urls_visited']} visited")
    print(f"\nData saved to: {OUT_DIR}/")

if __name__ == "__main__":
    asyncio.run(main())
