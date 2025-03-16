import cv2
import numpy as np
file="para1.jpg"
img=cv2.imread(file)
img1=cv2.resize(img,(640,480))
gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
blur=cv2.medianBlur(gray,5)
circles=cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,img1.shape[0]/4,param1=175,param2=14,minRadius=33,maxRadius=90)
if circles is not None:
    circles=np.uint16(np.around(circles))
    say=0
    for i in circles[0,:]:
        cv2.circle(img1,(i[0],i[1]),i[2],[0,0,255],2)
        say=say+1

font1=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img1,f"cember sayisi: {str(say)}",(150,50),font1,1,(255,0,0))      
        
print(say)
cv2.imshow("img",img1)
cv2.imshow("img1",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()