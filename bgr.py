import cv2
img = cv2.imread("cat.jpg")
b, g, r = img.copy(), img.copy(), img.copy()
b[:, :, 1], b[:, :, 2] = 0, 0
g[:, :, 0], g[:, :, 2] = 0, 0
r[:, :, 0], r[:, :, 1] = 0, 0
cv2.imshow('b', b)  # image show
cv2.imshow('g', g)
cv2.imshow('r', r)  
cv2.waitKey(0)
cv2.destroyAllWindows()