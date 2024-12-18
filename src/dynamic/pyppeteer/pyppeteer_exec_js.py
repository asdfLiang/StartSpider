from pyppeteer import launch
import asyncio

"""
    执行js
"""

width, height = 1920, 1080


async def main():
    browser = await launch()
    try:
        page = await browser.newPage()
        await page.setViewport({"width": width, "height": height})
        await page.goto("https://spa2.scrape.center/")
        await page.waitForSelector(".item .name")
        await asyncio.sleep(2)
        await page.screenshot(path="tests/downloads/example_js.png")
        dimensions = await page.evaluate(
            """() => {return {width: document.documentElement.clientWidth, height: document.documentElement.clientHeight, deviceScaleFactor: window.devicePixelRatio}}"""
        )
        print(dimensions)
    finally:
        await browser.close()


asyncio.run(main())
