import asyncio, requests

"""
    多任务协程（顺次执行）
"""


async def request():
    url = "https://www.baidu.com"
    status = requests.get(url=url)
    return status


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
# 创建批量任务
tasks = [asyncio.ensure_future(request()) for _ in range(5)]
print("Tasks:", tasks)
# 顺次执行任务
loop.run_until_complete(asyncio.wait(tasks))
for task in tasks:
    print("Task Result:", task.get_name(), task.result())
