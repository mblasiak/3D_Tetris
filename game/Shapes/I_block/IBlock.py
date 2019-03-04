from game.Box.Box import Box
from game.Shapes.Block import Block
from game.Shapes.I_block.States import LeftDownState


class IBlock(Block):

    def __init__(self, map_controller, center_x, center_y, model_type, box_factory):
        self.a = Box(center_x, center_y + 1, map_controller, model_type, box_factory)
        self.b = Box(center_x, center_y, map_controller, model_type, box_factory)
        self.c = Box(center_x, center_y - 1, map_controller, model_type, box_factory)
        self.d = Box(center_x, center_y - 2, map_controller, model_type, box_factory)
        self.map=map_controller

        super().__init__([self.a, self.b, self.c, self.d], LeftDownState(self), center_x, center_y, self.map)

    def rotate(self):
        if self.can_spin():
            self.state.rotate()

    def can_spin(self):
        neighbours = []
        for x in range(self.center_x - 1, self.center_x + 3):
            for y in range(self.center_y - 1, self.center_y + 3):
                field = self.map.check(y, x)
                if field.is_out_of_rang():
                    return False
                if field.is_taken():
                    neighbours.append(field.taken_by())
        for box in neighbours:
            if box not in self.boxes:
                return False
        return True
