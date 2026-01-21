import pygame, sys, time

from planarity.game_state import GameState
from game import *


if __name__ == '__main__':
    game = GameState()
    game.start_level(1)

    pygame.init()
    screen = pygame.display.set_mode(game.screen_size)
    pygame.display.set_caption("Planarity")
    graphics = Graphics(screen, game)

    input_handler = InputHandler()
    input_handler.add(QuitHandler())
    input_handler.add(MouseDragHandler())

    while True:
        input_handler.handle_events(pygame.event.get(), game)
        if game.redraw_required:
            graphics.draw_frame()
            game.redraw_required = False
        time.sleep(0.001)
