import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    clock = pygame.time.Clock()
    dt = 0
    
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_group = pygame.sprite.Group()
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)

    AsteroidField.containers = (updatable_group,)
    asteroid_field = AsteroidField()

    shot_group = pygame.sprite.Group()
    Shot.containers = (shot_group, updatable_group, drawable_group)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for thing in drawable_group:
            thing.draw(screen)
        updatable_group.update(dt)
        
        
        for asteroid in asteroid_group:
            if asteroid.is_colliding(player):
                print("Game Over!")
                sys.exit()
            for bullet in shot_group:
                if bullet.is_colliding(asteroid):
                    bullet.kill()
                    asteroid.split()
         
        pygame.display.flip()
        

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()