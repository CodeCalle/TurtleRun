import pygame

pygame.init()

class background:
  x = 0
  y = 0

  def __init__(self, x, y, sBackground, screen):
    self.x = x
    self.y = y
  
  def draw(self):
    screen.blit(sBackground, (0, 0))

class turtle:
  x = 100
  y = 350
  speed = 0
  maxSpeed = 0
  
  def __init__(self):
    pass
  
  def drawTurtle(self):
    screen.blit(turtleImage, (self.x, self.y))

    if self.y < 350:
      self.y += 5
  
  def jump(self):
    self.y = 200
    


## Create background image
#screen = pygame.display.set_mode((347, 260))
screen = pygame.display.set_mode((1280, 720))
sBackground = pygame.image.load("./images/background.png")
sBackground = pygame.transform.scale(sBackground, (1280, 720))


## Create turtle image
turtleImage = pygame.image.load("./images/dino.png")


bg = background(0, 0, sBackground, screen)
t = turtle()
pygame.display.set_caption("Turtle RUN!")

def gameLoop():

  running = True
  while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            t.jump()

    bg.draw()
    t.drawTurtle()
    pygame.display.update()

gameLoop()