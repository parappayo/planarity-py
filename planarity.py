import pygame
import sys
import time

import game_draw
import game_input
import game_state


def game_loop(game):
    pygame.init()
    game_draw.init(game)
    screen = pygame.display.set_mode(game.screen_size)
    pygame.display.set_caption("Planarity")

    while True:
        game_input.handle_events(pygame.event.get(), game)
        if game.redraw_required:
            game_draw.draw_frame(screen, game)
            game.redraw_required = False
        time.sleep(0.001)


if __name__ == '__main__':
    main_game = game_state.GameState()
    main_game.start_level(1)
    game_loop(main_game)
