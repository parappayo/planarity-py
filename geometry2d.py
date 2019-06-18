
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __str__(self):
		return '({point.x}, {point.y})'.format(point=self)

class Line:
	def __init__(self):
		self.y_intercept = 0
		self.slope = 0

	def __eq__(self, other):
		return self.y_intercept == other.y_intercept and self.slope == other.slope

	def __str__(self):
		return 'y_intercept={line.y_intercept}, slope={line.slope}'.format(line=self)

	def value_at_x(self, x):
		return self.y_intercept + self.slope * x

def intersection_x(line1, line2):
	delta_y_intercept = line1.y_intercept - line2.y_intercept
	delta_slope = line1.slope - line2.slope
	if delta_slope == 0:
		return False
	return -delta_y_intercept / delta_slope

def intersection_point(line1, line2):
	x = intersection_x(line1, line2)
	if x == False:
		return False
	y = line1.value_at_x(x)
	return Point(x, y)
