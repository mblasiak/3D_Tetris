from random import randrange

from game.BoxModels.BoxModels import ModelSwitcher
from game.Shapes.ShapeSwitcher import ShapeSwitcher


class ShapesFactory:

    def __init__(self, app, map_controller, spawn_x, spawn_y, box_factory, box_size):
        self.app = app
        self.map_controller = map_controller
        self.center_y = spawn_y
        self.center_x = spawn_x
        self.shape_switcher = ShapeSwitcher()
        self.model_switcher = ModelSwitcher()
        self.box_factory = box_factory
        self.box_size = box_size

    def get_random(self):
        rand = randrange(1, 8, 1)
        shape = self.shape_switcher.number_to_shape(rand)
        model = self.model_switcher.number_to_model(rand)
        return shape(self.map_controller, self.center_x, self.center_y, model(), self.box_factory)
