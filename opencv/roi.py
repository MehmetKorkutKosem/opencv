import cv2
import numpy as np
image=cv2.imread(r"D:\kta.jpg")
roi=image[100:250,100:200]
cv2.imshow("image",image)
cv2.imshow("roi",roi)

cv2.waitKey(0)
cv2.destroyAllWindows