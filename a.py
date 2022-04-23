import sys, pygame
pygame.init()
size = width, height = 1500, 780
black = 0, 0, 0
white = 255, 255, 255
x_rigth = [1, 0]
x_left = [-1, 0]
y_up = [0, -1]
y_down = [0, 1]
speed = [1, 1]
screen = pygame.display.set_mode(size)
#mickeyclock = pygame.image.load('images\\mickeyclock.jpeg')
#mickeyclock = pygame.transform.scale(mickeyclock, (100, 100))
#mickeyclock.set_colorkey(white)
#mickeyclock_rect = mickeyclock.get_rect()
ball = pygame.image.load('images\\Intro_ball.gif')
ball = pygame.transform.scale(ball, (100, 100))
ball.set_colorkey(white)
ball_rect = ball.get_rect()
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            sys.exit()
    #pressed = pygame.key.get_pressed()
    #if pressed[pygame.K_UP]: ball_rect = ball_rect.move(y_up)
    #elif pressed[pygame.K_DOWN]: ball_rect = ball_rect.move(y_down)
    #elif pressed[pygame.K_LEFT]: ball_rect = ball_rect.move(x_left)
    #elif pressed[pygame.K_RIGHT]: ball_rect = ball_rect.move(x_rigth)
    ball_rect = ball_rect.move(speed)
    #ball_rect = ball_rect.move(y_up)
    if ball_rect.left < 0 or ball_rect.right > width:
        #x_left[0], x_rigth[0] = -x_left[0], - x_rigth[0]
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        #y_up[1], y_down[1] = -y_up[1], - y_down[1]
        speed[1] = -speed[1]
    
    #mickeyclock_rect = mickeyclock_rect.move(speed)
    #if mickeyclock_rect.left < 0 or mickeyclock_rect.right > width:
    #    speed[0] = -speed[0]
    #if mickeyclock_rect.top < 0 or mickeyclock_rect.bottom > heigth:
    #    speed[1] = -speed[1]
    screen.fill(black)
    #screen.blit(mickeyclock, mickeyclock_rect)
    screen.blit(ball, ball_rect)
    pygame.display.flip()
    clock.tick(60)
