import pygame, sys
from pygame.locals import *

pygame.init()
#창 크기 정의 하는 변수



font = pygame.font.SysFont(pygame.font.get_default_font(), 45)
text = font.reder("Daddy's lab", True, (255,255,255))

 for i in range(5):
     for j in range(9):
         brick = pygmae. Rect(x, y, 80, 30)
#창닫기 버튼눌렀을떄 전채 종료 하느 코드
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(text,((width-text.get_width())/2, (height-text.get)))
    r1.x += vel[0]
    r1.y += vel[1]
    boll = pygame.Rect(5, 5, 5, 5)
# 공 튕겨주는 밭침대 움
    pygame.drow.rect(screen,())
    if ball.collidendect(stick):
    vel
    if r1.left <= 0 or r1.right >= width:
        vel[0] *= -1
    if r1.top <= 0 or r1.bottom >= height:
           vel[1] *= -1
    screen.fill((83, 193, 75))
    screen.blit(image1, r1)
    pygame.display.update()
if gameStart:
        keyInput = pygame.key.get_pressed()
        if keyIn




