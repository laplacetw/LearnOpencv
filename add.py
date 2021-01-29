import cv2
dog = cv2.imread("dog.jpg")
cat = cv2.imread("cat.jpg")
result = cv2.addWeighted(dog, 0.6, cat, 0.4, 0)
cv2.imshow('result', result)  # image show
cv2.waitKey(0)
cv2.destroyAllWindows()