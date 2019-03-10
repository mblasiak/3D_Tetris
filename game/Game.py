from direct.showbase.ShowBase import ShowBase, ClockObject, AntialiasAttrib
from direct.showbase.ShowBaseGlobal import globalClock
from game.MainGame import MainGame


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.set_up()

    def set_up(self):
        globalClock.setMode(ClockObject.MLimited)
        globalClock.setFrameRate(120)
        self.render.setAntialias(AntialiasAttrib.MAuto)
        self.disableMouse()
        MainGame(self)
