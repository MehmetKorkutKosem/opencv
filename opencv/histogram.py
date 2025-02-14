import cv2
import numpy as np
from matplotlib import pyplot as plt
img1=cv2.imread("orta.jpg")
b,g,r=cv2.split(img1)
img=np.zeros((500,500),np.uint8)+100
cv2.rectangle(img,(0,60),(60,120),(255,255,255),thickness=-1)
plt.hist(img.ravel(),256,[0,256])
plt.show()
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()