from game.BoxGfx.BoxGFX import BoxGFX


class BoxGfxFactory:
    def __init__(self, app, model_factory, box_size, offsets, gamespeed):
        self.app = app
        self.model_factory = model_factory
        self.box_size = box_size
        self.offsets = offsets
        self.game_speed = gamespeed

    def get_gfx_box(self, model_type,x,y):
        return BoxGFX(x, y, self.app, model_type, self.model_factory, self.box_size, self.offsets,
                      self.game_speed)
