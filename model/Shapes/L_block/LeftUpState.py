from model.Shapes.RotationState import RotationState


class LeftUpState(RotationState):

    def next_state(self):
        self.block.set_state(self)

    def rotate(self):
        return
        self.block.c.move(0, 1)
        self.block.c.move(0, 1)
        self.next_state()
