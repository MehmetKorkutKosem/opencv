import cv2
import numpy as np

# Görüntüyü oku
img = cv2.imread("orta.jpg")

# Görüntüyü gri tonlamaya çevir
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Float32 formatına çevir
img1 = np.float32(img1)

# Harris köşe tespiti uygula
corners = cv2.goodFeaturesToTrack(img1, 100, 0.01, 10)

# Tam sayı formatına çevir
corners = np.int32(corners)

# Köşeleri görüntü üzerine çiz
for corner in corners:
    x, y = corner.ravel()  # Buradaki hata düzeltildi
    cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

# Sonucu göster
cv2.imshow("corner", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
