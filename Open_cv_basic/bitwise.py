import cv2
import numpy as np
img1=cv2.imread("bitwise_1.png")
img2=cv2.imread("bitwise_2.png")
bitAnd=cv2.bitwise_and(img1,img2)#mantıksal operatör matığı ile harket eder siyah ekran 0 beyaz ekran 1 "siyak kısımın içinde beyz veya beyaz kısmın içinde siyah olursa durum değimez çünkü ayrı ayrı karşılaştırılır"
bitOr=cv2.bitwise_or(img1,img2)
bitXOR=cv2.bitwise_xor(img1,img2)
bitnot=cv2.bitwise_not(img1)
bitnot1=cv2.bitwise_not(img2)
cv2.imshow("picture1",img1)
cv2.imshow("picture2",img2)
cv2.imshow("picture3",bitOr)
cv2.imshow("picture4",bitAnd)
cv2.imshow("picture5",bitXOR)
cv2.imshow("picture6",bitnot)
cv2.imshow("picture7",bitnot1)


cv2.waitKey(0)
cv2.destroyAllWindows()