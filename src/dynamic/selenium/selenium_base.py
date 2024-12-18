from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""
    打开浏览器搜索'Python'
"""

browser = webdriver.Chrome()  # 初始化浏览器
with webdriver.Chrome() as browser:
    browser.get("https://www.baidu.com")  # 打开网页
    input = browser.find_element(By.ID, "kw")  # 找到目标元素
    input.send_keys("Python")  # 输入搜索内容
    input.send_keys(Keys.ENTER)  # 确认输入
    wait = WebDriverWait(browser, 10)  # 等待时间
    wait.until(EC.presence_of_element_located((By.ID, "su")))  # 等待到页面出现su
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
