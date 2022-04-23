import pygame, sys
from pygame.math import Vector2
pygame.init()
SIZE = WIDHT, HEIGHT = 720, 480
SCREEN = pygame.display.set_mode(SIZE)
dvd = pygame.image.load("images\\DVD.png").convert_alpha()
dvd.set_colorkey((255, 255, 255))
dvd = pygame.transform.scale(dvd, (200, 100))
dvd_rect = dvd.get_rect()
SPEED = Vector2(1, 1)
clock = pygame.time.Clock()
color = "white"
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            pygame.quit()
            sys.exit()
    SCREEN.fill(color)
    dvd_rect.move_ip(SPEED)
    if dvd_rect.bottom >= HEIGHT:
        SPEED.y = -1
        color = "red"
    if dvd_rect.right >= WIDHT: 
        SPEED.x = -1
        color = "blue"
    if dvd_rect.top <= 0: 
        SPEED.y = 1
        color = "white"
    if dvd_rect.left <= 0: 
        SPEED.x = 1
        color = "green"
    SCREEN.blit(dvd, dvd_rect)
    pygame.display.update()
    clock.tick(60)