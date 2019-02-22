class Block:

    def __init__(self, boxes_list, inital_state):
        self.state = inital_state
        self.boxes = boxes_list

    def can_fall(self):
        for box in self.boxes:
            z = box.under_neighbour()
            if not z.is_movable():
                continue
            if z.taken_by() not in self.boxes or z.is_out_of_rang():
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
            field = box.horizontal_neighbour(direction)
            if not field.is_movable():
                continue
            if field.taken_by() not in self.boxes or field.is_out_of_rang():
                return False
        return True

    def move(self, x_direction, y_direction):
        if self.can_move_horizontal(x_direction):
            for box in self.boxes:
                box.move(x_direction, y_direction)

    def remove(self):
        for box in self.boxes:
            box.remove()

    def set_state(self, new_state):
        self.state = new_state

    def rotate(self):
        pass
