from selenium import webdriver

"""
    Cookie
"""

with webdriver.Chrome() as browser:
    browser.get("https://www.zhihu.com/explore")
    print(browser.get_cookies())
    print()
    browser.add_cookie({"name": "name", "domain": "www.zhihu.com", "value": "germey"})
    print(browser.get_cookies())
    print()
    browser.delete_all_cookies()
    print(browser.get_cookies())
