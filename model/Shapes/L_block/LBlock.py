from model.Box import Box
from model.Shapes.Block import Block


class BlockL(Block):

    def __init__(self, game_manager, app, map_controller, x, y):
        self.a = Box(game_manager, x, y, app, map_controller)
        self.b = Box(game_manager, x, y - 1, app, map_controller)
        self.c = Box(game_manager, x, y - 2, app, map_controller)
        self.d = Box(game_manager, x + 1, y - 2, app, map_controller)
        self.state = 1
        super().__init__([self.a, self.b, self.c, self.d])

    def rotate(self):
        if self.state == 1:
            self.a.move_right()
            self.b.move_right()
            self.state += 1
            return
        if self.state == 2:
            self.c.jump_up()
            self.c.jump_up()
            self.state += 1
            return