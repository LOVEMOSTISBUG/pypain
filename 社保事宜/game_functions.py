import sys
import pygame
from game_object.Bullet import bullet
from game_object.Guai import guai
from time import sleep

def check_keydown_event(event,setting,screen,ship,bullets):
    """响应按下按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down =True
    if event.key == pygame.K_SPACE:
        fire_bullet(setting,screen,ship,bullets)
    if event.key == pygame.K_ESCAPE:
        sys.exit()


def fire_bullet(setting,screen,ship,bullets):
    """判断并发射发射物"""
    if len(bullets)<setting.bullet_limit:
        new_bullet = bullet(setting,screen,ship)
        bullets.add(new_bullet)
    
def check_keyup_event(event,ship):
    """响应松开按键"""
    if event.key == pygame.K_RIGHT:
       ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_play_button(xiaoguaimen,setting,screen,ship,bullets,stats,play_button,mouse_x,mouse_y):
    '''检查开始按钮是否按下'''
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #隐藏光标及重置游戏
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        xiaoguaimen.empty()
        bullets.empty()
        create_fleet(setting,screen,xiaoguaimen,ship)
        ship.center_ship()
        
def check_event(xiaoguaimen,setting,screen,ship,bullets,stats,play_button):
    """ 响应按键和鼠标事件"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_event(event,setting,screen,ship,bullets)
            elif event.type == pygame.KEYUP:
                check_keyup_event(event,ship)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x , mouse_y = pygame.mouse.get_pos()
                check_play_button(xiaoguaimen,setting,screen,ship,bullets,stats,play_button,mouse_x,mouse_y)
                    
def update_screen(game_setting,screen,ship,bullets,stats,guai,play_button):
    """更新屏幕"""
    #绘制背景，绘制发射物，绘制mememe,游戏停止时绘制按钮
    background = pygame.image.load('image/bbbbg.bmp')
    screen.blit(background,(0,0))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    guai.draw(screen)
    if not stats.game_active:
        play_button.draw_button()

    #让最近绘制的屏幕可见
    pygame.display.flip()

def bullet_update(bullets,xiaoguaimen,mememe,setting,screen):
    """ 更新发射物"""
    bullets.update()

    #  超出屏幕外的发射物消失在内存中
    for now_bullet in bullets.copy():
        if now_bullet.rect.bottom <= 0:
            bullets.remove(now_bullet)
    check_collsions(setting,screen,mememe,xiaoguaimen,bullets)
    
def check_collsions(setting,screen,mememe,xiaoguaimen,bullets):
    """检测碰撞"""
    #  发射物与guai们碰撞消失
    collisions = pygame.sprite.groupcollide(bullets,xiaoguaimen,True,True)
   
def ship_hit(mememe,stats,screen,setting,xiaoguaimen,bullets):
    '''检查mememe是否还活着'''
    if stats.ships_left > 0:
        stats.ships_left -= 1
        xiaoguaimen.empty()
        bullets.empty()
        create_fleet(setting,screen,xiaoguaimen,mememe)
        sleep(0.5)
    else :
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_guai_bottom(mememe,stats,screen,setting,xiaoguaimen,bullets):
    """检测guai是否到达底部"""
    screen_rect = screen.get_rect()
    for guai in xiaoguaimen.sprites():
        if guai.rect.bottom >= screen_rect.bottom:
            ship_hit(mememe,stats,screen,setting,xiaoguaimen,bullets)
            break
    
def create_fleet(setting,screen,xiaoguaimen,ship):
    """制造一行guai"""
    xiaoguai = guai(setting,screen)
    number_guai_x = get_number_guai(setting,xiaoguai.rect.width)
#    number_rows = get_number_rows(setting,ship.rect.height,xiaoguai.rect.height)
#    for row_number in range(number_rows):
    for guai_number in range(number_guai_x):
        creat_guai(setting,screen,xiaoguaimen,guai_number)
        
def get_number_guai(setting,xiaoguai_width):
    """计算每行能容纳的guai"""
    available_space_x = setting.screen_width - 2 * xiaoguai_width
    number_guai_x = int(available_space_x / (2 * xiaoguai_width))
    return number_guai_x

def creat_guai(setting,screen,xiaoguaimen,guai_number):
    """在指定位置制造guai"""
    xiaoguai = guai(setting,screen)
    xiaoguai_width = xiaoguai.rect.width
    xiaoguai.x  = xiaoguai_width + 2 * xiaoguai_width * guai_number
    xiaoguai.rect.y = xiaoguai.rect.height + 2 * xiaoguai.rect.height 
    xiaoguai.rect.x = xiaoguai.x
    xiaoguaimen.add(xiaoguai)

def update_guai(mememe,stats,screen,setting,xiaoguaimen,bullets):
    """更新guai们的状态"""
    xiaoguaimen.update()
    check_guai_bottom(mememe,stats,screen,setting,xiaoguaimen,bullets)
    if pygame.sprite.spritecollideany(mememe,xiaoguaimen):
        ship_hit(mememe,stats,screen,setting,xiaoguaimen,bullets)
    if len(xiaoguaimen)== 0 :
        bullets.empty()
        create_fleet(setting,screen,xiaoguaimen,mememe)
        
if __name__ == '__main__':
    print ('爷只是函数，运行我没用啊')
