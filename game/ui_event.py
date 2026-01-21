
subscribers = []


def handle_events(events, game):
    for event_handlers in subscribers:
        for event in events:
            if event.type not in event_handlers:
                continue
            event_handlers[event.type](event, game)
