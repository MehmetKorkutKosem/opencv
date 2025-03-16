import cv2
import numpy as np
img=cv2.imread("saha.png",0)
row,col=img.shape
print(row)
print(col)
M=np.float32([[1,0,10],[0,1,250]])# x ve y eksenleri boyunca kaydırma yapar
img1=cv2.warpAffine(img,M,(row,col))
cv2.imshow("dst",img1)
cv2.imshow("dst1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()