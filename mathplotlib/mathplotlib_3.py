import numpy as np
import matplotlib.pyplot as plt
path="D:\kta.jpg"
img=plt.imread(path)
r=img[:,:,0]
g=img[:,:,1]
b=img[:,:,2]
title=["img","red","green","blue"]
output=[img,r,g,b]
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.axis("off")
    plt.title(title[i])
    if i==0:
        plt.imshow(output[i])
    else:
        plt.imshow(output[i],cmap="gray")
    plt.show()

j=np.dstack((r,g,b))
plt.axis("off")
plt.title("final")
plt.imshow(j)
plt.show()

