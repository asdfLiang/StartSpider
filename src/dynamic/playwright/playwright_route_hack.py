from playwright.sync_api import sync_playwright
import time, re

"""
    利用网页劫持修改返回结果
"""

with sync_playwright() as p:

    def modify_response(route, response):
        route.fulfill(path="tests/resources/custom_response.html")

    browser = p.chromium.launch(headless=False)
    try:
        page = browser.new_page()
        page.route(re.compile("/"), modify_response)
        page.goto("https://spa6.scrape.center/")
        time.sleep(2)
    finally:
        browser.close()
