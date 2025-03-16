import cv2
import numpy as np
canvas=np.zeros((500,500,3),dtype=np.uint8)
font1=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(canvas,"opencv",(150,150),font1,3,(255,255,255),cv2.LINE_AA)
cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
