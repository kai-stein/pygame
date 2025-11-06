import pygame
from constants import *
from player import Player
from logger import log_state

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

    my_player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        my_player.draw(screen)
        my_player.update(dt)
        pygame.display.flip()
        tm = clock.tick(60) 
        dt = tm / 1000
        #print("loop")


if __name__ == "__main__":
    main()
