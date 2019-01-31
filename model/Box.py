from panda3d.core import Point3


class Box:

    def __init__(self, game_map, x, y, app, map_controller):
        self.game_map = game_map
        self.x = x
        self.y = y
        self.gfx_x = 0
        self.gfx_y = 0
        self.gfx_z = 170

        # 3d set up
        self.box_size = game_map.box_size
        self.box_model = app.loader.loadModel("resources/PS2.egg")
        self.box_model.reparentTo(app.render)
        self.box_model.setPos(self.gfx_x, self.gfx_z, self.gfx_y)
        self.move_down_itv = self.box_model.posInterval(self.game_map.game_speed,
                                                        Point3(self.gfx_x, self.gfx_z, self.gfx_y - self.box_size))

        self.m_c = map_controller
        self.m_c.block_field(self.y, self.x, self)

    def fall(self):
        self.box_model.setPos(self.gfx_x, self.gfx_z, self.gfx_y)
        if self.m_c.check_field(self.y - 1, self.x):
            self.move_down_itv = self.box_model.posInterval(self.game_map.game_speed,
                                                            Point3(self.gfx_x, self.gfx_z, self.gfx_y - self.box_size),
                                                            startPos=Point3(self.gfx_x, self.gfx_z, self.gfx_y))
            self.m_c.release_field(self.y, self.x)
            self.y = self.y - 1
            self.m_c.block_field(self.y, self.x, self)

            self.move_down_itv.start()
            self.gfx_y = self.gfx_y - self.box_size
            return 1
        else:
            return 0

    def is_animation_playing(self):
        return self.move_down_itv.isPlaying()

    def move_horizontal(self, direction):
        if self.m_c.check_field(self.y, self.x + direction):
            self.m_c.release_field(self.y, self.x)
            self.x = self.x + direction
            self.m_c.block_field(self.y, self.x, self)
            self.gfx_x = self.gfx_x + direction * self.box_size

    def move_left(self):
        self.move_horizontal(-1)

    def move_right(self):
        self.move_horizontal(+1)

    def remove(self):
        self.box_model.removeNode()
        self.move_down_itv = None
