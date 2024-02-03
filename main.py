import numpy as np
import cv2

img = cv2.imread("images/oranges/o1.jpeg")
# img = cv2.resize(img, (10, 10))
img = cv2.Canny(img, 100, 150)

print(np.array(img).flatten())

cv2.imshow("cat", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# matrix 5 x 5
