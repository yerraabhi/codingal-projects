#Create a Pygame window with an image in it. Use white colour as background RGB (255, 255, 255). You can use any image of your choice.
# import pygame

# pygame.init()
# screenwidth,screenheight=500,500

# displaysurface=pygame.display.set_mode((screenwidth,screenheight))
# pygame.display.set_caption("Adding image and background image.")

# bg=pygame.transform.scale(
#     pygame.image.load("tree.jpg").convert(),
#     (screenwidth,screenheight)
# )

# monkey=pygame.transform.scale(
#     pygame.image.load("monkey.png").convert_alpha(),(200,200)
# )

# monkey_rect=monkey.get_rect(center=(screenwidth//2,screenheight//2))

# text=pygame.font.Font(None,36).render("Hello World",True,
#                                       pygame.Color("black"))

# text_rect=text.get_rect(center=(screenwidth//2,screenheight//2+110))

# def game_loop():
#     clock = pygame.time.Clock()
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#         displaysurface.blit(bg, (0, 0))
#         displaysurface.blit(monkey, monkey_rect)
#         displaysurface.blit(text, text_rect)

#         pygame.display.flip()
#         clock.tick(30)

#     pygame.quit()

# if __name__ == '__main__':
#     game_loop()

# import pygame

# pygame.init()
# screen=pygame.display.set_mode((400,300))

# done=False

# while not done:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             done=True
#     pygame.draw.rect(screen,(0,125,255),pygame.Rect(150,80,90,100))

#     pygame.display.flip()

#Create a Pygame window with two circles, one solid and another hollow circle with border width 3. Keep the background colour as - white RGB(255, 255, 255) and the colour of the rectangle as green (0, 255, 0). Try changing the values of centre and radius to see how the position and size of the balls change.
# import pygame

# pygame.init()
# window=pygame.display.set_mode((400,400))

# window.fill((255,255,255))

# GREEN=(0,255,0)
# pygame.draw.circle(window,GREEN,(300,300),10)
# pygame.draw.circle(window,GREEN,(100,100),50,3)

# pygame.display.update()
# running=True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# pygame.quit()

import pygame

def main():
    pygame.init()
    screenwidth,screenheight=500,500
    screen=pygame.display.set_mode(screenwidth,screenheight)
    pygame.display.set_caption("colour changing sprite")

    colours={
        "red":pygame.Color("red"),
        "green":pygame.Color("green"),
        "blue":pygame.Color("blue"),
        "yellow":pygame.Color("yellow"),
        "white":pygame.Color("white")
    }

    currentcolour=colours["white"]

    x,y=30,30
    spritewidth,spriteheight=60,60

    clock=pygame.time.Clock()

    done=False

    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True