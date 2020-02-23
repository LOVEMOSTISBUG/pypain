import pygame
from pygame.sprite import Sprite

class bullet(Sprite):
    """发射物体的类"""
    def __init__(self,setting,screen,ship):
        """设置发射物体对象的位置为mememe所在位置"""
        super(bullet,self).__init__()
        self.screen = screen

        #在（0，0）处创建一个矩形的发射物对象，再设置正确的位置
        self.rect = pygame.Rect(0,0,setting.bullet_width,setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #储存用小数表示的的发射物位置（y坐标上）
        self.y = float(self.rect.y)

        #发射物的颜色及速度
        self.color = setting.bullet_color
        self.speed = setting.bullet_speed

    def update(self):
        """发射物状态更新"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """绘制发射物"""
        pygame.draw.rect(self.screen,self.color,self.rect)
