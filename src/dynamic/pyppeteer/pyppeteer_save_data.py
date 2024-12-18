from pyppeteer import launch
import asyncio

"""
    用户数据持久化
"""


async def main():
    browser = await launch(
        headless=False,
        userDataDir="./tests/downloads/taobao",
        args=["--disable-infobars"],
    )
    try:
        page = await browser.newPage()
        await page.goto("https://www.taobao.com")
        await asyncio.sleep(5)
    finally:
        await browser.close()


asyncio.run(main())
