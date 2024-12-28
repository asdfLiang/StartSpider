from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from parsel import Selector
import re
import requests

"""
    字体反爬 - 数据在css文件中
"""


def get_icon_map() -> dict:
    url = "https://antispider4.scrape.center/css/app.654ba59e.css"
    with requests.get(url=url) as response:
        pattern = re.compile('.icon-(.*?):before{content:"(.*?)"}')
        result = re.findall(pattern, response.text)
        return {item[0]: item[1] for item in result}


def parse_score(item) -> str:
    elements = item.css(".score .icon::attr(class)").re(r"icon-(.*)")
    return "".join([icon_map[element] for element in elements])


with webdriver.Chrome() as browser:
    # 获取网页
    browser.get("https://antispider4.scrape.center/")
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".item")))
    html = browser.page_source
    selector = Selector(text=html)
    # 获取字体映射
    icon_map = get_icon_map()
    # 替换字体
    for item in selector.css(".item"):
        name = item.css(".name ::text").get().strip()
        categories = [
            category.get().strip() for category in item.css(".categories button ::text")
        ]
        scroe = parse_score(item)
        print(f"name: {name}, categories: {categories}, scroe: {scroe}")
