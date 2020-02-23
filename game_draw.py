import pygame

pip_surface = False
level_complete_text = False


def init(game):
    global pip_surface
    pip_surface = create_pip(game)

    global level_complete_text
    level_complete_text = create_level_complete_text()


def draw_line(surface, game, line_segment):
    width = 4
    colour = 220, 220, 220
    if (line_segment == game.last_found_collision[0]) or (line_segment == game.last_found_collision[1]):
        colour = 255, 0, 0
    pygame.draw.line(surface, colour, line_segment[0].as_tuple(), line_segment[1].as_tuple(), width)


def draw_point(surface, game, point):
    dest_rect = pip_surface.get_rect()
    dest_rect.center = int(point.x), int(point.y)
    surface.blit(pip_surface, dest_rect)


def draw_pip(surface, game, point):
    inner_colour = 160, 160, 220
    outer_colour = 220, 220, 220
    border_thickness = 4
    pygame.draw.circle(surface, inner_colour, point, game.point_radius)
    pygame.draw.circle(surface, outer_colour, point, game.point_radius, border_thickness)


def create_pip(game):
    transparent_color = 0, 0, 0
    size = int(game.point_radius * 2)
    center = size // 2, size // 2
    surface = pygame.Surface((size, size), pygame.HWSURFACE)
    surface.set_colorkey(transparent_color)
    draw_pip(surface, game, center)
    return surface


def create_level_complete_text():
    text_color = 0, 255, 0
    background_colour = 0, 0, 0
    font = pygame.font.Font(pygame.font.get_default_font(), 32)
    surface = font.render('Level Complete', True, text_color, background_colour)
    surface.set_colorkey(background_colour)
    return surface


def draw_frame(surface, game):
    surface.fill(game.background_colour)

    for connection in game.connections:
        draw_line(surface, game, connection)

    for point in game.points:
        draw_point(surface, game, point)

    if game.level_complete:
        dest_rect = level_complete_text.get_rect()
        dest_rect.center = (game.screen_size[0] // 2, game.screen_size[1] // 2)
        surface.blit(level_complete_text, dest_rect)

    pygame.display.flip()
