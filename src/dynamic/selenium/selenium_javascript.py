from selenium import webdriver
import time

"""
    运行javaScript
"""

with webdriver.Chrome() as browser:
    # 打开网页
    browser.get("https://www.zhihu.com/explore")
    # 拉到网页底部
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # 弹出提示
    browser.execute_script("alert('To Buttom')")
    # 等待5s，观察结果
    time.sleep(5)
