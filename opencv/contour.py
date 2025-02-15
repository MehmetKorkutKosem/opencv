import cv2  # OpenCV kütüphanesini içe aktar

# Görüntüyü oku
img = cv2.imread("contour1.png")

# Görüntüyü gri tonlamaya çevir (çünkü kontur işlemleri gri tonlama ile daha kolaydır)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Belirli bir eşik değeri ile görüntüyü ikili (binary) hale getir 
# (175'in üzerindeki pikselleri beyaz, altındakileri siyah yapar)
_, trash = cv2.threshold(gray, 175, 255, cv2.THRESH_BINARY)

# Görüntüdeki konturları bul
# Kontur (Contour), bir şeklin veya nesnenin dış sınırını temsil eden noktaların kümesidir.
# RETR_TREE -> Tüm hiyerarşik konturları bulur
# CHAIN_APPROX_SIMPLE -> Gereksiz noktaları kaldırarak daha az veri kullanır
contur, _ = cv2.findContours(trash, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Bulunan tüm konturları kırmızı (0,0,255) renkte ve 3 kalınlıkta görüntü üzerine çiz
cv2.drawContours(img, contur, -1, (0, 0, 255), 3)


# Sonuç görüntüsünü göster
cv2.imshow("imgr", img)

# Kullanıcı bir tuşa basana kadar bekle
cv2.waitKey(0)

# Tüm penceleri kapat
cv2.destroyAllWindows()

