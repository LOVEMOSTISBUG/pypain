import pyautogui
import sys
import os

pyautogui.PAUSE = 0 #执行每个函数后暂停的秒数
pyautogui.FAILSAFE = True  # 防故障True开启 鼠标移动到左上方（0，0）启动防故障

#鼠标操作
# x, y = pyautogui.position() 获得鼠标实时位置
#pyautogui.click(x=cur_x, y=cur_y, button='left') 在指定位置左击一次 （left middle right）
#pyautogui.scroll(200) 滚轮向上200 正数往上
#pyautogui.doubleClick()

#键盘控制
#pyautogui.typewrite(['enter', 'a', 'b', 'left', 'left', 'X', 'Y'], '0.25') 
#pyautogui.keyDown('altleft')
#pyautogui.press('f4')
#pyautogui.keyUp('altleft')
#pyautogui.hotkey('altleft', 'f4') 这一行等于上面三行

#寻找目标
#next = pyautogui.locateOnScreen('aim.PNG',region=(0,0, 300, 400),grayscale=True)
# aim.PNG即目标截图 region是规定区域（左，顶部，宽度，高度） grayscale是灰度匹配可加快速度但可能误判
#x, y = pyautogui.center(next)   获得（左，顶部，宽度，高度）的中心坐标
#list(pyautogui.locateAllOnScreen('someButton.png')) 列出所有匹配的（左，顶部，宽度，高度）
#pyautogui.screenshot('ssln.PNG',(0,0,600,500)) 在(0,0,600,500))保存ssln.PNG


#提示框
#pyautogui.alert(text="123456",title="iyoukrls",button="ok") 简单提示框
#resp = pyautogui.confirm(text="123456",title="abcd",buttons=["ok","cancel","x"] 点击那个 resp便是 那个值
#text_P = pyautogui.prompt(text="123",title="text",default="456")
#text_p = pyautogui.password(text="123",title="text",default="456",mask="*")  

def get_screen():
    '''得到当前电脑的分辨度'''
    screenWidth, screenHeight = pyautogui.size()
    print('x='+str(screenWidth)+'\n'+'y='+str(screenHeight))
    return screenWidth, screenHeight

def find(aim):
    '''移动到aim的坐标，并返回aim当前坐标'''
    aim_x,aim_y = pyautogui.center(pyautogui.locateOnScreen(aim))  
    pyautogui.moveTo(x=aim_x, y=aim_y,duration=1)
    return aim_x,aim_y

def find_drag(aim1,aim2):
    '''将aim1拖拽至aim2'''
    find(aim1)
    pyautogui.mouseDown()
    find(aim2)
    pyautogui.mouseUp()

def drag_move_rel(x,y):
    '''相对拖拽x，y'''
    pyautogui.mouseDown()
    pyautogui.moveRel(x,y, duration=1)
    pyautogui.mouseUp()

def boom(d_file_name):
    '''本目录的d_file_name将被删除'''
    del_file = str(sys.path[0]+'\\'+str(d_file_name))
    os.remove(del_file)

def test_verify(password):
    '''验证密码返回布尔值'''
    verify_result = False
    response = pyautogui.password('你应该知道密码对吧？','这个是用来输入密码的窗口','','?')
    if response == password :
        verify_result = True
    return verify_result
def give_choice(choice1,choice2,choice3):
    '''给出选择项并返回之'''
    choice_response = str (pyautogui.confirm(text="做出你的选择吧",title="做出选择的窗口",buttons=[choice1,choice2,choice3]))
    return choice_response



