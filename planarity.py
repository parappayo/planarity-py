
from random import *
from geometry2d import *

def random_line():
	result = Line()
	result.y_intercept = randint(-500, 500)
	result.slope = randint(-20, 20)
	return result

def generate_graph(line_count):
	lines = []
	for i in range(0, line_count):
		line = random_line()
		intersection_points = []

		print(line)
		for old_line in lines:
			point = intersection_point(line, old_line)
			intersection_points.append(point)
			print("\t", point)
		lines.append(line)

if __name__ == '__main__':
	generate_graph(4)
