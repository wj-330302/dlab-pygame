import pygame, sys
from pygame.locals import *

# 색상 상수
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
color = RED
width = 500
height = 500

pygame.init()
screen = pygame.display.set_mode((width, height))

# Rect 객체 생성

# 렉트 변수 이름 = pygame.Rect( X좌표, Y좌표, 너비, 높이)
r1 = pygame.Rect( 100, 100, 100, 100 )
r2 = pygame.Rect( 300, 100, 50, 100 )
r3 = pygame.Rect( 100, 300, 50, 70 )
r4 = pygame.Rect( 300, 300, 100, 100 )


while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	# 키보드 이벤트 처리
	keyInput = pygame.key.get_pressed()
	if keyInput[K_LEFT] and r1.left >= 0:
		r1.left -= 1
	elif keyInput[K_RIGHT] and r1.right <= width:
		r1.right += 1
	elif keyInput[K_UP] and r1.top >= 0:
		r1.top -= 1
	elif keyInput[K_DOWN] and r1.bottom <= height:
		r1.bottom += 1

	if r1.colliderect(r2):
		color = GREEN
	elif r1.colliderect(r3):
		color = BLUE
	elif r1.colliderect(r4):
		color = BLACK
	screen.fill(WHITE)
	# 생성한 Rect 객체 그리기
	pygame.draw.rect(screen,color, r1,3)
	pygame.draw.rect(screen, GREEN, r2)
	pygame.draw.rect(screen, BLUE, r3)
	pygame.draw.rect(screen, BLACK, r4, 3)

	pygame.display.update()
