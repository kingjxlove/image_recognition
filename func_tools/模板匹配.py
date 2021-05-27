# 模板匹配
import cv2
import numpy as np

from utils import cv_show

img = cv2.imread('./imges/cat.png')
tmp = cv2.imread('./imges/cat_face.png')
h, w = tmp.shape[:2]

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

res = cv2.matchTemplate(img, tmp, cv2.TM_CCOEFF)
# print(res.shape)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# 匹配多个对象
img_rgb = cv2.imread("./imges/cat.png")
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
tmp = cv2.imread("./imges/cat_face.png", 0)
h, w = tmp.shape[:2]
res = cv2.matchTemplate(img_gray, tmp, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    btn_right = (pt[0] + w, pt[1] + h)
    cv2.rectangle(img_rgb, pt, btn_right, (0, 0, 255), 1)

cv_show(img_rgb, "img_rgb")
