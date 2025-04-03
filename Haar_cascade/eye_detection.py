import cv2
import numpy as np 
path="D:\\opencv\\tst_images\\face.png"
path1="D:\\opencv\\cascade\\Eye.xml"
path2="D:\\opencv\\cascade\\frontalface.xml"
image=cv2.imread(path)
face_cascade=cv2.CascadeClassifier(path2)
eye_cascade=cv2.CascadeClassifier(path1)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
face=face_cascade.detectMultiScale(gray,1.3,6)
for (x,y,w,h) in face:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

image2=image[y:y+h,x:x+w]#yüzü tepit ettiğiimiz bölgeyi değişkene atayıp göz tespiti o bölgede yapılacak 
gray2=gray[y:y+h,x:x+w]
eyes=eye_cascade.detectMultiScale(gray2,1.3,6)
for (ex,ey,ew,eh) in eyes:
    cv2.rectangle(image2,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)

cv2.imshow("image",image)
cv2.imshow("imag2",image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
