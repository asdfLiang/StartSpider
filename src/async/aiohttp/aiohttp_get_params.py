import asyncio, aiohttp

"""
    参数传递
"""


async def main():
    params = {"name": "germey", "age": 25}
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://www.httpbin.org/get", params=params
        ) as response:
            print(await response.text())


if __name__ == "__main__":
    asyncio.run(main())
