import pygame
from pygame.sprite import Sprite
class guai(Sprite):
    """guai类"""
    def __init__(self,setting,screen):
        """设置guai类的一些基本属性"""
        super(guai,self).__init__()
        self.screen = screen
        self.setting = setting

        #guai的图像和矩形
        self.image = pygame.image.load('image/huaji.bmp').convert()
        #把背景（0，0，0）变得透明
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """绘制guai"""
        self.screen.blit(self.image,self.rect)
        
    def update(self):
        """更新guai的状态"""
        self.y += (self.setting.guai_speed) * (self.setting.fleet_direction)
        self.rect.y = self.y

