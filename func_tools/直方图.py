# 直方图
import cv2
import matplotlib.pyplot as plt
import numpy as np

from utils import cv_show

img = cv2.imread('./imges/cat.png', 0)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.hist(img.ravel(), 256)
plt.show()

# 直方图均衡
equ = cv2.equalizeHist(img)
plt.hist(equ.ravel(), 256)
plt.show()
res = np.hstack((img, equ))
cv_show(res, 'res')
# 自适应均衡化
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
res_clahe = clahe.apply(img)
res = np.hstack((img, res_clahe))
cv_show(res, 'res')