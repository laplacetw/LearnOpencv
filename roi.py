import cv2
from matplotlib import pyplot as plt
img = cv2.imread("cat.jpg")
block = img[32:70, 250:290]  # copy
img[240:278, 5:45] = block   # paste

cv2.imshow('cat', img)  # image show
cv2.waitKey(0)
cv2.destroyAllWindows()