import pygame
import os
from copy import copy

W, H = 800, 600
black = (0, 0, 0)
white = (255, 255, 255)
green = (124,252,0)
col_spd = 1
def_col = [[120, 120, 240]]
col_dir = [[-1, 1, 1]]
texts = ["SPACE INVADERS"]
button = 0
minimum = 0
maximum = 255

def draw_text(screen, text, size, col, x, y):
    font = pygame.font.SysFont('climate crisis',size)
    text_surface = font.render(text, True, col)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def col_change(col, dir):
    for i in range(3):
        col[i] += col_spd * dir[i]
        if col[i] >= maximum or col[i] <= minimum:
            dir[i] *= -1

def surface(screen, col, dir, text, size, x, y):
    for i in range(len(col)):
        draw_text(screen, text[i], size, col[i], x, y + i*50)
        col_change(col[i], dir[i])

def line_length(center, surface):
    x1, y1 = center
    x2, y2 = surface
    length = (((x2-x1)**2)+((y2-y1)**2))**(1/2)
    return length

def bullets(screen, color, bullet_start, bullet_end, width):
    startY = bullet_start[1]
    i = 0
    while i < 100:
        if startY > 500:
            pygame.draw.line(screen, green, bullet_start, bullet_end, 8)
            i += 1

def play():
    pygame.init()
    display = pygame.Surface((W, H))
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("space invaders")
    clock = pygame.time.Clock()
    shooter_start = [390,500]
    shooter_end = [410,500]
    alienX = 100
    alienY = -50
    default_img_size = (50,40)
    alien_vel = 1
    bullet_start = [copy(shooter_start[0]+7), copy(shooter_start[1])]
    bullet_end = [copy(shooter_end[0]-7), copy(shooter_end[1])]
    bullets = []
    hit = None
    i = 0

    state = "OPENING"
    run = True
    fontIntro = pygame.font.SysFont("arial", 30)
    score = 0
    press = False
    while run:
        print(bullets)
        delta_t = clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and state == "OPENING":
                state = "PLAY"

        screen.fill((0,0,0))

        if state == "OPENING":
            surface(screen, def_col, col_dir, texts, 80, W/2, H/5)
            fontIntro = pygame.font.SysFont("arial", 30)
            text = fontIntro.render("Click to play!", 1, (255,255,255))
            screen.blit(text, (300,300,500,500))

        elif state == "PLAY":
            text = fontIntro.render(f'Score: {score}', True, (255, 255, 255))
            screen.blit(text, (10,10,500,200))

            # movement:
            if alienX >= 650 or alienX < 100:
                alien_vel *= -1
                alienY += 20
            alienX += alien_vel

            # render alien:
            if hit != "player":
                alien = pygame.image.load(os.path.join('Space_Invaders/img', 'green+transparantbackground.png')).convert_alpha()
                alien = pygame.transform.scale(alien, default_img_size)
                screen.blit(alien, (alienX, alienY))

            # render shooter & bullet:
            shooter = pygame.draw.line(screen, white, shooter_start, shooter_end, 8)
            bullet = pygame.draw.line(screen, green, bullet_start, bullet_end, 8)

            for b in bullets:
                b[1] += -0.1 * delta_t
                if b[1] < 0:
                    bullets.remove(b)
                pygame.draw.line(screen, green, b, [b[0] + 7, b[1]+7], 8)


            # move shooter:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and shooter_start[0] >100:
                shooter_start[0] -= 1
                shooter_end[0] -= 1
                bullet_start[0] -= 1
                bullet_end[0] -= 1
            if keys[pygame.K_RIGHT] and shooter_start[0]<650:
                shooter_start[0] += 1
                shooter_end[0] += 1
                bullet_start[0] += 1
                bullet_end[0] += 1
            
            if keys[pygame.K_SPACE] and not press:
                bullets.append(copy(shooter_start))
                press = True
            if not keys[pygame.K_SPACE]: 
                press = False


            # collisions:

            alien_height = line_length([alienX + 25, alienY], [alienX + 25, alienY + 40])
            #pygame.draw.line(screen, white, [alien_startX + 25, alien_startY], [alien_startX + 25, alien_startY + 40], 5)

            for b in bullets:
                bullet_to_alien_center = line_length([alienX + 25, alienY], [b[0] + 5, b[1]])
                #pygame.draw.line(screen, white, [alien_startX + 30, alien_startY], [bullet_start_pos[0] + 5, bullet_start_pos[1]], 5)
                
                # scoring => end game:
                if bullet_to_alien_center <= alien_height and hit != "player":
                    score += 1
                    hit = "player"

            aliens_win = 0
            if alienY >= 600:
                aliens_win += 1
            if aliens_win == 3:
                display.blit(screen, (0,0))
                text = fontIntro.render(f'Score: {score}', True, (255, 255, 255))
                screen.blit(text, (100,300,500,200))
                pygame.time.delay(5000)
                state = 'OPENING'

        display.blit(screen, (0,0))
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    play()