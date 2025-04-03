import cv2
import numpy as np
path1="D:\\opencv\\cascade\\Smile.xml"
path2="D:\\opencv\\tst_images\\Smile.jpg"
path3="D:\\opencv\\cascade\\frontalface.xml"
image=cv2.imread(path2)
smile=cv2.CascadeClassifier(path1)
face=cv2.CascadeClassifier(path3)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
Face=face.detectMultiScale(gray,1.3,5)
for (x,y,w,h) in Face:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),3)

image2=image[y:y+h,x:x+w]
gray2=gray[y:y+h,x:x+w]
Smile=smile.detectMultiScale(gray2,1.8,20)
for (ex,ey,ew,eh) in Smile:
    cv2.rectangle(image2,(ex,ey),(ex+ew,ey+eh),(0,255,0),3)
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()