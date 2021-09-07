import pygame, sys
from pygame.locals import *

pygame.init()

width = 800
height = 500
screen = pygame.display.set_mode((width, height))

r1 = pygame.Rect(0, 420, 80, 80)
#목표물
rectList = []
x = 25
y = 10
for i in range(8):
	rect = pygame.Rect(50, 50, 50, 50)
	rect.append(rectList)
	x+= 100		#일정한 좌표 변화

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	# r1 움직임(좌우)
	keyInput = pygame.key.get_pressed()
	if keyInput[K_LEFT] and r1.left >= 0:
		r1.left -= 1
	elif keyInput[K_RIGHT] and r1.right <= width:
		r1.right += 1

	screen.fill((255, 255, 255))
	pygame.draw.rect(screen, (0, 0, 255), r1)
	for r in rectList:
		pygame.draw.rect(screen,(0,0,225), r)

	pygame.display.update()