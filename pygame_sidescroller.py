# imports
import pygame, sys
from pygame.locals import *

pygame.init()

# colors
WHITE = (255, 255, 255)

# variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
BACKGROUND = pygame.image.load("background.png")


# setup display
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
DISPLAYSURF.blit(BACKGROUND, (0,0))

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("ship.png")
        self.rect = self.image.get_rect()
        self.rect.center = (0, 200)

SHIP = Ship()
# Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(SHIP.image, SHIP.rect)

    pygame.display.update()
