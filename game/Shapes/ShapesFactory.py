from random import randrange

from game.BoxModels.BoxModels import ModelSwitcher
from game.Shapes.ShapeSwitcher import ShapeSwitcher


class ShapesFactory:

    def __init__(self, game_manager, app, map_controller, drop_x, drop_y):
        self.app = app
        self.map_controller = map_controller
        self.center_y = drop_y
        self.center_x = drop_x
        self.game_manager = game_manager
        self.shape_switcher = ShapeSwitcher()
        self.model_switcher = ModelSwitcher()

    def get_random(self):
        rand = randrange(1, 8, 1)
        shape = self.shape_switcher.number_to_shape(rand)
        model=self.model_switcher.number_to_model(rand)
        return shape(self.game_manager, self.app, self.map_controller, self.center_x, self.center_y, model())