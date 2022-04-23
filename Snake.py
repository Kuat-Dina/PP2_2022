import pygame, sys, random, time
from pygame.math import Vector2

pygame.init()

BLOCK_SIZE     = 20
BLOCK_NUMBER   = 30
SCREEN         = pygame.display.set_mode((BLOCK_NUMBER * BLOCK_SIZE, BLOCK_NUMBER * BLOCK_SIZE))

FramePerSecond = pygame.time.Clock()
FPS            = 60

food = pygame.image.load("images\\Food.png").convert_alpha()
food = pygame.transform.scale(food, (BLOCK_SIZE, BLOCK_SIZE))
food.set_colorkey("white")
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

PAUSE = END = WIN = False
TIME, LEVEL = 150, 1
SNAKE_SPEED = round(1000 / TIME, 2)

class Timer:
    def __init__(self):
        self.start_time    = 0
        self.time_in_pause = 0
        self.elapsed_time  = 0

    def start(self):
        self.start_time = time.time()

    def pause(self):
        self.time_in_pause = self.elapsed_time
 
    def unpause(self):
        self.start_time = time.time()
        
    def current_time(self):
        self.elapsed_time = round(time.time() - self.start_time + self.time_in_pause, 2)
        game_time = font_small.render(f"time: {self.elapsed_time}", True, 'black')
        SCREEN.blit(game_time, (10, 50))

    def end(self):
        game_end_time = font_small.render(f"Seconds: {self.elapsed_time}", True, 'black')
        SCREEN.blit(game_end_time, (30, 300))

    def restart(self):
        self.__init__()
        self.start()

    def draw(self, time):
        time = font_small.render(f"time: {time}", True, 'black')
        SCREEN.blit(time, (10, 50))

class Food:
    def __init__(self):
        self.x   = random.randint(3, BLOCK_NUMBER - 1)
        self.y   = random.randint(2, BLOCK_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)

    def draw(self):
        self.food_rect = pygame.Rect(self.x * BLOCK_SIZE, self.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        SCREEN.blit(food, self.food_rect)
        #SCREEN.blit(food, (self.x * BLOCK_SIZE, self.y * BLOCK_SIZE))

    def change_location(self):
        self.__init__()

class Snake:
    def __init__(self):
        self.body = [Vector2(6, 10), Vector2(5, 10), Vector2(4, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

        self.snake_head_down  = pygame.image.load("images\\SnakeHeadDown.png").convert_alpha()
        self.snake_head_down  = pygame.transform.scale(self.snake_head_down, (BLOCK_SIZE, BLOCK_SIZE))

        self.snake_head_up    = pygame.image.load("images\\SnakeHeadUp.png").convert_alpha()
        self.snake_head_up    = pygame.transform.scale(self.snake_head_up, (BLOCK_SIZE, BLOCK_SIZE))

        self.snake_head_right = pygame.image.load("images\\SnakeHeadRight.png").convert_alpha()
        self.snake_head_right = pygame.transform.scale(self.snake_head_right, (BLOCK_SIZE, BLOCK_SIZE))

        self.snake_head_left  = pygame.image.load("images\\SnakeHeadLeft.png").convert_alpha()
        self.snake_head_left  = pygame.transform.scale(self.snake_head_left, (BLOCK_SIZE, BLOCK_SIZE))

    def draw(self):
        block_head_rect = pygame.Rect(self.body[0].x * BLOCK_SIZE, self.body[0].y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        
        if self.direction == Vector2(1, 0) or self.direction == Vector2(0, 0):
            SCREEN.blit(self.snake_head_right, block_head_rect)
        if self.direction == Vector2(0, 1):
            SCREEN.blit(self.snake_head_down, block_head_rect)
        if self.direction == Vector2(-1, 0):
            SCREEN.blit(self.snake_head_left, block_head_rect)
        if self.direction == Vector2(0, -1):
            SCREEN.blit(self.snake_head_up, block_head_rect)
        
        for block in self.body[1:]:
            block_rect = pygame.Rect(block.x * BLOCK_SIZE, block.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (0, 102, 0), block_rect)

    #проблема в движении змеи, доработай
    def move(self):
        if self.new_block:
            body_copy = self.body[:]
            self.new_block = False
        else:    
            body_copy = self.body[:-1]

        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def upgrade(self):
        global TIME, LEVEL, SNAKE_SPEED
        score = len(self.body) - 3
        if score % 3 == 0 and score > 0 : 
            TIME -= 10
            SNAKE_SPEED = round(1000 / TIME, 2)
            LEVEL += 1

    def play_sound(self):
        pygame.mixer.Sound("sounds\\yeahoo.mp3").play()

    def add_block(self):
        self.new_block = True

    def restart(self):
        self.body = [Vector2(6, 10), Vector2(5, 10), Vector2(4, 10)]
        self.direction = Vector2(1, 0)

class Main:
    def __init__(self):
        self.snake = Snake()
        self.food  = Food()
        self.timer = Timer()

    def update(self):
        self.snake.move()
        self.check_collision()
        self.check_fail()
        self.check_finish()

    def draw(self):
        self.food.draw()
        self.snake.draw()
        self.draw_score()
        self.draw_level()
        self.draw_speed()
        if not PAUSE: self.timer.current_time()
        else: main.timer.draw(self.timer.time_in_pause)
        
    def draw_score(self):
        score_text = len(self.snake.body) - 3
        score      = font_small.render(f"x{score_text}", True, "black")
        score_rect = score.get_rect(topleft = (BLOCK_SIZE + 10, 0))
        food_rect  = food.get_rect(topleft = (5, 5))
        SCREEN.blit(food, food_rect)
        SCREEN.blit(score, score_rect)

    def draw_level(self):
        level      = font_small.render(f"level: {LEVEL}", True, "black")
        level_rect = level.get_rect(topleft = (5, 100))
        SCREEN.blit(level, level_rect)

    def draw_speed(self):
        speed      = font_small.render(f"snake speed: {SNAKE_SPEED} b/s", True, "black")
        speed_rect = speed.get_rect(topleft = (5, 80))
        SCREEN.blit(speed, speed_rect)
        
    def check_collision(self):
        if self.food.pos == self.snake.body[0]:
            self.snake.play_sound()
            self.snake.add_block()
            self.snake.upgrade()
            self.food.change_location()

        for block in self.snake.body[1:]:
            if block == self.food.pos:
                self.food.change_location()
    
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < BLOCK_NUMBER or not 0 <= self.snake.body[0].y < BLOCK_NUMBER:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        global END
        END = True
        game_over      = font.render("Game Over", True, "black")
        game_over_rect = game_over.get_rect(center = ((BLOCK_NUMBER * BLOCK_SIZE) / 2, ((BLOCK_NUMBER - 10) * BLOCK_SIZE) / 2))
        SCREEN.fill("red")
        SCREEN.blit(game_over, game_over_rect) 
        self.draw_level()
        main.timer.end()
        
        pygame.display.update()

    def check_finish(self):
        if LEVEL > 12: self.win()

    def win(self):
        global WIN
        SCREEN.fill("white")
        font = pygame.font.SysFont("Verdana", 30)
        text = font.render("Congratulations! You win", True, "black")
        pygame.mixer.Sound("sounds\\WinMarioSound.wav").play(0)
        text_rect = text.get_rect(center = ((BLOCK_NUMBER * BLOCK_SIZE) / 2, ((BLOCK_NUMBER - 10) * BLOCK_SIZE) / 2))
        SCREEN.blit(text, text_rect)
        pygame.display.update()
        WIN = True
        
#150,140,130,120,110,100,90,80,70,60,50,40,30,20,10
#1  ,2  ,3  ,4  ,5  ,6  ,7 ,8 ,9 ,10,11,12,13,14,15
#150,135,120,105,90 ,75 ,60,45,30,15

main = Main()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, TIME)

main.timer.start()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE and not PAUSE and not WIN and not END:
            main.update()
            pygame.time.set_timer(SCREEN_UPDATE, TIME)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            main.snake.restart()
            main.food.change_location()
            main.timer.restart()
            END = PAUSE = WIN = False
            TIME, LEVEL = 150, 1
            SNAKE_SPEED = round(1000 / TIME, 2)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            if PAUSE:
                main.timer.unpause()
                PAUSE = False
            else:
                main.timer.pause()
                PAUSE = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if main.snake.direction.y != 1:
                main.snake.direction = Vector2(0, -1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if main.snake.direction.y != -1:
                main.snake.direction = Vector2(0, 1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if main.snake.direction.x != 1:
                main.snake.direction = Vector2(-1, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if main.snake.direction.x != -1:
                main.snake.direction = Vector2(1, 0)
    
    if END or PAUSE or WIN: pass
    else:
        SCREEN.fill((178, 255, 102))
        main.draw()
        pygame.display.update()
        FramePerSecond.tick(FPS)