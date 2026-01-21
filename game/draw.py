import pygame


def draw_pip(surface, radius, point):
    inner_colour = 160, 160, 220
    outer_colour = 220, 220, 220
    border_thickness = 4
    pygame.draw.circle(surface, inner_colour, point, radius)
    pygame.draw.circle(surface, outer_colour, point, radius, border_thickness)


def create_pip(radius):
    transparent_color = 0, 0, 0
    size = int(radius * 2)
    center = size // 2, size // 2
    surface = pygame.Surface((size, size), pygame.HWSURFACE)
    surface.set_colorkey(transparent_color)
    draw_pip(surface, radius, center)
    return surface


def create_level_complete_text():
    text_color = 0, 255, 0
    background_colour = 0, 0, 0
    font = pygame.font.Font(pygame.font.get_default_font(), 32)
    surface = font.render('Level Complete', True, text_color, background_colour)
    surface.set_colorkey(background_colour)
    return surface


class Graphics:

    def __init__(self, surface, game):
        self.surface = surface
        self.game = game
        self.pip_surface = create_pip(game.point_radius)
        self.level_complete_text = create_level_complete_text()

    def draw_frame(self):
        self.surface.fill(self.game.background_colour)

        for connection in self.game.connections:
            self.draw_line(connection)

        for point in self.game.points:
            self.draw_point(point)

        if self.game.level_complete:
            dest_rect = self.level_complete_text.get_rect()
            dest_rect.center = (self.game.screen_size[0] // 2, self.game.screen_size[1] // 2)
            self.surface.blit(self.level_complete_text, dest_rect)

        pygame.display.flip()

    def draw_line(self, line_segment):
        width = 4
        colour = 220, 220, 220
        if (line_segment == self.game.last_found_collision[0]) or (line_segment == self.game.last_found_collision[1]):
            colour = 255, 0, 0
        pygame.draw.line(self.surface, colour, line_segment[0].as_tuple(), line_segment[1].as_tuple(), width)


    def draw_point(self, point):
        dest_rect = self.pip_surface.get_rect()
        dest_rect.center = int(point.x), int(point.y)
        self.surface.blit(self.pip_surface, dest_rect)
