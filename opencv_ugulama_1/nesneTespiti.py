import cv2
import numpy as np
def nothing():
    pass

cap=cv2.VideoCapture(0)
cv2.namedWindow("setting")
cv2.createTrackbar("l_h","setting",0,180,nothing)
cv2.createTrackbar("l_s","setting",0,180,nothing)
cv2.createTrackbar("l_v","setting",0,255,nothing)
cv2.createTrackbar("u_h","setting",10,180,nothing)
cv2.createTrackbar("u_s","setting",0,180,nothing)
cv2.createTrackbar("u_v","setting",0,255,nothing)
cv2.setTrackbarPos("u_h","setting",180)
cv2.setTrackbarPos("u_s","setting",180)
cv2.setTrackbarPos("u_v","setting",255)

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    l_h=cv2.getTrackbarPos("l_h","setting")
    l_s=cv2.getTrackbarPos("l_s","setting")
    l_v=cv2.getTrackbarPos("l_v","setting")
    u_h=cv2.getTrackbarPos("u_h","setting")
    u_s=cv2.getTrackbarPos("u_s","setting")
    u_v=cv2.getTrackbarPos("u_v","setting")
    lower=np.array([l_h,l_s,l_v],np.uint8)
    upper=np.array([u_h,u_s,u_v],np.uint8)
    canvas=cv2.inRange(frame,lower,upper)
    bitwise=cv2.bitwise_and(frame,frame,mask=canvas)
    cv2.imshow("setting",frame)
    cv2.imshow("img",canvas)
    key = cv2.waitKey(30) & 0xff
    if key == ord("q"):
        break
    elif key == ord("k"):
       cv2.imwrite(r"D:\kayit\kayit_12.jpg", bitwise)  # Görüntüyü kaydet
    
cap.release()
cv2.destroyAllWindows()
