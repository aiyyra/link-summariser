# tools/page_crawler.py

import requests
from bs4 import BeautifulSoup

def crawl_page(url: str) -> str:
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        return soup.get_text()
    except Exception as e:
        return f"Error crawling page: {e}"
