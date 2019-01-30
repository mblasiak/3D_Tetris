from panda3d.core import Point3
from direct.interval.IntervalGlobal import *
from direct.interval.IntervalGlobal import Sequence


class Box:

    def __init__(self, game_map, x, y, app):
        self.game_map = game_map
        self.x = x
        self.y = y
        self.box = app.loader.loadModel("resources/PS2.egg")
        self.box.reparentTo(app.render)
        self.gfx_x = 0
        self.gfx_y = 0
        self.gfx_z = 10
        self.box.setPos(self.gfx_x, self.gfx_z, self.gfx_y)

        self.game_map.block_field(self.y, self.x)
        self.move_down_itv = self.box.posInterval(self.game_map.game_speed, Point3(self.gfx_x, self.gfx_z, self.gfx_y - 2))


    def fall(self):
        if self.game_map.check_field(self.y - 1, self.x):

            print(self.y)
            print("fall odpalony")
            self.move_down_itv = self.box.posInterval(self.game_map.game_speed,
                                                      Point3(self.gfx_x, self.gfx_z, self.gfx_y - 2),startPos= Point3(self.gfx_x, self.gfx_z, self.gfx_y))
            self.game_map.reales_field(self.y, self.x)
            self.y = self.y - 1
            self.game_map.block_field(self.y,self.x)
            print(self.gfx_y)

            self.move_down_itv.start()
            self.gfx_y=self.gfx_y-2
            return 1
        else:
            print("End")
            return 0

    def get_animation_stae(self):
        return self.move_down_itv.isPlaying()


    def move_left(self):
        if self.game_map.check_field(self.y,self.x-1):
            self.x = self.x - 1

    def move_left(self):
        if self.game_map.check_field(self.y,self.x+1):
            self.x = self.x+1
