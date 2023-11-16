import pygame

def get_score():
    pass

# pygame setup
pygame.init()
X = 700
Y = 800
screen = pygame.display.set_mode((X, Y))
clock = pygame.time.Clock()
running = True

white = (255,255,255)

pygame.display.set_caption('pacman')
centre = (X/2, Y/2)

current_score = get_score()

font = pygame.font.Font('freesansbold.ttf', 32)
score = font.render(f'score: {current_score}', True, white)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    # RENDER YOUR GAME HERE
    screen.blit(score, (300, 10))





    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()