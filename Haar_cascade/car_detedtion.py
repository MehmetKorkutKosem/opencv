import cv2
import numpy as np 
path1="D:\\opencv\\cascade\\Car.xml"
path2="D:\\opencv\\tst_images\\car.jpg"

image=cv2.imread(path2)
car=cv2.CascadeClassifier(path1)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
Car=car.detectMultiScale(gray,1.1,1)
for (x,y,w,h) in Car:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()