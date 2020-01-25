import random

from geometry2d import Point, Line, LineSegment, Intersection

def uniq_rand_int(lowest, highest, used_values, max_retries):
	result = random.randint(lowest, highest)

	loop_count = 0
	while result in used_values:
		result = randint(lowest, highest)
		loop_count += 1

		if loop_count > max_retries:
			print("warning: failed to generate unique random int")
			break

	used_values[result] = True
	return result

def random_line(used_y_intercepts, used_slopes):
	result = Line()
	result.y_intercept = uniq_rand_int(-1000, 1000, used_y_intercepts, 100)
	result.slope = uniq_rand_int(-200, 200, used_slopes, 100)
	return result

def generate_lines_intersections(line_count):
	intersections = []
	lines = []

	used_y_intercepts = {}
	used_slopes = {}

	for i in range(0, line_count):
		line = random_line(used_y_intercepts, used_slopes)

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
				connections.append(LineSegment(previous_point, point))
			previous_point = point

	return set(points), connections

def generate_level(line_count):
	lines, intersections = generate_lines_intersections(line_count)
	points, connections = find_point_neighbour_pairs(lines, intersections)
	return points, connections
