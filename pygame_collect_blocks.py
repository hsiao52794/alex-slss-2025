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


class Block(pygame.sprite.Sprite):
    def __init__(self):
        """A blue block"""
        super().__init__()

        self.image = pygame.Surface((20, 15))
        self.image.fill(BLUE)
        # rect represent the hitbox
        self.rect = self.image.get_rect()
        # change hitbox location
        self.rect.centerx = 100
        self.rect.centery = 100

class Mario(pygame.sprite.Sprite):
    def __init__(self):
        """Player"""
        super().__init__()
        self.image = pygame.image.load('assets/mario-snes.png')

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        """Goomba"""
        super().__init__()
        self.image = pygame.image.load('assets/goomba-nes.png')

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

    block_one = Block()
    block_one.rect.centerx = WIDTH / 2

    # create a sprite group
    all_sprites_group = pygame.sprite.Group()
    block_sprite_group = pygame.sprite.Group()
    enemy_sprite_group = pygame.sprite.Group()

    # create player
    player = Mario()
    # place mario at mid of screen
    player.rect.centerx = WIDTH / 2
    player.rect.centery = HEIGHT / 2
    all_sprites_group.add(player)

    # create enemy sprite
    for _ in range(10):
        enemy = Enemy()

        enemy.rect.centerx = random.randint(0, WIDTH)
        enemy.rect.centery = random.randint(0, HEIGHT)
        enemy.vel_x = random.randint(-5, 5)*2
        enemy.vel_y = random.randint(-5, 5)*2

        all_sprites_group.add(enemy)
        enemy_sprite_group.add(enemy)

    # create 100 blocks
    for _ in range(1000):
        block = Block()
        block.rect.centerx = random.randint(0, WIDTH)
        block.rect.centery = random.randint(0, HEIGHT)
        all_sprites_group.add(block)
        block_sprite_group.add(block)

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
        blocks_collided = pygame.sprite.spritecollide(player, block_sprite_group, True)
        if blocks_collided:
            print("collided!!")
            print(blocks_collided)

        # ------ DRAWING TO SCREEN
        screen.fill(WHITE)

        # draw all sprites
        all_sprites_group.draw(screen)

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60) # 60 fps

    pygame.quit()

if __name__ == "__main__":
    game()
