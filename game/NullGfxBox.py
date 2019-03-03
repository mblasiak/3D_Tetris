from panda3d.core import Point3


class NullGfxBox:

    def __init__(self, game_manager, x, y):
        self.gfx_x = x * game_manager.box_size - 30
        self.gfx_y = y * game_manager.box_size - 20
        self.gfx_z = 100
        self.box_size = game_manager.box_size
        self.game_manager = game_manager
        self.app = game_manager.app
        self.box_holder = self.app.render.attachNewNode("Box Holder")
        self.box_holder.setPos(self.gfx_x, self.gfx_z, self.gfx_y)
        self.move_down_itv = self.box_holder.posInterval(self.game_manager.game_speed,
                                                         Point3(self.gfx_x, self.gfx_z, self.gfx_y - self.box_size),
                                                         startPos=Point3(self.gfx_x, self.gfx_z, self.gfx_y))

    def move(self, direction):
        self.gfx_x = self.gfx_x + direction.x * self.box_size
        self.gfx_y = self.gfx_y + direction.y * self.box_size
        self.box_holder.setPos(self.gfx_x, self.gfx_z, self.gfx_y)

    def start_falling_animation(self):
        self.box_holder.setPos(self.gfx_x, self.gfx_z, self.gfx_y)
        self.move_down_itv = self.box_holder.posInterval(self.game_manager.game_speed,
                                                         Point3(self.gfx_x, self.gfx_z, self.gfx_y - self.box_size),
                                                         startPos=Point3(self.gfx_x, self.gfx_z, self.gfx_y))
        self.move_down_itv.start()
        self.gfx_y = self.gfx_y - self.box_size

