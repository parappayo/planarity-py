import pygame, sys, time

from game import *
import game_state # TODO: move to package "planarity"


def game_loop(game):
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


if __name__ == '__main__':
    main_game = game_state.GameState()
    main_game.start_level(1)
    game_loop(main_game)
