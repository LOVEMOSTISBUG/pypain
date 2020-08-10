import cv2
import numpy as np

cap  = cv2.VideoCapture(0)
#输出摄像头的基本参数
for i in range(0, 19):
     print(cap.get(i))
while(1):
     ret, frame = cap.read()
     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

     lower_blue = np.array([100, 47, 47])
     upper_blue = np.array([124, 255,255])

     mask = cv2.inRange(hsv, lower_blue, upper_blue) #蓝色掩模

     res = cv2.bitwise_and(frame, frame, mask = mask)

     cv2.imshow(u"Capture", frame)
     #cv2.imshow(u"mask", mask)
     cv2.imshow(u"res", res)

     key = cv2.waitKey(1)
     if key & 0xff == ord('q') or key == 27:
         print(frame.shape,ret)
         break
cap.release()
cv2.destroyAllWindows()
