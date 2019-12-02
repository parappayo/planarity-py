import sys, time, math, pygame

import level_generator

background_colour = 0, 0, 0 # rgb 256
screen_size = 1024, 768 # pixels
point_radius = 24

class GameState:
	def __init__(self, points, connections):
		self.points = points
		self.connections = connections
		self.mouse_drag_target = False

def arrange_in_circle(points):
	theta = 0
	theta_step = (2 * math.pi) / len(points)
	for point in points:
		point.x = (math.cos(theta) + 1) * screen_size[0] / 2
		point.y = (math.sin(theta) + 1) * screen_size[1] / 2
		theta += theta_step

def find_point_from_pos(points, pos, radius):
	for point in points:
		dx = point.x - pos[0]
		dy = point.y - pos[1]
		if dx * dx + dy * dy < radius * radius:
			return point
	return False

def draw_line(surface, from_point, to_point):
	start_pos = (from_point.x, from_point.y)
	end_pos = (to_point.x, to_point.y)
	width = 4
	colour = 220, 220, 220
	pygame.draw.line(surface, colour, start_pos, end_pos, width)

def draw_point(surface, point):
	inner_colour = 160, 160, 220
	outer_colour = 220, 220, 220
	border_thickness = 4
	center = int(point.x), int(point.y)
	pygame.draw.circle(surface, inner_colour, center, point_radius)
	pygame.draw.circle(surface, outer_colour, center, point_radius, border_thickness)

def draw_frame(surface, game_state):
	surface.fill(background_colour)

	for connection in game_state.connections:
		draw_line(surface, connection[0], connection[1])

	for point in game_state.points:
		draw_point(surface, point)

	pygame.display.flip()

def on_quit(event, game_state):
	sys.exit()

def on_key_down(event, game_state):
	if event.key == pygame.K_ESCAPE:
		sys.exit()

def on_mouse_down(event, game_state):
	game_state.mouse_drag_target = find_point_from_pos(game_state.points, event.pos, point_radius)

def on_mouse_up(event, game_state):
	game_state.mouse_drag_target = False

def on_mouse_move(event, game_state):
	target = game_state.mouse_drag_target
	if target:
		target.x, target.y = event.pos

def handle_input_events(input_event_handlers, game_state):
	for event in pygame.event.get():
		if not event.type in input_event_handlers:
			continue
		input_event_handlers[event.type](event, game_state)

def game_loop(game_state):
	input_event_handlers = {
		pygame.QUIT: on_quit,
		pygame.KEYDOWN: on_key_down,
		pygame.MOUSEBUTTONDOWN: on_mouse_down,
		pygame.MOUSEBUTTONUP: on_mouse_up,
		pygame.MOUSEMOTION: on_mouse_move
	}

	pygame.init()

	screen = pygame.display.set_mode(screen_size)

	while True:
		handle_input_events(input_event_handlers, game_state)
		draw_frame(screen, game_state)
		sys.stdout.flush()
		time.sleep(0.05) # cap at 20 fps

if __name__ == '__main__':
	points, connections = level_generator.generate_level(5)
	arrange_in_circle(points)
	game_loop(GameState(points, connections))
