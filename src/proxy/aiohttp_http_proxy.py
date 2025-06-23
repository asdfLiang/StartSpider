import aiohttp
import asyncio
from free_proxy import proxy

"""
    aiohttp 设置http代理（通过）
"""

proxy = "http://" + proxy  # Ensure the proxy is in the correct format


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://httpbin.org/get", proxy=proxy) as response:
            print(await response.text())


if __name__ == "__main__":
    asyncio.run(main())
