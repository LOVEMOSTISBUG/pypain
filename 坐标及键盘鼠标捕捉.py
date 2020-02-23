import pygame
import sys
import pyautogui

def action_catch():
    pygame.init()
    screenWidth, screenHeight = pyautogui.size()
    screen = pygame.display.set_mode((screenWidth,screenHeight),flags = pygame.FULLSCREEN)
    pygame.display.set_caption('捕捉动作')
    bg = (0,0,0)
    font = pygame.font.Font(None,30)
    screen.fill(bg)
    position = 0
    line_height = font.get_linesize()
    
    while True:
        for event in pygame.event.get():
            screen.blit(font.render(str(event),True,(0,255,0)),(0,position))
            position += line_height
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE :
                    sys.exit()
            if position > screenHeight:
                        position = 0
                        screen.fill(bg)
                        
        pygame.display.flip()
        
action_catch()
