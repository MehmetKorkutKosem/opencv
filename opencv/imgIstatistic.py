import numpy as np
import matplotlib.pyplot as plt
path='D:\saha.png'
img=plt.imread(path)
print(img)
print(img.min())# resmin pixellerinin en küçük değerini verir
print(img.max())# resmin pixellerinin en büyük değerini verir
print(img.mean())# resmin pixellerinin ortalamasını verir
print(np.median(img))# resmin pixellerinin medyanını verir
print(np.average(img))# mean ile aynı işlevi görür
print(np.mean(img))#meanın farklı göstrim şeklidir