from pyppeteer import launch
import asyncio

"""
    禁用提示条
"""


async def main():
    browser = await launch(headless=False, args=["--disable-infobars"])
    try:
        page = await browser.newPage()
        await page.goto("https://www.baidu.com")
        await asyncio.sleep(1)
    finally:
        await browser.close()


asyncio.run(main())
