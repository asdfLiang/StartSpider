from selenium import webdriver
import time

"""
    前进和后退
"""

with webdriver.Chrome() as browser:
    browser.get("https://www.baidu.com")
    browser.get("https://www.taobao.com")
    browser.get("https://leetcode.cn/")
    browser.back()
    time.sleep(1)
    browser.forward()
    time.sleep(1)
