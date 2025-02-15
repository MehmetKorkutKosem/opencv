import cv2

image=cv2.imread("contour.png")
contur=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
_,trash=cv2.threshold(contur,175,255,cv2.THRESH_BINARY)
M=cv2.moments(trash)# momentleri atar momentler şeklin matematiksel özelliklerini tanımlayan değerler
x=int(M["m10"]/M["m00"])
y=int(M["m01"]/M["m00"])
cv2.circle(image,(x,y),5,(0,0,255),thickness=-1)
cv2.imshow("ss",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
