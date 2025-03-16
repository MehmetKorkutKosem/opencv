import cv2
import numpy as np

cap=cv2.VideoCapture(0)
cv2.namedWindow("mouseEvent")
# kare ve dörtgen için size =40
size=40
circles=[]
rectangles=[]


def mouse (event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
       
        circles.append((x,y))
        
    
    if event==cv2.EVENT_RBUTTONDOWN:
       
        rectangles.append((x,y))

cv2.setMouseCallback("mouseEvent",mouse)
while True:
    _,frame=cap.read()
    frame1=cv2.flip(frame,1)
    for circle in circles:
        cv2.circle(frame1,circle,10,(0,0,255),-1)
        if len(circles)>1:
           cv2.polylines(frame1,[np.array((circles))],False,(0,255,0),3)
    
    for x,y in rectangles:
        cv2.rectangle(frame1,(x,y),(x+40,y+40),(0,0,255),-1)
    
    cv2.imshow("mouseEvent",frame1)
    if cv2.waitKey(30) & 0xff==ord("q"):
        break

    if cv2.waitKey(30) & 0xff==ord("c"):
        circles=[]
        rectangles=[]
    
cap.release()
cv2.destroyAllWindows()




