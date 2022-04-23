import sys, pygame
pygame.init()
white = 255, 255, 255
black = 0, 0, 0
right = pygame.image.load('images\\right.jpeg')
left = pygame.image.load('images\\right.jpeg')
sky = pygame.image.load('images\\sky.png')
sky = pygame.transform.scale(sky, (1500, 780))
x1, y1, x2, y2 = 200, 400, 600, 500
screen = pygame.display.set_mode((1500, 780))
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    right = pygame.transform.rotate(right, 90)
    screen.fill(black)
    x1 += 10
    y2 += 10
    if y2 > 780: y2 = -200
    if x1 > 1500: x1 = -200
    screen.blit(sky, (0, 0))
    screen.blit(right, (x1, y1))
    screen.blit(left, (x2, y2))
    pygame.display.update()
    clock.tick(60)