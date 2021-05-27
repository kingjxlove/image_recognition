# 背景建模
import cv2

cap = cv2.VideoCapture('./videos/test.avi')
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

fg_bg = cv2.createBackgroundSubtractorMOG2()
while (True):
    ret, frame = cap.read()
    fg_mask = fg_bg.apply(frame)
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)
    contours, hierarchy = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        perimeter = cv2.arcLength(c, True)
        if perimeter > 188:
            x, y, h, w = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    cv2.imshow('fg_mask', fg_mask)
    k = cv2.waitKey(100) & 0XFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
