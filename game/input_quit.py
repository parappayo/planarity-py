import sys, pygame

from .ui_event import *


def on_quit(event, game):
    sys.exit()


def on_key_down(event, game):
    if event.key == pygame.K_ESCAPE:
        sys.exit()


subscribers.append({
        pygame.QUIT: on_quit,
        pygame.KEYDOWN: on_key_down
    })
