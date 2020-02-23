import pyautogui
import time
try :
    puzi1 = ['3','3','4','5','5','4','3','2','1','1','2','3','3','2','2','space','3','3','4','5','5','4','3','2','1','1','2','3','2','1','1','space']
    puzi2 =[ '2','2','3','1','2','3','4','3','1','2','3','4','3','2','1','2','5','3','space','3','3','4','5','5','4','3','2','1','1','2','3','2','1','1','space']
    
    pyautogui.PAUSE = 1
    pyautogui.FAILSAFE = True  

    x_1,y_1 = pyautogui.center(pyautogui.locateOnScreen('aim.PNG'))  
    pyautogui.moveTo((x_1,y_1),duration=0.8)
    pyautogui.doubleClick(x_1,y_1)

    time.sleep(2)


    pyautogui.typewrite(puzi1,'0.6')
    pyautogui.typewrite(puzi2,'0.6')




except TypeError:
    print ('请把make_music放到能在屏幕上看到的位置\n否则程序无法正常运行')
except FileNotFoundError:
    print('文件缺失，请重新检查文件完整\n自行修补可尝试截一个aim.PNG的make_music')
    
