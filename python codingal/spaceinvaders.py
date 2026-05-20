import math
import random
import pygame

SCREENWIDTH=800
SCREENHEIGHT=500
PLAYERSTARTX=380
PLAYERSTARTY=370
ENEMYSTARTYMIN=50
ENEMYSTARTYMAX=150
ENEMYSPEEDX=4
ENEMYSPEEDY=40
BULLETSPEEDY=10
COLLISIONDISTANCE=27

pygame.init()

screen=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))

background=pygame.image.load("space.png")

pygame.display.set_caption("Space Invader")

playerImg=pygame.image.load("spaceship.png")
playerX=PLAYERSTARTX
playerY=PLAYERSTARTY
playerXchange=0

enemyImg=[]
enemyX=[]
enemyY=[]
enemyXchange=[]
enemyYchange=[]
numofenemies=6

for i  in range(numofenemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0,SCREENWIDTH-64))
    enemyY.append(random.randint(ENEMYSTARTYMIN,ENEMYSTARTYMAX))
    enemyXchange.append(ENEMYSPEEDX)
    enemyYchange.append(ENEMYSPEEDY)

bulletImg=pygame.image.load("bullet.png")
bulletX=0
bulletY=PLAYERSTARTY
bulletXchange=0
bulletYchange=BULLETSPEEDY
bulletstate="ready"

scorevalue=0
font=pygame.font.Font("freesansbold.ttf",32)
textX=10
textY=10

overfont=pygame.font.Font("freesansbold.ttf",64)