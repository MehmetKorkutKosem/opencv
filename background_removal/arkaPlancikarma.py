import cv2
import numpy as np
cap = cv2.VideoCapture("car.mp4")
_,frame=cap.read()
frame=cv2.resize(frame,(640,480))
gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)

while True:
  ret,frame1=cap.read()
  frame2=cv2.flip(frame1,1)
  gray2=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
  blur1=cv2.GaussianBlur(gray2,(5,5),0)
  blur1=cv2.resize(blur1,(640,480))
  dif=cv2.absdiff(blur,blur1)# hareket tespiti gibi durumlarda, absdiff() çok kullanışlıdır çünkü değişiklik olan bölgeleri net bir şekilde ayrıştırır,teml görevi iki görüntü arsındaki temel farkları hesaplar
  _,dif=cv2.threshold(dif,30,255,cv2.THRESH_BINARY)
  cv2.imshow("orginal",frame)
  cv2.imshow("frame_1",blur)
  cv2.imshow("frame_2",dif)
  key = cv2.waitKey(30) & 0xff
  if key == ord("q"):
        break
  elif key == ord("k"):
    cv2.imwrite(r"D:\kayit\kayit_11.jpg", dif)  # Görüntüyü kaydet

cap.release()
cv2.destroyAllWindows()

