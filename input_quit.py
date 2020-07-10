import sys, pygame
import game_input


def on_quit(event, game):
    sys.exit()


def on_key_down(event, game):
    if event.key == pygame.K_ESCAPE:
        sys.exit()


game_input.subscribers.append({
        pygame.QUIT: on_quit,
        pygame.KEYDOWN: on_key_down
    })
