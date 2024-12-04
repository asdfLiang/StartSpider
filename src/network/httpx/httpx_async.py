import httpx
import asyncio

"""
    异步请求
"""


async def fetch(url):
    async with httpx.AsyncClient(http2=True) as client:
        resp0 = await client.get(url=url)
        print(resp0.text)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(fetch("https://www.httpbin.org/get"))
