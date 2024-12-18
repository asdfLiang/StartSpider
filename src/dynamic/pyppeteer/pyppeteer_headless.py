from pyppeteer import launch
import asyncio

"""
    无头模式
"""


# 关闭无头模式（无头模式是默认开启的）
async def main():
    browser = await launch(headless=False)
    try:
        await asyncio.sleep(5)
    finally:
        await browser.close()


asyncio.run(main())
