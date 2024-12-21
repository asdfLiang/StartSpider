from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import logging
from urllib.parse import urljoin

"""
    selenium爬虫实践
"""

# 日志配置
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s"
)

# 网页配置
INDEX_URL = "https://spa2.scrape.center/page/{page}"
TIME_OUT = 10
TOTAL_PAGE = 1

# 初始化浏览器
browser = webdriver.Chrome()
wait = WebDriverWait(browser, TIME_OUT)


# 通用爬取方法
def scrape_page(url, condition, locator):
    logging.info("scraping %s", url)
    try:
        browser.get(url)
        wait.until(condition(locator))
    except TimeoutException:
        logging.error("error occurred while scraping %s", url, exc_info=True)


# 爬取列表页
def scrape_index(page):
    url = INDEX_URL.format(page=page)
    scrape_page(
        url,
        condition=EC.visibility_of_all_elements_located,
        locator=(By.CSS_SELECTOR, "#index .item"),
    )


# 爬取详情页
def scrape_detail(url):
    scrape_page(
        url,
        condition=EC.visibility_of_element_located,
        locator=(By.CSS_SELECTOR, "h2"),
    )


# 解析详情页
def parse_detail():
    url = browser.current_url
    name = browser.find_element(By.CSS_SELECTOR, "h2").text
    categories = [
        element.text
        for element in browser.find_elements(By.CSS_SELECTOR, ".categories button span")
    ]
    cover = browser.find_element(By.CSS_SELECTOR, ".cover").get_attribute("src")
    score = browser.find_element(By.CSS_SELECTOR, ".score").text
    drama = browser.find_element(By.CSS_SELECTOR, ".drama p").text
    return {
        "url": url,
        "name": name,
        "categories": categories,
        "cover": cover,
        "score": score,
        "drama": drama,
    }


# 解析链接
def parse_index():
    elements = browser.find_elements(By.CSS_SELECTOR, "#index .item .name")
    logging.debug("find %s elements in index page", len(elements))
    for element in elements:
        href = element.get_attribute("href")
        yield urljoin(INDEX_URL, href)


def main():
    try:
        for page in range(1, TOTAL_PAGE + 1):
            scrape_index(page)
            detail_urls = parse_index()
            for detail_url in detail_urls:
                logging.info("scraping detail page %s", detail_url)
                scrape_detail(detail_url)  # 这里会跳转到详情页
                data = parse_detail()  # 解析详情页
                logging.info("detail data %s", data)
                browser.back()  # 返回上一页
    finally:
        browser.close()


if __name__ == "__main__":
    main()
