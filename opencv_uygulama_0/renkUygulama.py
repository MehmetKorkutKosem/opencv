import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("canvas")

# Trackbar'ları oluştur
cv2.createTrackbar("l_h", "canvas", 0, 180, nothing)
cv2.createTrackbar("l_s", "canvas", 0, 255, nothing)
cv2.createTrackbar("l_v", "canvas", 0, 255, nothing)
cv2.createTrackbar("u_h", "canvas", 0, 180, nothing)
cv2.createTrackbar("u_s", "canvas", 0, 255, nothing)
cv2.createTrackbar("u_v", "canvas", 0, 255, nothing)
cv2.setTrackbarPos("u_h","canvas",180),
cv2.setTrackbarPos("u_s","canvas",255)
cv2.setTrackbarPos("u_v","canvas",255)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Görüntüyü sağa_sola çevirme (kamera ayna etkisi)
    frame = np.flip(frame, 1)
    frame1=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    

    # Trackbar'lardan B, G, R değerlerini al
    l_h = cv2.getTrackbarPos("l_h", "canvas")
    l_s = cv2.getTrackbarPos("l_s", "canvas")
    l_v= cv2.getTrackbarPos("l_v", "canvas")
    u_h = cv2.getTrackbarPos("u_h", "canvas")
    u_s = cv2.getTrackbarPos("u_s", "canvas")
    u_v= cv2.getTrackbarPos("u_v", "canvas")
    

    # Renk aralığını ayarlamak için minimum ve maksimum değerleri belirleyin
    lower_bound = np.array([l_h,l_s,l_v ])
    upper_bound = np.array([u_h,u_s,u_v])

    # `cv2.inRange()` fonksiyonunu kullanarak renk filtresi uygulama
    canvas = cv2.inRange(frame1, lower_bound, upper_bound)

    # Görüntüyü göster
    cv2.imshow("canvas", canvas)
    cv2.imshow("uyg", frame)

    # Çıkış için 'q' tuşuna basılmasını bekle
   

    if cv2.waitKey(30) & 0xFF == ord("c"):
        cv2.imwrite(r"D:\kayit\kayit8.jpg",canvas)
        
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
