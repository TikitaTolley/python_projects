import pygame

W, H = 1000, 600
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)

def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=10):
    origin = start_pos[1]
    target = end_pos[1]
    length = int(target - origin)
    dash_amount = int(length/dash_length)
    for index in range(0, dash_amount, 2):
        start = origin + (dash_amount *    index)
        end   = origin + (dash_amount * (index + 1))
        pygame.draw.line(surf, color, (500, start), (500,end), width)

def line_length(center, surface):
    x1, y1 = center
    x2, y2 = surface
    length = (((x2-x1)**2)+((y2-y1)**2))**(1/2)
    return length

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
    center_ball = [W/2, H/2]

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(black)

        text = font.render(f'Score: {player1_score} : {player2_score}', True, white)
        screen.blit(text, (200,10,500,200))

        draw_dashed_line(screen, white, (500, 0), (500, 600))

        player1 = pygame.draw.rect(screen, white, (910, dist_from_top[0], 10, 100))  # (left, top, width, height)
        player2 = pygame.draw.rect(screen, white, (90, dist_from_top[1], 10, 100))
        ball = pygame.draw.circle(screen, white, center_ball, 20)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            dist_from_top[0] -= 1
        if keys[pygame.K_DOWN]:
            dist_from_top[0] += 1
        
        if keys[pygame.K_w]:
            dist_from_top[1] -= 1
        if keys[pygame.K_s]:
            dist_from_top[1] += 1

        #ball_radius = line_length(center_ball, [center_ball[0] + 20, center_ball[1]])
        width_to_diag = range(20, int(((2600)**(1/2))+10))

        player2_dist_to_ball = line_length(center_ball, [90, dist_from_top[1] + 50])
        pygame.draw.line(screen, grey, center_ball, [90, dist_from_top[1] + 50])

        player1_dist_to_ball = line_length(center_ball, [920, dist_from_top[0] + 50])
        pygame.draw.line(screen, grey, center_ball, [920, dist_from_top[0] + 50])

        # ball movement and collisons:
        i = 10
        while i > 0:
            i - 1
            print(i)
            if center_ball[1] >= 600 or center_ball[1] <= 0:    # hitting sides, bottom - top
                #center_ball[0] += 1
                center_ball[1] -= 1

            if player1_dist_to_ball in width_to_diag:
                print('player 1 hits!')
            if player2_dist_to_ball in width_to_diag:
                print('player 2 hits!')            
            
            # scoring:
            if center_ball[0] <= 0:   # hitting sides, left
                player1_score +=1
                center_ball = [W/2, H/2]    # reset
            if center_ball[0] >= 1000:  # hitting sides, right
                player2_score += 1
                center_ball = [W/2, H/2]    # reset
            
            center_ball[0] -= 1
            #center_ball[1] += 1


        if i == 0:
            screen.fill(black)
            if player1_score > player2_score:
                winning1 = font.render('player 1 wins!', True, white)
                screen.blit(winning1, (500,300,500,200))
            if player2_score > player1_score:
                winning2 = font.render('player 2 wins!', True, white)
                screen.blit(winning2, (500,300,500,200))
            if player1_score == player2_score:
                winning3 = font.render('its a draw!', True, white)
                screen.blit(winning3, (500,300,500,200))

        
        display.blit(screen, (0,0))
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    play()