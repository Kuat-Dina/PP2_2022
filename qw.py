import sys, pygame

#black = 0, 0, 0
#white = 255, 255, 255
size = width, height = 1500, 780
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

mickeyclock = pygame.image.load('images\\mickeyclock.jpeg')
mickeyclock.set_colorkey('black')
mickeyclock = pygame.transform.scale(mickeyclock, (750, 750))
x, y = width // 2 - 375, height // 2 - 375

right_hand = pygame.image.load('images\\r.png')
right_hand.set_colorkey('black')
x_r, y_r = width // 2 - 160, height // 2 - 137

left_hand = pygame.image.load('images\\l.png')
left_hand.set_colorkey('black')
x_l, y_l = width // 2 - 10, height // 2 - 145

#image = pygame.image.load('images\\l.png')
#image.set_colorkey(black)

angle = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            pygame.quit()
            sys.exit()

    right_hand_rotated = pygame.transform.rotate(right_hand, angle)
    right_hand_rotated.set_colorkey('black')

    left_hand_rotated = pygame.transform.rotate(left_hand, angle)
    left_hand_rotated.set_colorkey('black')

    angle += 1
    
    screen.fill('white')
    screen.blit(mickeyclock, (x, y))
    screen.blit(right_hand_rotated, (x_r, y_r))
    screen.blit(left_hand_rotated, (x_l, y_l))
    pygame.display.flip()
    clock.tick(60)