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

def draw_text(text, size, col, x, y):
    font = pygame.font.get_default_font()
    font = pygame.font.Font(font,size)
    text_surface = font.render(text, True, col)
    text_rect = text_surface.get_rect()         # makes rectangle
    text_rect.center = (x, y)                   # draws with coordinates
    screen.blit(text_surface, text_rect)




pygame.init()

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_text("preview text", 40, white, W / 2, H / 2)

    clock.tick()

    display.blit(screen, (0,0))
    pygame.display.update()