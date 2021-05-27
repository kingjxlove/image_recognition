# 滤波器
import cv2
import numpy as np

img = cv2.imread('./imges/cat2.png', 0)
# 均值滤波
blur = cv2.blur(img, (3, 3))
# 高斯滤波
gaussian = cv2.GaussianBlur(img, (5, 5), 1)
# 中值滤波
median = cv2.medianBlur(img, 5)

res = np.hstack((gaussian, median))
cv2.imshow('result', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
