import pytesseract, time, re, numpy as np
from PIL import Image
from retrying import retry
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from io import BytesIO

"""
    识别验证码
"""


def preprocess(image):
    # 转化为灰度图像
    image = image.convert("L")
    # 根据阈值删除图片中的干扰点
    array = np.array(image)
    array = np.where(array > 195, 255, 0)
    image = Image.fromarray(array.astype(np.uint8))
    return image


@retry(stop_max_attempt_number=5, retry_on_result=lambda x: x is False)
def login():
    with webdriver.Chrome() as browser:
        browser.get("https://captcha7.scrape.center/")
        # # 输入用户名密码
        browser.find_element(By.CSS_SELECTOR, ".username input[type='text']").send_keys(
            "admin"
        )
        browser.find_element(
            By.CSS_SELECTOR, ".password input[type='password']"
        ).send_keys("admin")
        # 识别验证码
        captcha = browser.find_element(By.CSS_SELECTOR, "#captcha")
        image = Image.open(BytesIO(captcha.screenshot_as_png))
        image = preprocess(image)
        captcha = pytesseract.image_to_string(image)
        captcha = re.sub("[^A-Za-z0-9]", "", captcha).strip()
        # 输入验证码
        browser.find_element(By.CSS_SELECTOR, ".captcha input[type='text']").send_keys(
            captcha
        )
        time.sleep(1)
        # 点击登录
        browser.find_element(By.CSS_SELECTOR, "button[type='button']").click()
        # 判断是否登录成功
        try:
            WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[contains(text(), '登录成功')]")
                )
            )
            return True
        except TimeoutException as e:
            return False


if __name__ == "__main__":
    login()
