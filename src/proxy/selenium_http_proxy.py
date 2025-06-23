from selenium import webdriver
from free_proxy import proxy

"""
    Selenium 设置http代理
"""

options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://" + proxy)
with webdriver.Chrome(options=options) as broswer:
    broswer.get("https://httpbin.org/get")
    print(broswer.page_source)
