from pyppeteer import launch
import asyncio

"""
    调试模式
"""


async def main():
    browser = await launch(devtools=True)
    try:
        page = await browser.newPage()
        await page.goto("https://www.baidu.com")
        await asyncio.sleep(1)
    finally:
        await browser.close()


asyncio.run(main())
