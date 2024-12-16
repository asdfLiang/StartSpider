from selenium import webdriver
from selenium.webdriver.common.by import By

"""
    获取节点信息
"""

url = "https://spa2.scrape.center/"
with webdriver.Chrome() as browser:
    browser.get(url)
    print()

    # 获取属性值
    print("获取属性：")
    logo = browser.find_element(By.CLASS_NAME, "logo-image")
    print(logo)
    print(logo.get_attribute("src"))
    print()

    # 获取文本值
    print("获取文本值：")
    input = browser.find_element(By.CLASS_NAME, "logo-title")
    print(input.text)
    print()

    # 获取ID、位置、标签名和大小
    print("获取ID、位置、标签名和大小：")
    print(input.id)
    print(input.location)
    print(input.tag_name)
    print(input.size)
