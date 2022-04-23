import sys, pygame

pygame.init()

size = width, height = 400, 300
screen = pygame.display.set_mode(size)


music_1 = pygame.mixer.music.load('sounds\\Beinen.mp3')
songs = ['sounds\\Beinen.mp3', 'sounds\\Kolikpen.mp3', 'sounds\\Plastic Love.mp3', 'sounds\\Qairly tan.mp3']
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

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
        pressed = pygame.key.get_pressed()
        if event.type == pygame.QUIT or pressed[pygame.K_SPACE]:
            pygame.quit()
            sys.exit()

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

        if event.type == SONG_END:
            cnt += 1
            cnt = cnt % len(songs)
            play_right_to_music(songs, cnt)
            

               