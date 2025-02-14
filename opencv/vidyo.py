import cv2
"""#cap=cv2.VideoCapture("antalya.mp4")vidyo göstermek için kullanır
cap=cv2.VideoCapture(0)
while True:
   
    ret,frame=cap.read()
    #if ret==0: vidyonun bitip bitmediğini kontrol etmek için kullanılır
     #   break
    frame=cv2.flip(frame,1)#vidyonun yatayda ters çevrilmesini sağlar
    cv2.imshow("antalya",frame)
    if cv2.waitKey(30) & 0xff==ord("q"):#0xff=ord("q") q tuşuna  basıldığında kapanmasını sağlamak için yaptığımız bir düzenlemedir
       break

cap.release()
cv2.destroyAllWindows()"""
# video kaydetme komutları
cap=cv2.VideoCapture(0)
filename=r"D:\kayit\kayit.mp4"
codec=cv2.VideoWriter_fourcc("w","M","V","2")
framerate=30
resolution=(640,480)
videofileOutput=cv2.VideoWriter(filename,codec,framerate,resolution)
while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    videofileOutput.write(frame)
    cv2.imshow("web",frame)
    if cv2.waitKey(30) & 0xff==ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
