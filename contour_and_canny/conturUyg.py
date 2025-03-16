import cv2
import numpy as np
cap=cv2.VideoCapture("dog.mp4")
while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    sensivity=15#parlaklık eşiğini belirler
    low=np.array([0,0,255-sensivity])#taban değer
    upper=np.array([255,sensivity,255])#tavan değer 
    mask=cv2.inRange(hsv,low,upper)#beyaz renk için maskeleme yapar
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("fsv",frame)
    cv2.imshow("ssf",mask)
    cv2.imshow("sws",res)
    
    if cv2.waitKey(30) & 0xff==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()