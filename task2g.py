import pygame
import os

pygame.init()
pygame.mixer.init()

MUSIC_FOLDER = "music"
tracks = [os.path.join(MUSIC_FOLDER, file) for file in os.listdir(MUSIC_FOLDER) if file.endswith(".mp3")]
current_track_index = 0
if not tracks:
    pygame.quit()
    exit()


def play_track(index):
    global message
    pygame.mixer.music.load(tracks[index])
    pygame.mixer.music.play()
    message = "Now playing:" + os.path.basename(tracks[index])


def stop_track():
    global message
    pygame.mixer.music.stop()
    message = "Playback stopped."


def next_track():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(tracks)
    play_track(current_track_index)


def previous_track():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(tracks)
    play_track(current_track_index)


screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont("Arial", 25)

running = True
while running:
    screen.fill((30, 30, 30))
    message = 'p - play n - new track  b - prev track s - stop track'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_track(current_track_index)
            elif event.key == pygame.K_s:
                stop_track()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                previous_track()

    text_surface = font.render(message, True, 'white')
    screen.blit(text_surface, (0, 100))
    pygame.display.flip()

pygame.quit()
