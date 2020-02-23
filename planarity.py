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
            start = time.perf_counter()
            game_draw.draw_frame(screen, game)
            game.redraw_required = False
            print("draw frame time: ", time.perf_counter() - start)
        sys.stdout.flush()
        time.sleep(0.001)


if __name__ == '__main__':
    main_game = game_state.GameState()
    main_game.generate_level(5)
    main_game.arrange_in_circle()
    game_loop(main_game)
