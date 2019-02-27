from game.BoxModels.BoxModels import WoodenBox
from game.Shapes.I_block.IBlock import IBlock


class ShapesFactory:

    def __init__(self, game_manager, app, map_controller, drop_x, drop_y):
        self.app = app
        self.map_controller = map_controller
        self.center_y = drop_y
        self.center_x = drop_x
        self.game_manager = game_manager

    def get_random_shape(self):
        return IBlock(self.game_manager, self.app, self.map_controller, self.center_x, self.center_y, WoodenBox())
