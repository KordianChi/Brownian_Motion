import pygame
from pygame.locals import *
from random import uniform, gauss
from math import pi, cos, sin

pygame.init()

window = pygame.display.set_mode((600, 600))

clock = pygame.time.Clock()

player_rect_1 = Rect(280, 280, 5, 5)
player_rect_2 = Rect(280, 280, 5, 5)
player_rect_3 = Rect(280, 280, 5, 5)
player_rect_4 = Rect(280, 280, 5, 5)
player_rect_5 = Rect(280, 280, 5, 5)
player_rect_6 = Rect(280, 280, 5, 5)


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(10)

    actual_direction_1 = uniform(0, 2 * pi)
    actual_distance_1 = gauss(10, 5)

    actual_direction_2 = uniform(0, 2 * pi)
    actual_distance_2 = gauss(10, 5)

    actual_direction_3 = uniform(0, 2 * pi)
    actual_distance_3 = gauss(10, 5)

    actual_direction_4 = uniform(0, 2 * pi)
    actual_distance_4 = gauss(10, 5)

    actual_direction_5 = uniform(0, 2 * pi)
    actual_distance_5 = gauss(10, 5)

    actual_direction_6 = uniform(0, 2 * pi)
    actual_distance_6 = gauss(10, 5)

    player_rect_1.left += actual_distance_1 * cos(actual_direction_1)
    player_rect_1.top += actual_distance_1 * sin(actual_direction_1)

    player_rect_2.left += actual_distance_2 * cos(actual_direction_2)
    player_rect_2.top += actual_distance_2 * sin(actual_direction_2)

    player_rect_3.left += actual_distance_3 * cos(actual_direction_3)
    player_rect_3.top += actual_distance_3 * sin(actual_direction_3)

    player_rect_4.left += actual_distance_3 * cos(actual_direction_4)
    player_rect_4.top += actual_distance_3 * sin(actual_direction_4)

    player_rect_5.left += actual_distance_3 * cos(actual_direction_5)
    player_rect_5.top += actual_distance_3 * sin(actual_direction_5)

    player_rect_6.left += actual_distance_3 * cos(actual_direction_6)
    player_rect_6.top += actual_distance_3 * sin(actual_direction_6)

    if player_rect_1.left < 20:
        player_rect_1.left = 300
        player_rect_1.top = 300
    if player_rect_1.right > 580:
        player_rect_1.left = 300
        player_rect_1.top = 300
    if player_rect_1.top < 20:
        player_rect_1.left = 300
        player_rect_1.top = 300
    if player_rect_1.bottom > 580:
        player_rect_1.left = 300
        player_rect_1.top = 300

    if player_rect_2.left < 20:
        player_rect_2.left = 300
        player_rect_2.top = 300
    if player_rect_2.right > 580:
        player_rect_2.left = 300
        player_rect_2.top = 300
    if player_rect_2.top < 20:
        player_rect_2.left = 300
        player_rect_2.top = 300
    if player_rect_2.bottom > 580:
        player_rect_2.left = 300
        player_rect_2.top = 300

    if player_rect_3.left < 20:
        player_rect_3.left = 300
        player_rect_3.top = 300
    if player_rect_3.right > 580:
        player_rect_3.left = 300
        player_rect_3.top = 300
    if player_rect_3.top < 20:
        player_rect_3.left = 300
        player_rect_3.top = 300
    if player_rect_3.bottom > 580:
        player_rect_3.left = 300
        player_rect_3.top = 300

    if player_rect_4.left < 20:
        player_rect_4.left = 300
        player_rect_4.top = 300
    if player_rect_4.right > 580:
        player_rect_4.left = 300
        player_rect_4.top = 300
    if player_rect_4.top < 20:
        player_rect_4.left = 300
        player_rect_4.top = 300
    if player_rect_4.bottom > 580:
        player_rect_4.left = 300
        player_rect_4.top = 300

    if player_rect_5.left < 20:
        player_rect_5.left = 300
        player_rect_5.top = 300
    if player_rect_5.right > 580:
        player_rect_5.left = 300
        player_rect_5.top = 300
    if player_rect_5.top < 20:
        player_rect_5.left = 300
        player_rect_5.top = 300
    if player_rect_5.bottom > 580:
        player_rect_5.left = 300
        player_rect_5.top = 300

    if player_rect_6.left < 20:
        player_rect_6.left = 300
        player_rect_6.top = 300
    if player_rect_6.right > 580:
        player_rect_6.left = 300
        player_rect_6.top = 300
    if player_rect_6.top < 20:
        player_rect_6.left = 300
        player_rect_6.top = 300
    if player_rect_6.bottom > 580:
        player_rect_6.left = 300
        player_rect_6.top = 300

    pygame.draw.rect(window, (255, 255, 255), player_rect_1)
    pygame.draw.circle(surface=window, color=(255, 0, 0), center=(player_rect_1.left + 5, player_rect_1.top + 5),
                       radius=10)

    pygame.draw.rect(window, (255, 255, 255), player_rect_2)
    pygame.draw.circle(surface=window, color=(0, 255, 0), center=(player_rect_2.left + 5, player_rect_2.top + 5),
                       radius=10)

    pygame.draw.rect(window, (255, 255, 255), player_rect_3)
    pygame.draw.circle(surface=window, color=(0, 0, 255), center=(player_rect_3.left + 5, player_rect_3.top + 5),
                       radius=10)

    pygame.draw.rect(window, (255, 255, 255), player_rect_4)
    pygame.draw.circle(surface=window, color=(0, 255, 255), center=(player_rect_4.left + 5, player_rect_4.top + 5),
                       radius=10)

    pygame.draw.rect(window, (255, 255, 255), player_rect_5)
    pygame.draw.circle(surface=window, color=(255, 0, 255), center=(player_rect_5.left + 5, player_rect_5.top + 5),
                       radius=10)

    pygame.draw.rect(window, (255, 255, 255), player_rect_6)
    pygame.draw.circle(surface=window, color=(255, 255, 0), center=(player_rect_6.left + 5, player_rect_6.top + 5),
                       radius=10)

    pygame.display.update()

    window.fill((255, 255, 255))
pygame.quit()