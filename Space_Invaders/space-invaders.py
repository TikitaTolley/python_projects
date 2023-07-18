import pygame
import os
from copy import copy

pygame.init()

W, H = 800, 600
display = pygame.Surface((W, H))
screen = pygame.display.set_mode((W, H))
black = (0, 0, 0)
white = (255, 255, 255)
green = (124,252,0)
col_spd = 1
def_col = [[120, 120, 240]]
col_dir = [[-1, 1, 1]]
texts = ["SPACE INVADERS"]
default_img_size = (30,40)
button = 0
minimum = 0
maximum = 255

aliens = []
''' Create new Aliens '''
for a in range(10):
    alien = {'image': os.path.join('Space_Invaders/img', 'green+transparantbackground.png'),
             'pos': [100 + (50 * a), -50],
             'velocity': 1}
    aliens.append(alien)
 
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

def draw_alien(alien):
    image = alien['image']
    pos   = alien['pos']
    image = pygame.image.load(image).convert_alpha()
    image = pygame.transform.scale(image, default_img_size)
    screen.blit(image, pos)

def play():
    pygame.display.set_caption("space invaders")
    clock = pygame.time.Clock()
    shooter_start = [390,500]
    shooter_end = [410,500]
    bullet_start = [copy(shooter_start[0]+7), copy(shooter_start[1])]
    bullet_end = [copy(shooter_end[0]-7), copy(shooter_end[1])]
    bullets = []
    hit = None
    visible = False

    state = "OPENING"
    run = True
    fontIntro = pygame.font.SysFont("arial", 30)
    score = 0
    aliens_win = 0
    press = False
    print(aliens)
    while run:
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
            # render shooter:
            pygame.draw.line(screen, white, shooter_start, shooter_end, 8) #shooter

            for b in bullets:
                b[1] += -0.4 * delta_t
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
            for alien in aliens:
                # Bounce at edge
                if alien['pos'][0] >= 650 or alien['pos'][0] < 100:
                    alien['velocity'] *= -1
                    alien['pos'][1] += 50
                # Movement
                alien['pos'][0] += alien['velocity'] * 5

                # Collision Check    
                for b in bullets:
                    bullet_to_alien_center = line_length(alien['pos'], b)
                    if bullet_to_alien_center < 10:
                        score += 1
                        aliens.remove(alien)
                        bullets.remove(b)
                        break
                
                # Win check 
                if alien['pos'][1] > 600:
                    aliens_win += 1
                    aliens.remove(alien)
                
                draw_alien(alien)

            if aliens_win >= 3:
                state = 'GAME OVER'

        elif state == 'GAME OVER':
            display.blit(screen, (0,0))
            text = fontIntro.render(f'Score: {score}', True, (255, 255, 255))
            screen.blit(text, (100,300,500,200))
            text = fontIntro.render(f'Press space to continue!', True, (255, 255, 255))
            screen.blit(text, (100,400,500,300))
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                state = 'OPENING'

        display.blit(screen, (0,0))
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    play()