from playwright.sync_api import sync_playwright
from free_proxy import proxy

"""
    Playwright 设置http代理（通过）
"""

with sync_playwright() as p:
    browser = p.chromium.launch(proxy={"server": "http://" + proxy}, headless=False)
    try:
        page = browser.new_page()
        page.goto("https://www.httpbin.org/get")
        page.wait_for_load_state("networkidle")
        print(page.content())
    finally:
        browser.close()
