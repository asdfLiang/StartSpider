from playwright.sync_api import sync_playwright

"""
    获取页面源代码
"""

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    try:
        page = browser.new_page()
        page.goto("https://www.baidu.com")
        html = page.content()
        print(html)
    finally:
        browser.close()
