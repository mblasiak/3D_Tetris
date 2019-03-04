from panda3d.core import NodePath, Camera

from game.Config import Config


class UpcomingBlockDisplay:

    def __init__(self, app):
        self.displayRegion = app.win.makeDisplayRegion(Config.NextBlockRegion.cords)
        self.displayRegion.setSort(Config.NextBlockRegion.sort)
        self.renderer = NodePath('UpcomingBlockRender')

    def setCamera(self, cam):
        self.displayRegion.setCamera(cam)
