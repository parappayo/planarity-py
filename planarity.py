import sys, time, pygame

import level_generator, game_input, game_state

def draw_line(surface, game, from_point, to_point):
	start_pos = (from_point.x, from_point.y)
	end_pos = (to_point.x, to_point.y)
	width = 4
	colour = 220, 220, 220
	pygame.draw.line(surface, colour, start_pos, end_pos, width)

def draw_point(surface, game, point):
	inner_colour = 160, 160, 220
	outer_colour = 220, 220, 220
	border_thickness = 4
	center = int(point.x), int(point.y)
	pygame.draw.circle(surface, inner_colour, center, game.point_radius)
	pygame.draw.circle(surface, outer_colour, center, game.point_radius, border_thickness)

def draw_frame(surface, game):
	surface.fill(game.background_colour)

	for connection in game.connections:
		draw_line(surface, game, connection[0], connection[1])

	for point in game.points:
		draw_point(surface, game, point)

	pygame.display.flip()

def game_loop(game):
	pygame.init()

	screen = pygame.display.set_mode(game.screen_size)

	while True:
		game_input.handle_events(pygame.event.get(), game)
		draw_frame(screen, game)
		sys.stdout.flush()
		time.sleep(0.05) # cap at 20 fps

if __name__ == '__main__':
	game = game_state.GameState()
	game.generate_level(5)
	game.arrange_in_circle()
	game_loop(game)
