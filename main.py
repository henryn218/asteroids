import sys

import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    Shot.containers = (shots, updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    _ = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for sprite in updateable:
            sprite.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        delta = clock.tick(60)
        dt = delta / 1000


if __name__ == "__main__":
    main()
