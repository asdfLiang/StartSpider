from selenium import webdriver
from selenium.webdriver.common.by import By

"""
    查找单个节点
"""

browser = webdriver.Chrome()
try:
    browser.get("https://www.taobao.com")
    input1 = browser.find_element(By.ID, "q")  # 根据id搜索输入框
    input2 = browser.find_element(By.CSS_SELECTOR, "#q")  # css选择器搜索输入框
    input3 = browser.find_element(By.XPATH, ".//*[@id='q']")  # xpath搜索输入框
    print(input1)
    print(input2)
    print(input3)
finally:
    browser.close()
