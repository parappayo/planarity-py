
class InputHandler:
    def __init__(self):
        self.subs = []

    def add(self, sub):
        self.subs.append(sub)

    def handle_events(self, events, game):
        for handler in self.subs:
            for event in events:
                if event.type not in handler:
                    continue
                handler[event.type](event, game)
