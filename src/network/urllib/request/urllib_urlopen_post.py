import urllib.parse as parse
from urllib.request import urlopen

"""
    post 请求
"""

data = bytes(parse.urlencode({"name": "germey"}), encoding="utf-8")

response = urlopen("https://www.httpbin.org/post", data=data)
print(response.read().decode("utf-8"))
