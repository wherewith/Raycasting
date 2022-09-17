import math
import random
import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
import Player
import Map
pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 512
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Raycasting')
my_font = pygame.font.SysFont('Calibri', 50)
pygame.display.set_icon(my_font.render('γ', True, (0,150,50)))

FPS = 60
rays = 120

p = Player.Player(
    x           = SCREEN_WIDTH/2 /2 + 20,
    y           = SCREEN_WIDTH/2    + 20,
    radius      = 8,
    velocity    = 3,
    angle       = math.pi,
    turn_speed  = 0.05,
    fov         = math.pi / 3
)

map2D = Map.Map(
    s     = 8,
    scale = 64
)
map2D.generate()

def main():
    clock = pygame.time.Clock()
    run = True
    draw_window()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                run = False
        pygame.display.flip()

    pygame.quit()

def draw_window():
    screen.fill((125,125,125))

if __name__ == "__main__":
    main()