import pygame
import numpy as np

W, H = 1000, 600
black = (0, 0, 0)
white = (255, 255, 255)

def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=10):
    origin = start_pos[1]
    target = end_pos[1]
    length = int(target - origin)
    dash_amount = int(length/dash_length)
    print(f'length: {length}, dash_amount: {dash_amount}')

    for index in range(0, dash_amount, 2):
        start = origin + (dash_amount *    index    * dash_length)
        print(start)
        end   = origin + (dash_amount * (index + 1) * dash_length)
    pygame.draw.line(surf, color, (500, start), (500,end), width)

def play():
    pygame.init()
    display = pygame.Surface((W, H))
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption('Ping Pong')
    clock = pygame.time.Clock()

    run = True
    player1_score = 0
    player2_score = 0
    font = pygame.font.SysFont('arial', 30)
    dist_from_top = [150,150]

    while run:
        delta_t = clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(black)

        text = font.render(f'Score: {player1_score} : {player2_score}', True, white)
        screen.blit(text, (400,10,500,200))

        draw_dashed_line(screen, white, (500, 0), (500, 600))

        player1 = pygame.draw.rect(screen, white, (910, dist_from_top[0], 10, 100))  # (left, top, width, height)
        player2 = pygame.draw.rect(screen, white, (90, dist_from_top[1], 10, 100))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            dist_from_top[0] -= 1
        if keys[pygame.K_DOWN]:
            dist_from_top[0] += 1
        
        if keys[pygame.K_w]:
            dist_from_top[1] -= 1
        if keys[pygame.K_s]:
            dist_from_top[1] += 1

        ball = pygame.draw.circle(screen, white, (500, 300), 20 )
        

        display.blit(screen, (0,0))
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    play()