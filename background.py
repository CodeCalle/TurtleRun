import pygame

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

screen = pygame.display.set_mode((1280, 720))

# Loads background image from image file
sBackground = pygame.image.load("./images/backgroundVector.png").convert()
sBackground = pygame.transform.scale(sBackground, (1280, 720))
bg = background(0, 0, 6, sBackground, screen)