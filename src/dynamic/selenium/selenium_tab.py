from selenium import webdriver
import time

"""
    选项卡管理
"""

with webdriver.Chrome() as browser:
    browser.get("https://www.baidu.com")
    browser.execute_script("window.open()")  # 开启新选项卡
    print(browser.window_handles)
    print()

    browser.switch_to.window(browser.window_handles[1])  # 切换选项卡
    browser.get("https://www.taobao.com")
    time.sleep(1)
    browser.switch_to.window(browser.window_handles[0])  # 切换选项卡
    browser.get("https://www.leetcode.cn")
