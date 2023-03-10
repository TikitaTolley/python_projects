import emoji

gun_range = [[0 for x in range (5)] for y in range (5)]

def print_screen(screen):
    print()
    print("\033[0;35m   SPACE INVADERS")
    for row in screen[0:2][::]:
        print()
        for mark in row:
            if mark == 0:
                print(emoji.emojize(' :alien_monster:'), end=' ')
    for row in screen[2:4][::]:
        print()
        for mark in row:
            if mark == 0:
                print(' ', end=' ')
    for row in screen[-1:][::]:
        print()
        for mark in row:
            if mark == 0:
                print('\033[1;30m - ', end=' ')
    print()
    print()


print_screen(gun_range)

import pygame

W, H = 800, 600

display = pygame.Surface((W, H))
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("coloured text")
clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)

col_spd = 1

def_col = [[120, 120, 240]]
col_dir = [[-1, 1, 1]]
texts = ["SPACE INVADERS"]

minimum = 0
maximum = 255

def draw_text(text, size, col, x, y):
    font = pygame.font.SysFont('climate crisis',size)
    text_surface = font.render(text, True, col)
    text_rect = text_surface.get_rect()         # makes rectangle
    text_rect.center = (x, y)                   # draws with coordinates
    screen.blit(text_surface, text_rect)

def col_change(col, dir):
    for i in range(3):
        col[i] += col_spd * dir[i]
        if col[i] >= maximum or col[i] <= minimum:
            dir[i] *= -1

def array_func(col, dir, text, size, x, y):
    for i in range(len(col)):
        draw_text(text[i], size, col[i], x, y + i*50)
        col_change(col[i], dir[i])

pygame.init()

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0,0,0))

    array_func(def_col, col_dir, texts, 40, W/2, H/5)

    keys = pygame.key.get_pressed()
    direction = pygame.Vector2(0,0)
    if keys[pygame.K_LEFT]:
        direction.x -= 1
    
    if keys[pygame.K_RIGHT]:
            direction.x += 1

    clock.tick()

    display.blit(screen, (0,0))
    pygame.display.update()