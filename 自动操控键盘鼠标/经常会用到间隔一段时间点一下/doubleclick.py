import pyautogui
from time import sleep
import os

ls =  open ('config.txt','r').readline().split('*')
x,y,t = ls
c = 0
pyautogui.PAUSE = 0 #执行每个函数后暂停的秒数
pyautogui.FAILSAFE = True  # 防故障True开启 鼠标移动到左上方（0，0）启动防故障
print('想要退出将鼠标移至最左上角即可哦\n')

while True:
    try:
        if pyautogui.position() == (0,0):
            print(f'那么拜拜啦\n')
            os.system('pause')
            break
        else:
            pyautogui.doubleClick(x=int(x), y=int(y), button='left',duration=1)
            c += 1
            print(f'工作了{str(c)}次\n ')
            sleep(int(t))
    except Exception as e:
        print (str(e))
        print(f'总之哪里出错了 debug去吧。\n')
        os.system('pause')





