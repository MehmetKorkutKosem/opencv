import cv2
import numpy as np
canvas=np.zeros((500,500,3),dtype=np.uint8)+255
cv2.line(canvas,(0,0),(500,0),(255,0,0),thickness=5)
cv2.line(canvas,(500,500),(500,0),(0,255,0),thickness=5)
cv2.line(canvas,(0,0),(0,500),(0,0,255),thickness=5)
cv2.line(canvas,(0,500),(500,500),(0,0,255),thickness=5)
cv2.rectangle(canvas,(50,50),(450,450),(0,255,0),thickness=-1)
cv2.circle(canvas,(250,250),50,(255,0,0),thickness=-1)
cv2.ellipse(canvas,(100,100),(50,150),0,0,360,(150,200,250),thickness=-1)
point=np.array([[100,100],[200,100],[150,150]])
cv2.polylines(canvas,[point],True,(0,0,255),thickness=5)
cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
