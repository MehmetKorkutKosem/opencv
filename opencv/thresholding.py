import cv2
import numpy as np
img=cv2.imread("orta.jpg",0)
ret,th1=cv2.threshold(img,150,250,cv2.THRESH_BINARY)
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,2)#sondaki parametre değerlerinden ikiyi arttırır isek siyah bölgeler artar azaltır isek beyaz artar 11 olan kümeleri temsil eder artarsa kalınlaşma olur
th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow("dny",th1)
cv2.imshow("dny1",th2)
cv2.imshow("dny2",th3)
cv2.waitKey(0)
cv2.destroyAllWindows()