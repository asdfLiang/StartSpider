import asyncio

"""
    协程
"""


# 协程定义方式
async def execute(x: int) -> None:
    print("Number:", x)


"""
    使用协程
"""
coroutine = execute(1)
print("Coroutine:", coroutine)
print("After calling execute")
# 创建事件循环对象
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
# 启动loop
loop.run_until_complete(coroutine)
print("After calling loop")

print()

"""
    显式声明task对象
"""
coroutine = execute(1)
print("Coroutine:", coroutine)
print("After calling execute")
# 创建事件循环对象
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
# 定义任务
task = loop.create_task(coroutine)
print("Task:", task)
# 执行任务
loop.run_until_complete(task)
print("Task:", task)
print("After calling loop")

print()

"""
    另一种定义task方式
"""
coroutine = execute(1)
print("Coroutine:", coroutine)
print("After calling execute")
# 创建事件循环对象
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
# 定义任务
task = asyncio.ensure_future(coroutine)
print("Task:", task)
# 执行任务
loop.run_until_complete(task)
print("Task:", task)
print("After calling loop")
