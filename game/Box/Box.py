

class Box:

    def __init__(self, x, y, map_controller, model_type, box_gfx_factory):
        self.x = x
        self.y = y
        self.map_controller = map_controller
        self.map_controller.block(self.y, self.x, self)
        self.box_gfx = box_gfx_factory.get_gfx_box(model_type,self.x,self.y)

    def fall(self):
        self.map_controller.release(self.y, self.x, self)
        self.y = self.y - 1
        self.map_controller.block(self.y, self.x, self)
        self.box_gfx.start_falling_animation()

    def is_animation_playing(self):
        return self.box_gfx.is_animation_playing()

    def neighbour(self, direction):
        return self.map_controller.check(self.y + direction.y, self.x + direction.x)

    def move(self, direction):
        self.map_controller.release(self.y, self.x, self)
        self.x = self.x + direction.x
        self.y = self.y + direction.y
        self.map_controller.block(self.y, self.x, self)
        self.box_gfx.move(direction)

    def refresh(self):
        self.box_gfx.refresh()

    def remove(self):
        self.box_gfx.remove()
