import pygame
#'파이게임'을 불러온다

pygame.init()
# initialize의 줄임말로 초기화 한다는 뜻
#pygame 코드는 무족권 init()으로 시작해야한다.

screen = pygame.display.set_mode((500, 400))
# pygame 모둘 폴더 안에 display.py 파일 안에 set_mode() 함수 를 사용한다
# set_mode() 함수는 튜플 하나를 매개 변수로 받는다.
# 튜플 안에 첫번쨰 숫자는 너비, 투플안에는 두번쨰 숫자는 높이이다.
# 화면을 선언한뒤 screen이라는 뱐수에 저장해 두었다.

screen.fill((0,51,153))
# screen.fil()함수는 화면객채의 색깔을 정해준다.
# 매개변수로 튜플 하나를 밭는대 이 안에 rgb 갚이 순서대로 숫자로 주어저야 한다.
pygame.display.update()

while True:
    #코드가 바로 종료되지안토록 무한반복문을 작성한다.
    print()