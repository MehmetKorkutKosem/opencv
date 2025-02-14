import matplotlib.pyplot as plt
import numpy as np
path="D:\saha.png"
img=plt.imread(path)
plt.imshow(img)
plt.axis("off")
plt.show()
x=np.arange(10)
y=np.array([1,3,5,7,9,11,13,15,17,19])
plt.plot(x,y,"o")
plt.axis([0,10,1,19])
plt.legend("y=x+1")
plt.xlabel("x")
plt.ylabel("y")
plt.show()