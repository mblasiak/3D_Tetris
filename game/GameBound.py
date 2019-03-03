class GameBound:
    def __init__(self,app,game_manager):
        self.bound = app.loader.loadModel("resources/map.egg")
        self.gfx_z = 100
        self.box_size = game_manager.box_size
        self.game_manager = game_manager

        self.box_holder = app.render.attachNewNode("Box Holder")
        self.bound.instanceTo(self.box_holder)
        self.bound.setPos(0, self.gfx_z, 0)

