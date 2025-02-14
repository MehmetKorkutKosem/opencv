import cv2
import numpy as np
img=cv2.imread("coins.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.medianBlur(gray,1,5)
circles=cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,img.shape[0]/4,param1=200,param2=10,minRadius=15,maxRadius=89)#param1 gradient değeri  param 2 çember sayısı üzerinde ter orantılı bir etkisi varır minRadius min en küçük çaplı çember max en büyük çaplı çember,img.shape[0]/4 çemberler arası uzaklığı belirleyen değerdir
if circles is not None:
    circles=np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(img,(i[0],i[1]),i[2],[225,0,0],2)

cv2.imshow("img1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
