from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""
    节点交互
"""

browser = webdriver.Chrome()
try:
    browser.get("https://www.taobao.com")
    input = browser.find_element(By.ID, "q")  # 选择输入框
    input.send_keys("iPhone")  # 输入搜索内容
    time.sleep(1)
    input.clear()  # 清空输入内容
    input.send_keys("iPad")  # 输入新的搜索内容
    button = browser.find_element(By.CLASS_NAME, "btn-search")  # 搜索按钮
    button.click()  # 点击
finally:
    browser.close()
