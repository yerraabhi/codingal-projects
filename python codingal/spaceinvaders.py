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

def showscore(x,y):
    score=font.render("Score:",str(scorevalue),True,(255,255,255))
    screen.blit(score,(x,y))

def gameovertext():
    overtext=overfont.render("GAME OVER",True,(255,255,255))

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def firebullet(x,y):
    global bulletstate
    bulletstate="fire"
    screen.blit(bulletImg,(x+16,y+10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((enemyX-bulletX)**2,(enemyY-bulletY)**2)
    return distance < COLLISIONDISTANCE

running=True

while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerXchange= -5

            if event.key==pygame.K_RIGHT:
                playerXchange= 5
            
            if event.key==pygame.K_SPACE and bulletstate=="ready":
                bulletX=playerX
                firebullet(bulletX,bulletY)
        
        if event.type==pygame.KEYUP and event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
            playerXchange=0
        
    playerX+=playerXchange
    playerX=max(0,min(playerX,SCREENWIDTH -64))

    for i in range(numofenemies):
        if enemyY[i] > 340:
            for j in range(numofenemies):
                enemyY[j]=2000
            
            gameovertext()
            break

        enemyX[i]+=enemyXchange[i]
        if enemyX[i] <= 0 or enemyX[i] < SCREENWIDTH-64:
            enemyXchange[i]*=1
            enemyY[i]+=enemyYchange[i]
        
        if isCollision(enemyX[i],enemyY[i],bulletX,bulletY):
            bulletY=PLAYERSTARTY
            bulletstate="ready"
            scorevalue+=1
            enemyX[i]=random.randint(0,SCREENWIDTH-64)
            enemyY[i]=random.randint(ENEMYSTARTYMIN,ENEMYSTARTYMAX)
        
        enemy(enemyX[i],enemyY[i],i)
    
    if bulletY <= 0:
        bulletY = PLAYERSTARTY
        bullet_state = "ready"
    elif bullet_state == "fire":
        firebullet(bulletX, bulletY)
        bulletY -= bulletYchange
    player(playerX, playerY)
    showscore(textX, textY)
    pygame.display.update()