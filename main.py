import pygame
from constants import *
from player import Player



clock = pygame.time.Clock() # A new clock object
dt = 0 # The delta time variable



def main(screen_width, screen_height):
    print("Starting asteroids!")
    print(f"Screen width: {screen_width}")
    print(f"Screen height: {screen_height}")
    screen = pygame.display.set_mode((screen_width, screen_height))
    while screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black") # Fill the empty screen with black boxes

        x = screen_width / 2 # setting the x value for the player instance

        y = screen_height /2 # setting the y value for the player instance

        player = Player(x, y) # creating the player instance with the x and y variables

        player.draw(screen) # drawing the player on the screen

        pygame.display.flip()
        tick = clock.tick(60)
        dt = tick/1000
        

          


if __name__ == "__main__":
    main(SCREEN_WIDTH, SCREEN_HEIGHT)

