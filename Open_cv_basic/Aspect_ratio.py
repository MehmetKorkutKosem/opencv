import cv2
def resizeWithAspectRatio(img, width=None, height=None, inter=cv2.INTER_AREA):
    dimension=None
    (h,w)=img.shape[:2]
    if width is None and height is None:
        return img
    
    if width is None:
        r=height/float(h)
        dimension=(int(w*r),height)
    else:
        r=width/float(w)
        dimension=(width,int(h*r))
    
    return cv2.resize(img,dimension,interpolation=inter)


img=cv2.imread("saha.png")
img1=resizeWithAspectRatio(img,width=1000)
cv2.imshow("img",img)
cv2.imshow("img1",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
