import asyncio, requests, time

"""
    尝试协程异步执行(失败了，协程还是顺序执行的，为什么？)
"""

start = time.time()


async def get(url: str):
    # 因为requests.get()是阻塞调用，切换到其他协程执行后，会阻塞而不是异步执行，所以结果还是顺序执行的
    return requests.get(url)


async def request():
    url = "https://www.httpbin.org/delay/5"
    print("Waiting for ", url)
    response = await get(url)  # await关键字可以将耗时等待操作挂起，让出控制权
    print("Get response from", url, "response", response)


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
# 定义批量任务
tasks = [asyncio.ensure_future(request()) for _ in range(10)]
# 执行任务
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print("Cost time:", end - start)  # Cost time: 65.76079821586609
