import pygame
import background
from background import screen

class turtle:
  x = 100
  y = 350
  speed =  0
  maxSpeed = 0
  acceleration = 0 # How much faster the speed goes per frame
  
  def __init__(self, acceleration, maxSpeed):
    self.acceleration = acceleration # Sets the acceleration of turtle to 1
    self.maxSpeed = maxSpeed # Define the max speed of the turtle to 10

  def drawTurtle(self):

    if self.speed < self.maxSpeed:
      self.speed += self.acceleration
    
    self.y += self.speed

    if self.speed > 0:
      self.speed += self.acceleration
  
    screen.blit(turtleImage, (self.x, self.y))
  
  def jump(self):
    self.speed = -18

# Loads turtle image from image file
turtleImage = pygame.image.load("./images/dino.png")

t = turtle(1, 10)