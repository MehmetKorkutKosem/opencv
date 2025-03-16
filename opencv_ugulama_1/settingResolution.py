import cv2
import numpy as np
cv2.namedWindow("window")
cap=cv2.VideoCapture(0)
print("Width:"+str(cap.get(3)))
print("width:"+str(cap.get(4)))
cap.set(3,1200)
cap.set(4,720)
print("Width:"+str(cap.get(3)))#genişlik değerini verir
print("width:"+str(cap.get(4)))#uzunlukk değerini verir
while True:
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    cv2.imshow("window",frame)
    if cv2.waitKey(30) & 0xff==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

