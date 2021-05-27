import cv2
from sklearn.decomposition import PCA

import numpy as np
from PIL import Image


# 绘图展示
def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def loadImage(path):
    img = Image.open(path)
    # 将图像转换成灰度图
    img = img.convert("L")
    # 图像的大小在size中是（宽，高）
    # 所以width取size的第一个值，height取第二个
    width = img.size[0]
    height = img.size[1]
    data = img.getdata()
    # 为了避免溢出，这里对数据进行一个缩放，缩小100倍
    # data = np.array(data).reshape(height, width)
    data = np.array(data).reshape(height, width) / 100
    # 查看原图的话，需要还原数据
    # new_im = Image.fromarray(data)
    # new_im.show()
    new_im = Image.fromarray(data * 100)
    new_im.show()
    return data


def error(data, recdata):
    sum1 = 0
    sum2 = 0
    # 计算两幅图像之间的差值矩阵
    D_value = data - recdata
    # 计算两幅图像之间的误差率，即信息丢失率
    for i in range(data.shape[0]):
        sum1 += np.dot(data[i], data[i])
        sum2 += np.dot(D_value[i], D_value[i])
    error = sum2 / sum1
    print('信息丢失率为{}%'.format(error * 100))


if __name__ == '__main__':
    data = loadImage('./imges/cat.png')
    # 设置降维参数
    pca = PCA(n_components=460)
    # 降维
    x_new = pca.fit_transform(data)
    newImg = Image.fromarray(x_new * 100)
    newImg.show()
    # 还原降维后的数据到原空间
    recdata = pca.inverse_transform(x_new)
    # 计算误差
    (error(data, recdata))
    # 还原降维后的数据
    newImg = Image.fromarray(recdata * 100)
    newImg.show()
    # error(data, recdata)
