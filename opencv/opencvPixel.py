import cv2
import numpy as np
file="saha.png"
image=cv2.imread(file)
px=image[250,300]
px1=image[100,150]
px2=image[350,50]
px3=image[10,50]
image[100,150,0]=255#blue renk degeri değişir 
image[250,300,1]=200#Green renk degeri değişir
red=px2
print(red)

image.itemset((350,50,2),  110)



print("renk degeri",px)
print("renk degeri",px1)
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()