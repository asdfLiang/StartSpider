import requests

"""
    文件上传
"""

file = {"file": open("downloads/cookie.txt", "rb")}
response = requests.post("https://www.httpbin.org/post", files=file)
print(response.text)
