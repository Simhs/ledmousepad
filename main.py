#-*- coding: utf-8 -*-

import cv2




def cropFrom2t1Rate(img):
    h = img.shape[0]
    w =img.shape[1]
    crop_h = 1
    crop_w = 2
    while True:
        findout = [False,False]
        if w>=crop_w:
            findout[0] = True
        if h>=crop_h:
            findout[1] = True
        if findout[0] and  findout[1]:
            crop_h += 1
            crop_w += 2
        else:
            crop_h -= 1
            crop_w -= 2
            crop_img = img[int((h - crop_h)/2.0): int((h - crop_h)/2.0) + crop_h, int((w - crop_w)/2.0): int((w - crop_w)/2.0) + crop_w]
            return crop_img

cap = cv2.VideoCapture('video.mp4')
while(cap.isOpened()):
    ret, frame = cap.read()
    crop = cropFrom2t1Rate(frame)
    resized = cv2.resize(crop, (64, 32), interpolation=cv2.INTER_CUBIC)
    cv2.imshow('frame', resized)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

ori_img = cv2.imread("testdot.PNG")
h = ori_img.shape[0]
w = ori_img.shape[1]
cv2.imshow("hi", ori_img)
# 비율주어주면 이미지 최대한 중심에서 크게 자르기
crop = cropFrom2t1Rate(ori_img)

print resized.shape
cv2.imshow("hi",crop)
cv2.imshow("hi2",ori_img)
cv2.imshow("hi3",resized)

cv2.imwrite("utube.jpg",resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
