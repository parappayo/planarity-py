import math
import level_generator


def arrange_in_circle(points, screen_size):
    height_ratio = screen_size[1] / screen_size[0]
    center_x = screen_size[0] / 2
    center_y = screen_size[1] / 2
    width = screen_size[0] * height_ratio / 2.5
    height = screen_size[1] / 2.5

    theta = 0
    theta_step = (2 * math.pi) / len(points)
    for point in points:
        point.x = center_x + math.cos(theta) * width
        point.y = center_y + math.sin(theta) * height
        theta += theta_step


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
