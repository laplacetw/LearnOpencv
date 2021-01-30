import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cat.jpg')
rows, cols, _ = img.shape
# resize
res=cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
# OR
# height,width=img.shape[:2]
# res=cv2.resize(img,(2*width, 2*height),interpolation=cv2.INTER_CUBIC)

# translation
params = np.float32([
    [1, 0, 100],
    [0, 1, 100]
])
trans = cv2.warpAffine(img, params, (rows, cols))

# rotation
# getRotationMatrix2D(center, angle, zoom ratio)
params = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 0.6)
rotation = cv2.warpAffine(img, params, (rows, cols))

# affine
carplate = cv2.imread('carplate.jpg')
pts = np.float32([[20, 233], [459, 179], [499, 293], [86, 443]])
pts_ = np.float32([[0, 0], [345, 0], [345, 150], [0, 150]])
params = cv2.getPerspectiveTransform(pts, pts_)
carplate_ = cv2.warpPerspective(carplate, params, (345, 150))
carplate = cv2.cvtColor(carplate, cv2.COLOR_BGR2RGB)
carplate_ = cv2.cvtColor(carplate_, cv2.COLOR_BGR2RGB)

plt.subplot(231), plt.imshow(res), plt.title('Resize')
plt.subplot(232), plt.imshow(trans), plt.title('Translation')
plt.subplot(233), plt.imshow(rotation), plt.title('Rotation')
plt.subplot(223), plt.imshow(carplate), plt.title('Before Affine')
plt.subplot(224), plt.imshow(carplate_), plt.title('After Affine')
plt.show()