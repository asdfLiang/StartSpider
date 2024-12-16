import urllib.request, http.cookiejar

"""
    修改cookie
"""

# 构建handler
cookie = http.cookiejar.LWPCookieJar()
cookie.load("tests/downloads/cookie_lwp.txt", ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
# 构建opener
opener = urllib.request.build_opener(handler)

#
response = opener.open("https://www.baidu.com")
print(response.read().decode("utf-8"))
