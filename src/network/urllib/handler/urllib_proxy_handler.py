from urllib.request import ProxyHandler, build_opener

from urllib.error import URLError

"""
    使用代理请求
"""

# 构建handler
proxy_handler = ProxyHandler(
    {"http": "http://127.0.0.1:8080", "https": "https://127.0.0.1:8080"}
)
# 构建opener
opener = build_opener(proxy_handler)

try:
    response = opener.open("https://www.baidu.com")
    print(response.read().decode("utf-8"))
except URLError as e:
    print(e.reason)
