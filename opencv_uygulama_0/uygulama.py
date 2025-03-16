import cv2
cap=cv2.VideoCapture(0)
filename=r"D:\kayit\kayit1.mp4"
codec=cv2.VideoWriter_fourcc("w","M","V","2")
framerate=30
resolution=(640,480)
videofileOutput=cv2.VideoWriter(filename,codec,framerate,resolution)

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    videofileOutput.write(frame)
    cv2.imshow("web",frame)
    if cv2.waitKey(30) & 0xff==ord("e"):
        break
   
    if cv2.waitKey(30) & 0xff==ord("k"):
        cv2.imwrite(r"D:\kayit\kayit1.jpg",frame)

    
cap.release()
cv2.destroyAllWindows()


