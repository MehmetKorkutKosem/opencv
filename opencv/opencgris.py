import cv2

img = cv2.imread("saha.png")
cv2.namedWindow("img", cv2.WINDOW_NORMAL)
img=cv2.resize(img,(500,500)) #boyutlandırmak için resize kullanırız
cv2.imshow("img", img)  # Pencere adı ekleyin
cv2.imwrite("saha1.png",img)#resmi kaydeder
cv2.waitKey(0)  # Bir tuşa basılmasını bekleyin
cv2.destroyAllWindows()  # Tüm pencereleri kapatın

