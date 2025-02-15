import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot





def main(screen_width, screen_height):
    print("Starting asteroids!")
    print(f"Screen width: {screen_width}")
    print(f"Screen height: {screen_height}")

    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock() # A new clock object
    dt = 0 # initializing a delta time to use for movement

    
    updatable = pygame.sprite.Group() # Creating an instance of a group for updatable classes
    drawable = pygame.sprite.Group() # Creating an instance of a group for drawable classes
    shots = pygame.sprite.Group() # Creating an instance of a group for the shots class.
    asteroids = pygame.sprite.Group() # Creating an instanc of a group for the asteroids class.
    
    Player.containers = (updatable, drawable) # adding the Player class as a member of both drawable and updatable groups
    Asteroid.containers = (asteroids, updatable, drawable) # Adding the Asteroid class as a member of the three given groups.
    AsteroidField.containers = (updatable) # Adding the AsteroidField class as a member of the updatable group.
    Shot.containers = (shots, updatable, drawable) # Adding the Shot class to the given groups.

    x = screen_width / 2 # setting up the x value for the player.
    y = screen_height / 2 # setting up the y value for the player.
    player = Player(x, y) # creating the player instance with the x and y variables.
    asteroid_field = AsteroidField() # Initializing an AsteroidField object.
    

    
    while screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black") # Fill the empty screen with black boxes

        # update each member of the updatable group
        for sprite in updatable:
            sprite.update(dt)

        for asteroid in asteroids:
            status = player.collision(asteroid)
            if status == True:
                raise SystemExit("Game over!")
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()

        # drawing each member of the drawable group on the screen
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        tick = clock.tick(60)
        dt = tick/1000
        

if __name__ == "__main__":
    main(SCREEN_WIDTH, SCREEN_HEIGHT)

