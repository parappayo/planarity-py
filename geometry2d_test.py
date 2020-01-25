
import unittest, math
import geometry2d

class TestPoint(unittest.TestCase):

	def test_str(self):
		self.assertEqual(str(geometry2d.Point(1, 2)), "(1.00, 2.00)")

class TestLine(unittest.TestCase):

	def test_value_at_x(self):
		line = geometry2d.Line()
		line.y_intercept = 0
		line.slope = 1
		self.assertEqual(line.value_at_x(3), 3)

class TestLineSegment(unittest.TestCase):

	def test_intersects(self):
		tests = [
			(geometry2d.LineSegment(
				geometry2d.Point(1, 1), geometry2d.Point(1, 2)),
			geometry2d.LineSegment(
				geometry2d.Point(2, 1), geometry2d.Point(2, 2)),
			False),
			(geometry2d.LineSegment(
				geometry2d.Point(1, 1), geometry2d.Point(2, 2)),
			geometry2d.LineSegment(
				geometry2d.Point(2, 1), geometry2d.Point(1, 2)),
			True),
			(geometry2d.LineSegment(
				geometry2d.Point(1, 1), geometry2d.Point(1, 1)),
			geometry2d.LineSegment(
				geometry2d.Point(2, 2), geometry2d.Point(2, 2)),
			False),
			(geometry2d.LineSegment(
				geometry2d.Point(0, 0), geometry2d.Point(-1, 0)),
			geometry2d.LineSegment(
				geometry2d.Point(0, 1), geometry2d.Point(-1, 1)),
			False),
			(geometry2d.LineSegment(
				geometry2d.Point(0, 0), geometry2d.Point(-1, 5)),
			geometry2d.LineSegment(
				geometry2d.Point(0, 1), geometry2d.Point(-1, 1)),
			True),
			(geometry2d.LineSegment(
				geometry2d.Point(0, 0), geometry2d.Point(-1, 0.5)),
			geometry2d.LineSegment(
				geometry2d.Point(0, 1), geometry2d.Point(-1, 1)),
			False),

			# shares point tests
			(geometry2d.LineSegment(
				geometry2d.Point(1, 1), geometry2d.Point(2, 1)),
			geometry2d.LineSegment(
				geometry2d.Point(2, 1), geometry2d.Point(2, 2)),
			False),
			(geometry2d.LineSegment(
				geometry2d.Point(6, 5), geometry2d.Point(7, 0)),
			geometry2d.LineSegment(
				geometry2d.Point(7, 0), geometry2d.Point(2, 0)),
			False)

			# parallel lines tests
			# (geometry2d.LineSegment(
			# 	geometry2d.Point(1, 1), geometry2d.Point(1, 2)),
			# geometry2d.LineSegment(
			# 	geometry2d.Point(1, 2), geometry2d.Point(1, 1.5)),
			# True),
			# (geometry2d.LineSegment(
			# 	geometry2d.Point(1, 1), geometry2d.Point(1, 2)),
			# geometry2d.LineSegment(
			# 	geometry2d.Point(1, 2), geometry2d.Point(1, 3)),
			# False)
		]

		for test in tests:
			with self.subTest(test=test):
				line1, line2, expected = test
			self.assertEqual(line1.intersects(line2), expected)
			self.assertEqual(line2.intersects(line1), expected)

class TestIntersection(unittest.TestCase):

	def test_is_valid(self):
		line1 = geometry2d.Line()
		line1.y_intercept = 0
		line1.slope = 1

		line2 = geometry2d.Line()
		line2.y_intercept = 1
		line2.slope = 0

		intersection = geometry2d.Intersection(line1, line2)
		self.assertTrue(intersection.is_valid())

	def test_is_valid_parallel_lines(self):

		line1 = geometry2d.Line()
		line1.y_intercept = 0
		line1.slope = 0

		line2 = geometry2d.Line()
		line2.y_intercept = 1
		line2.slope = 0

		intersection = geometry2d.Intersection(line1, line2)
		self.assertFalse(intersection.is_valid())

class TestFunctions(unittest.TestCase):

	def test_slope(self):
		tests = [
			(geometry2d.Point( 0,  0), geometry2d.Point( 1,  0), 0),
			(geometry2d.Point( 0,  0), geometry2d.Point( 1,  1), 1),
			(geometry2d.Point( 0,  0), geometry2d.Point( 0,  1), math.nan),
			(geometry2d.Point( 1,  1), geometry2d.Point( 1,  0), math.nan),
			(geometry2d.Point( 0,  0), geometry2d.Point( 1,  3), 3),
			(geometry2d.Point( 0,  0), geometry2d.Point(-1,  3), -3),
			(geometry2d.Point( 0,  0), geometry2d.Point(-1, -3), 3),
			(geometry2d.Point( 1,  1), geometry2d.Point( 2,  2), 1),
			(geometry2d.Point(-1, -1), geometry2d.Point(-2, -2), 1),
			(geometry2d.Point( 1,  1), geometry2d.Point( 2, -2), -3),
		]

		for test in tests:
			with self.subTest(test=test):
				point1, point2, expected = test
				self.assertTrue(math.isnan(geometry2d.slope(point1, point1)))
				if math.isnan(expected):
					self.assertTrue(math.isnan(geometry2d.slope(point1, point2)))
					self.assertTrue(math.isnan(geometry2d.slope(point2, point1)))
				else:
					self.assertEqual(geometry2d.slope(point1, point2), expected)
					self.assertEqual(geometry2d.slope(point2, point1), expected)

	def test_is_clockwise(self):
		tests = [
			(geometry2d.Point( 0,  0), geometry2d.Point( 0,  0), geometry2d.Point( 0,  0), False),
			(geometry2d.Point( 0,  0), geometry2d.Point( 0,  0), geometry2d.Point( 1,  1), False),
			(geometry2d.Point( 0,  0), geometry2d.Point( 0,  0), geometry2d.Point( 1, -1), False),
			(geometry2d.Point( 0,  0), geometry2d.Point( 1,  1), geometry2d.Point( 0,  0), False),
			(geometry2d.Point( 0,  0), geometry2d.Point( 1, -1), geometry2d.Point( 0,  0), False),
			(geometry2d.Point( 0,  0), geometry2d.Point( 1,  0), geometry2d.Point( 1, -1), True),
			(geometry2d.Point( 0,  0), geometry2d.Point( 1,  0), geometry2d.Point( 1,  1), False),
			(geometry2d.Point( 1,  1), geometry2d.Point( 1,  0), geometry2d.Point( 0,  0), True),
			(geometry2d.Point( 5,  5), geometry2d.Point( 6,  4), geometry2d.Point( 5,  3), True),
			(geometry2d.Point( 5,  5), geometry2d.Point( 6,  4), geometry2d.Point( 7,  3), False),
		]

		for test in tests:
			with self.subTest(test=test):
				point1, point2, point3, expected = test
				if (not math.isnan(geometry2d.slope(point1, point2)) and
						not math.isnan(geometry2d.slope(point1, point3))):
					self.assertEqual(
						geometry2d.is_clockwise(point1, point2, point3),
						geometry2d.slow_is_clockwise(point1, point2, point3))
				self.assertEqual(geometry2d.is_clockwise(point1, point2, point3), expected)

	def test_intersection_x_parallel_lines(self):
		line1 = geometry2d.Line()
		line1.y_intercept = 0
		line1.slope = 0

		line2 = geometry2d.Line()
		line2.y_intercept = 1
		line2.slope = 0

		self.assertEqual(geometry2d.intersection_x(line1, line2), False)

	def test_intersection_point(self):
		line1 = geometry2d.Line()
		line1.y_intercept = 0
		line1.slope = 0.5

		line2 = geometry2d.Line()
		line2.y_intercept = 3
		line2.slope = 0.2

		self.assertEqual(geometry2d.intersection_point(line1, line2), geometry2d.Point(10, 5))

	def test_intersection_point_parallel_lines(self):
		line1 = geometry2d.Line()
		line1.y_intercept = 0
		line1.slope = 0

		line2 = geometry2d.Line()
		line2.y_intercept = 1
		line2.slope = 0

		self.assertEqual(geometry2d.intersection_point(line1, line2), False)

if __name__ == '__main__':
	unittest.main()
