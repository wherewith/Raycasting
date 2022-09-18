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
my_font = pygame.font.SysFont('Calibri', 50, bold = True)
pygame.display.set_icon(my_font.render('γ', True, (0,150,50)))

FPS = 60
RAYS = 120

p = Player.Player(
    x           = SCREEN_WIDTH/2 /2 + 25,
    y           = SCREEN_HEIGHT/2 + 25,
    radius      = 8,
    velocity    = 3,
    angle       = math.pi,
    turn_speed  = 0.05,
    fov         = math.pi / 3
)

game_map = Map.Map(
    s     = 8,
    scale = 64
)
game_map.generate()


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

        key_pressed = pygame.key.get_pressed()
        handle_input(p, key_pressed)

        draw_window()
        game_map.draw(screen)
        p.draw(screen)
        raycast(p, game_map, RAYS)

        pygame.display.flip()
    pygame.quit()


def handle_input(player, key_pressed):
    player.angle = player.angle % (2*math.pi)
    if key_pressed[ord('w')]:  # -
        player.x -= math.sin(player.angle) * player.velocity
        player.y += math.cos(player.angle) * player.velocity
    if key_pressed[ord('a')]:
        player.angle -= player.turn_speed
    if key_pressed[ord('s')]: # +
        player.x += math.sin(player.angle) * player.velocity
        player.y -= math.cos(player.angle) * player.velocity
    if key_pressed[ord('d')]:
        player.angle += player.turn_speed

def raycast(player, curr_map, num_rays):
    curr_angle = player.angle - player.fov/2 # current angle of ray being cast
    for ray in range(num_rays):
        for dist in range(int(curr_map.scale*curr_map.map2D.__len__())):
            x = player.x - math.sin(curr_angle) * dist
            y = player.y + math.cos(curr_angle) * dist
            r = int(x/curr_map.scale)
            c = int(y/curr_map.scale)
            if curr_map.map2D[c][r] == 1:
                pygame.draw.line(screen, (0, 255, 255), (player.x, player.y), (x, y))
                total_dist = math.dist([player.x, player.y], [x, y])
                # draw3D(pa, ca, ray, total_dist)
                if total_dist <= 1:
                    player.x = player.tx
                    player.y = player.ty
                else:
                    player.tx = player.x
                    player.ty = player.y
                break
        curr_angle += player.fov / num_rays

def draw_window():
    screen.fill((125,125,125))


if __name__ == "__main__":
    main()