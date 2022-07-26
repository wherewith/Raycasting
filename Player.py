import math
import pygame
from Named_Colors import *


class Player:
    def __init__(self, x, y, radius, velocity, angle, turn_speed, fov):
        self.x = x
        self.y = y
        self.tx = self.x
        self.ty = self.y
        self.radius = radius
        self.velocity = velocity
        self.angle = angle
        self.turn_speed = turn_speed
        self.fov = fov

    def draw(self, screen):
        pygame.draw.circle(screen, c_yellow, (self.x, self.y), self.radius)
        pygame.draw.line(screen, c_blue, (self.x, self.y),
                         (self.x - math.sin(self.angle) * 25, self.y + math.cos(self.angle) * 25), 3)
        self.draw_fov(screen)

    def draw_fov(self, screen):
        pygame.draw.line(screen, c_blue, (self.x, self.y),
                         (self.x - math.sin(self.angle - self.fov / 2) * 50, self.y + math.cos(self.angle - self.fov / 2) * 50), 3)
        pygame.draw.line(screen, c_blue, (self.x, self.y),
                         (self.x - math.sin(self.angle + self.fov / 2) * 50, self.y + math.cos(self.angle + self.fov / 2) * 50), 3)
