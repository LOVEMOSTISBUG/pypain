import numpy as np
import cv2
import time


last_time = time.time()
cap = cv2.VideoCapture(0) #读取计算机摄像头
#cap.set(3,640) #宽
#cap.set(4,480) #高
cap.set(10,100) #亮度

#faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades+
#                                    'haarcascade_frontalface_default.xml')
print(cv2.CascadeClassifier(cv2.data.haarcascades)
      )
faceCascade = cv2.CascadeClassifier("D:\\haarcascade_frontalface_default.xml")  
while True:
    print (f'{time.time()-last_time}')
    last_time = time.time()
    success,img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray,1.1,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0))
    cv2.imshow('original_image',img)
    

    #waitKey(25)表示显示25s 值为-1则一直显示
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
