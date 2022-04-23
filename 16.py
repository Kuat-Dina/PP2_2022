import pygame
pygame.init()
pygame.font.init() 
screen = pygame.display.set_mode((300, 300))

BLACK = (0, 0, 0)
pygame.mixer.music.load('sounds\\Beinen.mp3')
pygame.mixer.music.play()

myfont = pygame.font.SysFont('Comic Sans MS', 30)
text = myfont.render('Player', False, (200, 0, 0))
screen.blit(text,(110,20))
m = 0

songs = ['sounds\\Beinen.mp3', 'sounds\\Kolikpen.mp3', 'sounds\\Plastic Love.mp3', 'sounds\\Qairly tan.mp3']

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.pause()
        
            if event.key == pygame.K_s: 
                pygame.mixer.music.unpause()
        
            if event.key == pygame.K_UP or event.key == pygame.K_LEFT:
                m -= 1
                m %= 4
                previousSong = songs[m] 
                print(previousSong)   
                pygame.mixer.music.load(previousSong)
                pygame.mixer.music.play() 
                name1 = myfont.render(previousSong, False, (200, 0, 0))
                text = myfont.render('Player', False, (200, 0, 0))
                screen.fill(BLACK)
                screen.blit(text,(110,20))
                screen.blit(name1,(20,100))
        
            if event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT:
                m += 1
                m %= 4
                nextSong = songs[m]
                print(nextSong)
                pygame.mixer.music.load(nextSong)
                pygame.mixer.music.play()
                name2 = myfont.render(nextSong, False, (200, 0, 0))
                text = myfont.render('Player', False, (200, 0, 0))
                screen.fill(BLACK)
                screen.blit(text,(110,20))
                screen.blit(name2,(20,100))
    pygame.display.flip()