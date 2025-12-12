# engine/game_manager.py

import pygame
import math
import random
from config.constants import (
    BACKGROUND, TEXT_COLOR, HUD_COLOR,
    MAZE_LAYOUT, SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE
)
from .maze import Maze
from .hunter import Hunter
from .ghost import Ghost
from ai.agent import HunterAgent


class GameManager:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True

        self.maze = Maze()
        self.hunter = None
        self.ghost = None

        self.score = 0
        self.captures = 0
        self.win = False

        self.font = pygame.font.SysFont("Arial", 22)

        self._init_entities()
        self.agent = HunterAgent(self.hunter, self.ghost)

    def _init_entities(self):
        # Find S (hunter start)
        for r, row in enumerate(MAZE_LAYOUT):
            for c, tile in enumerate(row):
                if tile == "S":
                    self.hunter = Hunter(r, c)

        # Initial ghost position
        self.ghost = Ghost(8, 20)

    def reset(self):
        """Restart the game."""
        self.__init__(self.screen, self.clock)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if self.win and event.key == pygame.K_r:
                    self.reset()

    def update(self, dt):
        if self.win:
            return  # stop updating movement on win

        # AI moves hunter
        self.agent.update()
        self.hunter.update(dt, self.maze)

        # Ghost moves
        self.ghost.update(dt, self.maze)

        # -------- CAPTURE CHECK --------
        dx = self.hunter.x - self.ghost.x
        dy = self.hunter.y - self.ghost.y

        if (dx * dx + dy * dy) ** 0.5 < TILE_SIZE * 0.45:
            self.score += 50
            self.captures += 1

            # WIN CONDITION after 10 captures
            if self.captures >= 5:
                self.win = True
                return

            # Safe respawn far from hunter
            while True:
                r = random.randint(1, len(MAZE_LAYOUT)-2)
                c = random.randint(1, len(MAZE_LAYOUT[0])-2)

                if MAZE_LAYOUT[r][c] != "#":
                    dist = abs(r - self.hunter.row) + abs(c - self.hunter.col)
                    if dist > 6:
                        self.ghost = Ghost(r, c)
                        self.agent.ghost = self.ghost
                        break

    def draw(self):
        self.screen.fill(BACKGROUND)
        self.maze.draw(self.screen)

        self.hunter.draw(self.screen)
        self.ghost.draw(self.screen)

        # HUD
        pygame.draw.rect(
            self.screen,
            (0, 0, 0),
            (0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40),
        )
        score_text = self.font.render(f"Score: {self.score}", True, HUD_COLOR)
        captures_text = self.font.render(f"Captures: {self.captures}/5", True, HUD_COLOR)

        self.screen.blit(score_text, (10, SCREEN_HEIGHT - 32))
        self.screen.blit(captures_text, (150, SCREEN_HEIGHT - 32))

        # WIN MESSAGE
        if self.win:
            msg = self.font.render("YOU WIN! Press R to Restart", True, TEXT_COLOR)
            self.screen.blit(
                msg,
                (SCREEN_WIDTH // 2 - msg.get_width() // 2, SCREEN_HEIGHT // 2),
            )

        pygame.display.flip()

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000.0
            self.handle_events()
            self.update(dt)
            self.draw()
