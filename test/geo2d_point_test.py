import unittest, math

from geo2d import *


class TestPoint(unittest.TestCase):

    def test_str(self):
        self.assertEqual(str(Point(1, 2)), "(1.00, 2.00)")


class TestFunctions(unittest.TestCase):

    def test_slope(self):
        tests = [
            (Point(0, 0), Point(1, 0), 0),
            (Point(0, 0), Point(1, 1), 1),
            (Point(0, 0), Point(0, 1), math.nan),
            (Point(1, 1), Point(1, 0), math.nan),
            (Point(0, 0), Point(1, 3), 3),
            (Point(0, 0), Point(-1, 3), -3),
            (Point(0, 0), Point(-1, -3), 3),
            (Point(1, 1), Point(2, 2), 1),
            (Point(-1, -1), Point(-2, -2), 1),
            (Point(1, 1), Point(2, -2), -3),
        ]

        for test in tests:
            with self.subTest(test=test):
                point1, point2, expected = test
                self.assertTrue(math.isnan(slope(point1, point1)))
                if math.isnan(expected):
                    self.assertTrue(math.isnan(slope(point1, point2)))
                    self.assertTrue(math.isnan(slope(point2, point1)))
                else:
                    self.assertEqual(slope(point1, point2), expected)
                    self.assertEqual(slope(point2, point1), expected)

    def test_is_clockwise(self):
        tests = [
            (Point(0, 0), Point(0, 0), Point(0, 0), False),
            (Point(0, 0), Point(0, 0), Point(1, 1), False),
            (Point(0, 0), Point(0, 0), Point(1, -1), False),
            (Point(0, 0), Point(1, 1), Point(0, 0), False),
            (Point(0, 0), Point(1, -1), Point(0, 0), False),
            (Point(0, 0), Point(1, 0), Point(1, -1), True),
            (Point(0, 0), Point(1, 0), Point(1, 1), False),
            (Point(1, 1), Point(1, 0), Point(0, 0), True),
            (Point(5, 5), Point(6, 4), Point(5, 3), True),
            (Point(5, 5), Point(6, 4), Point(7, 3), False),
        ]

        for test in tests:
            with self.subTest(test=test):
                point1, point2, point3, expected = test
                if (not math.isnan(slope(point1, point2)) and
                        not math.isnan(slope(point1, point3))):
                    self.assertEqual(
                        is_clockwise(point1, point2, point3),
                        slow_is_clockwise(point1, point2, point3))
                self.assertEqual(is_clockwise(point1, point2, point3), expected)
