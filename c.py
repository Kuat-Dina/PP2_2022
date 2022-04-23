import sys, pygame
pygame.init()
screen = pygame.display.set_mode((480, 360))
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    x = pygame.mouse.get_pos
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()
