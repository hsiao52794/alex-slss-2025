
# Collect Blocks
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

class Block(pygame.sprite.Sprite):
    def __init__(self):
        """A blue block"""
        super().__init__()

        self.image = pygame.Surface((20, 15))
        # change the colour of our image to blue
        self.image.fill(BLUE)

        # rect represents the hitbox of our sprite
        # the hitbox gives information about:
        #    - location of the sprite x, y
        #    - the size of the sprite width, height
        self.rect = self.image.get_rect()
        # change the location of our hitbox
        self.rect.centerx = 100
        self.rect.centery = 100


        self.point_value = 1

    def level_up(self, val: int):
        """Incr point value"""
        self.point_value *= val

class Mario(pygame.sprite.Sprite):
    def __init__(self):
        """Player sprite"""
        super().__init__()

        # Two copies of image: right-facing and left-facing
        self.image_right = pygame.image.load("assets/mario-snes.png")
        self.image_right = pygame.transform.scale_by(self.image_right, 0.5)
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        self.image = self.image_right

        self.rect = self.image.get_rect()

        # Keep track of last x-coord
        self.last_x = 0

        # Mario's "Life"
        self.health = 100
        self.points = 0

    def decrease_health(self, mag: int) -> int:
        """Decrease player's health by magnitude.
        Returns:
            current health that Mario has after the change
        """
        self.health -= mag
        return self.health

    def increase_score(self, amt: int):
        self.points += amt

    def show_health_percentage(self) -> int:
        return self.health / 100

    def update(self):
        """Have Mario follow the mouse.
        Set the "right" Mario image based on where he's facing."""

        # Mario faces right if and only if the previous x
        # is less than the current x
        if self.last_x < self.rect.x:
            self.image = self.image_right
        elif self.last_x > self.rect.x:
            self.image = self.image_left

        # Update the last_x
        self.last_x = self.rect.x

class Map(pygame.sprite.Sprite):
    def __init__(self):
        """Player sprite"""
        super().__init__()

        self.image = pygame.Surface((200, 150))
        # change the colour of our image to blue
        self.image.fill(RED)

        self.rect = self.image.get_rect()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        """Goomba"""
        super().__init__()

        self.image = pygame.image.load("assets/goomba-nes.png")
        self.rect = self.image.get_rect()
        # No initial location -> (0, 0)

        # Velocity of the Enemy
        self.vel_x = 0
        self.vel_y = 0

        self.damage = 1

    def level_up(self):
        # increase damage
        self.damage *= 2


    def update(self):
        # movement in the x- and y-axis
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        # TODO: randomize movement

class HealthBar(pygame.Surface):
    def __init__(self):
        super().__init__((300, 10))
        self.fill(RED)

    def set_health(self, percentage: float):
        self.fill(RED)
        pygame.draw.rect(self, GREEN, (0, 0, (300 * percentage), 10))

def move(sprite, vel: int):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        sprite.rect.centerx += vel
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        sprite.rect.centerx -= vel
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        sprite.rect.centery += vel
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        sprite.rect.centery -= vel

def game():
    pygame.init()

    # CONSTANTS
    WIDTH = 960
    HEIGHT = 540
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Collect Blocks")
    pygame.mouse.set_visible(True)

    # Variables
    done = False

    clock = pygame.time.Clock()
    num_enemies = 3
    num_blocks = 200
    healthbar = HealthBar()
    level = 1
    vel = 5

    # Create a sprite group
    all_sprites_group = pygame.sprite.Group()
    block_sprites_group = pygame.sprite.Group()
    enemy_sprites_group = pygame.sprite.Group()
    map_sprites_group = pygame.sprite.Group()

    # map
    for map in range(20):
        map = Map()
        map.rect.center = random.randint(-1000, 1000), random.randint(-1000, 1000)
        map_last_center = map.rect.center
        all_sprites_group.add(map)
        map_sprites_group.add(map)

    # Create player sprite
    player = Mario()
    # Place Mario in the middle of the screen
    player.rect.centerx = WIDTH / 2
    player.rect.centery = HEIGHT / 2
    player_last_x = player.rect.centerx
    player_last_y = player.rect.centery
    all_sprites_group.add(player)

    # Create Enemies
    for _ in range(num_enemies):
        enemy_one = Enemy()
        # Randomize position at bottom-left
        random_x = random.randrange(20, 100)
        random_y = random.randrange(HEIGHT-100, HEIGHT-20)
        enemy_one.rect.center = random_x, random_y
        enemy_last_center = enemy_one.rect.center
        # Randomize velocity
        enemy_one.vel_x = random.choice([-3, -2, -1, 1, 2, 3])
        enemy_one.vel_y = random.choice([-3, -2, -1, 1, 2, 3])

        all_sprites_group.add(enemy_one)
        enemy_sprites_group.add(enemy_one)

    # Create 100 blocks
    for _ in range(num_blocks):
        block = Block()
        # randomize their location
        block.rect.centerx = random.randrange(-1000, 1000)
        block.rect.centery = random.randrange(-1000, 1000)
        block_last_center = block.rect.center
        # add them to the sprite group
        all_sprites_group.add(block)
        block_sprites_group.add(block)

    # delete overlapped map/blocks
    map_collided = pygame.sprite.spritecollide(player, map_sprites_group, True)
    for map in map_sprites_group:
        blocks_collided = pygame.sprite.spritecollide(map, block_sprites_group, True)

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC
        all_sprites_group.update()
        healthbar.set_health(player.show_health_percentage())

        # mario move
        keys = pygame.key.get_pressed()

        map_collided = pygame.sprite.spritecollide(player, map_sprites_group, False)
        if not map_collided:
            # shift mario a little bit
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                player.rect.centerx = (WIDTH / 2) - vel * 2
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                player.rect.centerx = (WIDTH / 2) + vel * 2
            elif keys[pygame.K_UP] or keys[pygame.K_w]:
                player.rect.centery = (HEIGHT / 2) - vel * 2
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                player.rect.centery = (HEIGHT / 2) + vel * 2
            else:
                player.rect.centerx = WIDTH / 2
                player.rect.centery = HEIGHT / 2

            # map move
            for map in map_sprites_group:
                move(map, vel)

            for blocks in block_sprites_group:
                move(blocks, vel)

            for enemies in enemy_sprites_group:
                move(enemies, vel)
            
        """
        # collision detection
        map_collided = pygame.sprite.spritecollide(player, map_sprites_group, False)
        if map_collided:
            vel = 0
            map.rect.center = map_last_center
            blocks.rect.center = block_last_center
            enemies.rect.center = enemy_last_center
        else:
            vel = 5
        
        map_last_center = map.rect.center
        block_last_center = blocks.rect.center
        enemy_last_center = enemies.rect.center
        """

        # Keep the enemies inside the screen
        for enemy in enemy_sprites_group:
            # x-axis and y-axis bounce
            if enemy.rect.left < 0 or enemy.rect.right > WIDTH:
                enemy.vel_x = -enemy.vel_x
            if enemy.rect.top < 0 or enemy.rect.bottom > HEIGHT:
                enemy.vel_y = -enemy.vel_y

        # Check if Mario collides with a block
        blocks_collided = pygame.sprite.spritecollide(player, block_sprites_group, True)
        for block in blocks_collided:
            player.increase_score(block.point_value)

        # Check if Mario collides with enemies
        enemies_collided = pygame.sprite.spritecollide(player, enemy_sprites_group, False)
        for enemy in enemies_collided:
            # Decrease Mario's life by some number
            player.decrease_health(enemy.damage)

        # LEVEL UP
        # Refill blocks
        # Increase enemy damage
        # Increase block point value
        if not block_sprites_group:
            level += 1

            for _ in range(num_blocks):
                block = Block()
                block.rect.center = random.randrange(0, WIDTH), random.randrange(0, HEIGHT)

                block.level_up(level)

                all_sprites_group.add(block)
                block_sprites_group.add(block)

            enemy = Enemy()
            enemy.vel_x, enemy.vel_y = random.choice([-5, -3, -1, 1, 3, 5]), random.choice([-5, -3, -1, 1, 3, 5])
            enemy.rect.center = (WIDTH/2, HEIGHT/2)
            all_sprites_group.add(enemy)
            enemy_sprites_group.add(enemy)

            for enemy in enemy_sprites_group:
                enemy.level_up()

        # End Game
        if player.health <= 0:
            done = True

        # ------ DRAWING TO SCREEN
        screen.fill(WHITE)

        # Draw all the sprites
        all_sprites_group.draw(screen)
        screen.blit(healthbar, (5, 5))

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60) # 60 fps


    # Display final score:
    print("Thanks for playing!")
    print("Final score is:", player.points)

    pygame.quit()

if __name__ == "__main__":
    game()
