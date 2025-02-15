import pygame # import the pygame module


# CircleShape class to create invisible circles for the player
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius
    
    # Draw method for child classes to override
    def draw(self, screen):
        pass
    
    # Update method for the child classes to override
    def update(self, dt):
        pass
    
    # Method to check the collision status between circle objects
    def collision(self, CircleShape):
        # Get the distance between the two positions
        distance = self.position.distance_to(CircleShape.position)

        # If the distance between the two objects is less than or equal to the combined radius of the two object a collision is detected
        if distance <= self.radius + CircleShape.radius:
            return True
        else:
            return False
    
        