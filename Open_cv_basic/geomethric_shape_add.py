import cv2
import numpy as np

canvas=np.zeros((500,500,3),dtype=np.uint8)+255
canvas1=np.zeros((500,500,3),dtype=np.uint8)+255
canvas3=np.zeros((500,500,3),dtype=np.uint8)+255
cv2.circle(canvas,(250,250),30,(255,0,0),thickness=-1)
cv2.rectangle(canvas1,(250,250),(150,150),(0,250,0),thickness=-1)
canvas3=cv2.add(canvas1,canvas)
cv2.imshow("circle",canvas)
cv2.imshow("rectangle",canvas1)
cv2.imshow("add",canvas3)
cv2.waitKey(0)
cv2.destroyAllWindows()
