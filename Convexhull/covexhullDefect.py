import cv2
import numpy as np


img = cv2.imread("star.png")  


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Renkli resmi gri tonlamaya çevirir

# Eşikleme işlemi: Görüntüdeki pikselleri siyah-beyaz hale getirmek için threshold kullanılır
_, thresh = cv2.threshold(gray, 127, 255, 0)  # 127 eşik değeriyle, 127'nin üzerindeki pikseller beyaz, altındaki pikseller siyah olur

# Görüntüdeki konturları (sınırları) bulma
contours, _ = cv2.findContours(thresh, 2, 1)  # Görüntüdeki konturları tespit eder. "2" dış konturları, "1" ise köşe noktalarını alır

cnt = contours[0]  # İlk bulunan konturu alıyoruz (genellikle bir nesne içeren kontur olur)

# Konveks hull (çevreyi saracak en küçük düzgün şekil) hesaplanır
hull = cv2.convexHull(cnt, returnPoints=False)  # Hull noktalarının yerine indeksleri döndürür

# Convexity defects (konveksite kusurları) hesaplanır
defects = cv2.convexityDefects(cnt, hull)  # Konveksite kusurlarını bulur (yani iç boşlukları ve çentikleri)

# Kusurları (boşlukları) görselleştirme
for i in range(defects.shape[0]):  # Her bir kusur için döngü
    s, e, f, d = defects[i, 0]  # Kusurun başlangıç, bitiş, uzak noktasını ve derinliğini alır
    start = tuple(cnt[s][0])  # Başlangıç noktasının koordinatlarını alır
    end = tuple(cnt[e][0])  # Bitiş noktasının koordinatlarını alır
    far = tuple(cnt[f][0])  # En uzak noktanın koordinatlarını alır
    
    # Kusurlar arasındaki çizgiyi çizer
    cv2.line(img, start, end, [0, 255, 0], 2)  # Yeşil renkli çizgilerle kontur noktalarını bağlar
    
    # Kusurun en uzak noktasına nokta çizer
    cv2.circle(img, far, 5, [0, 255, 0], -1)  # Yeşil renkli bir daire çizer

# Sonuçları görüntüler
cv2.imshow("img", img)  # İşlem görmüş resmi gösterir
cv2.waitKey(0)  # Bir tuşa basılmasını bekler
cv2.destroyAllWindows()  # Pencereyi kapatır
"""
import cv2
import numpy as np

img = cv2.imread("8.1 map.jpg.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray,(3,3))
ret,thresh = cv2.threshold(blur,40,255,cv2.THRESH_BINARY)

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

hull = []

for i in range(len(contours)):
    hull.append(cv2.convexHull(contours[i],False))

bg = np.zeros((thresh.shape[0],thresh.shape[1],3),np.uint8)

for i in range(len(contours)):
    cv2.drawContours(bg,contours,i,(255,0,0),3,8)
    cv2.drawContours(bg,hull,i,(0,255,0),1,8)


cv2.imshow("Image",bg)


cv2.waitKey(0)
cv2.destroyAllWindows()

ret,thresh = cv2.threshold()"""