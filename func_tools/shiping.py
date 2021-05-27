# 视频处理#
import cv2

vc = cv2.VideoCapture('./videos/test.avi')
if vc.isOpened():
    open_bool, frame = vc.read()
while open_bool:
    ret, frame = vc.read()
    if frame is None:
        break
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('result', gray)
        if cv2.waitKey(10) & 0xFF == 27:
            break
vc.release()
cv2.destroyAllWindows()
