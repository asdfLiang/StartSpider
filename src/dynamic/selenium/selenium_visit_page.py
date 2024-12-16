from selenium import webdriver

"""
    访问页面
"""

browser = webdriver.Chrome()

try:
    browser.get("https://www.taobao.com")
    print(browser.page_source)
finally:
    browser.close()
