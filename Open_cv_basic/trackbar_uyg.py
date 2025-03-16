
def nothing(x):
    pass

import cv2
import numpy as np
image=np.zeros((500,500,3),dtype="uint8")
cv2.namedWindow("image")
cv2.createTrackbar("R","image",0,255,nothing)
cv2.createTrackbar("G","image",0,255,nothing)
cv2.createTrackbar("B","image",0,255,nothing)
switch="0:off\n1:on"
cv2.createTrackbar(switch,"image",0,1,nothing)
while True:
    R=cv2.getTrackbarPos("R","image")
    G=cv2.getTrackbarPos("G","image")
    B=cv2.getTrackbarPos("B","image")
    s=cv2.getTrackbarPos(switch,"image")
    if s==0 :
        image[:]=[0,0,0]
    if s==1:
        image[:]=[B,G,R]
    
    if cv2.waitKey(1) & 0xFF ==ord("q") : 
        break

    cv2.imshow("image",image)
    
cv2.destroyAllWindows()