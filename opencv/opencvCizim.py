import cv2
import numpy as np
canvas=np.zeros((10,10,3),dtype=np.uint8)
canvas[0,0]=[255,255,255]
canvas[0,1]=[255,255,0]
canvas[0,2]=[50,0,0]
canvas=cv2.resize(canvas,(500,500),interpolation=cv2.INTER_AREA)
cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()