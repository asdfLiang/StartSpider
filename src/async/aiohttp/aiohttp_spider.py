import asyncio, aiohttp, logging, json
from motor.motor_asyncio import AsyncIOMotorClient

"""
    异步爬取
"""

"""
    基本配置
"""
# 日志配置
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# 页面爬取配置
INDEX_URL = "https://spa5.scrape.center/api/book?limit=18&offset={offset}"
DETAIL_URL = "https://spa5.scrape.center/api/book/{id}/"

PAGE_SIZE = 18
PAGE_NUMBER = 100
CONCURRENCY = 5

# 并发配置
semaphore = asyncio.Semaphore(CONCURRENCY)

# mongodb配置
MONGO_URL = "mongodb://liangzj:123456@localhost:27017"
MONGO_DB_NAME = "books"
MONGO_COLLECTION_NAME = "books"
client = AsyncIOMotorClient(MONGO_URL)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]


"""
    数据爬取
"""


# 网络查询
async def scrape_api(session, url):
    async with semaphore:
        try:
            logging.info("scraping %s", url)
            async with session.get(url) as response:
                return await response.json()
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


"""
    数据存储
"""


# 保存到文本文件中
async def save_to_text(file, data):
    file.write(data + "\n")


# 保存一页数据到text
async def scrape_details_text(session, index_data):
    with open("tests/downloads/scrape_details.txt", "a+", encoding="utf-8") as file:
        for item in index_data.get("results"):
            data = await scrape_detail(session, item.get("id"))
            await save_to_text(file, data)


# 保存到mongodb中
async def save_to_mongo(data):
    logging.info("saving data %s", data)
    if data:
        return await collection.update_one(
            {"id": data.get("id")}, {"$set": data}, upsert=True
        )


# 保存一页数据到mongodb
async def scrape_details_mongo(session, index_data):
    for item in index_data.get("results"):
        data = await scrape_detail(session, item.get("id"))
        await save_to_mongo(data)


"""
    任务构建
"""


# 批量任务构建
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.ensure_future(scrape_index(session, page))
            for page in range(1, PAGE_NUMBER + 1)
        ]
        result = await asyncio.gather(*tasks)
        for index_data in result:
            await scrape_details_text(session, index_data)
        logging.info("result %s", json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
