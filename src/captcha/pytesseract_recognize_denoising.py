import pytesseract as ocr
from PIL import Image
import numpy as np

"""
    处理验证码 - 图片去噪
"""

image0 = Image.open("tests/resources/1.png")
str_16fa = ocr.image_to_string(image0)
print("str_16fa: ", str_16fa)  # 识别错误
print(np.array(image0).shape)  # 高 宽 通道数
print(image0.mode)  # mode属性定义了图片的类型和像素的位宽

# 转化为灰度图像
image0 = image0.convert("L")

# 根据阈值删除图片中的干扰点
threshold = 80
array = np.array(image0)
array = np.where(array > threshold, 255, 0)
image0 = Image.fromarray(array.astype(np.uint8))

# 再次识别
str_16fa = ocr.image_to_string(image0)
print("str_16fa: ", str_16fa)
image0.show()
