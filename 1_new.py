import sys, pygame 
from datetime import datetime 
pygame.init() 
def degree(k): 
    k -= 6 
    return k 
n = 0 
k = 0 
pygame.init() 
size = width, height = 800, 800 
white = 255, 255, 255
black = 0, 0, 0
screen = pygame.display.set_mode((width, height))

mickeyclock = pygame.image.load('images\\MickeyMouse.png') 
mickeyclock = pygame.transform.scale(mickeyclock, (500, 500))

left_hand = pygame.image.load('images\\leftHand.png') 
left_hand.set_colorkey(white)

right_hand = pygame.image.load('images\\rightHand.png') 
right_hand.set_colorkey(white)
 
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            pygame.quit()
            sys.exit()
 
    screen.fill(white)    
    screen.blit(mickeyclock, (150, 180)) 
    n = degree(n) 
    pygame.time.wait(1000) 
    left_hand_rotated = pygame.transform.rotate(left_hand, degree(n)) 
    left_hand_rotated_rect = left_hand_rotated.get_rect(center = (400, 420)) 
    screen.blit(left_hand_rotated, left_hand_rotated_rect) 
 
    if n % 360 == 0: k -= 6 
 
    right_hand_rotated = pygame.transform.rotate(right_hand, k) 
    right_hand_rotated_rect = right_hand_rotated.get_rect(center = (400, 420)) 
    screen.blit(right_hand_rotated, right_hand_rotated_rect) 
    pygame.display.update() 
    pygame.time.delay(20)