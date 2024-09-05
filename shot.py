import pygame
from circleshape import *
from constants import *
from player import * 

class Shot(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 1)