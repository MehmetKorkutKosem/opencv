import numpy as np
import cv2
canvas=np.zeros((500,500,3),dtype=np.uint8)
canvas1=np.zeros((500,500,3),dtype=np.uint8)+255
print(canvas1)
print(canvas)
cv2.imshow("canvas",canvas)
cv2.imshow("canvas1",canvas1)
cv2.waitKey(0)
cv2.destroyAllWindows()

