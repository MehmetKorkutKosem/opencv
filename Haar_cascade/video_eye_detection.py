import cv2
import numpy as np
path="D:\\opencv\\tst_videos\\Eye.mp4"
path1="D:\\opencv\\cascade\\Eye.xml"
path2="D:\\opencv\\cascade\\frontalface.xml"
cap=cv2.VideoCapture(0)
face=cv2.CascadeClassifier(path2)
eye=cv2.CascadeClassifier(path1)
while True:
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    frame=cv2.resize(frame,(480,360))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face.detectMultiScale(gray,1.6,12)
    for (x,y,h,w) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    
    frame2=frame[y:y+h,x:x+w]
    gray2=gray[y:y+h,x:x+w]
    eyes=eye.detectMultiScale(gray2,1.1,6)
    for (ex,ey,eh,ew) in eyes:
        cv2.rectangle(frame2,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
    
    cv2.imshow("frame",frame)

    if cv2.waitKey(30) & 0xff==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


