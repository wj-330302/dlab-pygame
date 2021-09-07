import pygame,sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((500,500))

while True:
    for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
       elif event.type == MOUSEBUTTONUP:
           print(event.pos)

    screen.fill((0,0,0))
    pygame.display.update()
