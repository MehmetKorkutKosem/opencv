import cv2

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    edges=cv2.Canny(frame,50,150)#gradyan değeri 50'den küçükse kenar sayılmaz gradyan değeri 150 den yüksek ise bu bir kenardır
    cv2.imshow("frame",frame)
    cv2.imshow("edges",edges)
    if cv2.waitKey(30)&0xff==ord("q"):
        break


cap.release()
cv2.destroyAllWindows()