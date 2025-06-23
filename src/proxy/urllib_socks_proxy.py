import socks
import socket
from urllib import request
from urllib.error import URLError
from free_proxy import proxy, proxy_address, proxy_port

"""
    urllib 设置socks代理
"""

socks.set_default_proxy(socks.SOCKS5, proxy_address, proxy_port)
socket.socket = socks.socksocket
try:
    response = request.urlopen("https://www.httpin.org/get")
    print(response.read().decode("utf-8"))
except URLError as e:
    print(e.reason)
