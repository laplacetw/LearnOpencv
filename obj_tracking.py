import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # 0:built-in camera
while(True):
    ret, frame = cap.read()
    # brg -> hsv
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # threshold of color blue
    lower_blue = np.array([156,43,36])
    upper_blue = np.array([180,255,255])
    
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()