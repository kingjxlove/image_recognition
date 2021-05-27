# 图像填充#
import cv2
import matplotlib.pyplot as plt

w, s, a, d = (50, 50, 50, 50)
img = cv2.imread('./imges/cat.png', 0)
# 边缘复制
img_1 = cv2.copyMakeBorder(img, w, s, a, d, borderType=cv2.BORDER_REPLICATE)
# 反射
img_2 = cv2.copyMakeBorder(img, w, s, a, d, borderType=cv2.BORDER_REFLECT)
# 边缘对称反射
img_3 = cv2.copyMakeBorder(img, w, s, a, d, borderType=cv2.BORDER_REFLECT_101)
# 外包装
img_4 = cv2.copyMakeBorder(img, w, s, a, d, borderType=cv2.BORDER_WRAP)
# 常量
img_5 = cv2.copyMakeBorder(img, w, s, a, d, borderType=cv2.BORDER_CONSTANT, value=0)


plt.subplot(231), plt.imshow(img, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(img_1, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(img_2, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(img_3, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(img_4, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(img_5, 'gray'), plt.title('CONSTANT_value=0')
plt.show()