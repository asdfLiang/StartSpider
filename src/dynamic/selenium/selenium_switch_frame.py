from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

"""
    切换 Frame
"""
url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"

with webdriver.Chrome() as browser:
    browser.get(url)
    browser.switch_to.frame("iframeResult")
    try:
        logo = browser.find_element(By.CLASS_NAME, "logo")
    except NoSuchElementException as e:
        print("NO LOGO")
    browser.switch_to.parent_frame()
    logo = browser.find_element(By.CLASS_NAME, "logo")
    print(logo)
    print(logo.text)
    time.sleep(5)
