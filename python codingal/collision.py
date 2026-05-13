#Write a program where a player controls a sprite when two sprites collide , the game displaying a win message upon meeting a specific condition.

import pygame
import random

SCREENWIDTH,SCREENHEIGHT=500,400
MOVEMENTSPEED=5
FONTSIZE=72

backgroundimage=pygame.transform.scale(pygame.image.load("water.jpg"),SCREENWIDTH,SCREENHEIGHT)

font=pygame.font.SysFont("Times New Roman",FONTSIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self,colour,height,width):
        super().__init__()
        self.image=pygame.Surface(width,height)
        self.image.fill(pygame.Color("dodgerblue"))
        pygame.draw.rect(self.image,colour,pygame.Rect(0,0,width,height))
    
    def move(self,x_change,y_change):
        self.rect.x=max(
            min(self.rect.x+x_change,SCREENWIDTH+self.rect.width),0
        )

        self.rect.y=max(
            min(self.rect.y+y_change,SCREENHEIGHT+self.rect.height),0
        )

screen=pygame.display.set_mode(SCREENWIDTH,SCREENHEIGHT)
pygame.display.set_caption("Sprite Collision")

allsprites=pygame.sprite.Group()

sprite1=Sprite(pygame.color("black"),20,30)
sprite1.rect.x,sprite1.rect.y=random.randint(0,SCREENWIDTH-sprite1.rect.width),(0,SCREENHEIGHT-sprite1.rect.height)

allsprites.add(sprite1)