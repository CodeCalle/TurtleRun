import pygame
import classes
from classes import background

pygame.init()
pygame.font.init()




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


# Function to show text on screen
font = pygame.font.SysFont('comicsansms', 32)
text = font.render('Press Q to quit', True, (0, 128, 0))



## Create background image
#screen = pygame.display.set_mode((347, 260))

# Moved to classes
'''
screen = pygame.display.set_mode((1280, 720))
sBackground = pygame.image.load("./images/backgroundVector.png").convert()
sBackground = pygame.transform.scale(sBackground, (1280, 720))
'''

clock = pygame.time.Clock()
## Create turtle image
turtleImage = pygame.image.load("./images/dino.png")

#bg = background(0, 0, 6, sBackground, screen)
t = turtle(1, 10)
pygame.display.set_caption("Turtle RUN!")

def gameLoop():

  running = True
  show_text = False
  while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit();
          running = False
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            t.jump()
          elif event.key == ord('h'):
            show_text = True

        elif event.type == pygame.KEYUP:
          if event.key == ord('q'):
            pygame.quit()
            main = False
          elif event.key == ord('h'):
            show_text = False
            
    bg.draw()
    t.drawTurtle()
    
    # Prints help text on screen
    if (show_text == True):
      screen.blit(text, (100, 100))

    clock.tick(60)
    pygame.display.update()

gameLoop()