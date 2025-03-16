import cv2
import numpy as np
file=""
img=cv2.imread(file)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
trash=cv2.threshold(gray,cv2.THRESH_BINARY)
contur=cv2.findContours(trash,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
