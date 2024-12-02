from urllib.parse import quote, unquote

"""
    转换为URL编码格式
"""
keyword = "测试"
url = "https://www.baidu.com/?keyword=" + quote(keyword)

print(url)
print(unquote(url))
