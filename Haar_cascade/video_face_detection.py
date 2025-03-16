import cv2
import numpy as np
path="D:\\opencv\\tst_videos\\face.mp4"
path1="D:\\opencv\\cascade\\frontalface.xml"
cap=cv2.VideoCapture(0)
face=cv2.CascadeClassifier(path1)
while True:
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face.detectMultiScale(gray,1.3,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    
    cv2.imshow("frame",frame)
    if cv2.waitKey(30) & 0xff==ord("q"):
        break
cv2.release()
cv2.destroyAllWindows()
#webcam algılama
"""import cv2
import numpy as np
path="D:\\opencv\\tst_videos\\face.mp4"
path1="D:\\opencv\\cascade\\frontalface.xml"
cap=cv2.VideoCapture(0)
face=cv2.CascadeClassifier(path1)
while True:
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face.detectMultiScale(gray,1.4,6)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    
    cv2.imshow("frame",frame)
    if cv2.waitKey(30) & 0xff==ord("q"):
        break
cv2.release()
cv2.destroyAllWindows()"""
    
