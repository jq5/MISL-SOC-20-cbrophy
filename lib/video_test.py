# Test program for displaying screen input

from PIL import ImageGrab
import numpy as np
import cv2

while True:
    frame = np.array(ImageGrab.grab(bbox=None))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("frame", gray)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()