import cv2  # OpenCV kütüphanesini içe aktar

# Görüntüyü oku
image = cv2.imread("contour.png")

# Görüntüyü gri tonlamaya çevir (çünkü kontur işlemleri için genellikle gri tonlama kullanılır)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Belirli bir eşik değeriyle görüntüyü ikili (binary) hale getir (175'in üzerindekileri beyaz, altındakileri siyah yap)
_, thresh = cv2.threshold(gray, 175, 255, cv2.THRESH_BINARY)

# Görüntüdeki konturları bul (RETR_TREE: tüm hiyerarşik konturları bulur, CHAIN_APPROX_SIMPLE: gereksiz noktaları kaldırır)
contur, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# İlk bulunan konturu al (Eğer birden fazla kontur varsa, sadece ilkini seçiyoruz)
cnt = contur[0]

# Seçilen konturun alanını hesapla (piksel cinsinden)
area = cv2.contourArea(cnt)
print(area)  # Alanı ekrana yazdır

# Konturun momentlerini hesapla (Momentler, şeklin merkezi ve geometrik özellikleri hakkında bilgi verir)
M = cv2.moments(cnt)

# Momentlerden hesaplanan "m00" değeri, konturun alanına eşittir (Teorik olarak contourArea ile aynı olmalı)
print(M["m00"])

# Konturun çevresini (perimeter) hesapla (True: kapalı bir şekil olduğunu belirtir)
perimeter = cv2.arcLength(cnt, True)
print(perimeter)  # Çevre uzunluğunu ekrana yazdır
