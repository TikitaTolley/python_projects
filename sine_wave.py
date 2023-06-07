import pygame

W, H = 1000, 600
black = (0, 0, 0)
white = (255, 255, 255)

def play():
  pygame.init()
  display = pygame.Surface((W, H))
  screen = pygame.display.set_mode((W, H))
  pygame.display.set_caption("sine wave")
  clock = pygame.time.Clock()

  run = True
  
  velocity = 10
  circle_x = 100
  circle_y = 300

  while run:
      
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        
    screen.fill(black)

    if circle_y > 400 or circle_y < 200:
      velocity *= -1
      circle_x += 10
    circle_y += velocity
        
    point = pygame.draw.circle(screen, white, [circle_x, circle_y], 10)


    display.blit(screen, (0,0))
    pygame.display.update()
        
  pygame.quit()

play()