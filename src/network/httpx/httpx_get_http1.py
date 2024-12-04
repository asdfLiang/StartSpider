import httpx

"""
    http1请求
"""

# http1 请求
resp0 = httpx.get("https://www.httpbin.org/get")
print(resp0.status_code)
print(resp0.headers)
print(resp0.text)

print("===============================================================")

# 换一个User-agent请求
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
resp1 = httpx.get("https://www.httpbin.org/get", headers=headers)
print(resp1.text)

print("===============================================================")

# http2 请求，直接请求还是会报错，需要手动开启
""" # 错误演示
resp2 = httpx.get("https://spa16.scrape.center/")
print(resp2.status_code)
"""
