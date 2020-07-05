# Test program for displaying screen input

from PIL import ImageGrab
import numpy as np
import cv2 as cv

while True:
    frame = np.array(ImageGrab.grab(bbox=None))

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow("frame", gray)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cv.destroyAllWindows()