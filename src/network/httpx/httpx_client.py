import httpx

"""
    （官方推荐）使用with as句式
"""

# 这个写法等价于try finally
with httpx.Client() as client:
    resp0 = client.get("https://www.httpbin.org/get")
    print(resp0)

# 声明时指定header
headers = {"User-agent": "my-app/0.0.1"}
with httpx.Client(headers=headers) as client:
    resp1 = client.get("https://www.httpbin.org/headers")
    print(resp1.json()["headers"]["User-Agent"])

# 支持http2
with httpx.Client(http2=True) as client:
    resp2 = client.get("https://www.httpbin.org/get")
    print(resp2.text)
    print(resp2.http_version)
