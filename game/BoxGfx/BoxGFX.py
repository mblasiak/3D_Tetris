from panda3d.core import Point3
from game.BoxModels.BoxModels import *


class BoxGFX:

    def __init__(self, x, y, app, model_type, model_factory, box_size, gfx_offsets, game_speed):
        (x_offset, y_offset, z_offset) = gfx_offsets
        self.gfx_x = x * box_size + x_offset
        self.gfx_y = y * box_size + y_offset
        self.gfx_z = z_offset
        self.box_size = box_size
        self.game_speed = game_speed
        self.box_holder = app.render.attachNewNode("Box Holder")
        model_factory.get_model(model_type).instanceTo(self.box_holder)
        self.box_holder.setPos(self.gfx_x, self.gfx_z, self.gfx_y)
        self.move_down_itv = self.box_holder.posInterval(self.game_speed,
                                                         Point3(self.gfx_x, self.gfx_z, self.gfx_y - self.box_size))

    def start_falling_animation(self):
        self.box_holder.setPos(self.gfx_x, self.gfx_z, self.gfx_y)
        self.move_down_itv = self.box_holder.posInterval(self.game_speed,
                                                         Point3(self.gfx_x, self.gfx_z, self.gfx_y - self.box_size),
                                                         startPos=Point3(self.gfx_x, self.gfx_z, self.gfx_y))
        self.move_down_itv.start()
        self.gfx_y = self.gfx_y - self.box_size

    def is_animation_playing(self):
        return self.move_down_itv.isPlaying()

    def move(self, direction):
        self.gfx_x = self.gfx_x + direction.x * self.box_size
        self.gfx_y = self.gfx_y + direction.y * self.box_size
        self.refresh()

    def refresh(self):

        if self.is_animation_playing():
            time = self.move_down_itv.getDuration()
            self.move_down_itv.finish()
            self.move_down_itv = self.box_holder.posInterval(self.game_speed,
                                                             Point3(self.gfx_x, self.gfx_z, self.gfx_y),
                                                             startPos=Point3(self.gfx_x, self.gfx_z,
                                                                             self.gfx_y + self.box_size))
            self.move_down_itv.start()
            self.move_down_itv.setT(time)

        else:
            self.box_holder.setPos(self.gfx_x, self.gfx_z, self.gfx_y)

    def remove(self):
        self.box_holder.removeNode()
        self.move_down_itv = None
