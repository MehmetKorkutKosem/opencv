import cv2
import numpy as np
import matplotlib.pyplot as plt

def display(image, cmap="gray"):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(image, cmap="gray")
    plt.show()

file = "para1.jpg"
image = cv2.imread(file)
image1=cv2.imread(file)

alpha = 0.9  # Kontrastı daha fazla düşür
beta = -130  # Parlaklığı daha fazla azalt

darkened = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

#display(image)
blur = cv2.medianBlur(darkened, 5)
#display(blur)
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
#display(gray)

ret, trash = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
#display(trash)

contours, hierarchy = cv2.findContours(trash.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(image, contours, i, (0, 255, 0), 2)

#display(image)
kernel = np.ones((3, 3), np.uint8)
morp = cv2.morphologyEx(trash, cv2.MORPH_CLOSE, kernel, iterations=9)
#display(morp)
dist = cv2.distanceTransform(morp, cv2.DIST_L2, 5)
#display(dist)

ret, sureFG = cv2.threshold(dist, 0.4 * dist.max(), 255, 0)
#display(sureFG)
sureFG = np.uint8(sureFG)
sureBG = cv2.dilate(morp, kernel, iterations=2)
#display(sureBG)

unknown = cv2.subtract(sureBG, sureFG)
#display(unknown)

ret, makers = cv2.connectedComponents(sureFG)
makers = makers + 1
makers[unknown == 255] = 0
makers = cv2.watershed(image, makers)

#display(makers)
contours, hierarchy = cv2.findContours(makers.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(image, contours, i, (0, 0, 255), 3)

# Watershed sonucunu 8-bit gri tonlamaya çevirme
gray_markers = cv2.convertScaleAbs(makers)

# Hough Circle Dönüşümü Uygulama (gri tonlamalı görüntü ile)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1.2, minDist=100,
                           param1=221, param2=39, minRadius=90, maxRadius=310)

# Tespit edilen çemberleri çizme
if circles is not None:
    circles = np.uint16(np.around(circles))
    say=0
    for i in circles[0, :]:
        cv2.circle(image1, (i[0], i[1]), i[2], (255, 0, 0), 4)  # Çember dış çizgisi (mavi)
        say=say+1

font1=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image1,f"cember sayisi: {str(say)}",(150,50),font1,2,(255,0,0),thickness=3)  

image1 = cv2.resize(image1, (640, 480))
cv2.imshow("img", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

