
from random import *
from geometry2d import *

def random_line():
	result = Line()
	result.y_intercept = randint(-500, 500)
	result.slope = randint(-20, 20)
	return result

def generate_intersections(line_count):
	intersections = []
	lines = []

	for i in range(0, line_count):
		line = random_line()

		for old_line in lines:
			point = intersection_point(line, old_line)
			if point == False:
				continue
			intersections.append({
				'point': point,
				'from_line': line,
				'to_line': old_line
				})
		lines.append(line)

	return intersections

if __name__ == '__main__':
	print(generate_intersections(4))
