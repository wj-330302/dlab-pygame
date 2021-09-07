import pygame, sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((300,300))


while True:
    for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
        elif