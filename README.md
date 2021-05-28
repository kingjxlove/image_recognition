# image_recognition
此目录下一共包含四个模块:
  - func_tools 里面主要是包含一些在图像识别的学习过程中，运用到的一些实例，都是一些细化的模块，稍加改动就能在各个地方使用；
  - template-matching-ocr 对于opencv-ocr的运用，通过图片识别银行卡卡号；
  - ImageStich 对SITF的运用，实现图像的拼接（全景图）；
  - LPR 一个小型的Flask程序，通过上传车辆照片，识别图片中的车牌信息


接下来我会对这里面的一些功能进行描述及展示。
#### 1. [中值滤波器](https://github.com/kingjxlove/image_recognition/blob/main/func_tools/median_filter.py)
    滤波器常用的一般有低通滤波器、高斯低通滤波器和中值滤波器，其中效果最好的，主观认为是中值滤波器。
    中值滤波器：邻域内像素先进行灰度排序，取中间值，在去除噪声的同时，比较好的保留边缘。
    上面的链接是自己实现的中值滤波器，其实在opencv中已经集成的有相应模块，直接调用,
    传入参数，就能实现中值滤波 median = cv2.medianBlur(img, k) 在"滤波器.py"文件中也有相应展示.
    
   ![中值滤波器](https://github.com/kingjxlove/img/blob/master/%E6%BB%A4%E6%B3%A2%E5%99%A8.png)
    
#### 2. [PCA主成分分析](https://github.com/kingjxlove/image_recognition/blob/main/func_tools/pca_file.py)
    PCA（Principal Component Analysis）是一种常用的数据分析方法。
    PCA通过线性变换将原始数据变换为一组各维度线性无关的表示，可用于提取数据的主要特征分量，常用于高维数据的降维。
   
   ![PCA的降维与还原](https://github.com/kingjxlove/img/blob/master/pca%E4%B8%BB%E6%88%90%E5%88%86%E5%88%86%E6%9E%90.png)
## 。。。。。。（待补充）

# [LPR(暂时只做展示，待补充)](https://github.com/kingjxlove/image_recognition/tree/main/LPR)
![车牌识别1](https://github.com/kingjxlove/img/blob/master/%E8%BD%A6%E7%89%8C%E8%AF%86%E5%88%AB1.png)
![车牌识别2](https://github.com/kingjxlove/img/blob/master/%E8%BD%A6%E7%89%8C%E8%AF%86%E5%88%AB2.png)
	 
	
