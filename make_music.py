import pygame
import sys
import time

def start():
    pygame.init()
    screen = pygame.display.set_mode((600,200))
    pygame.display.set_caption('为什么要用自己演奏音乐？？')
    bg = (0,0,0)
    screen.fill(bg)
    font = pygame.font.Font(None,25)
    position = 0
    screen.blit(font.render('try press 1234567?',True,(0,255,0)),(0,position))
    screen.blit(font.render('press space to kill 0.8s',True,(0,255,0)),(0,25))
    
    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        pygame.mixer.music.load('ms/1.mp3')
                        pygame.mixer.music.play(0,0)
                    if event.key == pygame.K_2:
                        pygame.mixer.music.load('ms/2.mp3')
                        pygame.mixer.music.play(0,0)
                    if event.key == pygame.K_3:
                        pygame.mixer.music.load('ms/3.mp3')
                        pygame.mixer.music.play(0,0)
                    if event.key == pygame.K_4:
                        pygame.mixer.music.load('ms/4.mp3')
                        pygame.mixer.music.play(0,0)
                    if event.key == pygame.K_5:
                        pygame.mixer.music.load('ms/5.mp3')
                        pygame.mixer.music.play(0,0)
                    if event.key == pygame.K_6:
                        pygame.mixer.music.load('ms/6.mp3')
                        pygame.mixer.music.play(0,0)
                    if event.key == pygame.K_7:
                        pygame.mixer.music.load('ms/7.mp3')
                        pygame.mixer.music.play(0,0)
                    if event.key == pygame.K_SPACE:
                        time.sleep(0.8)
        except SystemExit:
            print('good bye')
                    
                        
        pygame.display.flip()
        
start()
