from panda3d.core import Point3
from model.BoxModels.BoxModels import *

class BoxGFX:

    def __init__(self, game_manager, x, y, app, map_controller):
        self.gfx_x = x * game_manager.box_size
        self.gfx_y = y * game_manager.box_size
        self.gfx_z = 170
        self.box_size = game_manager.box_size
        self.game_manager = game_manager

        self.box_model = app.render.attachNewNode("Box Holder")
        game_manager.model_factory.get_model(WoodenBox()).instanceTo(self.box_model)
        self.box_model.setPos(self.gfx_x, self.gfx_z, self.gfx_y)
        self.move_down_itv = self.box_model.posInterval(self.game_manager.game_speed,
                                                        Point3(self.gfx_x, self.gfx_z, self.gfx_y - self.box_size))

        self.m_c = map_controller

    def start_falling_animation(self):
        self.box_model.setPos(self.gfx_x, self.gfx_z, self.gfx_y)
        self.move_down_itv = self.box_model.posInterval(self.game_manager.game_speed,
                                                        Point3(self.gfx_x, self.gfx_z, self.gfx_y - self.box_size),
                                                        startPos=Point3(self.gfx_x, self.gfx_z, self.gfx_y))
        self.move_down_itv.start()
        self.gfx_y = self.gfx_y - self.box_size

    def is_animation_playing(self):
        return self.move_down_itv.isPlaying()

    def move(self, direction):
        self.gfx_x = self.gfx_x + direction.x * self.box_size
        self.gfx_y = self.gfx_y + direction.y * self.box_size

    def remove(self):
        self.box_model.removeNode()
        self.move_down_itv = None
