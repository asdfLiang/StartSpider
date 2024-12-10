import asyncio, aiohttp, logging, json

"""
    异步爬取
"""

# 基本配置
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

INDEX_URL = "https://spa5.scrape.center/api/book?limit=18&offset={offset}"
DETAIL_URL = "https://spa5.scrape.center/api/book/{id}/"

PAGE_SIZE = 18
PAGE_NUMBER = 100
CONCURRENCY = 5

semaphore = asyncio.Semaphore(CONCURRENCY)


# 网络查询
async def scrape_api(session, url):
    async with semaphore:
        try:
            logging.info("scraping %s", url)
            async with session.get(url) as response:
                return await response.text()
        except aiohttp.ClientError:
            logging.error("error occurred while scraping %s", url, exc_info=True)


# 查询一页数据
async def scrape_index(session, page):
    url = INDEX_URL.format(offset=PAGE_SIZE * (page - 1))
    return await scrape_api(session, url)


# 查询一条详情
async def scrape_detail(session, id):
    url = DETAIL_URL.format(id=id)
    return await scrape_api(session, url)


# 保存一条数据
async def save_data(file, data):
    file.write(data + "\n")


# 保存一页数据
async def save_page_data(session, index_data):
    with open("downloads/scrape_details.txt", "a+", encoding="utf-8") as file:
        for item in index_data.get("results"):
            data = await scrape_detail(session, item.get("id"))
            await save_data(file, data)


# 批量任务构建
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.ensure_future(scrape_index(session, page))
            for page in range(1, PAGE_NUMBER + 1)
        ]
        result = await asyncio.gather(*tasks)
        for index_data in result:
            await save_page_data(session, json.loads(index_data))
        logging.info("result %s", json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
