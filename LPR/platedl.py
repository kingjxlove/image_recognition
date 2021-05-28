import hyperlpr
import cv2
import os
import sys

if __name__ == "__main__":
    imgList = []
    rootdir = './pictures/'
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        timg = cv2.imread(path)
        imgList.append(timg)
    for img in imgList:
#        cv2.imshow('t', img)
        print(hyperlpr.HyperLPR_plate_recognition(img))
#        cv2.waitKey(0)

    print(len(imgList))
