import numpy as np
x=np.array([1,2,3],np.int16)
print(x)
#iki boyutlu diziler 
y=np.array([[1,2,3,4],[5,6,7,8]],np.int16)
print(y)
print(y[0][0])
print(y[0,0])
print(y[-1,-1])
print(y[:,2])
z=np.array([[[1,2,3],[4,5,6]],[[5,7,8],[0,7,8]]],np.int16)
print("a",z[1,0,0])
print(z.shape)#shape boyutlarını gösterir
print(x.ndim)# kaç boyutlu olduğunu gösterir
print(x.dtype)# dizinin veri tipini gösterir    
print(y.T)#transpozunu alır
a=np.empty([3,3],np.int16)#boş ama içine rastgele sayılar atar
print(a)
k=np.full((3,3,3),dtype=np.int16,fill_value=0)#np.full ile belirtilen boyutlarda ve veri tipinde dizi oluşturulur ve fill_value ile diziye atanacak değer belirlenir
print(k)
f=np.zeros((2,3,3),np.int16)#sıfırlardan oluşan dizi oluşturur
print(f)
g=np.ones((2,3,3),np.int16)#birlerden oluşan dizi oluşturur
print(g)