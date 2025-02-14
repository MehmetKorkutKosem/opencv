import cv2
import numpy as np
#cap=cv2.VideoCapture(0)
cap=cv2.VideoCapture("line.mp4")
while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    frame=cv2.flip(frame,1)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower=np.array([18,94,140],np.uint8)
    upper=np.array([48,255,255],np.uint8)
    mask=cv2.inRange(hsv,lower,upper)
    edges=cv2.Canny(mask,75,250)
    lines=cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=200)
    for line in lines:
        x1,y1,x2,y2=line[0]
        cv2.line(frame,(x1,y1),(x2,y2),(255,0,0),2)

    cv2.imshow("mv",frame)
    
    if cv2.waitKey(30) & 0xff==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
