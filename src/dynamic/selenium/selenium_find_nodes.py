from selenium import webdriver
from selenium.webdriver.common.by import By

"""
    查找多个节点
"""

browser = webdriver.Chrome()
try:
    browser.get("https://www.taobao.com")
    ls = browser.find_elements(
        By.CSS_SELECTOR, ".service-bd--LdDnWwA9 li"
    )  # 查找左侧导航栏
    print(ls)
finally:
    browser.close()
