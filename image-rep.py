import cv2
import numpy

# grayscale
img = numpy.array([
    [0, 0.8, 0.1, 0, 1],
    [0, 0.8, 0.1, 0, 0.5],
    [0, 0.8, 0.1, 0.6, 1],
    [0, 0.8, 0.1, 0, 0],
    [0, 0.8, 0.1, 0, 0],
])

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
