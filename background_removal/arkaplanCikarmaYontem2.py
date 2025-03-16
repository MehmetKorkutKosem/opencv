import cv2
import numpy as np
cap=cv2.VideoCapture("car.mp4")

subtractor=cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=50,detectShadows=True)#arka plan çıkarmak için tanımlı bir fonksiyon ilk parametresi frame miktarı ikinci parametresi threshold değeri son parametresi shadow değeri gölgelendirme diyebibiriz


while True :
    _,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    mask=subtractor.apply(frame)#hareketli nesneler ile arka plan arasındaki farkı hesaplar
 
    cv2.imshow("img",mask)
    cv2.imshow("img1",frame)
    key = cv2.waitKey(30) & 0xff
    if key == ord("q"):
        break
    elif key == ord("k"):
      cv2.imwrite(r"D:\kayit\kayit_12.jpg", mask)
    
cap.release()
cv2.destroyAllWindows()
