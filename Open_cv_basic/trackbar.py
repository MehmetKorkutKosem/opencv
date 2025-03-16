import cv2
import numpy as np

def nothing(x):
    pass

# Fotoğrafı yükleme
image = cv2.imread("saha.png")
if image is None:
    print("Hata: Resim bulunamadı! Lütfen dosya adını kontrol edin.")
    exit()

# Pencere oluştur
cv2.namedWindow("image")

# Trackbar'ları oluştur
cv2.createTrackbar("R", "image", 0, 255, nothing)
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("B", "image", 0, 255, nothing)

switch = "0:OFF\n1:ON"
cv2.createTrackbar(switch, "image", 0, 1, nothing)

while True:
    # Trackbar değerlerini oku
    R = cv2.getTrackbarPos("R", "image")
    G = cv2.getTrackbarPos("G", "image")
    B = cv2.getTrackbarPos("B", "image")
    s = cv2.getTrackbarPos(switch, "image")

    # Orijinal resmi kopyala (değişiklik yaparken orijinali kaybetmemek için)
    img_copy = image.copy()

    # Eğer switch ON ise renk ayarı uygula
    if s == 1:
        img_copy[:, :, 0] = cv2.add(img_copy[:, :, 0], B)  # Mavi kanal
        img_copy[:, :, 1] = cv2.add(img_copy[:, :, 1], G)  # Yeşil kanal
        img_copy[:, :, 2] = cv2.add(img_copy[:, :, 2], R)  # Kırmızı kanal

    # Güncellenmiş görüntüyü göster
    cv2.imshow("image", img_copy)

    # 'q' tuşuna basıldığında çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

