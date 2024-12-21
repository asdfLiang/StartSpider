import asyncio
from playwright.async_api import async_playwright

"""
    基本使用 - 异步请求
"""


async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = await browser_type.launch()
            try:
                page = await browser.new_page()
                await page.goto("https://www.baidu.com")
                await page.screenshot(path=f"async-screenshot-{browser_type.name}.png")
                print(await page.title())
            finally:
                await browser.close()


asyncio.run(main())
