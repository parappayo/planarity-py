import math
import level_generator

def arrange_in_circle(points, screen_size):
	theta = 0
	theta_step = (2 * math.pi) / len(points)
	for point in points:
		point.x = (math.cos(theta) + 1) * screen_size[0] / 2
		point.y = (math.sin(theta) + 1) * screen_size[1] / 2
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

		self.mouse_drag_target = False
		self.level_complete = False
		self.last_found_collision = (False, False)

		self.background_colour = 0, 0, 0 # rgb 256
		self.screen_size = 1024, 768 # pixels
		self.point_radius = 24 # pixels

	def generate_level(self, line_count):
		self.points, self.connections = level_generator.generate_level(line_count)
		self.mouse_drag_target = False

	def arrange_in_circle(self):
		arrange_in_circle(self.points, self.screen_size)

	def find_point_from_pos(self, pos):
		return find_point_from_pos(self.points, pos, self.point_radius)

	def check_win_condition(self):
		for connection1 in self.connections:
			for connection2 in self.connections:
				if connection1 == connection2:
					continue
				if connection1.intersects(connection2):
					self.last_found_collision = (connection1, connection2)
					return
		self.last_found_collision = (False, False)
		self.level_complete = True
