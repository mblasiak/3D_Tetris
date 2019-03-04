from panda3d.core import NodePath, Camera

from game.GameConfig import GameConfig


class UpcomingBlockDisplay:

    def __init__(self, app):
        self.displayRegion = app.win.makeDisplayRegion(GameConfig.upcoming_block_region)
        self.displayRegion.setSort(GameConfig.upcoming_block_region_sort)
        self.renderer = NodePath('UpcomingBlockRender')

    def setCamera(self, cam):
        self.displayRegion.setCamera(cam)
