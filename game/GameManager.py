import numpy as np
from game.GameButtonHandler import GameButtonHandler
from game.GameMap import GameMap
from game.BoxModelFactory import BoxModelFactory
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
        self.button_handler = GameButtonHandler(app, self.current_box)

    def drop_new(self):

        if not self.mc.check(self.top, self.middle).is_movable():
            box = self.shapes_factory.get_random()
            self.current_box = box
            self.button_handler.update_box(box)
            return True
        return False

    def play(self, task):
        if not self.current_box.is_animation_playing():
            if not self.current_box.fall():
                self.current_box = None
                self.mc.remove_full_rows()
                still_playing = self.drop_new()
                if not still_playing:
                    print("Exit")
                    self.app.ignoreAll()
                    return task.done

        return task.cont
