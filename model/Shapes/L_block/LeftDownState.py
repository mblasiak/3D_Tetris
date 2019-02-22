from model.Shapes.L_block.LeftUpState import LeftUpState
from model.Shapes.RotationState import RotationState
from model.Directions.Directions import *

class LeftDownState(RotationState):

    def next_state(self):
        self.block.set_state(LeftUpState(self.block))

    def rotate(self):
        self.block.a.move(OneUp())
        self.block.b.move(OneUp())
        self.next_state()
