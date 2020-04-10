import numpy as np
import cv2

img = cv2.imread('WeChat Image_20200221164050.jpg', 0)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()