# 导入工具包
import numpy as np
import cv2


def sort_contours(cnts, method="left-to-right"):
    reverse = False
    i = 0

    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True

    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]  # 用一个最小的矩形，把找到的形状包起来x,y,h,w
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                        key=lambda b: b[1][i], reverse=reverse))

    return cnts, boundingBoxes


def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(image, dim, interpolation=inter)
    return resized


# 绘图展示
def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 初始化卷积核
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))


# sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))

def img_init(img_path):
    # 读取一个模板图像
    img = cv2.imread(img_path)
    # cv_show('img', img)
    # 灰度图
    ref = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv_show('ref', ref)
    # 二值图像
    ref = cv2.threshold(ref, 10, 255, cv2.THRESH_BINARY_INV)[1]
    # cv_show('ref', ref)
    return img, ref


def img_han(img, ref):
    kernel = np.ones((30, 30), dtype=np.uint8)
    ref_1 = cv2.dilate(ref, kernel, 5)  # 更改迭代次数为5
    # cv_show('res', ref_1)
    refCnts, hierarchy = cv2.findContours(ref_1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, refCnts, -1, (0, 0, 255), 3)
    # cv_show('img', img)
    refCnts = sort_contours(refCnts, method="left-to-right")[0]  # 排序，从左到右，从上到下
    return ref, refCnts


def img_en_num(img, ref):
    # 通过闭操作（先膨胀，再腐蚀）将数字连在一起
    # ref = cv2.morphologyEx(ref, cv2.MORPH_CLOSE, rectKernel)
    # cv_show('gradX', ref)
    refCnts, hierarchy = cv2.findContours(ref.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(img, refCnts, -1, (0, 0, 255), 3)
    # cv_show('img', img)
    refCnts = sort_contours(refCnts, method="left-to-right")[0]  # 排序，从左到右，从上到下
    return ref, refCnts


tmp_en = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']
tmp_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
tmp_han = ['京', '津', '冀', '晋', '蒙', '辽', '吉', '黑', '沪', '苏', '浙', '皖',
           '闽', '赣', '鲁', '豫', '鄂', '湘', '粤', '桂', '琼', '渝', '川', '贵',
           '云', '藏', '陕', '甘', '青', '宁', '新', '港', '澳', '使', '领', '学', '警']


def get_img(ref, refCnts, str_1):
    tmp = []
    if str_1 in tmp_en:
        tmp = tmp_en
    elif str_1 in tmp_num:
        tmp = tmp_num
    elif str_1 in tmp_han:
        tmp = tmp_han
    digits = {}
    # 遍历每一个轮廓
    for (i, c) in enumerate(refCnts):
        # 计算外接矩形并且resize成合适大小
        (x, y, w, h) = cv2.boundingRect(c)
        (x1, y1, w1, h1) = cv2.boundingRect(ref)
        roi = ref[y:y + h, x:x + w]
        roi = cv2.resize(roi, (57, 88))
        # 每一个数字对应每一个模板
        digits[tmp[i]] = roi
    # cv_show('img', digits[str_1])
    return digits[str_1]


def getTempletImage(str_1):
    if str_1 in tmp_en:
        img_e, ref_e = img_init('./imges/en-line.png')
        ref_e, refCnts_e = img_en_num(img_e, ref_e)
        img = get_img(ref_e, refCnts_e, str_1)
        return img
    elif str_1 in tmp_num:
        img_n, ref_n = img_init('./imges/num-line.png')
        ref_n, refCnts_n = img_en_num(img_n, ref_n)
        img = get_img(ref_n, refCnts_n, str_1)
        return img
    elif str_1 in tmp_han:
        img_h, ref_h = img_init('./imges/han-line-ex.png')
        ref_h, refCnts_h = img_han(img_h, ref_h)
        img = get_img(ref_h, refCnts_h, str_1)
        return img
    else:
        print('该字符{}未在车牌模板中出现'.format(str_1))


def guiyi(image):
    cv2.imshow("input", image)
    result = np.zeros(image.shape, dtype=np.float32)
    cv2.normalize(image, result, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    print(result)
    cv2.imshow("norm", np.uint8(result * 255.0))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    image = getTempletImage('川')
    guiyi(image)
    # image = cv2.imread("./imges/car/4.jpg")
    # guiyi(image)
    # cv_show('img', img)
    # image = cv2.imread("D:/javaopencv/dahlia_4.jpg")
    # cv2.imshow("input", image)
    # result = np.zeros(image.shape, dtype=np.float32)
    # cv2.normalize(image, result, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    # print(result)
    # cv2.imshow("norm", np.uint8(result * 255.0))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
