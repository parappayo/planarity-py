import math
import level_generator


def circle_points(center, radius, point_count):
    theta = 0
    theta_step = (2 * math.pi) / point_count
    for i in range(point_count):
        yield (center[0] + math.cos(theta) * radius,
            center[1] + math.sin(theta) * radius)
        theta += theta_step


def arrange_in_circle(points, screen_size):
    dest_points = circle_points(
            (screen_size[0] / 2, screen_size[1] / 2),
            screen_size[1] / 2.5,
            len(points))

    for point in points:
        dest_point = next(dest_points)
        point.x = dest_point[0]
        point.y = dest_point[1]


def find_point_from_pos(points, pos, radius):
    for point in points:
        dx = point.x - pos[0]
        dy = point.y - pos[1]
        if dx * dx + dy * dy < radius * radius:
            return point
    return False


class GameState:
    def __init__(self):
        self.points = False
        self.connections = False

        self.redraw_required = False
        self.mouse_drag_target = False
        self.level_complete = False
        self.last_found_collision = (False, False)

        self.background_colour = 0, 0, 0  # rgb 256
        self.screen_size = 1024, 768  # pixels
        self.point_radius = 24  # pixels

    def start_level(self, level):
        line_count = level + 4
        self.points, self.connections = level_generator.generate_level(line_count)
        arrange_in_circle(self.points, self.screen_size)
        self.mouse_drag_target = False
        self.redraw_required = True

    def find_point_from_pos(self, pos):
        return find_point_from_pos(self.points, pos, self.point_radius)

    def check_win_condition(self):
        if self.level_complete:
            return
        for connection1 in self.connections:
            for connection2 in self.connections:
                if connection1 == connection2:
                    continue
                if connection1.intersects(connection2):
                    self.last_found_collision = (connection1, connection2)
                    return
        self.last_found_collision = (False, False)
        self.level_complete = True
        self.redraw_required = True
