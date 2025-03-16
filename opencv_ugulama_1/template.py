import cv2
import numpy as np 
path="starwars.jpg"
path1="starwars1.jpg"
image1=cv2.imread(path)
image2=cv2.imread(path1)


gray=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)#resmi gri değerlere çevirir
gray1=cv2.imread(path1,0)#gri şekilde okur resmi
gray2=cv2.imread(path1 ,cv2.IMREAD_GRAYSCALE)# gri şekilde okur resmi
gray4=cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
cv2.imshow("window1",image1)
cv2.imshow("window2",image2)

cv2.imshow("window1.1",gray)
cv2.imshow("window2.1",gray1)
cv2.imshow("window3",gray2)
result=cv2.matchTemplate(gray,gray2,cv2.TM_CCOEFF_NORMED)#cv2.matchTemplate() fonksiyonu, şablon eşleme (template matching) yapmak için kullanılır. Yani, bir görüntü içinde belirli bir alt bölgenin (şablonun) nerede olduğunu bulmaya yarar
location=np.where(result>=0.9)
h,w=gray2.shape[::-1]
for x in zip(*location[::-1]):#zip(*...) kullanarak her iki dizinin öğelerini birleştiriyoruz.
    print(x)
    cv2.rectangle(image1,(x),(x[0]+w,x[1]+h),(0,0,255),3)

cv2.imshow("temp",result)
cv2.imshow("temp1",image1)
cv2.waitKey(0)
cv2.destroyAllWindows()