from model.Shapes.L_block.LeftUpState import LeftUpState
from model.Shapes.RotationState import RotationState


class LeftDownState(RotationState):

    def next_state(self):
        self.block.set_state(LeftUpState(self.block))

    def rotate(self):
        self.block.a.move(1,0)
        self.block.b.move(1,0)
        self.next_state()
