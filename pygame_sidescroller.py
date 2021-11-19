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

        random_scale = random.randrange(10, 100, 5)
        self.image = pygame.image.load("Asteroid2.png")
        self.image = pygame.transform.scale(self.image, (random_scale, random_scale))
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 1000) , random.randint(0, SCREEN_HEIGHT - self.rect.height))

    def move(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.rect.topleft = (SCREEN_WIDTH, random.randint(0, SCREEN_HEIGHT - self.rect.height))

# create player and enemy objects
SHIP = Ship()
# create 10 asteroids
asteroid_list = []
for i in range(10):
    ASTEROID = Enemy()
    asteroid_list.append(ASTEROID)


# create sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# add sprites to the groups
all_sprites.add(SHIP)
for rock in asteroid_list:
    all_sprites.add(rock)
    enemies.add(rock)

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