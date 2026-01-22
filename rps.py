# Your Title Here
# Author:
# Date:

import random
import pygame
import time

# COLOURS - (R, G, B)
# CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
GREY  = (128, 128, 128)

# CONSTANTS
WIDTH = 480
HEIGHT = 270
SIZE = (WIDTH, HEIGHT)

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        """Goomba"""
        super().__init__()
        self.image = pygame.image.load('assets/rock.png')
        self.image = pygame.transform.scale_by(self.image, (0.03))

        self.rect = self.image.get_rect()

        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

class Paper(pygame.sprite.Sprite):
    def __init__(self):
        """Goomba"""
        super().__init__()
        self.image = pygame.image.load('assets/paper.png')
        self.image = pygame.transform.scale_by(self.image, (0.03))

        self.rect = self.image.get_rect()

        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

class Scissors(pygame.sprite.Sprite):
    def __init__(self):
        """Goomba"""
        super().__init__()
        self.image = pygame.image.load('assets/scissors.gif')
        self.image = pygame.transform.scale_by(self.image, (0.1))

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
    rock_sprites_group = pygame.sprite.Group()
    paper_sprites_group = pygame.sprite.Group()
    scissors_sprites_group = pygame.sprite.Group()

    n = 1000

    # create enemy sprite
    for _ in range(n):
        rock = Rock()

        rock.rect.centerx = random.randint(0, WIDTH)
        rock.rect.centery = random.randint(0, HEIGHT)
        rock.vel_x = random.choice([-3.1, -2, -1, 1, 2, 3])
        rock.vel_y = random.choice([-3, -2, -1, 1, 2, 3])

        all_sprites_group.add(rock)
        rock_sprites_group.add(rock)

    for _ in range(n):
        paper = Paper()

        paper.rect.centerx = random.randint(0, WIDTH)
        paper.rect.centery = random.randint(0, HEIGHT)
        paper.vel_x = random.choice([-3, -2, -1, 1, 2, 3])
        paper.vel_y = random.choice([-3, -2, -1, 1, 2, 3])

        all_sprites_group.add(paper)
        paper_sprites_group.add(paper)

    for _ in range(n):
        scissors = Scissors()

        scissors.rect.centerx = random.randint(0, WIDTH)
        scissors.rect.centery = random.randint(0, HEIGHT)
        scissors.vel_x = random.choice([-3, -2, -1, 1, 2, 3])
        scissors.vel_y = random.choice([-3, -2, -1, 1, 2, 3])

        all_sprites_group.add(scissors)
        scissors_sprites_group.add(scissors)

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC
        all_sprites_group.update()
        for rock in rock_sprites_group:
            if rock.rect.right > WIDTH:
                rock.vel_x *= -1
            if rock.rect.left < 0:
                rock.vel_x *= -1
            if rock.rect.top < 0:
                rock.vel_y *= -1
            if rock.rect.bottom > HEIGHT:
                rock.vel_y *= -1

        all_sprites_group.update()
        for paper in paper_sprites_group:
            if paper.rect.right > WIDTH:
                paper.vel_x *= -1
            if paper.rect.left < 0:
                paper.vel_x *= -1
            if paper.rect.top < 0:
                paper.vel_y *= -1
            if paper.rect.bottom > HEIGHT:
                paper.vel_y *= -1

        all_sprites_group.update()
        for scissors in scissors_sprites_group:
            if scissors.rect.right > WIDTH:
                scissors.vel_x *= -1
            if scissors.rect.left < 0:
                scissors.vel_x *= -1
            if scissors.rect.top < 0:
                scissors.vel_y *= -1
            if scissors.rect.bottom > HEIGHT:
                scissors.vel_y *= -1

        # check if mario collides with block
        # if mario collides with a block, print out "collided!!"
        # make a group of just blocks
        r_vs_p = pygame.sprite.spritecollide(paper, rock_sprites_group, True)
        # Rock vs Paper
        if r_vs_p:
            print("Paper")
        p_vs_s = pygame.sprite.spritecollide(scissors, paper_sprites_group, True)
        # Paper vs Scissors
        if p_vs_s:
            print("Scissors")
        s_vs_r = pygame.sprite.spritecollide(rock, scissors_sprites_group, True)
        # Scissors vs Rock
        if s_vs_r:
            print("Rock")



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
