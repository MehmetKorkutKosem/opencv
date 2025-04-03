import cv2
import numpy as np
path1="D:\\opencv\\cascade\\fullbody.xml"
path2="D:\\opencv\\tst_images\\body.jpg"
image=cv2.imread(path2)
body=cv2.CascadeClassifier(path1)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
Body=body.detectMultiScale(gray,1.3,6)
for (x,y,w,h) in Body:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
