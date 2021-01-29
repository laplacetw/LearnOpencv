import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# line
cv2.line(img, (0, 0), (500, 500), (255, 0, 255), 5)
# rectangle
for i in range(20, 100, 10):
    cv2.rectangle(img, (50+i, 50+i), (200+i, 200+i), (0, 255, 0), 5)
# circle
cv2.circle(img, (400, 400), 100, (0, 255, 0), 5)
# polylines
pts = np.array([[50, 450], [20, 350], [200, 350], [150, 300]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (255, 255, 0), 5)
# text
font = cv2.FONT_ITALIC
cv2.putText(img, "TEST", (50, 400), font, 2, (255, 255, 255), 5)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()