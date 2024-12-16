import urllib.request, http.cookiejar

"""
    保存 cookie
"""

# 构建handler
filename = "tests/downloads/cookie.txt"
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
# 构建opener
opener = urllib.request.build_opener(handler)

response = opener.open("https://www.baidu.com")
cookie.save(ignore_discard=True, ignore_expires=True)
