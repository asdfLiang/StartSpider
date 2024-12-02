from urllib import request, error
import socket

# 打开一个不存在的页面
try:
    response = request.urlopen("https://www.baidu.com/404")
except error.URLError as e:
    print(e.reason)

# 处理Http请求错误
try:
    response = request.urlopen("https://www.baidu.com/404")
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep="\n")

# reason是一个对象
try:
    response = request.urlopen("https://www.baidu.com/404", timeout=0.01)
except error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print("TIMEOUT")
