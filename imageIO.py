import cv2
import numpy as np
from matplotlib import pyplot as plt

# image read
img = cv2.imread("cat.jpg")  # bgr

# adjustable window
# cv2.namedWindow('cat', cv2.WINDOW_NORMAL)
cv2.imshow('cat', img)  # image show
cv2.waitKey(0)
cv2.destroyAllWindows()

#image write
cv2.imwrite('cat_copy.jpg', img)

# bgr -> rgb
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.show()