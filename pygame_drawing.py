# Drawing
# Author: Alex
# Date: jan 1, 2023

import pygame

def game():
    pygame.init()

    # COLOURS - (R, G, B)
    # CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
    WHITE = (255, 255, 255)
    BLACK = (  0,   0,   0)
    RED   = (255,   0,   0)
    GREEN = (  0, 255,   0)
    BLUE  = (  0,   0, 255)
    GREY  = (128, 128, 128)
    PURPLE = (228, 45, 216)

    # CONSTANTS
    WIDTH = 1920
    HEIGHT = 1080
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Drawing")

    # Variables
    done = False
    clock = pygame.time.Clock()

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC


        # ------ DRAWING TO SCREEN
        screen.fill(WHITE) # background
        # color random
        import random
        R_RED   = (255,   random.randint(0, 255),   0)
        R_BLUE  = (  0,   random.randint(0, 255), 255)
        """
        WHITE = (255, 255, 255)
        BLACK = (  0,   0,   0)
        RED   = (255,   0,   0)
        GREEN = (  0, 255,   0)
        BLUE  = (  0,   0, 255)
        GREY  = (128, 128, 128)
        PURPLE = (228, 45, 216)
        """
        for sky in range(5):
            pygame.draw.circle(screen, (sky * 51, 0, 255), (WIDTH / 2 - 50, HEIGHT / 2 - 50), 1125 - sky * 75)
        for sky in range(5):
            pygame.draw.circle(screen, (255, 0, 255 - 51 * sky), (WIDTH / 2 - 50, HEIGHT / 2 - 50), 750 - sky * 75)
        for sky in range(5):
            pygame.draw.circle(screen, (255, 51 * sky, 0), (WIDTH / 2 - 50, HEIGHT / 2 - 50), 375 - sky * 75)
        pygame.draw.rect(screen, BLUE, (0, HEIGHT / 2 + 10, WIDTH, HEIGHT))

        for reflect in range(50):
            # random_x = random.randint(-450, 450)
            # random_y = random.randint(HEIGHT / 2 + 10, HEIGHT)
            REFLECT_RED = (random.randint(0, 255), 0, 0)
            pygame.draw.line(screen, REFLECT_RED, (WIDTH / 2 - 50, HEIGHT / 2 - 50), (WIDTH / 2 + 50, HEIGHT / 2 + 50))
        """
        pygame.draw.rect(screen, RED, (WIDTH / 2 - 50, HEIGHT / 2 - 50, 100, 100))
        # Draw a circle on top of the rectangle
        pygame.draw.circle(screen, BLUE, (WIDTH / 2, HEIGHT / 2), 50)
        for offset in range(7):
            pygame.draw.line(screen, PURPLE, (WIDTH / 2 + 20, 20 + (offset * 75)), (WIDTH - 20, HEIGHT / 2 - 20 + (offset * 75)), 5)
        """

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60) # 60 fps

    pygame.quit()

if __name__ == "__main__":
    game()
