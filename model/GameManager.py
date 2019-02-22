import numpy as np
from model.GameMap import GameMap
from model.Shapes.L_block.LBlock import LBlock
from model.Shapes.O_block.OBlock import OBlock
from model.Directions.Directions import *
from model.BoxModelFactory import BoxModelFactory


class GameManager:

    def __init__(self, app):
        self.SIZE_X = 10
        self.SIZE_Y = 40
        game_space = np.zeros((self.SIZE_Y, self.SIZE_X)).tolist()
        self.mc = GameMap(game_space)
        self.app = app
        self.game_speed = 0.1
        self.box_size = 2
        self.current_box = None
        self.model_factory = BoxModelFactory(app)

    def drop_new(self):
        top = self.SIZE_Y - 1
        middle = round(self.SIZE_X / 2)
        if not self.mc.check(top, middle).is_movable():
            box = LBlock(self, self.app, self.mc, middle, top)
            #box = OBlock(self, self.app, self.mc, middle, top)
            self.current_box = box
            return True
        return False

    def handle_buttons(self):
        self.app.accept("arrow_left", self.current_box.move, [OneLeft()])
        self.app.accept("arrow_right", self.current_box.move, [OneRight()])
        self.app.accept("space", self.current_box.rotate)

    def play(self, task):
        self.handle_buttons()
        if not self.current_box.is_animation_playing():

            if not self.current_box.fall():
                self.mc.remove_full_rows()
                still_playing = self.drop_new()
                if not still_playing:
                    return task.done
        return task.cont
