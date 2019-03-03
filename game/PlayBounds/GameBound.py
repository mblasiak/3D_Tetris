class GameBound:
    def __init__(self, app, game_manager):
        self.model = app.loader.loadModel("resources/models/cargoBox.egg")
        self.gfx_z = 100
        self.box_size = game_manager.box_size
        self.game_manager = game_manager
        X = game_manager.SIZE_X
        Y = game_manager.SIZE_Y
        y_offset=22
        x_offset=-30
        y_draw_start=2
        self.all_holders = []

        for x in range(0, X):
            box_holder = app.render.attachNewNode("Box Holder")
            self.all_holders.append(box_holder)
            self.model.instanceTo(box_holder)
            box_holder.setPos(x * self.box_size+x_offset, self.gfx_z, -y_offset)

        for y in range (0,Y-2):
            box_holder = app.render.attachNewNode("Box Holder")
            self.all_holders.append(box_holder)
            self.model.instanceTo(box_holder)
            box_holder.setPos(-self.box_size+x_offset, self.gfx_z, y*self.box_size-y_offset)

        for y in range (0,Y-2):
            box_holder = app.render.attachNewNode("Box Holder")
            self.all_holders.append(box_holder)
            self.model.instanceTo(box_holder)
            box_holder.setPos(X*self.box_size+x_offset, self.gfx_z, y*self.box_size-y_offset)
