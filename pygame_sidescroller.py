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
SCORE = 0

# setting up fonts
font = pygame.font.SysFont("Veranda", 30)
font_large = pygame.font.SysFont("Veranda", 100)


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
        global SCORE
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.rect.topleft = (SCREEN_WIDTH, random.randint(0, SCREEN_HEIGHT - self.rect.height))            
            SCORE += 1

# create player and enemy objects
SHIP = Ship()
ASTEROID = Enemy()

# create sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# add sprites to the groups
all_sprites.add(SHIP)
enemies.add(ASTEROID)
all_sprites.add(ASTEROID)

# Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(BACKGROUND, (0,0))
    score = font.render(f"SCORE: {str(SCORE)}", True, WHITE)
    DISPLAYSURF.blit(score, (10, 10))

    # moves and redraws all sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    if ASTEROID.rect.right < 1:
        new_rock = Enemy()
        enemies.add(new_rock)
        all_sprites.add(new_rock)
    
    if pygame.sprite.spritecollideany(SHIP, enemies):
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit

    pygame.display.update()
    clock.tick(FPS)