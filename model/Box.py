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

    def can_fall(self):
        return self.map_controller.check_field(self.y - 1, self.x)

    def refresh(self):
        self.box_gfx.refresh()

    def move_up(self):
        if self.map_controller.check_field(self.y, self.x) == self:
            self.map_controller.release_field(self.y, self.x)
        self.y = self.y + 1
        self.map_controller.block_field(self.y, self.x, self)
        self.box_gfx.move_up()

    def fall(self):
        if self.map_controller.check_field(self.y, self.x) == self:
            self.map_controller.release_field(self.y, self.x)
        self.y = self.y - 1
        self.map_controller.block_field(self.y, self.x, self)
        self.box_gfx.start_falling_animation()

    def is_animation_playing(self):
        return self.box_gfx.is_animation_playing()

    def can_move_horizontal(self, direction):
        return self.map_controller.check_field(self.y, self.x + direction)

    def move_horizontal(self, direction):
        if self.map_controller.check_field(self.y, self.x) == self:
            self.map_controller.release_field(self.y, self.x)
        self.x = self.x + direction
        self.map_controller.block_field(self.y, self.x, self)
        self.box_gfx.move_horizontal(direction)

    def move_left(self):
        self.move_horizontal(-1)

    def move_right(self):
        self.move_horizontal(+1)

    def remove(self):
        self.box_gfx.remove()
