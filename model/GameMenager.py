import numpy as np
from model.MapController import MapController
from .Box import Box


class GameMenager:

    def __init__(self, app):
        game_space = np.zeros((20, 15)).tolist()
        self.mc = MapController(game_space)
        self.app = app
        self.game_speed = 0.1
        self.box_size = 2
        self.current_box = None

    def drop_new(self):
        if self.mc.check_field(19, 5):
            box = Box(self, 5, 19, self.app, self.mc)
            self.current_box = box
            return True
        return False

    def handle_buttons(self):
        self.app.accept("arrow_left", self.current_box.move_left)
        self.app.accept("arrow_right", self.current_box.move_right)

    def moveBlocks(self, task):
        self.handle_buttons()
        if not self.current_box.is_animation_playing():

            if not self.current_box.fall():
                self.mc.remove_full_row()
                still_playing = self.drop_new()
                if not still_playing:
                    return task.done
        return task.cont
