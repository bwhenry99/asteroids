from constants import *
import pygame
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Create groups
    updateable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    # create player
    Player.containers = (updateable_group, drawable_group)
    Shot.containers = (updateable_group, drawable_group, shot_group)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)

    # create asteroids
    Asteroid.containers = (updateable_group, drawable_group, asteroid_group)
    AsteroidField.containers = (updateable_group)
    field = AsteroidField()


    while True:
        screen.fill("black")

        # update all objects
        for object in updateable_group:
            object.update(dt)
        
        # draw all objects
        for object in drawable_group:
            object.draw(screen)

        for asteroid in asteroid_group:
            if asteroid.collision(player):
                print("Game over!")
                return
            
        for shot in shot_group:
            for asteroid in asteroid_group:
                if(shot.collision(asteroid)):
                    asteroid.kill()

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
