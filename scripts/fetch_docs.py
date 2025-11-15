#!/usr/bin/env python3
"""Fetch ShipAny documentation from website"""
import requests
from bs4 import BeautifulSoup
import time

def fetch_page(url):
    """Fetch and parse a single page"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract main content
        article = soup.find('article')
        if article:
            return article.get_text(separator='\n', strip=True)
        return None
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def main():
    base_url = "https://shipany.ai/docs"

    # Key documentation pages
    pages = [
        "",  # Introduction
        "/quick-start",
        "/database",
        "/auth",
        "/payment",
    ]

    all_content = []

    for page in pages:
        url = f"{base_url}{page}"
        print(f"Fetching: {url}")
        content = fetch_page(url)
        if content:
            all_content.append(f"\n\n# Page: {url}\n\n{content}")
        time.sleep(1)  # Be respectful

    return "\n".join(all_content)

if __name__ == "__main__":
    docs = main()
    print(docs)
