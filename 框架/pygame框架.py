import pygame
import sys
import math

#需要全屏？
#import pyautogui         
#screenWidth, screenHeight = pyautogui.size()  

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

def run_game():
    '''初始化界面'''
    pygame.init()
    size = width,height = 640,480
    screen = pygame.display.set_mode(size)
    
    #需要全屏？
    #screen = pygame.display.set_mode((screen_width,screen_height),flags = pygame.FULLSCREEN|pygame.HWSURFACE)

    pygame.display.set_caption('看什么看我是窗口')
    game_clock = pygame.time.Clock()
    
    while True:
        draw_screen(screen)
        event_check()
        pygame.display.flip()
        game_clock.tick(144)

def event_check():
    '''检查鼠标键盘动作'''
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            check_keydown(event)
        if event.type == pygame.KEYUP:
            check_keyup(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_click(mouse_x,mouse_y)
        
def check_keydown(event):
    if event.key == pygame.K_ESCAPE:
        sys.exit()
def check_keyup(event):
    if event.key == pygame.K_q:
        print('ssln')
def check_click(mouse_x,mouse_y):
    pass
    
def draw_screen(screen):
    '''绘制屏幕'''
    #background = pygame.image,load('ssln.png').convert_alpha()
    #screen.blit(background)
    screen.fill(WHITE)
def collide_check(oba,obb):
    '''圆形碰撞检测 返回布尔值 True为存在碰撞'''
    boom = False
    distance = math.sqrt( math.pow((oba.rect.center[0] - obb.rect.center[0]),2) + ((oba.rect.center[1] - obb.rect.center[1]),2))
    if ditance <= (oba.rect.width + obb.rect.width)/2 :
        boom = True
    return boom

run_game()

#self.image = pygame.image.load('image/mememe.bmp').convert()
#        #把背景（0，0，0）变得透明
#        self.image.set_colorkey((0,0,0))
