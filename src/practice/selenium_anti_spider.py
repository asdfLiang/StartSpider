from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from parsel import Selector

"""
    CSS位置偏移反扒实践 - 文字的位置由css控制
"""


def parse_name(name_html: Selector):
    if name_html.css(".whole"):
        return name_html.css("::text").get().strip()

    chars = name_html.css(".char")
    items = []
    for char in chars:
        items.append(
            {
                "text": char.css("::text").get().strip(),
                "left": int(char.css("::attr(style)").re_first(r"(\d+)px")),
            }
        )
    items.sort(key=lambda x: x["left"])
    return "".join([item["text"] for item in items])


with webdriver.Chrome() as driver:
    driver.get("https://antispider3.scrape.center/")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".item"))
    )
    html = driver.page_source
    selector = Selector(text=html)
    names = selector.css(".item .name")
    for name in names:
        name = parse_name(name)
        print(name)
