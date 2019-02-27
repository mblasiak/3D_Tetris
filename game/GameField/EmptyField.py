from game.GameField.Field import GameField


class EmptyField(GameField):

    def is_movable(self):
        return False

    def is_out_of_rang(self):
        return False

    def taken_by(self):
        return None

    def is_taken(self):
        return False
