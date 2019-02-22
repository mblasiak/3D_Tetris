from model.Shapes.RotationState import RotationState
from model.Directions.Directions import *
from model.Shapes.L_block.RightDownState import RightDownState


class LeftDownState(RotationState):

    def next_state(self):
        self.block.set_state(RightDownState(self.block))

    def rotate(self):
        self.block.a.move(OneRight())
        self.block.b.move(OneRight())
        self.next_state()
