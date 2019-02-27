from model.Box import Box
from model.Shapes.Block import Block
from model.Shapes.S_block.States import DownState


class SBlock(Block):

    def __init__(self, game_manager, app, map_controller, center_x, center_y):
        self.a = Box(game_manager, center_x+1, center_y+1, app, map_controller)
        self.b = Box(game_manager, center_x, center_y+1, app, map_controller)
        self.c = Box(game_manager, center_x, center_y, app, map_controller)
        self.d = Box(game_manager, center_x-1, center_y, app, map_controller)
        super().__init__([self.a, self.b, self.c, self.d], DownState(self), center_x, center_y,game_manager)

    def rotate(self):
        if self.can_spin():
            self.state.rotate()