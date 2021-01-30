import cv2
import numpy as np

def callback(x):
    pass

img = cv2.imread('butterfly.jpg', 0)
edges = cv2.Canny(img, 50, 100)
cv2.namedWindow('butterfly')
cv2.createTrackbar('Min', 'butterfly', 0, 255, callback)
cv2.createTrackbar('Max', 'butterfly', 0, 255, callback)

while(True):
    minval = cv2.getTrackbarPos('Min', 'butterfly')
    maxval = cv2.getTrackbarPos('Max', 'butterfly')
    edges = cv2.Canny(img, minval, maxval)
    # display value of Trackbar for OSX
    font = cv2.FONT_HERSHEY_SIMPLEX
    label = 'Max: ' + str(maxval) + ' Min: ' + str(minval)
    cv2.putText(edges, label, (500, 500), font, 1, 220, 2)
    cv2.imshow('butterfly', edges)

    if cv2.waitKey(1) == ord('q'):
        break