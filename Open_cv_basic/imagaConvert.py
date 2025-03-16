import cv2
import numpy as np 
file="aircraft.jpg"
file1="aircraft1.jpg"
image=cv2.imread(file)
image1=cv2.imread(file1)
image=cv2.resize(image,(640,480))
image1=cv2.resize(image1,(640,480))
image2=cv2.medianBlur(image1,5)
if image.shape==image1.shape:
    print("same size")
else:
    print("note same size")

#diff=cv2.subtract(image1,image)#iki resim arasındaki farklılıkları bulur 
diff=cv2.subtract(image1,image2)
b,g,r=cv2.split(diff)#farklı olan alanları renk formatına ayırır
if cv2.countNonZero(b)==0 and cv2.countNonZero(g)==0 and cv2.countNonZero(r)==0:
    print("resimler eşit")
else:
    print("resimler esit degil")
cv2.imshow("subtract",diff)
cv2.imshow("image",image)
cv2.imshow("image1",image1)
cv2.waitKey(0)
cv2.destroyAllWindows()