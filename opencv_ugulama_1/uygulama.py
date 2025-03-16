


   



import cv2
import numpy as np 

# Görüntüyü yükle
img = cv2.imread("polygons.png")  # Buraya kendi dosya adını ekle

# Griye çevir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Eşikleme uygula (Binary Thresholding)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Konturları bul
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Yazı tipi tanımla
font = cv2.FONT_HERSHEY_SIMPLEX  

# Konturları işle
for cnt in contours:
    epsilon = 0.01 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)

    # Konturu çiz
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 2)

    # İlk noktanın koordinatlarını al
    x, y = approx.ravel()[0], approx.ravel()[1]
    print(cnt)
    print(len(cnt))
 
    # Kenar sayısına göre şekil ismini yaz
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), font, 1, (0, 0, 0), 2)
    elif len(approx) == 4:
        cv2.putText(img, "dörtegn", (x, y), font, 1, (0, 0, 0), 2)
    elif len(approx) == 5:
        cv2.putText(img, "beşgen", (x, y), font, 1, (0, 0, 0), 2)
    elif len(approx) == 6:
        cv2.putText(img, "altigen", (x, y), font, 1, (0, 0, 0), 2)
    elif len(approx) == 7:
        cv2.putText(img, "yedigen", (x, y), font, 1, (0, 0, 0), 2)
    else:
        cv2.putText(img,"ellipse",(x,y),font,1,(0,0,0),2)




# Sonucu göster
cv2.imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

