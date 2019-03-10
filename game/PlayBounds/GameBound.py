class GameBound:
    def __init__(self, app, x, y, box_size, offsets):
        self.model = app.loader.loadModel("resources/models/cargoBox.egg")
        self.box_size = box_size
        self.X = x
        self.Y = y
        (self.x_offset, self.y_offset, self.z_offset) = offsets
        self.y_offset -= box_size
        self.all_holders = []
        self.app = app
        self.set_up()

    def set_up(self):
        for x in range(0, self.X):
            box_holder = self.app.render.attachNewNode("Box Holder")
            self.all_holders.append(box_holder)
            self.model.instanceTo(box_holder)
            box_holder.setPos(x * self.box_size + self.x_offset, self.z_offset, +self.y_offset)

        for y in range(0, self.Y - 2):
            box_holder = self.app.render.attachNewNode("Box Holder")
            self.all_holders.append(box_holder)
            self.model.instanceTo(box_holder)
            box_holder.setPos(-self.box_size + self.x_offset, self.z_offset, y * self.box_size + self.y_offset)

        for y in range(0, self.Y - 2):
            box_holder = self.app.render.attachNewNode("Box Holder")
            self.all_holders.append(box_holder)
            self.model.instanceTo(box_holder)
            box_holder.setPos(self.X * self.box_size + self.x_offset, self.z_offset, y * self.box_size + self.y_offset)

    def clear(self):
        for holder in self.all_holders:
            holder.detachNode()

    def __del__(self):
        self.clear()
