import cv2
import matplotlib.pyplot as plt
path="D:\saha.png"
img=cv2.imread(path,1)#BGR
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#BGR to RGB *1 (COLOR_BGR2GRAY)
plt.imshow(img,cmap='gray')# plt.imshow(img,cmap='gray',interpolation='BICUBIC') gri tonlarında göstermek için kullanılır #RGB
plt.show()#resimde boxunma olur çünkü BGR okuyupn rgb göstermeye çalışıoyoruz bu nedenle sorun olur sorunun çözümü numaralkışekilde yapılır

