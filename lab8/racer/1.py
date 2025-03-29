# Importing libraries
import pygame, sys
from pygame.locals import *
import random, time

#Initializing pygame
pygame.init()

#Setting up FPS
FPS = 60
clock = pygame.time.Clock()

#Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other variables that we need for the task
width, height = 400, 600
speed, score, coin_score = 5, 0, 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

# Creating a white screen
screen = pygame.display.set_mode((width, height))
screen.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if(self.rect.top > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)
        
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load("coin.png").convert_alpha(), 0.035)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)

    def move(self):
        self.rect.move_ip(0, speed)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies. add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while True:
    # Cycles through all events occuring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            speed += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    scores = font_small.render(str(score), True, BLACK)
    coin_scores_1 = font_small.render("Coins: ", True, BLACK)
    coin_scores_2 = font_small.render(str(coin_score), True, BLACK)
    screen.blit(scores, (10, 10))
    screen.blit(coin_scores_1, (width - 75, 10))
    screen.blit(coin_scores_2, (width - 50, 30))

    # Moves and redraws all Sprites
    for entries in all_sprites:
        screen.blit(entries.image, entries.rect)
        entries.move()

    # Run, if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        screen.fill(RED)
        screen.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Checking for collision between Player and Coin
    coins_collided = pygame.sprite.spritecollide(P1, coins, True)
    for coin in coins_collided:
        coin_score += 1
        coin.rect.top = 0
        coin.rect.center = (random.randint(40, width - 40), 0)
        coins.add(coin)
        all_sprites.add(coin)

    pygame.display.update()
    clock.tick(FPS)