import re
from playwright.sync_api import Playwright, sync_playwright, expect

"""
    代码生成

    playwright codegen -o [文件名.py] -b firefox
"""


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com/")
    page.locator("#kw").fill("hello")
    page.get_by_text("hello kitty").click()
    page.get_by_role("button", name="百度一下").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Hello Kitty - 百度百科").click()
    page1 = page1_info.value

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
