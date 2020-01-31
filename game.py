# Import pygame module
import pygame

# Import background class file
import background
from background import *

# Import turtle class file
import turtle
from turtle import *

# Initialize pygame and add system font
pygame.init()
pygame.font.init()

# Function to show text on screen
font = pygame.font.SysFont('comicsansms', 32)
text = font.render('Press Q to quit', True, (0, 128, 0))

# Initialize the clock function that later is being used to set the framerate
clock = pygame.time.Clock()

# Define the caption text on the game window
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