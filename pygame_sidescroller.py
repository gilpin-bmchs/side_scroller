# imports
import pygame, sys, random
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
# DISPLAYSURF.fill(WHITE)
DISPLAYSURF.blit(BACKGROUND, (0,0))

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.transform.rotate(pygame.image.load("ship.png"), -90)
        self.rect = self.image.get_rect()

        self.rect.center = (20, 200)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("Asteroid2.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (SCREEN_WIDTH, random.randint(0, SCREEN_HEIGHT - self.rect.height))

    def move(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.rect.topleft = (SCREEN_WIDTH, random.randint(0, SCREEN_HEIGHT - self.rect.height))

# create player and enemy objects
SHIP = Ship()
ASTEROID = Enemy()

# create sprite groups
enemies = pygame.sprite.Group()
enemies.add(ASTEROID)
all_sprites = pygame.sprite.Group()
all_sprites.add(SHIP)
all_sprites.add(ASTEROID)


# Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # pygame.draw.rect(DISPLAYSURF, RED, SHIP.rect)
    DISPLAYSURF.blit(BACKGROUND, (0,0))

    # moves and redraws all sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # DISPLAYSURF.blit(SHIP.image, SHIP.rect)
    # DISPLAYSURF.blit(ASTEROID.image, (200, 200))

    pygame.display.update()
    clock.tick(FPS)