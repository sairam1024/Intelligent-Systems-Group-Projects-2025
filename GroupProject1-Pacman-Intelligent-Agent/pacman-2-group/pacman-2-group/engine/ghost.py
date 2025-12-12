# engine/ghost.py

import pygame
import random
from config.constants import TILE_SIZE, GHOST_COLOR


class Ghost:
    def __init__(self, r, c):
        self.row = r
        self.col = c
        self.x = c*TILE_SIZE + TILE_SIZE/2
        self.y = r*TILE_SIZE + TILE_SIZE/2
        self.speed = 70
        self.dir = random.choice([(1,0),(-1,0),(0,1),(0,-1)])
        self.captures = 0
        self.win = False


    def update(self, dt, maze):
        dr, dc = self.dir
        nr = self.row + dr
        nc = self.col + dc

        if maze.is_wall(nr, nc):
            self.dir = random.choice([(1,0),(-1,0),(0,1),(0,-1)])
            return

        tx = nc*TILE_SIZE + TILE_SIZE/2
        ty = nr*TILE_SIZE + TILE_SIZE/2

        dx = tx - self.x
        dy = ty - self.y
        dist = (dx*dx + dy*dy)**0.5

        if dist < 2:
            self.row = nr
            self.col = nc
            self.x = tx
            self.y = ty
            return

        self.x += (dx/dist) * self.speed * dt
        self.y += (dy/dist) * self.speed * dt

    def draw(self, screen):
        radius = TILE_SIZE//2 - 6
        offset = TILE_SIZE * 0.20  # move down 20%
        pygame.draw.circle(
            screen,
            GHOST_COLOR,
            (int(self.x), int(self.y + offset)),
            radius
        )
