import sys
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    dt = 0
    
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        for item in updatable:
            item.update(dt)
        
        
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()
        
        
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()
       
        screen.fill("black")

        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()