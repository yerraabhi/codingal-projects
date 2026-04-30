#Create a Pygame window with an image in it. Use white colour as background RGB (255, 255, 255). You can use any image of your choice.
import pygame

pygame.init()
screenwidth,screenheight=500,500

displaysurface=pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("Adding image and background image.")

bg=pygame.transform.scale(
    pygame.image.load("tree.jpg").convert(),
    (screenwidth,screenheight)
)

monkey=pygame.transform.scale(
    pygame.image.load("monkey.png").convert_alpha(),(200,200)
)

monkey_rect=monkey.get_rect(center=(screenwidth//2,screenheight//2))

text=pygame.font.Font(None,36).render("Hello World",True,
                                      pygame.Color("black"))

text_rect=text.get_rect(center=(screenwidth//2,screenheight//2+110))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        displaysurface.blit(bg, (0, 0))
        displaysurface.blit(monkey, monkey_rect)
        displaysurface.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    game_loop()