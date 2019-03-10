from panda3d.core import NodePath, Camera

from game.BoxGfx.BoxGfxFactory import BoxGfxFactory
from game.Config import Config
from game.GameCore.NextBoxTypeObserver import NextBoxTypeObserver
from game.GameMap.GameMap import GameMap
from game.Shapes.ShapesFactory import ShapesFactory
from game.StartClear import StartClear

gp = Config.GamePlay
gpm = Config.GamePlay.GameMap
gpfx = Config.GamePlay.Gfx


class NextBlockDisplay(NextBoxTypeObserver,StartClear):

    def __init__(self, app, model_factory):
        self.displayRegion = app.win.makeDisplayRegion(Config.NextBlockRegion.cords)
        self.displayRegion.setSort(Config.NextBlockRegion.sort)
        self.renderer = NodePath('UpcomingBlockRender')
        gm_nx = GameMap(gpm.X, gpm.Y)
        gfx_next_box_factory = BoxGfxFactory(self.renderer, model_factory, gpfx.box_size, gpfx.offset, gp.game_speed)
        self.sf = ShapesFactory(app, gm_nx, gpm.spawn_pos, gfx_next_box_factory)

        self.current_box = None
        self.cam = None

    def setCamera(self, cam):
        self.displayRegion.setCamera(cam)
        cam.reparentTo(self.renderer)
        self.cam = cam

    def add_to_display(self, object):
        object.reparentTo(self.renderer)

    def remove_from_display(self, object):
        object.detachNode()

    def clear(self):
        if self.current_box is not None:
            self.current_box.remove()

    def update(self, numb):
        if self.current_box is not None:
            self.current_box.remove()
        self.current_box = self.current_box = self.sf.get_shape_from_numb(numb)
