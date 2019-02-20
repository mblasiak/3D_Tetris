from model.Box import Box
from model.MapManager import GameField


class Block:

    def __init__(self, boxes_list,inital_state):
        self.state=inital_state
        self.boxes = boxes_list

    def can_fall(self):
        for box in self.boxes:
            z = box.can_fall()
            if z == GameField.free:
                continue
            if z not in self.boxes or z == GameField.out_of_range:
                return False
        return True

    def fall(self):
        for box in self.boxes:
            box.refresh()
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
            if z == GameField.free:
                continue
            if z not in self.boxes or z == GameField.out_of_range:
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

    def set_state(self, new_state):
        self.state = new_state

    def rotate(self):
        pass
