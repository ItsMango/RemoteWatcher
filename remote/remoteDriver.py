import cv2

img = cv2.imread("/home/pi/Pictures/1.jpg", cv2.IMREAD_COLOR)
cv2.imshow("img", img)
cv2.waitKey(1)
