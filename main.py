import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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

    # groups

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # add shots to containers
    Shot.containers = (updatable, drawable, shots)

    # add player to the drawable and updatable sprite groups
    Player.containers = (updatable, drawable)

    # add asteroids to containers
    Asteroid.containers = (asteroids, updatable, drawable)

    # add asteroidfield to updatable container

    AsteroidField.containers = (updatable)

    # create a player object, see player.py
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    asteroidfield = AsteroidField()
    # main game loop
    while True:
        # capture the quick event from pressing the X on a window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # paint the screen background black
        screen.fill("black")
        
        # run update on updatable group
        for obj in updatable:
            obj.update(dt)

        # check for collisions with the player
        for obj in asteroids:
            if obj.is_colliding(player):
                print("Game over!")
                exit()

        # check for collisions between asteroids and shots
        for roid in asteroids:
            for shot in shots:
                if roid.is_colliding(shot):
                    roid.split()
                    shot.kill()

        # run draw on drawable group
        for obj in drawable:
            obj.draw(screen)

        # runs a frame buffer flip
        pygame.display.flip()

        # captures deltatime, also limits frames to x frames per second see https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick
        dt = clock.tick(60) / 1000

# Makes only this file execute the main method
if __name__ == "__main__":
    main()

