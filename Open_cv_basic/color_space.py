import cv2
file="saha1.png"
img=cv2.imread(file)
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img3=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("img",img)
cv2.imshow("img1",img1)
cv2.imshow("img2",img2),
cv2.imshow("img3",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()