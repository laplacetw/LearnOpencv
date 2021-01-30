import cv2
import numpy as np
from matplotlib import pyplot as plt

i = 0
pts1 = np.float32([[0,0],[0,0],[0,0],[0,0]])
def savexy(event, x, y, flags, param):
    global i, pts1
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        cv2.circle(img, (x, y), 4, (0, 0, 255), -1)
        pts1[i]=[x,y]
        i += 1

img = cv2.imread('carplate.jpg')
rows, cols, ch = img.shape
pts2 = np.float32([[0, 0], [300, 0], [300, 300], [0, 300]])
cv2.namedWindow('carplate')
cv2.setMouseCallback('carplate', savexy)
while(True):
    cv2.imshow('carplate', img)
    if cv2.waitKey(1) == ord('q') or i > 3:
        break
cv2.destroyAllWindows()

params = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, params, (300, 300))
dst1 = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
dst1 = cv2.resize(dst1, (345, 150))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.subplot(121), plt.imshow(img), plt.title('Before')
plt.subplot(122), plt.imshow(dst1), plt.title('After')
plt.show()