import cv2
import numpy as np
img=cv2.imread("star.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.blur(gray,(5,5))
_,trash=cv2.threshold(blur,110,175,cv2.THRESH_BINARY)
contur,_hiararcy=cv2.findContours(trash,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
hull=[]
for i in range(len(contur)):
    hull.append(cv2.convexHull(contur[i],False))#convexhull dışbükey örtü çizer contur[i],False) kontur indekslerini döndürür

bg=np.zeros((trash.shape[0],trash.shape[1],3),np.uint8)
for i in range(len(contur)):
    cv2.drawContours(bg,contur,i,(0,0,255),3,8)
    cv2.drawContours(bg,hull,i,(0,255,0),1,8)

cv2.imshow("bbg",bg)
cv2.waitKey(0)
cv2.destroyAllWindows()

