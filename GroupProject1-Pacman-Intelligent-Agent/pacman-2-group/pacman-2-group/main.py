import pygame
from config.settings import SETTINGS
from engine.game_manager import GameManager


def main():
    pygame.init()
    screen = pygame.display.set_mode(
        (SETTINGS["screen_width"], SETTINGS["screen_height"])
    )
    pygame.display.set_caption(SETTINGS["window_title"])
    clock = pygame.time.Clock()

    game = GameManager(screen, clock)
    game.run()

    pygame.quit()


if __name__ == "__main__":
    main()
