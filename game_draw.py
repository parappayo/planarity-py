import pygame

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
