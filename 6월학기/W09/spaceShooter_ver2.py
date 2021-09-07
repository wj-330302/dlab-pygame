import pygame, sys
from pygame.locals import *
import random
pygame.init()
#함수 정의
def drawEnemies():
	for enemy in enemies:
		enemy['rect'].x -= 3
		screen.blit(enemy['image'], enemy['rect'])
		if enemy['rect'].left <0:
			enemies.remove(enemy)

def loading():
	image = pygame.image.load('start.jpg')
	image = pygame.transform.scale(image, (width, height))
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN and event.key == K_SPACE:
				return

		screen.blit(image, (0,0))
		pygame.display.update()

width = 700
height = 500
screen = pygame.display.set_mode((width, height))

# 배경
bgImage = pygame.image.load('background.jpg')
bgImage = pygame.transform.scale(bgImage, (width, height))
backX = 0
backX2 = width-10

# 주인공
img = pygame.image.load('spaceship.png')
spaceship = {'rect': pygame.Rect(30, 215, 70, 70),
			 'image': pygame.transform.scale(img, (70, 70))}

# 총알
bullets = []
bulletImage = pygame.image.load('bullet1.png')
bulletImage = pygame.transform.scale(bulletImage, (20, 10))

#운석들
enemies = []
cnt = 0
imgList =[pygame.image.load('stone1.png'),
		  pygame.image.load('stone2.png')]


# 점수와 hp
score = 0
font = pygame.font.SysFont(pygame.font.get_default_font(), 40)
text = font.render(str(score), True, (255,255,255))

hpBar = pygame.Rect(10,10,200,20)
outline = pygame.Rect(10,10,200,20)

loading()

while True:
	cnt += 1
	pygame.time.delay(5)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN and event.key == K_SPACE:
			bullet = pygame.Rect(spaceship['rect'].centerx - 10,
								 spaceship['rect'].centery - 5,
								 20, 10)
			bullets.append(bullet)

	# 키보드 이벤트
	keyInput = pygame.key.get_pressed()
	if keyInput[K_RIGHT]:
		backX -= 3
		backX2 -= 3
		drawEnemies()

	if keyInput[K_UP] and spaceship['rect'].top > 0:
		spaceship['rect'].top -= 3
	elif keyInput[K_DOWN] and spaceship['rect'].bottom < height:
		spaceship['rect'].bottom += 3

	# 배경 움직임
	if backX <= width * -1:
		backX = width-10

	if cnt == 30:
		cnt = 0
		size = random.randint(5,30)
		enemy = {'rect': pygame.Rect(width, random.randint(0, height - size),size,size), 'image' : pygame.transform.scale(random.choice(imgList), (size, size))}
		enemies.append(enemy)

	if backX2 <= width * -1:
		backX2 = width-10
#hpBAR = pyg
	if backX >= 0:
		backX -= width-10
		backX2 -= width-10
	for bullet in bullets:
		for enemy in enemies:
			if bullet.colliderect(enemy['rect']):
				score += 1
				enemies.remove(enemy)
				text = font.render(str(score), True, (255, 255, 255))
	screen.blit(bgImage, (backX, 0))
	screen.blit(bgImage, (backX2, 0))
	drawEnemies()

	for bullet in bullets:
		bullet.x += 5
		screen.blit(bulletImage, bullet)
		if bullet.right >= width:
			bullets.remove(bullet)

	for enemy in enemies:
		if spaceship['rect'].colliderect(enemy['rect']):
			enemies.remove(enemy)
			hpBar.width -= 10
			if hpBar.width <= 0:
				pygame.quit()
				sys.exit()

	screen.blit(spaceship['image'], spaceship['rect'])
	screen.blit(text, ((width - text.get_width())/2, 10))


	pygame.draw.rect(screen, (255,0,0), hpBar)
	pygame.draw.rect(screen, (0, 0, 0), outline, 2)
	pygame.display.update()
