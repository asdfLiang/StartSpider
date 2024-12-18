from pyppeteer import launch
from parsel import Selector
import asyncio

"""
    节点选择器
"""


async def main():
    browser = await launch()
    try:
        page = await browser.newPage()
        await page.goto("https://spa2.scrape.center/")
        await page.waitForSelector(".item .name")
        j_result1 = await page.J(".item .name")
        j_result2 = await page.querySelector(".item .name")
        jj_result1 = await page.JJ(".item .name")
        jj_result2 = await page.querySelectorAll(".item .name")
        print("J Result1:", j_result1)
        print()
        print("J Result2:", j_result2)
        print()
        print("JJ Result1:", jj_result1)
        print()
        print("JJ Result1:", jj_result2)
    finally:
        await browser.close()


asyncio.run(main())
