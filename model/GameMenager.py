from .Box import Box


class GameMenager:

    def __init__(self, app):
        self.map = [[None] * 10] * 20
        self.app = app

    def check_field(self, x, y):
        if self.map[x][y] is None:
            return True

        else:
            return False

    def drop_new(self):

        self.map[19][9] = Box(self, 10, 20, self.app)
