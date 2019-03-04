from game.Box.Box import Box
from game.Shapes.Block import Block
from game.Shapes.RotationState import RotationState


class OBlock(Block):

    def __init__(self, map_controller, center_x, center_y, model_type, box_factory):
        self.a = Box(center_x - 1, center_y, map_controller, model_type,box_factory)
        self.b = Box(center_x, center_y, map_controller, model_type,box_factory)
        self.c = Box(center_x, center_y - 1, map_controller, model_type,box_factory)
        self.d = Box(center_x - 1, center_y - 1, map_controller, model_type,box_factory)
        self.map=map_controller
        super().__init__([self.a, self.b, self.c, self.d], RotationState(self), center_x, center_y,self.map)
