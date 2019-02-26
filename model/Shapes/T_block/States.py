from model.Directions.Directions import *
from model.Shapes.RotationState import RotationState


class DownState(RotationState):

    def next_state(self):
        self.block.set_state(LeftState(self.block))

    def rotate(self):
        self.block.a.move(OneRight())

        self.block.a.move(OneDown())

        self.block.b.refresh()

        self.block.c.move(OneUp())
        self.block.c.move(OneRight())

        self.block.d.move(OneDown())
        self.block.d.move(OneLeft())

        self.next_state()


class LeftState(RotationState):

    def next_state(self):
        self.block.set_state(UpState(self.block))

    def rotate(self):
        self.block.a.move(OneDown())
        self.block.a.move(OneLeft())

        self.block.b.refresh()

        self.block.c.move(OneRight())
        self.block.c.move(OneDown())

        self.block.d.move(OneLeft())
        self.block.d.move(OneUp())

        self.next_state()


class UpState(RotationState):

    def next_state(self):
        self.block.set_state(RightState(self.block))

    def rotate(self):
        self.block.a.move(OneLeft())
        self.block.a.move(OneUp())

        self.block.d.move(OneRight())
        self.block.d.move(OneUp())

        self.block.b.refresh()

        self.block.c.move(OneLeft())
        self.block.c.move(OneDown())


        self.next_state()


class RightState(RotationState):

    def next_state(self):
        self.block.set_state(DownState(self.block))

    def rotate(self):
        self.block.a.move(OneUp())
        self.block.a.move(OneRight())

        self.block.b.refresh()

        self.block.c.move(OneLeft())
        self.block.c.move(OneUp())

        self.block.d.move(OneDown())
        self.block.d.move(OneRight())

        self.next_state()
