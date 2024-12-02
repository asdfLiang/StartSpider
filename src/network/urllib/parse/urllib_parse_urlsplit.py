from urllib.parse import urlsplit, urlunsplit

"""
    url识别和分段（与urlparse的区别是不单独解析params）
"""

# URL分段 [scheme    netloc  path   query   fragment]
result = urlsplit("https://www.baidu.com/index.html;user?id=5#comment")
print(result)

# URL构造
data = ["https", "www.baidu.com", "index.html", "a=6", "comment"]
print(urlunsplit(data))
