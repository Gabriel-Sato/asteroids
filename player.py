import pygame
from circleshape import *

Class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y