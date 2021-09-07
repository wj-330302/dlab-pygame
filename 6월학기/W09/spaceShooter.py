import pygame, sys
from pygame.locals import *

pygame.init()

width = 700
height = 500
screen = pygame.display.set_mode((width, height))

#배경
bgImage = pygame.image.load('background.jpg')
spaceship ={}
bgImage =pygame.transform.scale(bgImage, (width, height))
backX = 0
backX2 = width
#주인공
img = pygame.image.load('spaeship.png')
spaceship = {'rect': pygame.Rect(0,215,70,70), 'image': pygame.transform.scale(img, (70,70))}
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	'''
	#배경 움직임
	backX -=1
	backX2 -=1
	'''
	keyInput = pygame.key.get_pressed()

	if keyInput[K_LEFT]:
		backX += 3
		backX2 += 3
		if spaceship['rect'].left.0]:
			spaceship['rect'].left -= 3

	elif keyInput[K_RIGHT]:
		backX -= 3
		backX2 -= 3
		if spaceship['rect'].rigt]:
			spaceship['rect'].rigt +=3

	if keyInput [K_UP] and spaceship['rect'] .top > 0:
		spaceship[]
	if backX < width * -1:
		backX = width

	if backX2 < width * -1:
		backX2 = width
	screen.blit(bgImage, (backX,0))
	screen.blit(bgImage, (backX2,0))

	pygame.display.update()



