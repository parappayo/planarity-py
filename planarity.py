
from random import *
from geometry2d import *

def random_line():
	result = Line()
	result.y_intercept = randint(-500, 500)
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

if __name__ == '__main__':
	lines, intersections = generate_lines_intersections(4)
	print("lines: ", lines)
	print("intersections: ", intersections)
	for line in lines:
		points_on_line = find_points_along_line(line, intersections)
		print("points on line: ", line, points_on_line)