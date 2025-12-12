import pygame
from config.constants import TILE_SIZE, HUNTER_COLOR


class Hunter:
    def __init__(self, r, c):
        self.row = r
        self.col = c
        self.x = c * TILE_SIZE + TILE_SIZE/2
        self.y = r * TILE_SIZE + TILE_SIZE/2
        self.speed = 140
        self.dir_row = 0
        self.dir_col = 0

    def set_direction(self, dr, dc):
        self.dir_row = dr
        self.dir_col = dc

    def update(self, dt, maze):
        nr = self.row + self.dir_row
        nc = self.col + self.dir_col

        if not maze.is_wall(nr, nc):
            tx = nc * TILE_SIZE + TILE_SIZE/2
            ty = nr * TILE_SIZE + TILE_SIZE/2

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
        size = TILE_SIZE//2 - 4
        pygame.draw.rect(screen, HUNTER_COLOR, (self.x-size, self.y-size, size*2, size*2), border_radius=4)
