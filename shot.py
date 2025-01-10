import pygame

from circleshape import CircleShape
from constants import *


class Shot(CircleShape):

    def __init__(self, x, y, direction):
        super().__init__(x, y, SHOT_RADIUS)

        self.__set_direction(direction)

    def update(self, dt):
        self.position += self.velocity * PLAYER_SHOOT_SPEED * dt

    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, radius=self.radius, width=2)

    def __set_direction(self,direction):
        self.velocity = pygame.Vector2(0, 1).rotate(direction)
