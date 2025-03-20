import pygame
import os
pygame.init()

screen = pygame.display.set_mode((800, 600))
running = True
clock = pygame.time.Clock()

songs = [
    'LEEONA_-_LEEONA_-_Do_I.mp3',
    'Alone_-_Color_Out.mp3'
]
current_song_index = 0

def play_song(index):
    if os.path.exists(songs[index]):
        pygame.mixer.music.load(songs[index])
        pygame.mixer.music.play()
    else:
        print(f"Error: {songs[index]} not found.")

def stop_music():
    pygame.mixer.music.stop()

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)
    play_song(current_song_index)

def previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs)
    play_song(current_song_index)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_song(current_song_index) 
            elif event.key == pygame.K_s:
                stop_music()  
            elif event.key == pygame.K_n:
                next_song()
            elif event.key == pygame.K_b:
                previous_song()  

    screen.fill('white')
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
