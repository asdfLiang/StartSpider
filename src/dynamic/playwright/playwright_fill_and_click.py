from playwright.sync_api import sync_playwright
import time

"""
    页面输入、点击
"""

# 打开百度搜索python
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    try:
        page = browser.new_page()
        page.goto("https://www.baidu.com")
        page.fill("#kw", "python")
        page.click("#su")
        time.sleep(2)
    finally:
        browser.close()
