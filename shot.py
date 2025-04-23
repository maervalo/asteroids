import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.position = pygame.Vector2(x,y)
        self.radius = SHOT_RADIUS
        self.velocity = pygame.Vector2(0,0)

        if hasattr(self.__class__, 'containers'):
            for container in self.__class__.containers:
                container.add(self)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position), self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt