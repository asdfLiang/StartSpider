from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

"""
    异常处理
"""

with webdriver.Chrome() as browser:
    try:
        browser.get("https://www.baidu.com")
        browser.find_element(By.ID, "hello")
    except TimeoutException:
        print("Time Out")
    except NoSuchElementException:
        print("No Element")
