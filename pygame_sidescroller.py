# imports
import pygame, sys
from pygame.locals import *

pygame.init()

# FPS Clock
clock = pygame.time.Clock()
FPS = 60

# colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

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

        self.image = pygame.transform.rotate(pygame.image.load("ship.png"), -90)
        self.rect = self.image.get_rect()

        self.rect.center = (20, 200)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.top > 0:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)

SHIP = Ship()
# pygame.transform.rotate(SHIP.image, 90)
# Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    SHIP.move()
    # pygame.draw.rect(DISPLAYSURF, RED, SHIP.rect)
    DISPLAYSURF.blit(SHIP.image, SHIP.rect)

    pygame.display.update()
    clock.tick(FPS)