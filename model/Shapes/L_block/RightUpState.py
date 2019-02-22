from model.Shapes.L_block.LeftUpState import LeftUpState
from model.Shapes.RotationState import RotationState
from model.Directions.Directions import *


class RightUpState(RotationState):

    def next_state(self):
        self.block.set_state(LeftUpState(self.block))


    def rotate(self):
        self.block.b.move(OneLeft())
        self.block.d.move(OneLeft())
        self.next_state()
