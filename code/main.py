import pygame
from pygame.locals import *

#Game Variables
BOARD_WIDTH=800
BOARD_HEIGHT=800
FPS=60
RUNNING=True

#0=White and 1 =black
L=[[0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0]]

white_s=pygame.image.load('../assets/img/white_sqr.png')
black_s=pygame.image.load('../assets/img/brown_sqr.png')
white_s=pygame.transform.scale(white_s,(100,100))
black_s=pygame.transform.scale(black_s,(100,100))

screen=pygame.display.set_mode((BOARD_WIDTH,BOARD_HEIGHT))
clock=pygame.time.Clock()

def create_board():
    for i,x in enumerate(L):
        for j,y in enumerate(x):
            if y==0:
                screen.blit(white_s,(i*100,j*100))
            elif y==1:
                screen.blit(black_s,(i*100,j*100))
                



while RUNNING:

    clock.tick(FPS)
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit()
            RUNNING=False
    
    create_board()
    pygame.display.update()