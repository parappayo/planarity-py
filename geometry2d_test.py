
import unittest
import geometry2d

class TestPoint(unittest.TestCase):

	def test_str(self):
		self.assertEqual(str(geometry2d.Point(1, 2)), "(1, 2)")

class TestLine(unittest.TestCase):

	def test_value_at_x(self):
		line = geometry2d.Line()
		line.y_intercept = 0
		line.slope = 1
		self.assertEqual(line.value_at_x(3), 3)

class TestFunctions(unittest.TestCase):

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
