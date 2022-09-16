import math
import random
import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 512
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Raycasting")

FPS = 60

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