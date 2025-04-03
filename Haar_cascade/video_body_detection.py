import cv2
import numpy as np 
path1="D:\\opencv\\cascade\\fullbody.xml"
path2="D:\\opencv\\tst_videos\\body.mp4"
cap=cv2.VideoCapture(path2)
body=cv2.CascadeClassifier(path1)
while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    Body=body.detectMultiScale(gray,1.3,8)
    for (x,y,w,h) in Body:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    
    cv2.imshow("frame",frame)
    if cv2.waitKey(30) & 0xff==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()