import pygame
import sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroid_field = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)
    player = Player(x= SCREEN_WIDTH /2, y = SCREEN_HEIGHT / 2)
    field = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                sys.exit()
        for shot in shots:
            for asteroid in asteroids:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
