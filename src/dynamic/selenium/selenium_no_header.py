from selenium import webdriver
import time

"""
    无头模式
"""

# 设置无头模式，设置后不弹出浏览器
option = webdriver.ChromeOptions()
option.add_argument("--headless")
with webdriver.Chrome(options=option) as browser:
    browser.set_window_size(1920, 1080)
    browser.get("https://www.baidu.cn/")
    browser.get_screenshot_as_file("downloads/preview.png")  # 截图
    print("executed")
