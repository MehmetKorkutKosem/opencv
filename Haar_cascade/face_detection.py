import cv2
import numpy as np
path="D:\\opencv\\tst_images\\face.png"
path1="D:\\opencv\\cascade\\frontalface.xml"
image=cv2.imread(path)
face_cascade=cv2.CascadeClassifier(path1)#cv2.CascadeClassifier(path1): OpenCV'nin Haar Cascade sınıflandırıcısını yükler
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.3,6)# parametre 1.3 resmi boyutlandırma ,parametre "6" aradığımız bölgenin doğruluğunu bulmak için o bölgede bulunan kare sayısı
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("window",image)

cv2.waitKey(0)
cv2.destroyAllWindows()