import pygame, sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((300,300))
print(pygame.event.get())

red = 255
while True:
    for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
       elif event.type == KEYUP:
           if event.key == K_UP:
                if red <= 20:
                    red += 20
           else:
               red = 255
        elif event.key == K_DOWN:
            if red >= 20:
                red-=20
            else:
                red = 255
        elif event.key == K_DOWN:
            red == 255
       elif event.key == KEYDOWN:
           if event.key == K_ESCAPE:
               pygame.quit()
               sys.exit()

    screen.fill((red,0,0))
    pygame.display.update()


