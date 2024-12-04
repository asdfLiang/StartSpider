import requests

"""
    get请求
"""

response = requests.get(url="https://www.baidu.com")

# 获取网页内容
# print(response.text) # 获取到的是字符串，可能乱码
print(response.content.decode())

# 获取状态码
print(response.status_code)

# 获取请求头信息, 请求头中的 'User-Agent': 'python-requests/2.32.3' 暴露了是个爬虫，因此没有获取到完整的网页内容
print(response.request.headers)


print("=====================================================================")

# 带参数的get请求
data = {"name": "germey", "age": 25}
print(requests.get("https://httpbin.org/get", params=data).text)
