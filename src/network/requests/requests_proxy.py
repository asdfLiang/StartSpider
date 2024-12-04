import requests

"""
    代理设置
"""

# 普通代理设置
proxies = {"http": "http://10.10.10.10:1080", "https": "https://10.10.10.10.1080"}
requests.get("https://www.httpbin.org/get", proxies=proxies)

# 使用身份认证
proxies = {"https": "http://user:password@10.10.10.10.1080"}

# 使用socks代理
proxies = {
    "http": "socks5://user:password@host:port",
    "https": "socks5://user:password@host:port",
}
