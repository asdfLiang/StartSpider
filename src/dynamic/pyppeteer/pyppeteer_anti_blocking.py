from pyppeteer import launch
import asyncio

"""
    防止检测
"""

width, height = 1920, 1080


# 被检测
async def be_blocking():
    # 设置窗口大小
    browser = await launch(
        headless=False, args=["--disable-infobars", f"--window-size={width}, {height}"]
    )
    try:
        page = await browser.newPage()
        await page.setViewport({"width": width, "height": height})  # 设置页面大小
        await page.goto("https://antispider1.scrape.center/")
        await asyncio.sleep(5)
    finally:
        await browser.close()


asyncio.run(be_blocking())


# 防止检测
async def anti_blocking():
    # 设置窗口大小
    browser = await launch(
        headless=False, args=["--disable-infobars", f"--window-size={width}, {height}"]
    )
    try:
        page = await browser.newPage()
        await page.setViewport({"width": width, "height": height})  # 设置页面大小
        await page.evaluateOnNewDocument(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )
        await page.goto("https://antispider1.scrape.center/")
        await asyncio.sleep(5)
    finally:
        await browser.close()


asyncio.run(anti_blocking())
