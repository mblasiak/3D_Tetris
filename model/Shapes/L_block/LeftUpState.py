from model.Shapes.L_block.LeftDownState import LeftDownState, RotationState
#from model.Shapes.RotationState import RotationState
from model.Directions.Directions import *


class LeftUpState(RotationState):

    def next_state(self):
        self.block.set_state(LeftDownState(self.block))

    def rotate(self):
        self.block.c.move(OneUp())
        self.block.c.move(OneUp())
        self.next_state()
