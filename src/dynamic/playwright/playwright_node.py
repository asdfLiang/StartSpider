from playwright.sync_api import sync_playwright

"""
    获取单个节点
"""


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    try:
        page = browser.new_page()
        page.goto("https://www.baidu.com")
        page.wait_for_load_state("networkidle")
        placeholder = page.get_attribute("input#kw", "placeholder")
        print(placeholder)
    finally:
        browser.close()
