import pygame

pygame.init()

class background:
  x = 0
  y = 0

  def __init__(self, x, y, sBackground, screen):
    self.x = x
    self.y = y
  
  def draw(self):
    screen.blit(sBackground, (100, 10))


screen = pygame.display.set_mode((347, 260))
sBackground = pygame.image.load("./images/background.png")

bg = background(0, 0, sBackground, screen)
pygame.display.set_caption("Frog RUN!")


def gameLoop():
  while True:
    bg.draw()

gameLoop()