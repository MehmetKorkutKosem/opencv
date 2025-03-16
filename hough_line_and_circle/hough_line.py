import cv2
import numpy as np

img=cv2.imread("h.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edge=cv2.Canny(gray,75,175)#
lines=cv2.HoughLinesP(edge,1,np.pi/180,50,maxLineGap=200) # çizgi takibi yapar maxLineGap=200 parametresi çizgiler arası boşluğu kapatır n.pi durumu açı hassasiyetidir bir derecelik açı hassasiyeti ile takip eder
for line in lines:
   x1,y1,x2,y2=line[0] # kordinatların olduğu bölümdeki değerleri alır
   cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow("img",img)
cv2.imshow("img1",edge)

cv2.waitKey(0)
cv2.destroyAllWindows()


