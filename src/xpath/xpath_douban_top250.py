import requests
from lxml import etree

"""
    豆瓣电影top250
"""


class DouBan:
    url = "https://movie.douban.com/top250?start=%d&filter="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

    def getTop250(self) -> list:
        top250_list = []
        for i in range(10):
            url = self.url % (i * 25)
            page = requests.get(url=url, headers=self.headers).content.decode()
            # 解析网页
            html = etree.HTML(page)
            page_list = html.xpath("//*[@class='grid_view']/li")
            # 解析列表数据
            for li in page_list:
                rank = li.xpath(".//em/text()")[0]
                title = li.xpath(".//span[@class='title']/text()")[0]
                rating_num = li.xpath(".//div[@class='star']/span/text()")[0]
                num = li.xpath(".//div[@class='star']/span/text()")[1]
                top250_list.append(
                    f"{rank} 电影名称：{title}    评分：{rating_num}    {num}"
                )

        return top250_list


if __name__ == "__main__":
    douBan = DouBan()
    top_list = douBan.getTop250()
    for elm in top_list:
        print(elm)
