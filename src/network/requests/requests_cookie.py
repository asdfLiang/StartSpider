import requests
import requests.cookies

"""
    Cookie 操作
"""

# 获取cookie
response = requests.get("https://www.baidu.com")
print(response.cookies)
for key, value in response.cookies.items():
    print(f"{key} = {value}")

# 使用cookie维持登录状态
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Cookie": "_octo=GH1.1.1007063068.1731250252; _device_id=002747cbc6dfefd0c20e20037f67ca75; saved_user_sessions=23564563%3A85npgY_c2hGBwVgx6lj6MWVQhbtcoGpeEeScboExPXN2WfI5; user_session=85npgY_c2hGBwVgx6lj6MWVQhbtcoGpeEeScboExPXN2WfI5; __Host-user_session_same_site=85npgY_c2hGBwVgx6lj6MWVQhbtcoGpeEeScboExPXN2WfI5; logged_in=yes; dotcom_user=asdfLiang; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; cpu_bucket=xlg; preferred_color_mode=light; tz=Asia%2FShanghai; _gh_sess=mf0N7P3GAc1nQdpjYUto4vpO20LCRKSuEjMXNlkQcLcd1BvTV%2B2hrKAsRSsrVJCXOZkovlXKwoDB%2FKJz2kHc%2FV%2B1%2FIFjTWbFJis6DXhzQGlGLb1ixcuYVo%2F389xdU%2BoMnz%2FPjKkYfTdI1RKWPESWn7XRliQCBptl1ttIx5hpRsodV3gOSmXUj8hmGTbwOq%2BoFhYDDXF1wC3UGwT5KbvhSt155QXhPirga1qfjnxJJCz4Z1wcQtjTAtKeTS5KsfiNIhf2jGsi4S8W90YnU83AJeW3pvzjhrFyBCXiokqXF2QvBBgsPk1D7Bx7tJNX9XlglMHeLWjEx1JsHT%2Bwpk%2FeMG76M6zsGC9g4gFny1mo2XQBGHAqSuZs%2BeZMWt8nllup--J2U5cgiR1%2BS0WKQl--XK5loD2svPrAl0OeY07Zfg%3D%3D",
}
resp = requests.get("https://github.com/", headers=headers)
print(resp.text)

with open("downloads/asdfLiang_github.html", "wb") as f:
    f.write(resp.content)
