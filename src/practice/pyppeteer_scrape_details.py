from pyppeteer import launch
from pyppeteer.errors import TimeoutError
import asyncio
import logging

"""
    pyppeteer爬虫实践
"""

# 日志配置
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s"
)

# 网页配置
INDEX_URL = "https://spa2.scrape.center/page/{page}"
TIME_OUT = 10
TOTAL_PAGE = 2

WINDOW_WIDTH, WINDOW_HEIGHT = 1366, 768
HEADLESS = False

browser, tab = None, None


# 初始化浏览器
async def init():
    global browser, tab
    browser = await launch(
        headless=HEADLESS,
        args=["--disable-infobars", f"--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}"],
    )
    tab = await browser.newPage()
    await tab.setViewport({"width": WINDOW_WIDTH, "height": WINDOW_HEIGHT})


# 通用爬取方法
async def scrape_page(url, selector):
    logging.info("scraping %s", url)
    try:
        await tab.goto(url)
        await tab.waitForSelector(selector, options={"timeout": TIME_OUT * 1000})
    except TimeoutError:
        logging.error("error occurred while scraping %s", url, exc_info=True)


# 爬取列表页
async def scrape_index(page):
    url = INDEX_URL.format(page=page)
    await scrape_page(url, ".item .name")


# 爬取详情页
async def scrape_detail(url):
    await scrape_page(url, "h2")


# 解析详情页链接
async def parse_index():
    return await tab.querySelectorAllEval(
        ".item .name", "nodes => nodes.map(node => node.href)"
    )


# 解析详情页
async def parse_detail():
    url = tab.url
    name = await tab.querySelectorEval(".item h2", "node => node.innerText")
    category = await tab.querySelectorEval(".item .category", "node => node.innerText")
    cover = await tab.querySelectorEval(".item .cover", "node => node.src")
    scroe = await tab.querySelectorEval(".item .score", "node => node.innerText")
    drama = await tab.querySelectorEval(".item .drama p", "node => node.innerText")
    return {
        "url": url,
        "name": name,
        "category": category,
        "cover": cover,
        "scroe": scroe,
        "drama": drama,
    }


async def main():
    await init()
    try:
        for page in range(1, TOTAL_PAGE + 1):
            await scrape_index(page)
            detail_urls = await parse_index()
            for detail_url in detail_urls:
                await scrape_detail(detail_url)
                detail_data = await parse_detail()
                logging.info("detail data %s", detail_data)
    finally:
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
