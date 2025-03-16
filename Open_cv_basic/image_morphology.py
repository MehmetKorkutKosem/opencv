import cv2
import numpy as np

img=cv2.imread("orta.jpg",0)
kernel=np.ones((5,5),np.uint8)
erosion=cv2.erode(img,kernel,iterations=1)#siyahlıklar artar
dletion=cv2.dilate(img,kernel,iterations=5)#beyazlıklar artar
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)#resimdeki bozuntu gürültüyü giderir
closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)#resimdeki beyaz kısımdaki gürültüyü giderir
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)#resimdeki kenar kısımlarını belirginleştirir
tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)#iç kısımlatı karartır
cv2.imshow("dny",erosion)
cv2.imshow("dzt1",dletion)
cv2.imshow("fsl",opening)
cv2.imshow("sss",closing)
cv2.imshow("sfs",gradient)
cv2.imshow("orginal",img)
cv2.imshow("tph",tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()