import cv2
import numpy as np 
def nothing():
    pass 

image=cv2.imread("aircraft.jpg")
image=cv2.resize(image,(640,480))
image1=cv2.imread("balls.jpg")
image1=cv2.resize(image1,(640,480))
output=cv2.addWeighted(image,0.5,image1,0.5,0)#cv2.addWeighted() fonksiyonu, iki görüntüyü belirli ağırlıklarla birleştirmek için kullanılır.
cv2.namedWindow("translation")
cv2.createTrackbar("Alpha","translation",0,1000,nothing)
while True:
    alpha=cv2.getTrackbarPos("Alpha","translation")/1000
    beta=1-alpha
    output=cv2.addWeighted(image,alpha,image1,beta,0)
    print(alpha,beta)
    cv2.imshow("image",output)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cv2.destroyAllWindows()