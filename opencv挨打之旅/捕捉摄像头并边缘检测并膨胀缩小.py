import numpy as np
import cv2
import time
from PIL import ImageGrab

def process_img(original_image):
    '''边缘检测？？'''
    #把原图像转化为灰度图
    process_img = cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)
    #转化了的灰度图进一步加工 thresholds是一个范围内
    process_img = cv2.Canny(process_img,threshold1=200,threshold2=300)
    return process_img

def roi (img,vertices):
    '''截取需要分析的目标区域同时排除干扰'''
    mask = np.zeros_like(img)
    cv2.fillPoly(mask,vertices,255)
    masked = cv2.bitwise_and(img,mask)
    return masked

last_time = time.time()
cap = cv2.VideoCapture(0) #读取计算机摄像头
#cap.set(3,640) #宽
#cap.set(4,480) #高
cap.set(10,100) #亮度
kernel = np.ones((5,5),np.uint8) # magic no touch

while True:
    print (f'{time.time()-last_time}')
    last_time = time.time()

    success,img = cap.read()
    imgblur = cv2.GaussianBlur(process_img(img),(9,9),0) #9,9是模糊参数？
    dialation_img = cv2.dilate(process_img(img),kernel,iterations=2)
    eroded_img = cv2.erode(dialation_img,kernel,iterations=2)

    cv2.imshow('original_image',img)
    #cv2.imshow('canny',process_img(img))
    #cv2.imshow('blur',imgblur)
    cv2.imshow('dialation',dialation_img) #膨胀
    cv2.imshow('eroded',eroded_img)
    #waitKey(25)表示显示25s 值为-1则一直显示
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
