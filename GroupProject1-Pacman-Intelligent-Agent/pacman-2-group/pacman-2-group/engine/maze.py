import pygame
from config.constants import TILE_SIZE, MAZE_LAYOUT, WALL_COLOR, FLOOR_COLOR


class Maze:
    def __init__(self):
        self.grid = MAZE_LAYOUT

    def is_wall(self, r, c):
        return self.grid[r][c] == "#"

    def draw(self, screen):
        for r, row in enumerate(self.grid):
            for c, tile in enumerate(row):
                x = c * TILE_SIZE
                y = r * TILE_SIZE
                if tile == "#":
                    pygame.draw.rect(screen, WALL_COLOR, (x, y, TILE_SIZE, TILE_SIZE))
                else:
                    pygame.draw.rect(screen, FLOOR_COLOR, (x, y, TILE_SIZE, TILE_SIZE))
