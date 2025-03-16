import cv2
import numpy as np
file="eye.mp4"
cap=cv2.VideoCapture(file)
while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    if ret is False:
        break
    roi=frame[80:210,200:450]
    gray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    _,treshold=cv2.threshold(gray,2,250,cv2.THRESH_BINARY_INV)
    contours,_=cv2.findContours(treshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)#sorted sıralama için kullanılır
    rows,cols,_=roi.shape
    for cnt in contours:
         (x,y,h,w)=cv2.boundingRect(cnt)#contour çevresinin bounding box'ının kordinatlarını alır 
         cv2.rectangle(roi,(x,y),(x+w,y+h),(0,0,255),2)
         cv2.line(roi,(x+w//2,0),(x+w//2,rows),(0,255,0),2)
         cv2.line(roi,(0,y+h//2),(cols,y+h//2),(0,255,0),2)
         break
    frame[80:210,200:450]=roi
    cv2.imshow("img ",roi)
    cv2.imshow("thres",treshold)
    cv2.imshow("frame",frame)
       
    if cv2.waitKey(30) & 0xff==ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
    


