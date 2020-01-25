import math

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __eq__(self, other):
		if not isinstance(other, Point): return False
		return self.x == other.x and self.y == other.y

	def __hash__(self):
		return hash((self.x, self.y))

	def __repr__(self):
		return '<Point x:{point.x:.2f}, y:{point.y:.2f}>'.format(point=self)

	def __str__(self):
		return '({point.x:.2f}, {point.y:.2f})'.format(point=self)

	def as_tuple(self):
		return (self.x, self.y)

def slope(point1, point2):
	dx = (point2.x - point1.x)
	if dx == 0:
		return math.nan
	return (point2.y - point1.y) / dx

def slow_is_clockwise(point1, point2, point3):
	"""Reference implementation; easy to grok, but does unnecessary branches and divides.
	Handling of edge cases where points share an x-coordinate is different than is_clockwise."""
	return slope(point1, point2) > slope(point1, point3)

def is_clockwise(point1, point2, point3):
	return (point2.y - point1.y) * (point3.x - point1.x) > (point3.y - point1.y) * (point2.x - point1.x)

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

class LineSegment:
	def __init__(self, point1, point2):
		self.point1 = point1
		self.point2 = point2

	def __getitem__(self, index):
		if index == 0: return self.point1
		if index == 1: return self.point2

	def __eq__(self, other):
		if not isinstance(other, LineSegment): return False
		return self.point1 == other.point1 and self.point2 == other.point2

	def __repr__(self):
		return '<LineSegment point1:{line.point1}, point2:{line.point2}>'.format(line=self)

	def __str__(self):
		return '(point1={line.point1}, point2={line.point2})'.format(line=self)

	def intersects(self, other):
		return ((is_clockwise(self.point1, other.point1, other.point2) !=
				is_clockwise(self.point2, other.point1, other.point2)) and
			(is_clockwise(self.point1, self.point2, other.point1) !=
				is_clockwise(self.point1, self.point2, other.point2)))

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
