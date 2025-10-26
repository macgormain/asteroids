import pygame
from circleshape import CircleShape
import random
from constants import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, width = 2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        pos = self.position
        old_radius = self.radius
        vel = self.velocity
        self.kill()
        if old_radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            angle = random.uniform(20,50)
            v1 = vel.rotate(angle)
            v2 = vel.rotate(-angle)
            v1 *= 1.2
            v2 *= 1.2
            a1 = Asteroid(pos.x, pos.y, new_radius)
            a2 = Asteroid(pos.x, pos.y, new_radius)
            a1.velocity = v1
            a2.velocity = v2
