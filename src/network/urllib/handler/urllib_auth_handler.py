from urllib.request import (
    HTTPPasswordMgrWithDefaultRealm,
    HTTPBasicAuthHandler,
    build_opener,
)
from urllib.error import URLError

"""
    模拟登录
"""

username = "admin"
password = "admin"
url = "https://ssr3.scrape.center/"

# 构建Handler
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
# 构建Opener
opener = build_opener(auth_handler)

try:
    res = opener.open(url)
    html = res.read().decode("utf-8")
    print(html)
except URLError as e:
    print(e.reason)
