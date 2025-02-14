import cv2

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("kanal",frame)
    if cv2.waitKey(30) & 0xff==ord("q"):
        break


cv2.release()
cv2.destroyAllWindows()