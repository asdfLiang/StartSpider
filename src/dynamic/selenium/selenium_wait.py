from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
    延时等待
"""


with webdriver.Edge() as browser:
    # 显式等待, 指定等待的节点
    browser.get("https://www.taobao.com")
    wait = WebDriverWait(browser, 10)
    # 等待这两个节点10s，10s内加载出来就返回，否则报错
    input = wait.until(EC.presence_of_element_located((By.ID, "q")))
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-search")))
    print(input, button)


with webdriver.Chrome() as browser:
    # 隐式等待，不指定等待节点
    browser.implicitly_wait(10)
    browser.get("https://spa2.scrape.center/")
    input = browser.find_element(By.CLASS_NAME, "logo-image")
    print(input)
