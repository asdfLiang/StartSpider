from urllib.request import urlopen

"""
    get请求
"""

url = "http://www.baidu.com"


response = urlopen(url=url)
print(response.read().decode("utf-8"))
print(type(response))
print(type(response.read()))

with open("tests/downloads/mybaidu.html", "wb") as f:
    f.write(response.read())
