# tools/semantic_crawler.py

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl_semantic_content(url: str) -> dict:
    """
    Crawl a URL and extract semantically useful elements:
    - Article title
    - Metadata (description, author, date)
    - Main text content (cleaned)
    - Headings
    - Links
    - Images
    - Code blocks
    """
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, "html.parser")

        # Title
        title = soup.title.string.strip() if soup.title else ""

        # Meta tags
        meta = {
            "description": "",
            "author": "",
            "published": ""
        }

        for tag in soup.find_all("meta"):
            name = tag.get("name", "").lower()
            prop = tag.get("property", "").lower()
            content = tag.get("content", "").strip()

            if name == "description" or prop == "og:description":
                meta["description"] = content
            elif name == "author":
                meta["author"] = content
            elif name in ["article:published_time", "date", "pubdate"]:
                meta["published"] = content

        # Main text content (remove nav/footer/sidebar)
        for tag in soup(["nav", "footer", "aside", "script", "style"]):
            tag.decompose()

        main_text = soup.get_text(separator="\n", strip=True)

        # Headings
        headings = [h.get_text(strip=True) for h in soup.find_all(["h1", "h2", "h3"])]

        # Image URLs
        images = [
            urljoin(url, img['src'])
            for img in soup.find_all("img", src=True)
            if img['src'].startswith("http") or img['src'].startswith("/")
        ]

        # Links
        links = [
            urljoin(url, a['href'])
            for a in soup.find_all("a", href=True)
            if not a['href'].startswith("#")
        ]

        # Code blocks
        code_blocks = [c.get_text(strip=True) for c in soup.find_all(["pre", "code"])]

        return {
            # "url": url,
            "title": title,
            # "meta": meta,
            "headings": headings,
            "text": main_text,
            # "images": images,
            "links": links,
            # "code_blocks": code_blocks
        }

    except Exception as e:
        return {"error": str(e)}
