from direct.showbase.ShowBase import ShowBase, ClockObject, AntialiasAttrib
from direct.showbase.ShowBaseGlobal import globalClock

from game.GameManager import GameManager
from panda3d.core import loadPrcFileData

from game.GamePlayCamera import GamePlayCamera
from game.UpcomingBlockDisplay import UpcomingBlockDisplay


class MyApp(ShowBase):
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


loadPrcFileData('', 'win-size 800 800')
# loadPrcFileData('', 'want-pstats 1')
app = MyApp()
app.setFrameRateMeter(True)
app.run()
