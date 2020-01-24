import pygame

pygame.init()

class background:
  x = 0
  y = 0
  speed = 0

  def __init__(self, x, y, speed, sBackground, screen):
    self.x = x
    self.y = y
    self.speed = speed
  
  def draw(self):
    x = self.x

    screen.blit(sBackground, (0 - self.x, 0))
    screen.blit(sBackground, (1280 - self.x, 0))

    if x >= 1280:
      self.x = 0
    self.x += self.speed


class turtle:
  x = 100
  y = 350
  speed =  0 ### How fast it goes
  maxSpeed = 0
  acceleration = 0 # How much faster the speed goes per frame
  
  def __init__(self, acceleration, maxSpeed):
    self.acceleration = acceleration
    self.maxSpeed = maxSpeed

  def drawTurtle(self):

    if self.speed < self.maxSpeed:
      self.speed += self.acceleration
    
    self.y += self.speed

    if self.speed > 0:
      self.speed += self.acceleration
  
    screen.blit(turtleImage, (self.x, self.y))
  
  def jump(self):
    self.speed = -18
    


## Create background image
#screen = pygame.display.set_mode((347, 260))
screen = pygame.display.set_mode((1280, 720))
sBackground = pygame.image.load("./images/backgroundVector.png").convert()
sBackground = pygame.transform.scale(sBackground, (1280, 720))

clock = pygame.time.Clock()
## Create turtle image
turtleImage = pygame.image.load("./images/dino.png")


bg = background(0, 0, 6, sBackground, screen)
t = turtle(1, 10)
pygame.display.set_caption("Turtle RUN!")

def gameLoop():

  running = True
  while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit();
          running = False
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            t.jump()
        elif event.type == pygame.KEYUP:
          if event.key == ord('q'):
            pygame.quit()
            main = False
            
    bg.draw()
    t.drawTurtle()
    clock.tick(120)
    print(clock)
    pygame.display.update()

gameLoop()