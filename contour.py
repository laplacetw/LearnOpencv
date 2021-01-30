import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('rec.jpg')
img_ = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)

contours1, hierarchy1 = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours2, hierarchy2 = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt1 = contours1[0]
cnt2 = contours2[0]
draw1 = cv2.drawContours(img, cnt1, -1, (0, 255, 0), 10)
draw2 = cv2.drawContours(img_, cnt2, -1, (0, 255, 0), 10)

plt.subplot(121), plt.imshow(cv2.cvtColor(draw1, cv2.COLOR_BGR2RGB)), plt.title('APPROX_NONE')
plt.subplot(122), plt.imshow(cv2.cvtColor(draw2, cv2.COLOR_BGR2RGB)), plt.title('APPROX_SIMPLE')
plt.show()