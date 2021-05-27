# SIFT函数
import cv2

from utils import cv_show

img = cv2.imread('./imges/cat.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT.create()
kp = sift.detect(gray, None)
img = cv2.drawKeypoints(gray, kp, img)
cv_show(img, 'img')
# 关键点和特征向量
kp, des = sift.compute(gray, kp)


