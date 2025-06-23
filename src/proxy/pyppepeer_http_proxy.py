from pyppeteer import launch
import asyncio
from free_proxy import proxy

"""
    pyppeteer 设置http代理（通过）
"""


async def main():
    browser = await launch(
        {"args": ["--proxy-server=http://" + proxy], "headless": False}
    )
    try:
        page = await browser.newPage()
        await page.goto("https://httpbin.org/get")
        print(await page.content())
    finally:
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
