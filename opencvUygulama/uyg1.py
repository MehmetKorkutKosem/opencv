import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower=np.array([38,100,100])
    uppr=np.array([75,255,255])
    mask=cv2.inRange(hsv,lower,uppr)
    cv2.imshow("screen",mask)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    