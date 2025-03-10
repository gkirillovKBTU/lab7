# Example file showing a basic pg "game loop"
import pygame as pg
import os
import time
import datetime

# pygame setup
pg.init()

main_dir = os.path.split(os.path.abspath(__file__))[0]
size = (1280, 720)
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
running = True


def scale(image, scalar_scale=0.5):
    image_size = image.get_size()
    image_size = (image_size[0] * scalar_scale, image_size[1] * scalar_scale)
    image = pg.transform.scale(image, image_size)
    return image, image_size


def center_on_screen(image, offset=[0, 0]):
    image_size = image.get_size()
    screen_center = screen.get_rect().center
    coordinates_centered = (screen_center[0] - image_size[0]//2 + offset[0],
                            screen_center[1] - image_size[1]//2 + offset[1])
    return coordinates_centered


def blit_rotate_pivot(surf, image, pivot, angle):
    image_pivot = pg.math.Vector2(image.get_width() / 2, image.get_height())
    image_center = pg.math.Vector2(image.get_rect().center)
    offset = image_pivot - image_center  # This is how far the pivot is from the center

    rotated_offset = offset.rotate(-angle)
    print(rotated_offset)

    # pivot = pg.math.Vector2(pivot)  # Convert pivot to a vector
    new_center = pivot - rotated_offset
    # print(pivot, new_center)

    rotated_image = pg.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=new_center)

    surf.blit(rotated_image, new_rect.topleft)

bottom_x, bottom_y = 100, 100


def rot_center(image, angle, x, y):
    rotated_image = pg.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=(x, y))
    return rotated_image, new_rect


def rotate_point(point, center, angle):
    """Rotates a point around a center by angle degrees."""
    print(point - center)
    rotated = (point - center).rotate(angle) + center
    return rotated

# def test_rotate(image, angle):
#     image_size = image.get_size()
#     bottom = image_size.height



main_image = pg.image.load("mickeyclock.jpeg")
main_image = main_image.convert()
main_image, main_image_size = scale(main_image)

short_hand = pg.image.load("shorthand.png")
short_hand, short_hand_size = scale(short_hand, 0.7)
short_hand_center = center_on_screen(short_hand, offset=[5, -50])

long_hand = pg.image.load("longhand.png")
long_hand, long_hand_size = scale(long_hand, 0.7)
long_hand_center = center_on_screen(long_hand, offset=[20, -10])

long_center_point = pg.math.Vector2(center_on_screen(long_hand, offset=[0, long_hand_size[1] // 2]))


while running:
    # time.sleep(1)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill('white')

    screen.blit(main_image, center_on_screen(main_image))

    local_time = time.localtime()
    mins_angle = local_time.tm_min * 6
    secs_angle = local_time.tm_sec * 6

    blit_rotate_pivot(screen, long_hand,  screen.get_rect().center, -secs_angle)
    blit_rotate_pivot(screen, short_hand, screen.get_rect().center, -mins_angle)

    clock.tick(60)

    pg.display.flip()


pg.quit()
