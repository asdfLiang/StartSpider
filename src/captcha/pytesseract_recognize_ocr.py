import pytesseract as ocr
from PIL import Image

"""
    OCR 技术识别验证码
"""

image0 = Image.open("tests/resources/1.png")
image1 = Image.open("tests/resources/2.webp")
image2 = Image.open("tests/resources/3.png")
str_16fa = ocr.image_to_string(image0)
str_FUks = ocr.image_to_string(image1)
str_867b = ocr.image_to_string(image2)
print("str_16fa: ", str_16fa)
print("str_FUks: ", str_FUks)
print("str_867b: ", str_867b)
