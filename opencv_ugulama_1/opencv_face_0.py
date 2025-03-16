import cv2
import numpy as np 
cap=cv2.VideoCapture(0)
cv2.namedWindow("scan")
cv2.resizeWindow("scan",640,480)

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    roi=frame[50:250,270:470]
    cv2.rectangle(frame,(270,50),(470,250),(255,0,0),3)
    hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    lower=np.array([0,45,79],np.uint8)
    upper=np.array([17,255,255],np.uint8)
    mask=cv2.inRange(hsv,lower,upper)
    kernel=np.ones((5,5),np.uint8)
    mask=cv2.dilate(mask,kernel,iterations=1)
    cv2.imshow("scan",frame)
    cv2.imshow("roi",roi)
    cv2.imshow("mask",mask)
    if cv2.waitKey(30) & 0xff==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()