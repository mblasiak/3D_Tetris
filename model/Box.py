from panda3d.core import Point3

from model.BoxGFX import BoxGFX


class Box:

    def __init__(self, game_manager, x, y, app, map_controller):
        self.game_manager = game_manager
        self.x = x
        self.y = y
        self.map_controller = map_controller
        self.map_controller.block_field(self.y, self.x, self)
        self.box_gfx = BoxGFX(game_manager, x, y, app, map_controller)

    def under_neighbour(self):
        return self.map_controller.check_field(self.y - 1, self.x)

    def refresh(self):
        self.box_gfx.refresh()

    def move_up(self):
        self.move(0, 1)
        self.box_gfx.move(0, 1)

    def fall(self):
        self.move(0, -1)
        self.box_gfx.start_falling_animation()

    def is_animation_playing(self):
        return self.box_gfx.is_animation_playing()

    def horizontal_neighbour(self, direction):
        return self.map_controller.check_field(self.y, self.x + direction)

    def move(self, x_direction, y_direction):
        self.map_controller.release_field(self.y, self.x, self)
        self.x = self.x + x_direction
        self.y = self.y + y_direction
        self.map_controller.block_field(self.y, self.x, self)

    def move_left(self):
        self.move(-1, 0)
        self.box_gfx.move(-1, 0)

    def move_right(self):
        self.move(+1, 0)
        self.box_gfx.move(1, 0)

    def remove(self):
        self.box_gfx.remove()
