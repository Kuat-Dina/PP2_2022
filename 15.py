import pygame # не мой код
pygame.init()

x, y = 25, 25

WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((450, 450))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_RIGHT:
                if x <= 405:
                    x += 20 
            if event.key == pygame.K_LEFT:
                if x >= 45:
                    x -= 20
            if event.key == pygame.K_UP:
                if y >= 45:
                    y -= 20
            if event.key == pygame.K_DOWN:
                if y <= 405:
                    y += 20   
    screen.fill(WHITE) 
    pygame.draw.circle(screen, RED, (x, y), 25)   
    pygame.display.flip()