import pygame
import game_input

def on_mouse_down(event, game):
    game.mouse_drag_target = game.find_point_from_pos(event.pos)


def on_mouse_up(event, game):
    game.mouse_drag_target = False
    game.check_win_condition()


def on_mouse_move(event, game):
    target = game.mouse_drag_target
    if target:
        target.x, target.y = event.pos
        game.redraw_required = True


game_input.subscribers.append({
        pygame.MOUSEBUTTONDOWN: on_mouse_down,
        pygame.MOUSEBUTTONUP: on_mouse_up,
        pygame.MOUSEMOTION: on_mouse_move
	})
