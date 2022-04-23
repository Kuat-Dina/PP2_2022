import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    prevX = 0
    prevY = 0
    
    screen.fill((0, 0, 0))

    isMouseDown = False

    while True:
        
        pressed = pygame.key.get_pressed()

        currentX = prevX
        currentY = prevY
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
                return

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                screen.fill('black')

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: 
                    isMouseDown = False

            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                currentX =  event.pos[0]
                currentY =  event.pos[1]
                
        
        if isMouseDown:
            pygame.draw.line(screen, (200, 200,200), (prevX, prevY), (currentX, currentY))

        prevX = currentX
        prevY = currentY
        
        pygame.display.flip()
        clock.tick(60)

main()