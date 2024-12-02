from urllib.parse import urlencode

"""
    构造GET请求参数
"""

params = {"name": "germey", "age": 25}

base_url = "https://www.baidu.com?"
url = base_url + urlencode(params)

print(url)
