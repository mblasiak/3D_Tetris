from game.Directions.Directions import OneRight, OneLeft


class GameButtonHandler:

    def __init__(self, app, current_box):
        self.current_box = current_box
        self.app = app
        self.app.accept("arrow_left", self.move_box, [OneLeft()])
        self.app.accept("arrow_right", self.move_box, [OneRight()])
        self.app.accept("space", self.rotate_box)

    def update_box(self, box):
        self.current_box = box

    def move_box(self, direction):
        print("HOOHO")
        if self.current_box is not None:
            self.current_box.move(direction)

    def rotate_box(self):
        if self.current_box is not None:
            self.current_box.rotate()
