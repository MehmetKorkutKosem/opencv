import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower=np.array([100,20,50])
    uppr=np.array([140,200,160])
    mask=cv2.inRange(hsv,lower,uppr)
    kernel=np.ones((10,10),np.uint8)
    mask =cv2.erode(mask,kernel)
    contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area=cv2.contourArea(contour)

        epsilon=0.005*cv2.arcLength(contour,True)
        approx=cv2.approxPolyDP(contour,epsilon,True)
        x=approx.ravel()[0]
        y=approx.ravel()[1]
        M = cv2.moments(approx)
        
        if M["m00"] != 0:  # Sıfıra bölmeyi önlemek için kontrol et
            a = int(M["m10"] / M["m00"])
            b = int(M["m01"] / M["m00"])
            cv2.circle(frame, (a, b), 5, (0, 0, 255), thickness=-1) 
       
        if area>300:
          cv2.drawContours(frame,[approx],0,(0,0,255),3)

    cv2.imshow("screen",mask)
    cv2.imshow("screen1",frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

    
