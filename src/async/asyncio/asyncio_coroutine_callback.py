import asyncio, requests

"""
    绑定回调
"""


async def request():
    url = "https://www.baidu.com"
    status = requests.get(url)
    return status


def callback(task):
    print("Status:", task.result())


"""
    使用回调方法处理结果
"""
coroutine = request()
# 定义事件循环对象
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
# 定义任务
task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)  # 绑定回调
print("Task:", task)
# 执行任务
loop.run_until_complete(task)
print("Task:", task)

print()

"""
    不使用回调方法，直接输出结果
"""
coroutine = request()
# 定义事件循环对象
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
# 定义任务
task = asyncio.ensure_future(coroutine)
print("Task:", task)
# 执行任务
loop.run_until_complete(task)
print("Task:", task)
print("Task Result:", task.result())
