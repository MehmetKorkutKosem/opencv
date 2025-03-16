import matplotlib.pyplot as plt
import numpy as np
x=np.arange(4)#verilen argümana kadar sayar
print(x)
y=np.array([1,5,7,8],np.int16)#verilen aralıkta sayar
plt.plot(x,y)#plt.plot(x,y,"o"),plt.plot(x,y,"o-"),plt.plot(x,y,o--)
plt.plot(x,-y)
plt.title("Grafik Başlığı")
plt.show()
n=12
z=np.linspace(0,10,n)# sıfır ile on arasında n tane sayı oluşturur ve eşit aralıklarla böler
print(z)
k=z
plt.plot(z,k)
plt.show()#plt.axis("off") grafiğin eksenlerini kapatır
t=np.arange(5)
plt.plot(t,[a**2 for a in t])
plt.plot(t,[a**0.5 for a in t])
plt.plot(t,[(a**2)+2*a+1 for a in t])
plt.axis([0,4,0,20])#x ekseninin 0 ile 4 arasında y ekseninin 0 ile 20 arasında olmasını sağlar
plt.grid(True)# değerlşerin karşılıklarının daha anlaşılkır olmasını sağlar ızgara göünümü verir
print(plt.axis)# eksenlerin maksimum  değerlerini verir
plt.legend(["x**2","x**0.5","x**2+2a+1"],loc="upper center")#legend grafiğin hangi değerlerin hangi değerlere karşılık geldiğini gösterir loc konum belirler
plt.xlabel("x ekseni")
plt.ylabel("y ekseni")# eksenleri etiketlemek ve isim vermek için kullanılır
plt.savefig("D:\plt.png")#oluşturulan grafiği kaydeder
plt.show()