from direct.showbase.ShowBase import ShowBase, ClockObject, AntialiasAttrib
from direct.showbase.ShowBaseGlobal import globalClock

from game.GameManager import GameManager
from panda3d.core import loadPrcFileData


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.gM = GameManager(self)
        self.set_up_environment()
        self.set_up_gameplay()

    def set_up_gameplay(self):
        self.gM.drop_new()
        self.taskMgr.add(self.gM.play, "MovAll")

    def set_up_environment(self):
        globalClock.setMode(ClockObject.MLimited)
        globalClock.setFrameRate(120)
        self.render.setAntialias(AntialiasAttrib.MAuto)
        self.disableMouse()
        # self.render.analyze()


