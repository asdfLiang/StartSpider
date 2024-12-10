import asyncio, aiohttp

"""
    post 请求
"""


# 传递data参数
async def post_data():
    data = {"name": "germey", "age": 25}
    async with aiohttp.ClientSession() as session:
        async with session.post("https://www.httpbin.org/post", data=data) as response:
            print(await response.text())


# 传递json参数
async def post_json():
    data = {"name": "germey", "age": 25}
    async with aiohttp.ClientSession() as session:
        async with session.post("https://www.httpbin.org/post", json=data) as response:
            print("status:", response.status)
            print("headers:", response.headers)
            print("body:", await response.text())
            print("bytes:", await response.read())
            print("json", await response.json())


if __name__ == "__main__":
    asyncio.run(post_json())
