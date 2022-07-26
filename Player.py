import math


class Player:
    def __init__(self, x, y, velocity, angle, turn_speed, fov):
        self.x = x
        self.y = y
        self.tx = self.x
        self.ty = self.y
        self.velocity = velocity
        self.angle = angle
        self.turn_speed = turn_speed
        self.fov = fov
