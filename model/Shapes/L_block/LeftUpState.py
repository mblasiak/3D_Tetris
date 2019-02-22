from model.Shapes.RotationState import RotationState
from model.Directions.Directions import *

class LeftUpState(RotationState):

    def next_state(self):
        self.block.set_state(self)

    def rotate(self):
        return
        self.block.c.move(OneRight())
        self.block.c.move(OneRight())
        self.next_state()
