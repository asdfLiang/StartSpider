from urllib.parse import urlparse, urlunparse

"""
    url的识别和分段
"""

# 识别URL [scheme    netloc  path    params  query   fragment]
result = urlparse("https://www.baidu.com/index.html;user?id=5#comment")
print(type(result))
print(result)

# 构造URL
data = ["https", "www.baidu.com", "index.html", "user", "a=6", "comment"]
print(urlunparse(data))
