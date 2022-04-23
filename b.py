import sys, pygame
pygame.init()
image = pygame.image.load('images\\my_ball.png')
#a = image.get_rect(topleft = (1000, 500))
#image = pygame.transform.scale(image, (400, 400))
#image.set_colorkey((255, 255, 255))
screen = pygame.display.set_mode((1500, 780))
clock = pygame.time.Clock()
angle = 0
x = 200
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            sys.exit()
    screen.fill((0, 0, 0))
    #r_image = pygame.transform.rotate(image, angle)
    #angle += 1
    #screen.blit(r_image, (550, 190))
    x += 10
    if x > 1500: x = -400
    screen.blit(image, (x, 300))
    #screen.blit(image, a)
    pygame.display.flip()
    clock.tick(60)
