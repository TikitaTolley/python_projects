import pygame

W, H = 1000, 600
black = (0, 0, 0)
white = (255, 255, 255)

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

    while run:
        delta_t = clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(black)

        text = font.render(f'Score: {player1_score} : {player2_score}', True, white)
        screen.blit(text, (400,10,500,200))

        player1 = pygame.draw.rect(screen, white, (90, 150, 10, 100))  # (left, top, width, height)

        player2 = pygame.draw.rect(screen, white, (910, 150, 10, 100))

        display.blit(screen, (0,0))
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    play()