import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    baseLayer = pygame.Surface((640, 480))

    clock = pygame.time.Clock()
    
    prevX = -1
    prevY = -1
    currentX = -1
    currentY = -1

    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    COLOR = RED
        
    screen.fill((0, 0, 0))

    isMouseDown = False
    font = pygame.font.SysFont("Verdana", 20)
    current_shape = "rect"
    while True:
        pressed = pygame.key.get_pressed()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
                return

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                screen.fill('black')
                baseLayer.fill("black")

            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                COLOR = RED
            if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                COLOR = GREEN
            if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                COLOR  = BLUE
            if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                COLOR = WHITE

            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                current_shape = "rect"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                current_shape = "square"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]    
                    prevX =  event.pos[0]
                    prevY =  event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baseLayer.blit(screen, (0, 0))


            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
                #coordinates = font.render(str(event.pos), True, "white")
                #screen.blit(coordinates, (10, 10))
                #baseLayer.blit(coordinates, (50, 50))
                #print(event.pos)
        
        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
            screen.blit(baseLayer, (0, 0))
            if current_shape == "rect":
                rect = calculateRect(prevX, prevY, currentX, currentY)
                pygame.draw.rect(screen, COLOR, rect, 1)
            if current_shape == "square":
                square = calculateSquare(prevX, prevY, currentX, currentY)
                pygame.draw.rect(screen, COLOR, square, 1)
            #pygame.draw.rect(screen, (255, 0, 0), square, 1)
            #print("{} {} {} {}".format(prevX, prevY, currentX, currentY))
            #print((abs(prevX - currentX)**2 + abs(prevY - currentY)**2)**0.5)
            radius = (abs((prevX - currentX) / 2) ** 2 + abs((prevY - currentY) / 2) ** 2) ** 0.5
            center = (abs((prevX + currentX) / 2), abs((prevY + currentY) / 2))
            pygame.draw.circle(screen, COLOR, center, radius, 1)
    
        pygame.display.flip()
        clock.tick(60)
        
def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1- x2), abs(y1 - y2))

def calculateSquare(x1, y1, x2, y2):
    length = max(abs(x2 - x1), abs(y2 - y1))
    return pygame.Rect(min(x1, x2), min(y1, y2), length, length)

def calculateCirle(x1, y1, x2, y2):
    pass

main()