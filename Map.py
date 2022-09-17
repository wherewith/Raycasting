class Map:
    def __init__(self, x, y, scale):
        self.x = x
        self.y = y
        self.scale = scale
        self.map2D = [[]]

    def print_map(self):
        for x in range(self.map2D.__len__()):
            print()
            for y in range(self.map2D[x].__len__()):
                print(self.map2D[x][y], end=" ")