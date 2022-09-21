import pygame
import random
from Named_Colors import *

class Map:
    def __init__(self, s, scale):
        self.s = s
        self.scale = scale
        self.map2D = [[]]

    def show(self):
        for x in range(self.map2D.__len__()):
            print()
            for y in range(self.map2D[x].__len__()):
                print(self.map2D[x][y], end=" ")

    def generate(self, default = True, weight = .5):
        if default:
            self.map2D = \
                [
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 1, 0, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 1, 0, 1],
                    [1, 0, 0, 1, 1, 1, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1]
                ]
        else:
            self.map2D = self.generate_random(weight)

    def generate_random(self, weight):
        new_map = []
        for r in range(self.s):
            new_row = []
            for c in range(self.s):
                if r == 0 or c == 0 or r == self.s - 1 or c == self.s - 1:
                    new_row.append(1)
                elif r == self.s / 2 and c == self.s / 2:  # starting point
                    new_row.append(0)
                else:
                    possible = [1] + [0]*(int(1/weight)-1) #create ratio
                    print(possible)
                    new_row.append(random.choice(possible))
            new_map.append(new_row)
        return new_map


    def draw(self, screen):
        for r in range(self.map2D.__len__()):
            for c in range(self.map2D[r].__len__()):
                color = pygame.Color(c_silver)
                if self.map2D[c][r] == 0:  # hate this array
                    color = pygame.Color(c_gray)
                x_scale = r * self.scale
                y_scale = c * self.scale
                v1 = (x_scale + 1, y_scale + 1)
                v2 = (x_scale + 1, y_scale + self.scale - 1)
                v3 = (x_scale + self.scale - 1, y_scale + self.scale - 1)
                v4 = (x_scale + self.scale - 1, y_scale + 1)
                pygame.draw.polygon(screen, color, [v1, v2, v3, v4])  # polygon for cute inverted color grid :)