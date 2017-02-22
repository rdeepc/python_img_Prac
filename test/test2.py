import cv2
import numpy as np

img = cv2.imread('ds/s1/1.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)

cv2.imshow('thresh', thresh)

cv2.waitKey(00)
cv2.destroyAllWindows()
