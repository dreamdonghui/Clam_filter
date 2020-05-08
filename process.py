import numpy as np
import cv2

img = cv2.imread('WeChat Image_20200221164050.jpg', 0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
ret, mask = cv2.threshold(img, 190, 255, cv2.THRESH_BINARY)
cv2.namedWindow('mask of characters', cv2.WINDOW_NORMAL)
cv2.imshow('mask of characters', mask)
cv2.waitKey(0)
dst = cv2.inpaint(img, mask, 20, cv2.INPAINT_NS)
cv2.namedWindow('Characters removed', cv2.WINDOW_NORMAL)
cv2.imshow('Characters removed', dst)
cv2.waitKey(0)

thresh = 100
max_thresh = 255
blur = cv2.blur(dst, (3, 3))
cv2.namedWindow('after blur', cv2.WINDOW_NORMAL)
cv2.imshow('after blur', blur)
cv2.waitKey(0)

# Detect edges using canny
canny_output = cv2.Canny(blur, thresh, thresh * 2, 3)
# Find contours
img2, contours, hierarchy = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.namedWindow('findcontoursinblack', cv2.WINDOW_NORMAL)
cv2.imshow('findcontoursinblack', img2)
cv2.waitKey(0)
cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.namedWindow('findcontours', cv2.WINDOW_NORMAL)
cv2.imshow('findcontours', img)
cv2.waitKey(0)

# blur = cv2.medianBlur(dst,1)
# cv2.imwrite('blur.jpg',blur)
# cv2.imshow('image', blur)
# cv2.waitKey(0)
#
# #gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# sift = cv2.xfeatures2d.SIFT_create()
# kp = sift.detect(blur,None)
# img=cv2.drawKeypoints(blur,kp,img)
# cv2.imwrite('sift_keypoints.jpg',img)
# cv2.imshow('image', img)
# cv2.waitKey(0)
#
# #blur = cv2.cvtColor(blur,cv2.COLOR_GRAY2BGR)
# circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,20, param1=50,param2=30,minRadius=0,maxRadius=0)
# circles = np.uint16(np.around(circles))
# for i in circles[0,:]:
#     # draw the outer circle
#     cv2.circle(blur,(i[0],i[1]),i[2],(0,255,0),2)
#     # draw the center of the circle
#     cv2.circle(blur,(i[0],i[1]),2,(0,0,255),3)
# cv2.imshow('detected circles',blur)
# cv2.waitKey(0)

cv2.destroyAllWindows()
