# 图像梯度处理
import cv2
import numpy as np

from utils import cv_show

# sobel算子
img = cv2.imread('./imges/tidu.png', cv2.IMREAD_GRAYSCALE)
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel_y = cv2.convertScaleAbs(sobel_y)
# sobel算子x,y相加. 最好先分别算再相加
sobel_xy = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
# cv_show(sobel_xy, 'tidu_xy')

# charr算子
scharr_x = cv2.Sobel(img, cv2.CV_64F, 1, 0)
scharr_x = cv2.convertScaleAbs(scharr_x)
scharr_y = cv2.Sobel(img, cv2.CV_64F, 0, 1)
scharr_y = cv2.convertScaleAbs(scharr_y)
scharr_xy = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
# cv_show(scharr_xy, 'tidu_xy')

# laplacian算子
laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)
# cv_show(laplacian, 'tidu_xy')

# 不同算子的差异
res = np.hstack((sobel_xy, scharr_xy, laplacian))
# cv_show(res, 'res')

# 边缘检测
img2 = cv2.imread('./imges/1.jpg', cv2.IMREAD_GRAYSCALE)
v1 = cv2.Canny(img2, 5, 30)
v2 = cv2.Canny(img2, 50, 130)
res = np.hstack((v1, v2))
# cv_show(res, 'res')


# 图像金字塔
# 向上采集
up = cv2.pyrUp(img)
# cv_show(up, 'up')
# 向下采集
down = cv2.pyrDown(img)
# cv_show(down, 'down')


img3 = cv2.imread('./imges/lunkuo.png')
gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# cv_show(thresh, "thresh")
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# 绘制轮廓, 复制图片, 避免原图变换
draw_img = img3.copy()
res = cv2.drawContours(draw_img, contours, -1, (0, 255, 0), 2)
cv_show(res, 'res')

# 轮廓特征
cnt = contours[0]
# 面积
cv2.contourArea(cnt)
# 周长
cv2.arcLength(cnt, True)

epsilon = 0.1 * cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)
draw_img = img3.copy()
res = cv2.drawContours(draw_img, [approx], -1, (0, 0, 255), 1)
cv_show(res, 'res')

# 边界矩形
x, y, w, h = cv2.boundingRect(cnt)
img = cv2.rectangle(img3, (x, y), (x + w, y + h), (0, 255, 0), 1)
cv_show(img, "img")
