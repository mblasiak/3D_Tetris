import numpy as np

from game.BoxModels.BoxModels import WoodenBox
from game.GameMap import GameMap
from game.Shapes.I_block.IBlock import IBlock
from game.Shapes.J_block.JBlock import JBlock
from game.Shapes.L_block.LBlock import LBlock
from game.Shapes.O_block.OBlock import OBlock
from game.Directions.Directions import *
from game.BoxModelFactory import BoxModelFactory
from game.Shapes.S_block.SBlock import SBlock
from game.Shapes.T_block.TBlock import TBlock
from game.Shapes.Z_block.ZBlock import ZBlock
from game.ShapesFactory import ShapesFactory


class GameManager:

    def __init__(self, app):
        self.SIZE_X = 10
        self.SIZE_Y = 20
        game_space = np.zeros((self.SIZE_Y, self.SIZE_X)).tolist()
        self.mc = GameMap(game_space)
        self.app = app
        self.game_speed = 0.3
        self.box_size = 2
        self.current_box = None
        self.model_factory = BoxModelFactory(app)
        self.top = self.SIZE_Y - 2
        self.middle = round(self.SIZE_X / 2)

        self.shapes_factory = ShapesFactory(self, app, self.mc, self.middle, self.top)

    def drop_new(self):

        if not self.mc.check(self.top, self.middle).is_movable():
            # box = LBlock(self, self.app, self.mc, middle, top)
            # box = OBlock(self, self.app, self.mc, middle, top)
            # box=TBlock(self, self.app, self.mc, middle, top)
            # box=JBlock(self, self.app, self.mc, middle, top)
            # box=SBlock(self, self.app, self.mc, middle, top)
            # box = ZBlock(self, self.app, self.mc, middle, top)
            # box = IBlock(self, self.app, self.mc, middle, top,WoodenBox())
            box = self.shapes_factory.get_random_shape()
            self.current_box = box
            return True
        return False

    def handle_buttons(self):
        self.app.accept("arrow_left", self.current_box.move, [OneLeft()])
        self.app.accept("arrow_right", self.current_box.move, [OneRight()])
        self.app.accept("space", self.current_box.rotate)

    def play(self, task):
        print("In task")
        if not self.current_box.is_animation_playing():
            if not self.current_box.fall():
                self.mc.remove_full_rows()
                still_playing = self.drop_new()
                if not still_playing:
                    print("Exit")
                    self.app.ignoreAll()
                    return task.done
        self.handle_buttons()
        return task.cont
