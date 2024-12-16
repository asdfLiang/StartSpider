from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

"""
    动作链
"""
url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
browser = webdriver.Chrome()
try:
    browser.get(url)
    browser.switch_to.frame("iframeResult")
    source = browser.find_element(By.CSS_SELECTOR, "#draggable")
    target = browser.find_element(By.CSS_SELECTOR, "#droppable")
    # 动作，在目标元素上按住左键，然后移动都目标位置松开
    actions = ActionChains(browser)
    actions.drag_and_drop(source, target)
    actions.perform()
finally:
    browser.close()
