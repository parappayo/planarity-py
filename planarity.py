
import sys, pygame

from random import *
from geometry2d import *

background_colour = 0, 0, 0 # rgb 256
screen_size = 1024, 768 # pixels

def random_line():
	result = Line()
	result.y_intercept = randint(100, 600)
	result.slope = randint(-20, 20)
	return result

def generate_lines_intersections(line_count):
	intersections = []
	lines = []

	for i in range(0, line_count):
		line = random_line()

		for old_line in lines:
			intersection = Intersection(line, old_line)
			if intersection.is_valid():
				intersections.append(intersection)

		lines.append(line)

	return (lines, intersections)

def find_points_along_line(line, intersections):
	intersections_on_line = filter(lambda x: x.is_on_line(line), intersections)
	points_on_line = map(lambda x: x.point, intersections_on_line)
	return list(points_on_line)

def draw_line(surface, line):
	start_pos = (0, line.y_intercept)
	end_pos = (screen_size[0], line.value_at_x(screen_size[0]))
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

def draw_frame(surface, lines, intersections):
	for line in lines:
		draw_line(surface, line)

	for intersection in intersections:
		draw_point(surface, intersection.point)

def game_loop(lines, intersections):
	pygame.init()

	screen = pygame.display.set_mode(screen_size)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		screen.fill(background_colour)
		draw_frame(screen, lines, intersections)
		pygame.display.flip()

if __name__ == '__main__':
	lines, intersections = generate_lines_intersections(4)
	print("lines: ", lines)
	print("intersections: ", intersections)
	for line in lines:
		points_on_line = find_points_along_line(line, intersections)
		print("points on line: ", line, points_on_line)

	game_loop(lines, intersections)
