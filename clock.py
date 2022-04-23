import pygame, sys, os, datetime

pygame.init()

size = width, height = 1500, 780
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
white = 255, 255, 255

mickeyclock = pygame.transform.scale(pygame.image.load('images\\mickeyclock.jpeg'),(width, height))
mickeyclock = pygame.transform.scale(mickeyclock, (750, 750))

sec_img = pygame.image.load('images\\left.png')
x_sec, y_sec = width / 2 + 10 , height / 2

min_img = pygame.image.load('images\\right.png')
x_min, y_min = width / 2, height / 2 + 10

def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)
    return rotated_image, new_rect

while True:
   for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            pygame.quit()
            sys.exit()
      
   screen.fill(white)
   screen.blit(mickeyclock, (370, 10))
   now = datetime.datetime.now()
   second = now.second
   screen.blit(rot_center(sec_img, -second * 6, x_sec, y_sec)[0], rot_center(sec_img, -second * 6, x_sec, y_sec)[1])
   minute = now.minute
   screen.blit(rot_center(min_img, -minute * 6, x_min, y_min)[0], rot_center(min_img, -minute * 6, x_min, y_min)[1])
   pygame.draw.circle(screen, (53,54,55), (width / 2, height / 2), 30)
   pygame.display.update()
   clock.tick(60)