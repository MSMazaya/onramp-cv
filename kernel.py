import numpy as np
import cv2
img = cv2.imread("images/oranges/o1.jpeg")


def gaussian_kernel(size, sigma):
    if size % 2 == 0:
        print("size harus ganjil")
        return

    kernel = np.fromfunction(
        lambda x, y: (1/(2*np.pi*sigma**2)) * np.exp(-((x-(size-1)/2)
                                                       ** 2 + (y-(size-1)/2)**2) / (2*sigma**2)),
        (size, size)
    )

    return kernel / np.sum(kernel)


def sobel_kernel(size):
    if size % 2 == 0:
        print("size harus ganjil")
        return

    sobel_x = np.fromfunction(lambda x, y: -(x - (size-1)/2) / (2 * np.pi),
                              (size, size), dtype=int)

    sobel_y = np.fromfunction(lambda x, y: -(y - (size-1)/2) / (2 * np.pi),
                              (size, size), dtype=int)

    return sobel_x, sobel_y


gaussian_k = gaussian_kernel(5, 100)
sobel_k_x, sobel_k_y = sobel_kernel(5)

# print("Gaussian Kernel:")
# print(gaussian_k)
# print(sobel_k_y)

img = cv2.filter2D(img, -1, gaussian_k)
img = cv2.filter2D(img, -1, sobel_k_y)
# img_sobel_y = cv2.filter2D(img, -1, sobel_k_y)
# t_lower = 50  # Lower Threshold
# t_upper = 150  # Upper threshold
#
# # Display the final result
cv2.imshow("cat", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
