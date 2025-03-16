import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("setting")
font = cv2.FONT_HERSHEY_SIMPLEX  

# HSV renk eşik değerleri için trackbar oluşturuluyor
cv2.createTrackbar("l_h", "setting", 0, 180, nothing)
cv2.createTrackbar("l_s", "setting", 0, 180, nothing)
cv2.createTrackbar("l_v", "setting", 0, 255, nothing)
cv2.createTrackbar("u_h", "setting", 0, 180, nothing)
cv2.createTrackbar("u_s", "setting", 0, 180, nothing)
cv2.createTrackbar("u_v", "setting", 0, 255, nothing)

# Trackbar başlangıç değerleri belirleniyor
cv2.setTrackbarPos("u_h", "setting", 180)
cv2.setTrackbarPos("u_s", "setting", 180)
cv2.setTrackbarPos("u_v", "setting", 255)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Ayna efekti uygulanıyor
    frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # BGR'den HSV renk uzayına dönüştürme

    # Trackbar'dan alınan alt ve üst HSV değerleri
    l_h = cv2.getTrackbarPos("l_h", "setting")
    l_s = cv2.getTrackbarPos("l_s", "setting")
    l_v = cv2.getTrackbarPos("l_v", "setting")
    u_h = cv2.getTrackbarPos("u_h", "setting")
    u_s = cv2.getTrackbarPos("u_s", "setting")
    u_v = cv2.getTrackbarPos("u_v", "setting")

    lower = np.array([l_h, l_s, l_v])
    upper = np.array([u_h, u_s, u_v])

    # Renk aralığına göre maskeleme işlemi
    canvas = cv2.inRange(frame1, lower, upper)

    # Gürültüyü azaltmak için erozyon uygulanıyor
    kernel = np.ones((5, 5), np.uint8)
    canvas = cv2.erode(canvas, kernel)

    # Kontur bulma işlemi
    contours, _ = cv2.findContours(canvas, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)  # Kontur alanı hesaplanıyor
        epsilon = 0.02 * cv2.arcLength(cnt, True)  # Konturun basitleştirilmesi için epsilon değeri belirleniyor
        approx = cv2.approxPolyDP(cnt, epsilon, True)  # Konturün köşe noktaları hesaplanıyor

        x = approx.ravel()[0]  # Metnin konumunu belirlemek için x koordinatı
        y = approx.ravel()[1]  # Metnin konumunu belirlemek için y koordinatı
        
        if area > 400:  # Küçük şekilleri göz ardı et
            cv2.drawContours(frame, [approx], 0, (0, 255, 0), 5)  # Tespit edilen şeklin etrafına çizgi çiz
            if len(approx) == 3:
                cv2.putText(frame, "Triangle", (x, y), font, 1, (0, 255, 0))  # Üçgen
            elif len(approx) == 4:
                cv2.putText(frame, "Quadrilateral", (x, y), font, 1, (0, 255, 0))  # Dörtgen
            elif len(approx) == 5:
                cv2.putText(frame, "Pentagon", (x, y), font, 1, (0, 255, 0))  # Beşgen
            elif len(approx) > 5 and len(approx) <= 9:
                cv2.putText(frame, "Polygon", (x, y), font, 1, (0, 255, 0))  # Genel çokgen
            elif len(approx) > 9:
                cv2.putText(frame, "Ellipse", (x, y), font, 1, (0, 255, 0))  # Elips

    # Pencereleri göster
    cv2.imshow("canvas", canvas)
    cv2.imshow("setting", frame1)
    cv2.imshow("ana", frame)

    # Çıkış ve kayıt işlemleri
    key = cv2.waitKey(30) & 0xff
    if key == ord("q"):
        break
    elif key == ord("k"):
        cv2.imwrite(r"D:\kayit\kayit_10.jpg", frame)  # Görüntüyü kaydet

cap.release()
cv2.destroyAllWindows()
