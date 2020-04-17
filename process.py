import numpy as np
import cv2

img = cv2.imread('WeChat Image_20200221164050.jpg', 0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
ret, mask = cv2.threshold(img, 210, 255, cv2.THRESH_BINARY)
cv2.namedWindow('mask of characters', cv2.WINDOW_NORMAL)
cv2.imshow('mask of characters', mask)
cv2.waitKey(0)
dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)
cv2.namedWindow('Characters removed', cv2.WINDOW_NORMAL)
cv2.imshow('Characters removed', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
