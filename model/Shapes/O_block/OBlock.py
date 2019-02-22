from model.Box import Box
from model.Shapes.Block import Block
from model.Shapes.RotationState import RotationState


class OBlock(Block):

    def __init__(self, game_manager, app, map_controller, x, y):
        self.a = Box(game_manager, x - 1, y, app, map_controller)
        self.b = Box(game_manager, x, y, app, map_controller)
        self.c = Box(game_manager, x, y - 1, app, map_controller)
        self.d = Box(game_manager, x - 1, y - 1, app, map_controller)
        super().__init__([self.a, self.b, self.c, self.d], RotationState(self))
