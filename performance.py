import cv2
import numpy as np
from functools import reduce

time1 = []
for i in range(1000):
    img = cv2.imread("cat.jpg")
    e1 = cv2.getTickCount()
    # image processing...
    b, g, r = cv2.split(img)
    e2 = cv2.getTickCount()
    time1.append((e2 - e1) / cv2.getTickFrequency())
print('%f.5' % (reduce(lambda x, y: x + y, time1) / 100))

time2 = []
for i in range(1000):
    b, g, r = img.copy(), img.copy(), img.copy()
    e1 = cv2.getTickCount()
    b[:, :, 1], b[:, :, 2] = 0, 0
    g[:, :, 0], g[:, :, 2] = 0, 0
    r[:, :, 0], r[:, :, 1] = 0, 0
    e2 = cv2.getTickCount()
    time2.append((e2 - e1) / cv2.getTickFrequency())
print('%f.5' % (reduce(lambda x, y: x + y, time2) / 100))