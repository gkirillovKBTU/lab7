import pygame
import os

pygame.init()

WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving ball ")
clock = pygame.time.Clock()


def center_on_screen(radius, offset=[0, 0]):
    screen_center = screen.get_rect().center
    coordinates_centered = (screen_center[0] - radius + offset[0],
                            screen_center[1] - radius + offset[1])
    return coordinates_centered


class MovingBall(pygame.sprite.Sprite):

    def __init__(self, radius, x, y, step=5):
        super().__init__()
        self.radius = radius
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, 'red', (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT]: self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed
        if keys[pygame.K_UP]: self.rect.y -= self.speed
        if keys[pygame.K_DOWN]: self.rect.y += self.speed
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))


running = True
playing_ball = MovingBall(25, *screen.get_rect().center, 100)

while running:
    screen.fill('white')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    playing_ball.update(keys)

    screen.blit(playing_ball.image, playing_ball.rect)

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
