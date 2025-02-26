import cv2
import numpy as np
file="para.jpg"
img=cv2.imread(file)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.medianBlur(gray,5)
circles=cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,img.shape[0]/6,param1=200,param2=15,minRadius=15,maxRadius=60)
if circles is not None:
    circles=np.uint16(np.around(circles))
    say=0
    for i in circles[0,:]:
        cv2.circle(img,(i[0],i[1]),i[2],[0,0,255],2)
        say=say+1

font1=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,f"cember sayisi: {str(say)}",(150,50),font1,1,(255,255,255))      
        
print(say)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    