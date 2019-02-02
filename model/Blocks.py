from .Box import Box
from .MapController import FiledStatus


class Block:

    def __init__(self, boxes_list):
        self.boxes = boxes_list

    def can_fall(self):
        for box in self.boxes:
            z = box.can_fall()
            if z == FiledStatus.free:
                continue
            if z not in self.boxes or z == FiledStatus.out_of_range:
                return False
        return True

    def fall(self):
        for box in self.boxes:
            box.update_box()
        if self.can_fall():
            for box in self.boxes:
                box.fall()
            return True
        return False

    def is_animation_playing(self):
        for box in self.boxes:
            if box.is_animation_playing():
                return True
        return False

    def can_move_horizontal(self, direction):
        for box in self.boxes:
            z = box.can_move_horizontal(direction)
            if z == FiledStatus.free:
                continue
            if z not in self.boxes or z == FiledStatus.out_of_range:
                return False
        return True

    def move_horizontal(self, direction):
        if self.can_move_horizontal(direction):
            for box in self.boxes:
                box.move_horizontal(direction)

    def move_left(self):
        self.move_horizontal(-1)

    def move_right(self):
        self.move_horizontal(1)

    def remove(self):
        for box in self.boxes:
            box.remove()

    def rotate(self):
        pass


class BlockBox(Block):

    def __init__(self, game_manager, app, map_controller, x, y):
        self.a = Box(game_manager, x - 1, y, app, map_controller)
        self.b = Box(game_manager, x, y, app, map_controller)
        self.c = Box(game_manager, x, y - 1, app, map_controller)
        self.d = Box(game_manager, x - 1, y - 1, app, map_controller)
        super().__init__([self.a, self.b, self.c, self.d])


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
