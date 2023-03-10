import emoji

gun_range = [[0 for x in range (5)] for y in range (5)]

def print_screen(screen):
    print()
    print("   SPACE INVADERS")
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
                print(' - ', end=' ')


print_screen(gun_range)