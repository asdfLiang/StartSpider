from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener
from free_proxy import proxy

"""
    urllib 设置http代理（通过）
"""
proxy_handler = ProxyHandler({"http": f"http://{proxy}", "https": f"http://{proxy}"})
opener = build_opener(proxy_handler)
try:
    response = opener.open("https://www.httpbin.org/get", timeout=10)
    print(response.read().decode("utf-8"))
except URLError as e:
    print(e.reason)
