import cv2
import numpy as np 
import math 

cap=cv2.VideoCapture(0)
cv2.namedWindow("scan")
cv2.resizeWindow("scan",640,480)
def findMaxContour(contours):
    max_i=0
    max_Area=0
    for i in range(len(contours)):

        area=cv2.contourArea(contours[i])
        if max_Area<area:
            max_Area=area
            max_i=i
            
    try:
        c=contours[max_i]
    except:
        c = np.array([[[0, 0]]])

    return c

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    roi=frame[50:250,270:470]
    cv2.rectangle(frame,(270,50),(470,250),(255,0,0),0)
    hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    lower=np.array([0,0,30],np.uint8)
    upper=np.array([48,255,255],np.uint8)
    mask=cv2.inRange(hsv,lower,upper)
    kernel=np.ones((5,5),np.uint8)
    mask=cv2.dilate(mask,kernel,iterations=1)
    blur=cv2.medianBlur(mask,15)
    contours,_=cv2.findContours(blur,cv2.CHAIN_APPROX_NONE,cv2.RETR_TREE)
    if len(contours)> 0:
        
            c=findMaxContour(contours)
            
            exLeft=tuple(c[c[:,:,0].argmin()][0]) #tüm değerlerin x değerini alır ve bunu iki boyutlu bir dizi şeklinde alır argmin minumum x değerini
            exRight=tuple(c[c[:,:,0].argmax()][0])
            exTop=tuple(c[c[:,:,1].argmin()][0])
            exBottom=tuple(c[c[:,:,1].argmax()][0])
            cv2.circle(roi,exLeft,5,(0,255,0),2)
            cv2.circle(roi,exRight,5,(0,255,0),2)
            cv2.circle(roi,exTop,5,(0,255,0),2)
            
            point=np.array([[exTop],[exLeft],[exRight]])
            cv2.polylines(roi,[point],True,(0,0,255),2)
            a=math.sqrt((exRight[0]-exTop[0])**2+(exRight[1]-exTop[1])**2)
            c=math.sqrt((exLeft[0]-exTop[0])**2+(exLeft[1]-exTop[1])**2)
            b=math.sqrt((exRight[0]-exLeft[0])**2+(exRight[1]-exLeft[1])**2)
            
            if a + b > c and a + c > b and b + c > a:
            # Açıyı hesaplıyoruz (Yunus'un teoremine göre)
                  # 57 ile dereceye çeviriyoruz
            # Hesaplanan açıyı ekrana yazdırıyoruz
                try :
                    angle = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * b * c)) * 57
                    cv2.putText(roi,str(angle),(exTop[0]-10,exTop[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2,cv2.LINE_AA)
                    if angle>70:
                       cv2.rectangle(roi,(0,0),(100,100),(255,0,0),2)
                except:
                    cv2.putText(roi,"?",(exTop[0]-10,exTop[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2,cv2.LINE_AA)
            else:
               cv2.putText(roi, "Invalid triangle", (exRight[0] - 10, exRight[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            
            
            


    cv2.imshow("scan",frame)
    cv2.imshow("roi",roi)
    cv2.imshow("mask",mask)
    if cv2.waitKey(30) & 0xff==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

