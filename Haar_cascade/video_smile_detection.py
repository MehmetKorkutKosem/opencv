import cv2
import numpy as np 
path1="D:\\opencv\\cascade\\Smile.xml"
path2="D:\\opencv\\tst_videos\\Smile.mp4"
path3="D:\\opencv\\cascade\\frontalface.xml"
cap=cv2.VideoCapture(path2)
face=cv2.CascadeClassifier(path3)
smile=cv2.CascadeClassifier(path1)
while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    frame=cv2.resize(frame,(640,480))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    Face=face.detectMultiScale(gray,1.3,4)
    for (x,y,w,h) in Face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    frame2=frame[y:y+h,x:x+w]
    gray2=gray[y:y+h,x:x+w]
    Smile=smile.detectMultiScale(gray2,1.8,3)
    for (ex,ey,ew,eh)in Smile:
        cv2.rectangle(frame2,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)   
    cv2.imshow("frame",frame)
    if cv2.waitKey(30) & 0xff==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
"""
import cv2
import numpy as np 
path1="D:\\opencv\\cascade\\Smile.xml"
path2="D:\\opencv\\tst_videos\\Smile.mp4"
path3="D:\\opencv\\cascade\\frontalface.xml"
cap=cv2.VideoCapture(0)
face=cv2.CascadeClassifier(path3)
smile=cv2.CascadeClassifier(path1)
while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    frame=cv2.resize(frame,(640,480))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    Face=face.detectMultiScale(gray,1.3,4)
    for (x,y,w,h) in Face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    frame2=frame[y:y+h,x:x+w]
    gray2=gray[y:y+h,x:x+w]
    Smile=smile.detectMultiScale(gray2,1.8,3)
    for (ex,ey,ew,eh)in Smile:
        cv2.rectangle(frame2,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)   
    cv2.imshow("frame",frame)
    if cv2.waitKey(30) & 0xff==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
"""