import pygame
from constants import *
from player import Player
from logger import log_state
from logger import log_event
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    try:
        pygame.init() # This still initializes other modules
        # Explicitly initialize the display module and catch any errors
        pygame.display.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        print("Pygame display set up successfully!")
    except pygame.error as e:
        print(f"A Pygame display error occurred: {e}")
        print("This might be due to a missing display server or driver issues.")
        return # Exit if display setup failed
    
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable) 
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    shot.containers = (shots,updatable, drawable)

    my_player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    my_asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for to_update in updatable:
            to_update.update(dt)

        for to_draw in drawable:
            to_draw.draw(screen)
        
        for ast in asteroids:
            if ast.collides_with(my_player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()


        pygame.display.flip()
        tm = clock.tick(60) 
        dt = tm / 1000
        #print("loop")


if __name__ == "__main__":
    main()
