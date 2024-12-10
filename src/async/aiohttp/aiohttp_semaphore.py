import asyncio, aiohttp

"""
    并发限制
"""

CONCURRENCY = 5
URL = "https://www.baidu.com"

semaphore = asyncio.Semaphore(CONCURRENCY)


async def scrape_api(session):
    async with semaphore:
        print("scraping", URL)
        async with session.get(URL) as response:
            await asyncio.sleep(1)
            return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(scrape_api(session)) for _ in range(100)]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
