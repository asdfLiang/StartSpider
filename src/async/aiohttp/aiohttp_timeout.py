import asyncio, aiohttp

"""
    超时设置
"""


async def main():
    timeout = aiohttp.ClientTimeout(total=1)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get("https://www.httpbin.org/get") as response:
            print("status:", response.status)


if __name__ == "__main__":
    asyncio.run(main())
