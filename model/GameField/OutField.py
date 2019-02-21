from model.GameField.Field import GameField


class OutField(GameField):

    def is_movable(self):
        return True

    def is_out_of_rang(self):
        return True

    def taken_by(self):
        return None
