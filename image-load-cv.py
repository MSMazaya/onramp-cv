import cv2

img = cv2.imread("cat.jpg")

print("RGB Image Data:")
for i in range(3):
    row = img[i]
    print("[", end="")
    for j in range(3):
        col = row[j]
        print(f'(r:{col[2]},g:{col[1]},b:{col[0]})', end=" ")
    print("]")

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
