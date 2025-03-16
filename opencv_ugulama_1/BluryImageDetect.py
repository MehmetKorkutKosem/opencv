import cv2
import numpy as np
file="starwars.jpg"
image=cv2.imread(file)
blurr=cv2.medianBlur(image,7)
laplacian=cv2.Laplacian(image,cv2.CV_64F).var()#görüntünün keskinliğini analiz eder
laplacian1=cv2.Laplacian(blurr,cv2.CV_64F).var()
print("laplacian")
print("laplacian1")
array={laplacian:"image2",laplacian1:"image1"}
for i,name in array.items():
    if i < 500:
        
        print(f"used blur this image {name}")

cv2.destroyAllWindows()
