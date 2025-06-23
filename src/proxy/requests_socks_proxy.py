import requests
from free_proxy import proxy

"""
    requests 设置socks代理
"""


proxies = {"http": f"socks5://{proxy}", "https": f"socks5://{proxy}"}
try:
    response = requests.get("https://www.httpbin.org/get", proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print("Error", e.args)
