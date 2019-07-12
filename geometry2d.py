
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __eq__(self, other):
		if not isinstance(other, Point): return False
		return self.x == other.x and self.y == other.y

	def __repr__(self):
		return '<Point x:{point.x:.2f}, y:{point.y:.2f}>'.format(point=self)

	def __str__(self):
		return '({point.x:.2f}, {point.y:.2f})'.format(point=self)

class Line:
	def __init__(self):
		self.y_intercept = 0
		self.slope = 0

	def __eq__(self, other):
		if not isinstance(other, Line): return False
		return self.y_intercept == other.y_intercept and self.slope == other.slope

	def __repr__(self):
		return '<Line y_intercept:{line.y_intercept:.2f}, slope:{line.slope:.2f}>'.format(line=self)

	def __str__(self):
		return '(y_intercept={line.y_intercept:.2f}, slope={line.slope:.2f})'.format(line=self)

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

class Intersection:
	def __init__(self, from_line, to_line):
		self.point = intersection_point(from_line, to_line)
		self.from_line = from_line
		self.to_line = to_line

	def __repr__(self):
		return '<Intersection point:{i.point}, from_line:{i.from_line}, to_line:{i.to_line}>'.format(i=self)

	def __str__(self):
		return '(point:{i.point}, from_line:{i.from_line}, to_line:{i.to_line})'.format(i=self)

	def is_valid(self):
		return not self.point == False

	def is_on_line(self, line):
		return (self.is_valid() and
			(self.from_line == line or
			self.to_line == line))
