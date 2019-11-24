import cv2

img = cv2.imread("/home/pi/Pictures/1.jpg", cv2.IMREAD_COLOR)
width, heigh = img.shape[0: 2]
print("Width: %d, %d" % (width, heigh))
img = cv2.resize(img, (int(heigh/4), int(width/4)))
cv2.imshow("img", img)
cv2.waitKey(0)
