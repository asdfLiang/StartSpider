from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time

"""
    反屏蔽
"""

url = "https://antispider1.scrape.center/"

# 使用Chrome开发工具协议
option = ChromeOptions()
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option("userAutomationExtension", False)
with webdriver.Chrome() as browser:
    # 执行CDP方法
    browser.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {
            "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        },
    )
    browser.get(url)
    time.sleep(5)
