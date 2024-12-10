import asyncio, aiohttp, time

"""
    异步请求
"""

start = time.time()


async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)  # 自动切换，这个操作是非阻塞的，所以可以异步
    await response.text()  # 挂起
    await session.close()  # 挂起
    return response


async def request():
    url = "https://www.httpbin.org/delay/5"
    print("Waiting for", url)
    response = await get(url)  # 挂起
    print("Get response from", url, "response", response)


async def main():
    tasks = [asyncio.ensure_future(request()) for _ in range(10)]
    await asyncio.gather(*tasks)


# 批量任务执行
asyncio.run(main())

end = time.time()
print("Cost time:", end - start)  # Cost time: 6.764430522918701
