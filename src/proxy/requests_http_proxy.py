import requests
from free_proxy import proxy

"""
    requests 的代理设置（通过）
"""

proxies = {"http": "http://" + proxy, "https": "http://" + proxy}

try:
    response = requests.get("https://www.httpbin.org/get", proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print("Error", e.args)
