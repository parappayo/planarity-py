from random import *
from geometry2d import *

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

def find_point_neighbour_pairs(lines, intersections):
	points = []
	connections = []

	for line in lines:
		points_on_line = find_points_along_line(line, intersections)

		previous_point = False
		for point in points_on_line:
			points.append(point)
			if previous_point:
				connections.append((previous_point, point))
			previous_point = point

	return set(points), connections

def generate_level(line_count):
	lines, intersections = generate_lines_intersections(line_count)
	points, connections = find_point_neighbour_pairs(lines, intersections)
	return points, connections
