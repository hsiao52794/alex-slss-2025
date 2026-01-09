# Your Title Here
# Author:
# Date:

import random
import pygame

# COLOURS - (R, G, B)
# CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
GREY  = (128, 128, 128)

# CONSTANTS
WIDTH = 1920
HEIGHT = 1080
SIZE = (WIDTH, HEIGHT)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        """Goomba"""
        super().__init__()
        self.image = pygame.image.load('assets/dvd-logo-png-33.png')

        self.rect = self.image.get_rect()

        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

def game():
    pygame.init()

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("collect blocks")

    # Variables
    done = False
    clock = pygame.time.Clock()

    # create a sprite group
    all_sprites_group = pygame.sprite.Group()
    enemy_sprite_group = pygame.sprite.Group()

    # create enemy sprite
    enemy = Enemy()

    enemy.rect.centerx = random.randint(100, WIDTH-100)
    enemy.rect.centery = random.randint(100, HEIGHT-100)
    enemy.vel_x = random.randint(-5, 5)*2
    enemy.vel_y = random.randint(-5, 5)*2

    all_sprites_group.add(enemy)
    enemy_sprite_group.add(enemy)

    # create 100 blocks

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC
        all_sprites_group.update()
        for enemy in enemy_sprite_group:
            if enemy.rect.right > WIDTH:
                enemy.vel_x *= -1
            if enemy.rect.left < 0:
                enemy.vel_x *= -1
            if enemy.rect.top < 0:
                enemy.vel_y *= -1
            if enemy.rect.bottom > HEIGHT:
                enemy.vel_y *= -1
        # check if mario collides with block
        # if mario collides with a block, print out "collided!!"
        # make a group of just blocks

        # ------ DRAWING TO SCREEN
        screen.fill(BLACK)

        # draw all sprites
        all_sprites_group.draw(screen)

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60) # 60 fps

    pygame.quit()

if __name__ == "__main__":
    game()
