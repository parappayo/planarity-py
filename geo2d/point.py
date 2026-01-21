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
