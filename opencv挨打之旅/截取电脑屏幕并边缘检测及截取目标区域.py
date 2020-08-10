import numpy as np
import cv2
import time
from PIL import ImageGrab

def process_img(original_image):
    '''边缘检测？？'''
    #把原图像转化为灰度图
    process_img = cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)
    #转化了的灰度图进一步加工 thresholds是一个范围内
    process_img = cv2.Canny(process_img,threshold1=150,threshold2=300)
    return process_img

def roi (img,vertices):
    '''截取需要分析的目标区域同时排除干扰'''
    mask = np.zeros_like(img)
    cv2.fillPoly(mask,vertices,255)
    masked = cv2.bitwise_and(img,mask)
    return masked

last_time = time.time()
while True:
    screen = np.array(ImageGrab.grab(bbox = (0,0,800,640)))
    new_screen = process_img(screen)
    vertices = np.array([[10,500],[10,300],[300,200],[300,600]])
    roi_new_screen = roi(new_screen,[vertices])
    print (f'{time.time()-last_time}')
    last_time = time.time()
    cv2.imshow('original_image',cv2.cvtColor((screen),cv2.COLOR_BGR2RGB))
    #cv2.imshow('灰度图边缘检测',new_screen)
    cv2.imshow('aim',roi_new_screen)

    #waitKey(25)表示显示25s 值为-1则一直显示
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
