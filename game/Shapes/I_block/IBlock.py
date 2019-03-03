from game.Box.Box import Box
from game.Shapes.Block import Block
from game.Shapes.I_block.States import LeftDownState


class IBlock(Block):

    def __init__(self, game_manager, app, map_controller, center_x, center_y, model_type):
        self.a = Box(game_manager, center_x, center_y + 1, app, map_controller, model_type)
        self.b = Box(game_manager, center_x, center_y, app, map_controller, model_type)
        self.c = Box(game_manager, center_x, center_y - 1, app, map_controller, model_type)
        self.d = Box(game_manager, center_x, center_y - 2, app, map_controller, model_type)
        super().__init__([self.a, self.b, self.c, self.d], LeftDownState(self), center_x, center_y, game_manager)

    def rotate(self):
        if self.can_spin():
            self.state.rotate()

    def can_spin(self):
        neighbours = []
        for x in range(self.center_x - 1, self.center_x + 3):
            for y in range(self.center_y - 1, self.center_y + 3):
                field = self.game_manager.mc.check(y, x)
                if field.is_out_of_rang():
                    return False
                if field.is_taken():
                    neighbours.append(field.taken_by())
        for box in neighbours:
            if box not in self.boxes:
                return False
        return True
