import cv2
import numpy as np

file="saha.png"
image=cv2.imread(file)
bulur=cv2.blur(image,(5,5))
bulur1=cv2.GaussianBlur(image,(5,5),cv2.BORDER_DEFAULT)
bulur2=cv2.medianBlur(image,5)
bulur3=cv2.bilateralFilter(image,9,75,75)
cv2.imshow("image",image)
cv2.imshow("dzn",bulur)
cv2.imshow("dzn1",bulur1)
cv2.imshow("dzn2",bulur2)
cv2.imshow("dzn4",bulur3)
cv2.waitKey(0)
cv2.destroyAllWindows()