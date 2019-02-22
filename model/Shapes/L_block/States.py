from model.Directions.Directions import *
from model.Shapes.RotationState import RotationState


class LeftDownState(RotationState):

    def next_state(self):
        self.block.set_state(RightDownState(self.block))

    def rotate(self):
        self.block.a.move(OneRight())
        self.block.b.move(OneRight())
        self.next_state()


class LeftUpState(RotationState):

    def next_state(self):
        self.block.set_state(LeftDownState(self.block))

    def rotate(self):
        self.block.c.move(OneUp())
        self.block.c.move(OneUp())
        self.next_state()


class RightDownState(RotationState):

    def next_state(self):
        self.block.set_state(RightUpState(self.block))

    def rotate(self):
        self.block.c.move(OneUp())
        self.block.c.move(OneUp())
        self.next_state()


class RightUpState(RotationState):

    def next_state(self):
        self.block.set_state(LeftUpState(self.block))

    def rotate(self):
        self.block.b.move(OneLeft())
        self.block.d.move(OneLeft())
        self.next_state()
