import pygame, sys
from pygame.locals import *

pygame.init() # pygame 초기화

def a():
	global gameStart
	gameStart = False
	stick.centerx =width
stick = pygame.Rect(340, 470, 120, 20)

ball = pygame. Rect(240 ,240, 20, 20)
vel = [-1, 1]
#게임 화면 크기 설정
width = 800 # 화면 크기 (가로, 세로 => 너비, 높이)를 변수화 시킨 것. 너비.
height = 500 # 높이
screen = pygame.display.set_mode((width, height))

stick = pygame.Rect(340, 470, 120, 20)# Rect 객체 선언
# pygame.Rect() -> Rect객체를 선언하는 코드.
# pygame.Rect(x좌표, y좌표, 너비, 높이)

vel = [-1, -1] # 공의 속도를 설정하는 코드.
# 리스트로 만든 이유? 2개의 값을 한 변수로 관리하기 위함.
# 대각선 움직임 -> x 와 y를 동시에 움직여야 함.

#목표물
brickList = []
x = 20
y = 10

gameStart = False
#목표물들을 생성하는 코드
for i in range(5):
	for j in range(9):
		brick = pygame.Rect(x, y, 80, 30)
		brickList.append(brick)
		x += 85
	x = 20
	y += 35

""" 1줄당 4개, 총 3줄 (12개)의 벽돌을 그리는 코드
x=10
y=10
for i in range(3):
	for j in range(4):
		brick = pygame.Rect(x,y,30,10)
		brickList.append(brick)
		x += 45
	x=10
	y+=20
"""
ball = pygame.Rect(390, 240, 20, 20)
while True:
	#창닫기 눌렀을떄 전채 코드 중지하는 코드
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN and event.key == K_SPACE:
			bullent.type == KEYDOWN and (r1)
			gameStart = True

	if gameStart:
		# 밑 막대기의 움직임(좌우)
		keyInput = pygame.key.get_pressed()
		if keyInput[K_LEFT] and stick.left >= 0:
			stick.left -= 1
		elif keyInput[K_RIGHT] and stick.right <= width:
			stick.right += 1
		ball.x += vel[0]
		ball.y += vel[1]

	if stick.colliderect(ball):
		vel[1] *= -1

	for brick in brickList:
		if brick.colliderect(ball):
			vel[1] *= -1
			brickList.remove(brick)
	#공의 튕김의 각도를 설정해주는 코드
	screen.fill((0, 0, 0))
	for brick in brickList:
		pygame.draw.rect(screen, (0,0,255), brick)
	pygame.draw.rect(screen, (255, 100, 0), ball)

	if ball.left <= 0 or ball.right >= width:
		vel[0] *= -1

	if ball.top <= 0 or ball.bottom > height:
		vel[1] *= -1

    #공과 막대기의 충돌
    if ball.colliderect(stick):
        vel *= -1 = stick.top

    screen.fill((0, 0, 0))
    for brick in brickList
        pygame.drow.rect(screen, (0, 0, 255), brick)
    #공과 펵돌의 충돌
    for brick in brickList
        if ball.colliderect(brick):
            brickList.remove(brick)
            vel[1] *= -1
	pygame.draw.rect(screen, (255, 255, 255), stick)
    pygame.draw.rect(screen, (255, 100, 0), ball)
	pygame.display.update()


