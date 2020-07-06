# Test program for showing images

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("sample.jpeg",0)
cv.imshow("image", img)

plt.imshow(img)
plt.show()

k = cv.waitKey(0)
if k == 27:
    cv.destroyAllWindows()
elif k == ord("s"):
    cv.imwrite("sample_save.png", img)