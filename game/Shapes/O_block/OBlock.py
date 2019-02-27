from game.Box import Box
from game.Shapes.Block import Block
from game.Shapes.RotationState import RotationState


class OBlock(Block):

    def __init__(self, game_manager, app, map_controller, center_x, center_y, model_type):
        self.a = Box(game_manager, center_x - 1, center_y, app, map_controller, model_type)
        self.b = Box(game_manager, center_x, center_y, app, map_controller, model_type)
        self.c = Box(game_manager, center_x, center_y - 1, app, map_controller, model_type)
        self.d = Box(game_manager, center_x - 1, center_y - 1, app, map_controller, model_type)
        super().__init__([self.a, self.b, self.c, self.d], RotationState(self), center_x, center_y, game_manager)