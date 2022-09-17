import pygame

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

    def generate(self, default = True):
        if default:
            self.map2D = \
                [
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 1, 0, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 1, 0, 1],
                    [1, 0, 0, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1]
                ]

    def draw(self, screen):
        for r in range(self.map2D.__len__()):
            for c in range(self.map2D[r].__len__()):
                color = pygame.Color((255, 255, 255))
                if self.map2D[c][r] == 0:  # hate this array
                    color = pygame.Color((0, 0, 0))
                x_scale = r * self.scale
                y_scale = c * self.scale
                v1 = (x_scale + 1, y_scale + 1)
                v2 = (x_scale + 1, y_scale + self.scale - 1)
                v3 = (x_scale + self.scale - 1, y_scale + self.scale - 1)
                v4 = (x_scale + self.scale - 1, y_scale + 1)
                pygame.draw.polygon(screen, color, [v1, v2, v3, v4])  # polygon for cute inverted color grid :)