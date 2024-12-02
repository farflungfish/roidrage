import pygame
from constants import *
from player import Player

def main():
    # initializes pygame https://www.pygame.org/docs/ref/pygame.html#pygame.init
    pygame.init()

    # creates a python screen, sets resolution
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # creates a clock https://www.pygame.org/docs/ref/time.html#pygame.time.Clock
    # important so we can track delta time and limit frames per second
    clock = pygame.time.Clock()

    # delta time
    dt = 0

    # middle of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # create a player object, see player.py
    player = Player(x, y, PLAYER_RADIUS)

    # main game loop
    while True:
        # capture the quick event from pressing the X on a window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # paint the screen background black
        screen.fill("black")

        player.update(dt)
        print(player.rotation)

        # draw the player on the screen, above the black
        player.draw(screen)

        # runs a frame buffer flip
        pygame.display.flip()

        # captures deltatime, also limits frames to x frames per second see https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick
        dt = clock.tick(60) / 1000

# Makes only this file execute the main method
if __name__ == "__main__":
    main()

