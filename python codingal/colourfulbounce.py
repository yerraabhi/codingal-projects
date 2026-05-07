import pygame
import random

pygame.init()

SPRITECOLOURCHANGEEVENT=pygame.USEREVENT+1
BACKGROUNDCOLOURCHANGEEVENT=pygame.USEREVENT+2

BLUE=pygame.Color("blue")
LIGHTBLUE=pygame.Color("lightblue")
DARKBLUE=pygame.Color("darkblue")

YELLOW=pygame.Color("yellow")
MAGENTA=pygame.Color("magenta")
ORANGE=pygame.Color("orange")
WHITE=pygame.Color("white")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color,height,width):
        super().__init__()

        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
    
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit=False
        
        if self.rect.left <=0 or self.rect.right>=500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit=True
        
        if self.rect.top<=0 or self.rect.bottom >=400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit=True
        
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITECOLOURCHANGEEVENT))
            pygame.event.post(pygame.event.Event(BACKGROUNDCOLOURCHANGEEVENT))
    
    def changecolour(self):
        self.image.fill(YELLOW,MAGENTA,ORANGE,WHITE)

def changebackgroundcolour():
    global bgcolour
    bgcolour=random.choice(BLUE,LIGHTBLUE,DARKBLUE)

allspriteslist=pygame.sprite.Group()

sp1=Sprite(WHITE,20,30)
sp1.rect.x=random.randint(0,480)
sp1.rect.y=random.randint(0,370)

allspriteslist.add(sp1)

screen=pygame.display.set_mode((500,400))
pygame.display.set_caption("Colourful Bounce")

bgcolour=BLUE
screen.fill(bgcolour)

exit=False

clock=pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=True
        elif event.type==SPRITECOLOURCHANGEEVENT:
            sp1.changecolour()
        elif event.type==BACKGROUNDCOLOURCHANGEEVENT:
            changebackgroundcolour()
    
    allspriteslist.update
    screen.fill(bgcolour)
    allspriteslist.draw(screen)

    pygame.display.flip()

    clock.tick(240)

pygame.quit()