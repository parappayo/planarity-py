import unittest, math

from geo2d import *


class TestLine(unittest.TestCase):

    def test_value_at_x(self):
        line = Line()
        line.y_intercept = 0
        line.slope = 1
        self.assertEqual(line.value_at_x(3), 3)


class TestLineSegment(unittest.TestCase):

    def test_intersects(self):
        tests = [
            (LineSegment(
                Point(1, 1), Point(1, 2)),
             LineSegment(
                 Point(2, 1), Point(2, 2)),
             False),
            (LineSegment(
                Point(1, 1), Point(2, 2)),
             LineSegment(
                 Point(2, 1), Point(1, 2)),
             True),
            (LineSegment(
                Point(1, 1), Point(1, 1)),
             LineSegment(
                 Point(2, 2), Point(2, 2)),
             False),
            (LineSegment(
                Point(0, 0), Point(-1, 0)),
             LineSegment(
                 Point(0, 1), Point(-1, 1)),
             False),
            (LineSegment(
                Point(0, 0), Point(-1, 5)),
             LineSegment(
                 Point(0, 1), Point(-1, 1)),
             True),
            (LineSegment(
                Point(0, 0), Point(-1, 0.5)),
             LineSegment(
                 Point(0, 1), Point(-1, 1)),
             False),

            # shares point tests
            (LineSegment(
                Point(1, 1), Point(2, 1)),
             LineSegment(
                 Point(2, 1), Point(2, 2)),
             False),
            (LineSegment(
                Point(6, 5), Point(7, 0)),
             LineSegment(
                 Point(7, 0), Point(2, 0)),
             False)

            # parallel lines tests
            # (LineSegment(
            # 	Point(1, 1), Point(1, 2)),
            # LineSegment(
            # 	Point(1, 2), Point(1, 1.5)),
            # True),
            # (LineSegment(
            # 	Point(1, 1), Point(1, 2)),
            # LineSegment(
            # 	Point(1, 2), Point(1, 3)),
            # False)
        ]

        for test in tests:
            with self.subTest(test=test):
                line1, line2, expected = test
            self.assertEqual(line1.intersects(line2), expected)
            self.assertEqual(line2.intersects(line1), expected)


class TestIntersection(unittest.TestCase):

    def test_is_valid(self):
        line1 = Line()
        line1.y_intercept = 0
        line1.slope = 1

        line2 = Line()
        line2.y_intercept = 1
        line2.slope = 0

        intersection = Intersection(line1, line2)
        self.assertTrue(intersection.is_valid())

    def test_is_valid_parallel_lines(self):
        line1 = Line()
        line1.y_intercept = 0
        line1.slope = 0

        line2 = Line()
        line2.y_intercept = 1
        line2.slope = 0

        intersection = Intersection(line1, line2)
        self.assertFalse(intersection.is_valid())


class TestFunctions(unittest.TestCase):

    def test_intersection_x_parallel_lines(self):
        line1 = Line()
        line1.y_intercept = 0
        line1.slope = 0

        line2 = Line()
        line2.y_intercept = 1
        line2.slope = 0

        self.assertEqual(intersection_x(line1, line2), False)

    def test_intersection_point(self):
        line1 = Line()
        line1.y_intercept = 0
        line1.slope = 0.5

        line2 = Line()
        line2.y_intercept = 3
        line2.slope = 0.2

        self.assertEqual(intersection_point(line1, line2), Point(10, 5))

    def test_intersection_point_parallel_lines(self):
        line1 = Line()
        line1.y_intercept = 0
        line1.slope = 0

        line2 = Line()
        line2.y_intercept = 1
        line2.slope = 0

        self.assertEqual(intersection_point(line1, line2), False)
