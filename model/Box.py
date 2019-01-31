from panda3d.core import Point3


class Box:

    def __init__(self, game_map, x, y, app):
        self.game_map = game_map
        self.x = x
        self.y = y
        self.box = app.loader.loadModel("resources/PS2.egg")
        self.box.reparentTo(app.render)
        self.gfx_x = 0
        self.gfx_y = 0
        self.gfx_z = 170
        self.box.setPos(self.gfx_x, self.gfx_z, self.gfx_y)

        self.game_map.block_field(self.y, self.x)
        self.move_down_itv = self.box.posInterval(self.game_map.game_speed,
                                                  Point3(self.gfx_x, self.gfx_z, self.gfx_y - 2))

    def fall(self):

        self.box.setPos(self.gfx_x, self.gfx_z, self.gfx_y)
        if self.game_map.check_field(self.y - 1, self.x):
            self.move_down_itv = self.box.posInterval(self.game_map.game_speed,
                                                      Point3(self.gfx_x, self.gfx_z, self.gfx_y - 2),
                                                      startPos=Point3(self.gfx_x, self.gfx_z, self.gfx_y))
            self.game_map.release_field(self.y, self.x)
            self.y = self.y - 1
            self.game_map.block_field(self.y, self.x)

            self.move_down_itv.start()
            self.gfx_y = self.gfx_y - 2
            return 1
        else:
            return 0

    def is_animation_finished(self):
        return self.move_down_itv.isPlaying()

    def move_left(self):
        if self.game_map.check_field(self.y, self.x - 1):
            self.game_map.release_field(self.y, self.x)
            self.x = self.x - 1
            self.game_map.block_field(self.y, self.x)
            self.gfx_x=self.gfx_x-2

    def move_right(self):
        if self.game_map.check_field(self.y, self.x + 1):
            self.game_map.release_field(self.y, self.x)
            self.x = self.x + 1
            self.game_map.block_field(self.y, self.x)
            self.gfx_x = self.gfx_x + 2

