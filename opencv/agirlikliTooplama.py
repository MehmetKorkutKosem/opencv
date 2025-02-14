import cv2
import numpy as np

canvas=np.zeros((500,500,3),dtype=np.uint8)
canvas1=np.zeros((500,500,3),dtype=np.uint8)
cv2.circle(canvas,(250,250),30,(255,0,0),thickness=-1)
cv2.rectangle(canvas1,(200,200),(350,350),(0,255,0),thickness=-1)
dst=cv2.addWeighted(canvas1,0.7,canvas,0.3,0)
cv2.imshow("canvas1",canvas1)
cv2.imshow("canvas",canvas)
cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()