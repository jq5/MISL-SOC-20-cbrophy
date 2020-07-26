import cv2

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
print(ret, frame)

cap.release()
cv2.destroyAllWindows()
