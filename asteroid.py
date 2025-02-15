import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    # override the draw method from the parent class to draw a circle
    def draw(self, screen):
        pygame.draw.circle(surface = screen, color = "white", center = self.position, radius = self.radius, width = 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            # Creating two directly split vectors to base the new asteroids off of
            vector1 = self.velocity.rotate(random_angle)
            vector2 = self.velocity.rotate(-random_angle)
            
            # Creating the new radius of the new asteroids
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            # Creating the two new asteroid objects
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            # Setting the velocity of the new asteroids and increasing speed
            asteroid1.velocity = vector1 * 1.2 # multiplyer for speed upgrade
            asteroid2.velocity = vector2 * 1.2 # multiplyer for speed upgrade





    