import pygame

W, H = 1000, 600
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)
brown = (255,248,220)

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
    font = pygame.font.SysFont('monospace', 30)
    dist_from_top = [150,150]
    center_ball = [W/2, H/2]
    velocityX = 2
    velocityY = 2
    last_hit = None

    counter, text = 10, '10'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    while run:

        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else 'boom!'
            if event.type == pygame.QUIT:
                run = False

        screen.fill(black)

        score = font.render(f'Score: {player1_score} : {player2_score}', True, white)
        screen.blit(score, (200,10,500,200))

        time_left = font.render(f'Time Left: {text}', True, white)
        screen.blit(time_left, (700,10,500,200))

        draw_dashed_line(screen, white, (500, 0), (500, 600))

        milli_since_last_frame = clock.tick(30)    # rate of each frame
        ticks = pygame.time.get_ticks()     # gives time program's been running in milliseconds
        seconds = ticks/1000
        #print(seconds)                
        posX, posY = center_ball

        # line connections (ball + paddle):
        player2_dist_to_ball = line_length([posX, posY], [90, dist_from_top[1] + 50])
        #pygame.draw.line(screen, grey, [posX, posY], [90, dist_from_top[1] + 50])

        player1_dist_to_ball = line_length([posX, posY], [920, dist_from_top[0] + 50])
        #pygame.draw.line(screen, grey, [posX, posY], [920, dist_from_top[0] + 50])
        
        # basic movement and bouncing:
        if posY >= 600 or posY < 0:
            velocityY *= -1
        posY += velocityY
        posX += velocityY

        # paddle-ball bouncing p1:
        if player1_dist_to_ball <= 100 and posX >= 900:
            if last_hit != "player1":
                velocityX *= -1
                velocityY *= -1
                last_hit = "player1"
        posX += velocityX
        posY += velocityY
        print(player1_dist_to_ball, posX)

        # paddle-ball bouncing p2:
        if player2_dist_to_ball <= 100 and posX <= 90:
            if last_hit != "player2":
                velocityX *= -1
                velocityY *= -1
                last_hit = "player2"
        posX += velocityX
        posY += velocityY

        # scoring:
        if posX >= 1000:
            player2_score += 1
            posX = W/2 
            posY = H/2
        posX += velocityX
        posY += velocityY

        if posX < 0:
            player1_score += 1
            posX = W/2
            posY = H/2
        posX += velocityX
        posY += velocityY

        center_ball = posX, posY
        #print(posX, posY, velocityX, velocityY)
        

        #horizontal = pygame.draw.line(screen, brown, [posX, posY], [posX + 200, posY])
        #vertical = pygame.draw.line(screen, brown, [posX, posY], [posX, posY + 200])

        player1 = pygame.draw.rect(screen, white, (910, dist_from_top[0], 10, 100))  # (left, top, width, height)
        player2 = pygame.draw.rect(screen, white, (90, dist_from_top[1], 10, 100))
        ball = pygame.draw.circle(screen, white, [posX, posY], 20)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and dist_from_top[0] > 0:
            dist_from_top[0] -= 10
        if keys[pygame.K_DOWN] and dist_from_top[0] < 500:
            dist_from_top[0] += 10
        
        if keys[pygame.K_w] and dist_from_top[1] > 0:
            dist_from_top[1] -= 10
        if keys[pygame.K_s] and dist_from_top[1] < 500:
            dist_from_top[1] += 10

        
        
        # end screen:
        if seconds >= 10:
            screen.fill(black)
            if player1_score > player2_score:
                winning1 = font.render('player 1 wins!', True, white)
                screen.blit(winning1, (500,300,500,200))
            elif player2_score > player1_score:
                winning2 = font.render('player 2 wins!', True, white)
                screen.blit(winning2, (500,300,500,200))
            else:
                winning3 = font.render('its a draw!', True, white)
                screen.blit(winning3, (500,300,500,200))
            
        
        display.blit(screen, (0,0))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    play()