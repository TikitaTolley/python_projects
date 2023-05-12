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
        end   = origin + (dash_amount * (index + 1) * dash_length)
        print(f'start: {start}, end: {end}')
        pygame.draw.line(surf, color, (500, start), (500,end), width)

def line_length(center, surface):
    x1, y1 = center
    x2, y2 = surface
    length = (((x2-x1)**2)+((y2-y1)**2))**(1/2)
    return length

def center_of_rectangle(dist_from_left, dist_from_top):
    width_center = dist_from_left + 5           # along x-axis
    height_center = dist_from_top + 50
    center = [width_center, height_center]   # x-value, with changing y-values for each player
    return center

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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        ticks = pygame.time.get_ticks()
        print(ticks)

        screen.fill(black)

        text = font.render(f'Score: {player1_score} : {player2_score}', True, white)
        screen.blit(text, (400,10,500,200))

        #draw_dashed_line(screen, white, (500, 0), (500, 600))

        player1 = pygame.draw.rect(screen, white, (910, dist_from_top[0], 10, 100))  # (left, top, width, height)
        player2 = pygame.draw.rect(screen, white, (90, dist_from_top[1], 10, 100))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            top_1 = dist_from_top[0] - 1
        if keys[pygame.K_DOWN]:
            top_1 = dist_from_top[0] + 1
        
        if keys[pygame.K_w]:
            top_2 = dist_from_top[1] - 1
        if keys[pygame.K_s]:
            top_2 = dist_from_top[1] + 1

        ball = pygame.draw.circle(screen, white, (500, 300), 20 )

        #player_1 = center_of_rectangle(910, top_1)
        #player_2 = center_of_rectangle(90, top_2)

        #ball_radius = line_length(center_ball, [center_ball[0] + 20, center_ball[1]])

        #player_half_width = line_length()

        display.blit(screen, (0,0))
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    play()