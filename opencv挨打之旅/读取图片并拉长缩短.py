import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    success,img = cap.read()
    cv2.putText(img,"Print f word to here",(0,25),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255))
    cv2.imshow('original_image',img)

    img1 = cv2.resize(img, (266,200)) #放大缩小随意
    cv2.imshow("img1", img1)


    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
