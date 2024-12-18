import asyncio
from pyppeteer import launch
from parsel import Selector

"""
    基本使用
"""


# 打开网页，提取内容
async def extract():
    browser = await launch()
    try:
        # 网页请求
        page = await browser.newPage()
        await page.goto("https://spa2.scrape.center/")
        await page.waitForSelector(".item .name")
        # 提取文本
        selector = Selector(text=await page.content())
        names = [item for item in selector.css(".item .name *::text").getall()]
        print("Names", names)
    finally:
        await browser.close()


asyncio.run(extract())


width, height = 1920, 1080


# 页面截图
async def screenshot():
    browser = await launch()
    try:
        page = await browser.newPage()
        await page.setViewport({"width": width, "height": height})
        await page.goto("https://spa2.scrape.center/")
        await page.waitForSelector(".item .name")
        await asyncio.sleep(2)
        await page.screenshot(path="tests/downloads/example.png")
        dimensions = await page.evaluate(
            """() => {
                return {
                    width: document.documentElement.clientWidth,
                    height: document.documentElement.clientHeight,
                    deviceScaleFactor: window.devicePixelRatio,
                }
            }"""
        )
        print(dimensions)
    finally:
        await browser.close()


asyncio.run(screenshot())
