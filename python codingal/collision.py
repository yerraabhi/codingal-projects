#Write a program where a player controls a sprite when two sprites collide , the game displaying a win message upon meeting a specific condition.

import pygame
import random

pygame.init()

SCREENWIDTH,SCREENHEIGHT=500,400
MOVEMENTSPEED=5
FONTSIZE=72

backgroundimage=pygame.transform.scale(pygame.image.load("water.jpg"),(SCREENWIDTH,SCREENHEIGHT))

font=pygame.font.SysFont("Times New Roman",FONTSIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self,colour,height,width):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(pygame.Color("dodgerblue"))
        pygame.draw.rect(self.image,colour,pygame.Rect(0,0,width,height))
    
    def move(self,x_change,y_change):
        self.rect.x=max(
            min(self.rect.x+x_change,SCREENWIDTH+self.rect.width),0
        )

        self.rect.y=max(
            min(self.rect.y+y_change,SCREENHEIGHT+self.rect.height),0
        )

screen=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
pygame.display.set_caption("Sprite Collision")

allsprites=pygame.sprite.Group()

sprite1=Sprite(pygame.Color("black"),20,30)
sprite1.rect.x,sprite1.rect.y=random.randint(
    0,SCREENWIDTH - sprite1.rect.width),random.randint,(
        0,SCREENHEIGHT - sprite1.rect.height)

allsprites.add(sprite1)

sprite2=Sprite(pygame.color("red"),20,30)
sprite2.rect.x,sprite2.rect.y=random.randint(0,SCREENWIDTH-sprite2.rect.width),(0,SCREENHEIGHT-sprite2.rect.height)

allsprites.add(sprite2)

running,won=True,False
clock=pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.type==pygame.K_x):
            running=False
    
    if not won:
        keys=pygame.key.get_pressed()

        x_change=(keys[pygame.K_RIGHT],keys[pygame.K_LEFT])*MOVEMENTSPEED
        y_change=(keys[pygame.K_DOWN],keys[pygame.K_UP])*MOVEMENTSPEED

        sprite1.move(x_change,y_change)

        if sprite1.rect.colliderect(sprite2.rect):
            allsprites.remove(sprite2)
            won=True
    
    screen.blit(backgroundimage(0,0))
    allsprites.draw(screen)
    
    if won:
        wintext=font.render("You win",True,pygame.Color("black"))
        screen.blit(wintext,((SCREENWIDTH-wintext.get_width())//2,(SCREENWIDTH-wintext.get_height())//2))
    pygame.display.flip()
    clock.tick(90)

pygame.quit()