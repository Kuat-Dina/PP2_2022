import sys, pygame

pygame.init()

size = width, height = 720, 480
screen = pygame.display.set_mode(size)
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
move = 20
radius = 25
x, y = width // 2, height // 2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            pygame.quit()
            sys.exit()
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: 
            y -= move
            if y - radius < 0: y = radius
        elif pressed[pygame.K_DOWN]: 
            y += move
            if y + radius > height: y = height - radius
        elif pressed[pygame.K_LEFT]: 
            x -= move
            if x - radius < 0: x = radius
        elif pressed[pygame.K_RIGHT]: 
            x += move
            if x + radius > width: x = width - radius

    screen.fill(white)
    ball = pygame.draw.circle(screen, red, (x, y), radius)
    pygame.display.flip()
    clock.tick(60)