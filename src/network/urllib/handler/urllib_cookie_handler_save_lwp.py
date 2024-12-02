import urllib.request, http.cookiejar

"""
    保存LWP格式的Cookie文件
"""

# 构建handler
filename = "downloads/cookie_lwp.txt"
cookie = http.cookiejar.LWPCookieJar(filename=filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
# 构建opener
opener = urllib.request.build_opener(handler)

response = opener.open("https://www.baidu.com")
cookie.save(ignore_discard=True, ignore_expires=True)
