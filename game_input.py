import sys, pygame


def on_quit(event, game):
    sys.exit()


def on_key_down(event, game):
    if event.key == pygame.K_ESCAPE:
        sys.exit()


subscribers = [
    {
        pygame.QUIT: on_quit,
        pygame.KEYDOWN: on_key_down
    }
]


def handle_events(events, game):
    for event_handlers in subscribers:
        for event in events:
            if event.type not in event_handlers:
                continue
            event_handlers[event.type](event, game)
