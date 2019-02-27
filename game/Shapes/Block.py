from game.Directions.Directions import *


class Block:

    def __init__(self, boxes_list, initial_state, center_x, center_y, game_manager):
        self.game_manager = game_manager
        self.center_y = center_y
        self.center_x = center_x
        self.state = initial_state
        self.boxes = boxes_list

    def fall(self):
        if self.can_move(OneDown()):
            for box in self.boxes:
                box.fall()
            self.center_y = self.center_y - 1
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
            self.center_x = self.center_x + direction.x
            self.center_y = self.center_y + direction.y

    def remove(self):
        for box in self.boxes:
            box.remove()

    def set_state(self, new_state):
        self.state = new_state

    def can_spin(self):
        neighbours = []
        for x in range(self.center_x - 1, self.center_x + 2):
            for y in range(self.center_y - 1, self.center_y + 2):
                field=self.game_manager.mc.check(y, x)
                if field.is_out_of_rang():
                    return False
                if field.is_taken():
                    neighbours.append(field.taken_by())
        for box in neighbours:
            if box not in self.boxes:
                return False
        return True

    def rotate(self):
        pass
