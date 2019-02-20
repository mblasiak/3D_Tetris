from model.GameField.GameField import GameField


class TakenField(GameField):

    def is_taken(self):
        return True

    def is_out_of_rang(self):
        return False

    def taken_by(self):
        return self.box

    def __init__(self, box):
        self.box = box
