import pygame

class ship() :

    def __init__(self,screen,ship_setting):
        """mememe的各类属性"""
        self.screen = screen
        
        #加载mememe的图像并获取其外接矩形
        self.ship_setting = ship_setting
        self.image = pygame.image.load('image/mememe.bmp').convert()
        #把背景（0，0，0）变得透明
        self.image.set_colorkey((0,0,0))
        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #将新mememe放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def blitme(self) :
        """屏幕上绘制mememe"""
        self.screen.blit(self.image,self.rect)

    def update(self) :
        """更新mememe位置状态"""
        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.rect.centerx += self.ship_setting.ship_speed
        if self.moving_left and self.rect.left > 0 :
            self.rect.centerx -= self.ship_setting.ship_speed
        if self.moving_up :
            self.rect.bottom -= self.ship_setting.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += self.ship_setting.ship_speed

    def center_ship(self):
            self.rect.centerx = self.screen_rect.centerx
            self.rect.bottom = self.screen_rect.bottom