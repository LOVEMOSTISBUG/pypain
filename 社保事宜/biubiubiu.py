import pygame
from  game_object.base_setting import setting
from  game_object.my_ship import ship
from  game_object.Guai import guai
import game_functions as gf
from pygame.sprite import Group
from  game_object.game_stats import Game_stats
from  game_object.button import Button

def run_game():

    #初始化界面并创建一个屏幕对象
    pygame.init()
    game_setting = setting()
    screen = pygame.display.set_mode((game_setting.screen_width,game_setting.screen_height),flags = pygame.FULLSCREEN|pygame.HWSURFACE)
    pygame.display.set_caption('滑稽大战')

    game_clock = pygame.time.Clock()

    #创建mememe及发射物组还有小怪及开始按钮
    mememe = ship(screen,game_setting)
    bullets = Group()
    xiaoguaimen =Group()
    stats = Game_stats(game_setting)
    gf.create_fleet(game_setting,screen,xiaoguaimen,mememe)
    play_button = Button(game_setting,screen,'let us go ')
    
    while True:
        # magic do not touch
        game_clock.tick(144)
        #检查并响应键盘和鼠标事件
        gf.check_event(xiaoguaimen,game_setting,screen,mememe,bullets,stats,play_button)

        #更新mememe和发射物和小怪们的状态
        if stats.game_active:
            mememe.update()
            gf.update_guai(mememe,stats,screen,game_setting,xiaoguaimen,bullets)
            gf.bullet_update(bullets,xiaoguaimen,mememe,game_setting,screen)  
            
        #每次循环都重绘屏幕
        gf.update_screen(game_setting,screen,mememe,bullets,stats,xiaoguaimen,play_button)

run_game()
