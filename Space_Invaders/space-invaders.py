import pygame
import os


W, H = 800, 600
black = (0, 0, 0)
white = (255, 255, 255)
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

def play():
    pygame.init()
    display = pygame.Surface((W, H))
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("space invaders")
    clock = pygame.time.Clock()
    shooter_start_pos = [390,500]
    shooter_end_pos = [410,500]
    alien_startX = 100
    alien_startY = 100
    default_img_size = (50,40)
    alien_vel = 1
    bullet_start_pos = [shooter_start_pos[0]+7, shooter_start_pos[1]]
    bullet_end_pos = [shooter_end_pos[0]-7, shooter_end_pos[1]]

    state = "OPENING"
    run = True
    fontIntro = pygame.font.SysFont("arial", 30)
    score = 0
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

            if alien_startX >= 650 or alien_startX < 100:
                alien_vel *= -1
            alien_startX += alien_vel

            alien = pygame.image.load(os.path.join('img', 'green+transparantbackground.png')).convert_alpha()
            alien = pygame.transform.scale(alien, default_img_size)
            screen.blit(alien, (alien_startX, alien_startY))
            shooter = pygame.draw.line(screen, white, shooter_start_pos, shooter_end_pos, 8)
            bullet = pygame.draw.line(screen, (124,252,0), bullet_start_pos, bullet_end_pos, 8)
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                shooter_start_pos[0] -= 1
                shooter_end_pos[0] -= 1
                bullet_start_pos[0] -= 1
                bullet_end_pos[0] -= 1
            if keys[pygame.K_RIGHT]:
                shooter_start_pos[0] += 1
                shooter_end_pos[0] += 1
                bullet_start_pos[0] += 1
                bullet_end_pos[0] += 1
            if keys[pygame.K_SPACE]:
                bullet_start_pos[1] -= 20
                bullet_end_pos[1] -= 20

            alien_mask = pygame.mask.from_surface(alien)
            bullet_mask = pygame.mask.from_surface(bullet)
            # offset = (),()
            if alien_mask.overlap(bullet_mask): # , offset
                score += 1
                # alien disappears
                # bullet resets

        display.blit(screen, (0,0))
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    play()