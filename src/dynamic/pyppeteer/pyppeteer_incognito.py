from pyppeteer import launch
import asyncio

"""
    开启无痕模式
"""

width, height = 1920, 1080


async def main():
    browser = await launch(
        headless=False, args=["--disable-infobars", f"--window-size={width},{height}"]
    )
    try:
        context = await browser.createIncogniteBrowserContext()
        page = await context.newPage()
        await page.setViewport({"width": width, "height": height})
        await page.goto("https://www.baidu.com")
        await asyncio.sleep(5)
    finally:
        await browser.close()


asyncio.run(main())
