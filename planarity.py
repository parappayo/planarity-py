
import sys, math, pygame

from level_generator import *

background_colour = 0, 0, 0 # rgb 256
screen_size = 1024, 768 # pixels

def arrange_in_circle(points):
	theta = 0
	theta_step = (2 * math.pi) / len(points)
	for point in points:
		point.x = (math.cos(theta) + 1) * screen_size[0] / 2
		point.y = (math.sin(theta) + 1) * screen_size[1] / 2
		theta += theta_step

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
	radius = 24
	pygame.draw.circle(surface, inner_colour, center, radius)
	pygame.draw.circle(surface, outer_colour, center, radius, border_thickness)

def draw_frame(surface, points, connections):
	for connection in connections:
		draw_line(surface, connection[0], connection[1])

	for point in points:
		draw_point(surface, point)

def game_loop(points, connections):
	pygame.init()

	screen = pygame.display.set_mode(screen_size)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		screen.fill(background_colour)
		draw_frame(screen, points, connections)
		pygame.display.flip()

if __name__ == '__main__':
	points, connections = generate_level(5)
	arrange_in_circle(points)
	game_loop(points, connections)
