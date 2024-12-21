from playwright.sync_api import sync_playwright

"""
    事件监听机制
"""


def on_response(response):
    print(f"Statue {response.status}: {response.url}")


# 监听response事件
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    try:
        page = browser.new_page()
        page.on("response", on_response)
        page.goto("https://spa6.scrape.center/")
        page.wait_for_load_state("networkidle")
    finally:
        browser.close()


def filter_movie(response):
    if "/api/movie" in response.url and response.status == 200:
        print(response.json())


# 过滤指定ajax响应内容
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    try:
        page = browser.new_page()
        page.on("response", filter_movie)
        page.goto("https://spa6.scrape.center/")
        page.wait_for_load_state("networkidle")
    finally:
        browser.close()
