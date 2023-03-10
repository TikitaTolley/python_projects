import pygame


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
    text_rect = text_surface.get_rect()         # makes rectangle
    text_rect.center = (x, y)                   # draws with coordinates
    screen.blit(text_surface, text_rect)

def col_change(col, dir):
    for i in range(3):
        col[i] += col_spd * dir[i]
        if col[i] >= maximum or col[i] <= minimum:
            dir[i] *= -1

def array_func(screen, col, dir, text, size, x, y):
    for i in range(len(col)):
        draw_text(screen, text[i], size, col[i], x, y + i*50)
        col_change(col[i], dir[i])


def play():

    # INIT
    pygame.init()
    display = pygame.Surface((W, H))
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("space invaders")
    clock = pygame.time.Clock()
    characterX = [100,100]
    characterY = [110,100]

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
            
            array_func(screen, def_col, col_dir, texts, 80, W/2, H/5)
            fontIntro = pygame.font.SysFont("arial", 30)
            text = fontIntro.render("Click to play!", 1, (255,255,255))
            screen.blit(text, (300,300,500,500))
        elif state == "PLAY":
            text = fontIntro.render(f'Score: {score}', True, (255, 255, 255))
            screen.blit(text, (10,10,500,200))

            character = pygame.draw.line(screen, white, characterX, characterY, 8)
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                characterX[0] = characterX[0] - 3
            if pressed[pygame.K_RIGHT]:
                characterX[0] = characterX[0] + 3
            
            
        display.blit(screen, (0,0))
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    play()