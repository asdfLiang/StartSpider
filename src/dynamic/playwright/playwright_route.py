from playwright.sync_api import sync_playwright
import re

"""
    网络劫持
"""

with sync_playwright() as p:

    def cancel_request(route, request):
        route.abort()

    browser = p.chromium.launch(headless=False)
    try:
        page = browser.new_page()
        page.route(re.compile(r"(\.png)|(\.jpg)"), cancel_request)
        page.goto("https://spa6.scrape.center")
        page.wait_for_load_state("networkidle")
        page.screenshot(path="tests/downloads/no_picture.png")
    finally:
        browser.close()
