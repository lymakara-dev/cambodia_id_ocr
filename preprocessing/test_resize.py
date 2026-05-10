import cv2

from resize import resize_with_padding

image = cv2.imread("id_0001.png")

result = resize_with_padding(image)

cv2.imshow("result", result)
cv2.waitKey(0)