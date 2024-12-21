from playwright.sync_api import sync_playwright

"""
    获取节点属性
"""

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://spa6.scrape.center/")
    page.wait_for_load_state("networkidle")
    href = page.get_attribute("a.name", "href")
    print(href)
    browser.close()
