import sys, pygame

pygame.init()

size = width, height = 400, 300
screen = pygame.display.set_mode((width, height))
black = 0, 0, 0
white = 255, 255, 255
clock = pygame.time.Clock()

music_1 = pygame.mixer.music.load('sounds\\Beinen.mp3')
songs = ['sounds\\Beinen.mp3', 'sounds\\Kolikpen.mp3', 'sounds\\Plastic Love.mp3', 'sounds\\Qairly tan.mp3']

cnt = 0

def play_right_to_music(songs, pos):
    pygame.mixer.music.load(songs[pos])
    pygame.mixer.music.play(0)

def play_left_to_music(songs, pos):
    pygame.mixer.music.load(songs[pos])
    pygame.mixer.music.play(0)

OK = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            pygame.quit()
            sys.exit()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RETURN]:
            pygame.mixer.music.play()
        elif pressed[pygame.K_DOWN]:
            if OK:
                pygame.mixer.music.pause()
                OK = False
            else:
                pygame.mixer.music.unpause()
                OK = True
        elif pressed[pygame.K_RIGHT]:
            cnt += 1
            cnt = cnt % len(songs)
            play_right_to_music(songs, cnt)
        elif pressed[pygame.K_LEFT]:
            cnt -= 1
            cnt = cnt % len(songs)
            play_left_to_music(songs, cnt)
            
    screen.fill(white)
    pygame.display.flip()
    clock.tick(60)
               