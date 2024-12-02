import http.cookiejar as cookiejar, urllib.request

"""
    获取cookie
"""

# 构建handler
cookie = cookiejar.CookieJar()
hander = urllib.request.HTTPCookieProcessor(cookie)
# 构建opener
opener = urllib.request.build_opener(hander)

response = opener.open("https://www.baidu.com")
for item in cookie:
    print(f"{item.name} = {item.value}")
