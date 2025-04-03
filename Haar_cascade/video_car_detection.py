import cv2
import numpy as np
path="D:\\opencv\\tst_videos\\Car_D.mp4"
path1="D:\\opencv\\cascade\\Car.xml"

cap=cv2.VideoCapture(path)
car=cv2.CascadeClassifier(path1)
while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    Car=car.detectMultiScale(gray,1.1,6)
    for (x,y,w,h) in Car:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow("frame",frame)
    if cv2.waitKey(30) & 0xff==ord("q"):
        break

cap.release()
cv2.destroyAllWindows() 