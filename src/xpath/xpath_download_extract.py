import requests
from lxml import etree

"""
    xpath

    pip install lxml
"""

url = "https://movie.douban.com/cinema/nowplaying/hangzhou/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

page = requests.get(url=url, headers=headers).content.decode()

# 豆瓣电影-电影票-杭州
html = etree.HTML(page)
data_list = html.xpath("//*[@class='list-item']")
for li in data_list:
    title = li.xpath("./@data-title")[0]
    score = li.xpath("./@data-score")
    print(f"电影名称：{title} 评分：{score}")
# print(data_list)

# 先下载再过滤
# with open("src/spider/downloads/douban_hangzhou.html", "wb") as f:
#     f.write(requests.get(url=url, headers=headers).content)

# with open("src/spider/downloads/douban_hangzhou.html", "r", encoding="utf-8") as f:
#     page = f.read()

#     html = etree.HTML(page)
#     data_list = html.xpath("//*[@class='stitle']/a/text()")
#     print(data_list)
