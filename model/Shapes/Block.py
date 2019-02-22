from model.Directions.Directions import *


class Block:

    def __init__(self, boxes_list, initial_state):
        self.state = initial_state
        self.boxes = boxes_list

    def fall(self):
        for box in self.boxes:
            box.refresh()
        if self.can_move(OneDown()):
            for box in self.boxes:
                box.fall()
            return True
        return False

    def is_animation_playing(self):
        for box in self.boxes:
            if box.is_animation_playing():
                return True
        return False

    def can_move(self, direction):
        for box in self.boxes:
            field = box.neighbour(direction)
            if not field.is_movable():
                continue
            if field.taken_by() not in self.boxes or field.is_out_of_rang():
                return False
        return True

    def move(self, direction):
        if self.can_move(direction):
            for box in self.boxes:
                box.move(direction)

    def remove(self):
        for box in self.boxes:
            box.remove()

    def set_state(self, new_state):
        self.state = new_state

    def rotate(self):
        pass
