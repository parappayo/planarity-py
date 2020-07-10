import unittest
import game_state
from geometry2d import Point


def floats_equal(x, y):
    """A deeply inadequate floating point comparison."""
    small = 0.0001
    if x == y or x < small and y < small:
        return True
    epsilon = max(abs(x), abs(y)) * small
    return abs(x - y) < epsilon


def points_equal(a, b):
    return floats_equal(a[0], b[0]) and floats_equal(a[1], b[1])


class TestFunctions(unittest.TestCase):

    def test_circle_4_points(self):
        count = 4
        points_gen = game_state.circle_points((0, 0), 1, count)
        points = [next(points_gen) for i in range(count)]

        self.assertEqual(len(points), count)
        self.assertTrue(points_equal(points[0], (1, 0)))
        self.assertTrue(points_equal(points[1], (0, 1)))
        self.assertTrue(points_equal(points[2], (-1, 0)))
        self.assertTrue(points_equal(points[3], (-1, -1)))

    def test_find_point_from(self):
        tests = [
            ((), (0, 0), 1000, False),
            ([], (0, 0), 1000, False),
            ([Point(0, 0)], (1, 0), 2, Point(0, 0)),
            ([Point(0, 0)], (2, 0), 1, False),
            ((Point(0, 0), Point(0, 1)), (1, 0), 2, Point(0, 0)),
            ([Point(0, 0), Point(0, 1)], (1, 0), 2, Point(0, 0)),
            ([Point(0, 0), Point(0, 1)], (5, 5), 2, False),
        ]

        for test in tests:
            with self.subTest(test=test):
                points, pos, radius, expected = test
                result = game_state.find_point_from_pos(
                    points,
                    pos,
                    radius)
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
