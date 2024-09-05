import pygame
from circleshape import *
from constants import *
from player import * 

class Shot(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 1) * PLAYER_SHOOT_SPEED

    def update(self, dt):
        self.position += (self.velocity * dt)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 1)