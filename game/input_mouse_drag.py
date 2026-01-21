import pygame


mouse_drag_target = False


def on_mouse_down(event, game):
    global mouse_drag_target
    mouse_drag_target = game.find_point_from_pos(event.pos)


def on_mouse_up(event, game):
    global mouse_drag_target
    mouse_drag_target = False
    game.check_win_condition()
    game.redraw_required = True


def on_mouse_move(event, game):
    global mouse_drag_target
    if mouse_drag_target:
        mouse_drag_target.x, mouse_drag_target.y = event.pos
        game.redraw_required = True


def MouseDragHandler():
    return {
        pygame.MOUSEBUTTONDOWN: on_mouse_down,
        pygame.MOUSEBUTTONUP: on_mouse_up,
        pygame.MOUSEMOTION: on_mouse_move
    }
