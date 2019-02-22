from model.Shapes.L_block.RightUpState import RightUpState
from model.Shapes.RotationState import RotationState
from model.Directions.Directions import *


class RightDownState(RotationState):

    def next_state(self):
        self.block.set_state(RightUpState(self.block))

    def rotate(self):
        self.block.c.move(OneUp())
        self.block.c.move(OneUp())
        self.next_state()
