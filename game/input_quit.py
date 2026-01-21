import sys, pygame


def on_quit(event, game):
    sys.exit()


def on_key_down(event, game):
    if event.key == pygame.K_ESCAPE:
        sys.exit()


def QuitHandler():
    return {
        pygame.QUIT: on_quit,
        pygame.KEYDOWN: on_key_down
    }
