from playwright.sync_api import sync_playwright

"""
    基本使用
"""

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        with browser_type.launch(headless=False) as browser:
            page = browser.new_page()
            page.goto("https://www.baidu.com")
            page.screenshot(path=f"tests/downloads/screenshot-{browser_type.name}.png")
            print(page.title())
