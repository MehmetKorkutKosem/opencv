import numpy as np
import matplotlib.pyplot as plt
path="D:\kta.jpg"
img=plt.imread(path)
plt.subplot(4,2,1)
plt.title("img")
plt.axis("off")
plt.imshow(img)

plt.subplot(4,2,2)
plt.title("img+img")
plt.axis("off")
plt.imshow(img+img)

plt.subplot(4,2,3)
plt.title("img-img")
plt.axis("off")
plt.imshow(img-img)

plt.subplot(4,2,4)
plt.title("np.flip")
plt.axis("off")
plt.imshow(np.flip(img,0))

plt.subplot(4,2,5)
plt.title("np.flip")
plt.axis("off")
plt.imshow(np.flip(img,1))

plt.subplot(4,2,6)
plt.title("np.flip")
plt.axis("off")
plt.imshow(np.flip(img,2))#renk değişir

plt.subplot(4,2,7)
plt.title("np.flipud")#flipud up to down
plt.axis("off")
plt.imshow(np.flipud(img))

plt.subplot(4,2,8)
plt.title("np.fliplr") #fliplr left to right
plt.axis("off")
plt.imshow(np.fliplr(img))

plt.show()
