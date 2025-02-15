import pygame
import random
from asteroid import Asteroid
from constants import *

class AsteroidField(pygame.sprite.Sprite):
    """ Class containing the logic for spawning new Asteroids """

    # setting up the edges for spawn locations
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT), 
        ], 
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt

        # Reset the spawn timer after going over the spawn rate and spawn a new asteroid
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)

            # randomly assign the speed
            speed = random.randint(40, 100)

            # get the velocity
            velocity = edge[0] * speed

            # Change the direction of the asteroid based on projecting the velocity
            velocity = velocity.rotate(random.randint(-30, 30))

            # uniformly distributes the spawn locations
            position = edge[1](random.uniform(0, 1)) 
            
            # Randomly selects the kind of asteroid from 1 - 3 (multiplier for size)
            kind = random.randint(1, ASTEROID_KINDS)

            # Spawning the asteroid
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)



