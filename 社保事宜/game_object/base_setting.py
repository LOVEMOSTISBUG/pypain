import pyautogui

screenWidth, screenHeight = pyautogui.size()

class setting():
    
    """  储存各类设置的类"""
    def __init__(self):
        """  设置属性  """
        self.screen_width = screenWidth
        self.screen_height =  screenHeight

        self.ship_speed = 9
        self.ships_limit = 3

        self.bullet_speed = 15
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 255,0,0
        self.bullet_limit = 5

        self.guai_speed = 1
        self.fleet_direction = 1
        
