import pygame

pygame.init() #init()이란 처음 상태로 초기화 시켜주는 함수

screen = pygame.display.set_mode((300, 300))

#파이게임 실행행창을 실행해주고 크기를 정해주는 코드

myColor = (255,193,158) #'MY Color' 실행창의 색상갑(튜플)정의주는 코드
screen.fill(myColor)  #'MY Color'의 갚을 불러와서 실행창에다가 불러와주는 코드
pygame.display.update()#앞에있는코트를 싷행창에다가 세로고침(업대이트)

while True:
    print()
