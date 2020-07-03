import cv2 as cv
import numpy as np

img = cv.imread("sample.jpeg",0)

cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()