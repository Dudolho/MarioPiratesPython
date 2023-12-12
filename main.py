import pygame
import sys
from settings import *
from level import Level

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_heigt))
clock = pygame.time.Clock()
level = Level(level_map, screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill('black')
    level.run()
    #framerate
    pygame.display.update()
    clock.tick(60)
    

