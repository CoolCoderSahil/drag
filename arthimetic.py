import cv2


img1 = cv2.imread("bjp.jpeg")
img2 = cv2.imread("modi.jpeg")
img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

add = img1+ img2_resized
sub= img1- img2_resized
mul = img1* img2_resized
div = img1/img2_resized

cv2.imshow("Addition", add)
cv2.imshow("Subraction", sub)
cv2.imshow("Multiplication", mul)
cv2.imshow("Division", div)

cv2.waitKey(0)
cv2.destroyAllWindows()
