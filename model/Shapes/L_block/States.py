from model.Directions.Directions import *
from model.Shapes.RotationState import RotationState


class LeftDownState(RotationState):

    def next_state(self):
        self.block.set_state(RightDownState(self.block))

    def rotate(self):
        self.block.a.move(OneRight())
        self.block.a.move(OneRight())
        self.block.a.move(OneDown())

        self.block.b.move(OneRight())

        self.block.c.move(OneUp())

        self.block.d.move(OneLeft())
        self.next_state()


class RightDownState(RotationState):

    def next_state(self):
        self.block.set_state(RightUpState(self.block))

    def rotate(self):
        self.block.a.move(OneDown())
        self.block.b.move(OneRight())

        self.block.c.move(OneRight())
        self.block.c.move(OneRight())

        self.block.c.move(OneUp())

        self.block.d.move(OneUp())
        self.block.d.move(OneUp())

        self.block.d.move(OneRight())

        self.next_state()


class RightUpState(RotationState):

    def next_state(self):
        self.block.set_state(LeftUpState(self.block))

    def rotate(self):
        self.block.d.move(OneRight())

        self.block.c.move(OneDown())

        self.block.b.move(OneLeft())

        self.block.a.move(OneLeft())
        self.block.a.move(OneLeft())
        self.block.a.move(OneUp())

        self.next_state()


class LeftUpState(RotationState):

    def next_state(self):
        self.block.set_state(LeftDownState(self.block))

    def rotate(self):
        self.block.a.move(OneUp())

        self.block.b.move(OneDown())
        self.block.b.move(OneLeft())

        self.block.c.move(OneLeft())
        self.block.c.move(OneLeft())

        self.block.d.move(OneDown())
        self.block.d.move(OneDown())
        self.block.d.move(OneLeft())

        self.next_state()
