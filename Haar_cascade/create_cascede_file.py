"""
**Cascade Dosyası Oluşturma Aşamaları (Cascade Trainer ile)**  

1. **Veri Toplama:** Pozitif (nesneyi içeren) ve negatif (nesneyi içermeyen) görüntüler hazırlanır.    
2. **Eğitim Parametreleri Ayarlanır:** Aşama sayısı, hata oranı gibi değerler belirlenir.  
3. **Eğitim Başlatılır:** Model eğitilir ve nesneyi tanıyabilmesi sağlanır.  
4. **XML Dosyası Alınır:** Eğitilen model bir `cascade.xml` dosyası olarak kaydedilir ve kullanılmaya hazır hale gelir.
"""
import cv2
import numpy as np
path="D:\\opencv\\tst_videos\\Car_D.mp4"
path1="D:\\opencv\\cascade\\cascade.xml"

cap=cv2.VideoCapture(path)
car=cv2.CascadeClassifier(path1)
while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    Car=car.detectMultiScale(gray,1.2,15)
    for (x,y,w,h) in Car:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow("frame",frame)
    if cv2.waitKey(30) & 0xff==ord("q"):
        break

cap.release()
cv2.destroyAllWindows() 