import numpy as np
import matplotlib.pyplot as plt
path='D:\opencv\saha.png'
img=plt.imread(path)#resim dosyasını okur
print(img)
plt.imshow(img)#resmi gösterir
plt.axis("off")
plt.show()
print(img.shape)
print(img.ndim)
print(img.dtype)