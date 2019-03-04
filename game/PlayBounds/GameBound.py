class GameBound:
    def __init__(self, app, x, y, box_size, offsets):
        self.model = app.loader.loadModel("resources/models/cargoBox.egg")
        self.box_size = box_size
        X = x
        Y = y
        (x_offset, y_offset, z_offset) = offsets
        y_offset-=box_size
        self.all_holders = []

        for x in range(0, X):
            box_holder = app.render.attachNewNode("Box Holder")
            self.all_holders.append(box_holder)
            self.model.instanceTo(box_holder)
            box_holder.setPos(x * self.box_size + x_offset, z_offset, +y_offset)

        for y in range(0, Y - 2):
            box_holder = app.render.attachNewNode("Box Holder")
            self.all_holders.append(box_holder)
            self.model.instanceTo(box_holder)
            box_holder.setPos(-self.box_size + x_offset, z_offset, y * self.box_size + y_offset)

        for y in range(0, Y - 2):
            box_holder = app.render.attachNewNode("Box Holder")
            self.all_holders.append(box_holder)
            self.model.instanceTo(box_holder)
            box_holder.setPos(X * self.box_size + x_offset, z_offset, y * self.box_size + y_offset)
