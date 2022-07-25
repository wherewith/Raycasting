import math

import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
from pygame import gfxdraw
pygame.init()

SCREEN_WIDTH = 1024 #
SCREEN_HEIGHT = 512
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Raycasting :)")

FPS = 60

px = 300
py = 300
tx = px #teleport values - for collisions with no jankiness
ty = py
velocity = 3
pa = math.pi
rot_speed = 0.05
pfov = math.pi / 3

rays = 60

mapX = 8
mapY = 8
map_scale = 64
map2D = \
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

def main():
    clock = pygame.time.Clock()
    run = True
    draw_window()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                run = False

        key_pressed = pygame.key.get_pressed()
        check_WASD(key_pressed)

        draw_window()  # jic
        draw_map2D()
        raycast()
        draw_player()

        pygame.display.flip()

    pygame.quit()

def draw_map2D():
    for r in range(map2D.__len__()):
        for c in range(map2D[r].__len__()):
            color = pygame.Color((255,255,255))
            if map2D[c][r] == 0: # hate this array
                color = pygame.Color((0,0,0))
            x_scale = r*map_scale
            y_scale = c*map_scale
            v1 = (x_scale + 1, y_scale + 1)
            v2 = (x_scale + 1, y_scale+map_scale - 1)
            v3 = (x_scale + map_scale - 1, y_scale + map_scale - 1)
            v4 = (x_scale + map_scale - 1, y_scale + 1)
            pygame.draw.polygon(screen, color, [v1, v2, v3, v4]) # polygon for cute inverted color grid :)

def print_map():  # when debugging tells u that u messed up its so depressing
    for x in range(mapX):
        print()
        for y in range(mapY):
            print(map2D[x][y], end = " ")
print_map()

def check_WASD(key_pressed):
    global px, py, pa
    pa = pa % (2*math.pi)
    if key_pressed[ord('w')]:  # -
        px -= math.sin(pa) * velocity
        py += math.cos(pa) * velocity
    if key_pressed[ord('a')]:
        pa -= rot_speed
    if key_pressed[ord('s')]: # +
        px += math.sin(pa) * velocity
        py -= math.cos(pa) * velocity
    if key_pressed[ord('d')]:
        pa += rot_speed

# this one is just bad bruh its so jank
# def collision_correct():
#     global px
#     global py
#     if direction == 1:
#         px += math.sin(pa) * 2
#         py -= math.cos(pa) * 2
#     elif direction == -1:
#         px -= math.sin(pa) * 2
#         py += math.cos(pa) * 2

def draw_player():
    pygame.draw.circle(screen, (255,255,0), (px, py), 8)
    pygame.draw.line(screen, (255, 255, 0), (px, py), (px - math.sin(pa) * 25, py + math.cos(pa) * 25), 3)
    draw_fov()

def draw_fov():
    pygame.draw.line(screen, (240, 100, 90), (px ,py),
                     (px - math.sin(pa - pfov/2) * 50, py + math.cos(pa - pfov/2) * 50), 3)
    pygame.draw.line(screen, (240, 100, 90), (px, py),
                     (px - math.sin(pa + pfov / 2) * 50, py + math.cos(pa + pfov / 2) * 50), 3)

def raycast():
    global tx, ty, py, px
    ca = pa - pfov/2 # current angle of ray being cast
    for ray in range(rays):
        for dist in range(int(map_scale*map2D.__len__())):
            x = px - math.sin(ca) * dist
            y = py + math.cos(ca) * dist
            r = int(x/map_scale)
            c = int(y/map_scale)
            if map2D[c][r] == 1:
                pygame.draw.line(screen, (0, 255, 255), (px, py), (x, y))
                total_dist = math.dist([px, py], [x, y])
                draw3D(pa, ca, ray, total_dist)
                if total_dist <= 1:
                    px = tx
                    py = ty
                else:
                    tx = px
                    ty = py
                break
        ca += pfov / rays

def draw3D(player_angle, ray_angle, ray, total_dist):
    current_angle = max(0, min(player_angle-ray_angle, 2*math.pi)) # current angle between 0 and 2pi (?) unsure if necessary
    total_dist *= math.cos(current_angle)

    line_height = min((map_scale * 320/max(1, total_dist)), 320)
    line_width = SCREEN_WIDTH/2 / rays

    # black and white shader
    line_color_unit = 1/(max(1, total_dist * total_dist * 0.0001)) * 255
    if total_dist <= 1:
        line_color_unit = 0
    line_color = (line_color_unit, line_color_unit, line_color_unit)
    # line_color = (255,0,0)

    pygame.draw.rect(screen, line_color, pygame.Rect(SCREEN_HEIGHT+ray*line_width, (SCREEN_HEIGHT/2) - (line_height/2), line_width +1, line_height))

def draw_window():
    screen.fill((125,125,125))

if __name__ == "__main__":
    main()