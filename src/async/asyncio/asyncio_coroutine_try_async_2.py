import asyncio, requests, time

"""
    尝试异步执行（失败，为什么？）
"""


async def request():
    url = "https://www.httpbin.org/delay/5"
    return requests.get(url)


# 定义一个简单的异步函数
async def async_function(name, delay):
    print(f"{name} is starting to wait for {delay} seconds.")
    await request()  # 异步等待
    print(f"{name} has finished waiting.")


async def main():
    # 创建多个协程任务
    task1 = asyncio.create_task(async_function("Task 1", 2))
    task2 = asyncio.create_task(async_function("Task 2", 1))

    # 等待所有任务完成
    await task1
    await task2


# 运行主协程
start = time.time()
asyncio.run(main())
end = time.time()
print("Cost: ", end - start)
