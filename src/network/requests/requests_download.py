import requests

"""
    下载内容
"""

url = "https://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

response = requests.get(url=url, headers=headers)

with open("downloads/baidu.html", "wb") as f:
    f.write(response.content)
