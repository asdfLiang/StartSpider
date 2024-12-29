import cv2

"""
    识别滑动验证码缺口
"""

GAUSSIAN_BLUR_SIZE = (5, 5)
GAUSSIAN_BLUR_SIGMA_X = 0
CANNY_THRESHOLD1 = 200
CANNY_THRESHOLD2 = 450


# 高斯滤波 - 就是把一张图片模糊化，方便边缘检测，输出值是图片
def get_guassian_blur(image):
    # cv2.GaussianBlur(
    #   src: 必传，需要处理的图片,
    #   ksize: 必传，高斯核大小(包含x、y两个元素),
    #   sigmaX: 必传，X方向的标准差,
    #   sigmaY: Y方向的标准差)
    return cv2.GaussianBlur(image, GAUSSIAN_BLUR_SIZE, GAUSSIAN_BLUR_SIGMA_X)


# 边缘检测 - Canny算法，输出值是边缘图片
def get_canny(image):
    # cv2.Canny(
    #   image: 必传，需要处理的图片,
    #   threshold1: 必传，最小判定临界点,
    #   threshold2: 必传，最大判定临界点,
    #   apertureSize: 可选，用于计算图像梯度的Sobel卷积核大小,
    #   L2gradient: 可选，一个布尔值，指定了计算图像梯度幅值的方程)
    return cv2.Canny(image, CANNY_THRESHOLD1, CANNY_THRESHOLD2)


# 轮廓提取 - 输出值是轮廓信息（不是图片）
def get_contours(image):
    # cv2.findContours(
    #   image: 必传，需要处理的图片,
    #   mode: 必传，轮廓检索模式,
    #   method: 必传，轮廓逼近方法)
    return cv2.findContours(image, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)[0]


# 阈值方法 - 定义目标轮廓的面积下限和面积上限
def get_contours_area_threshold(image_width, image_height):
    contours_area_min = (image_width * 0.15) * (image_height * 0.25) * 0.8
    contours_area_max = (image_width * 0.15) * (image_height * 0.25) * 1.2
    return contours_area_min, contours_area_max


# 阈值方法 - 定义目标轮廓的周长下限和周长上限
def get_arc_length_threshold(image_width, image_height):
    arc_length_min = ((image_width * 0.15) + (image_height * 0.25)) * 2 * 0.8
    arc_length_max = ((image_width * 0.15) + (image_height * 0.25)) * 2 * 1.2
    return arc_length_min, arc_length_max


# 阈值方法 - 定义缺口位置的偏移量下限和偏移量上限
def get_offset_threshold(image_width):
    offset_min = 0.2 * image_width
    offset_max = 0.85 * image_width
    return offset_min, offset_max


image_raw = cv2.imread("tests/resources/captcha_0.png")
image_height, image_width, _ = image_raw.shape
image_guassian_blur = get_guassian_blur(image_raw)  # 高斯过滤后图片
image_canny = get_canny(image_guassian_blur)  # 轮廓图片
contours = get_contours(image_canny)  # 轮廓信息


# 取出阈值
contours_area_min, contours_area_max = get_contours_area_threshold(
    image_width, image_height
)
arc_length_min, arc_length_max = get_arc_length_threshold(image_width, image_height)
offset_min, offset_max = get_offset_threshold(image_width)

# 提取目标缺口位置
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if (
        contours_area_min < cv2.contourArea(contour) < contours_area_max
        and arc_length_min < cv2.arcLength(contour, True) < arc_length_max
        and offset_min < x < offset_max
    ):
        cv2.rectangle(image_raw, (x, y), (x + w, y + h), (0, 0, 255), 2)  # 圈出目标位置
        print("offset", x)
cv2.imwrite("tests/downloads/image_label.png", image_raw)
