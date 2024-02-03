import cv2
import numpy as np

image_data = np.random.randint(0, 256, (3, 3, 3), dtype=np.uint8)

print("RGB Image Data:")
for row in image_data:
    print("[", end="")
    for col in row:
        print(f'(r:{col[2]},g:{col[1]},b:{col[0]})', end=" ")
    print("]")

cv2.imshow('RGB Image', image_data)
cv2.waitKey(0)
cv2.destroyAllWindows()
