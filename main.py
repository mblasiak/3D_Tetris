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
        self.gM.drop_new()
        self.taskMgr.add(self.gM.play, "MovAll")
        globalClock.setMode(ClockObject.MLimited)
        globalClock.setFrameRate(120)
        self.render.setAntialias(AntialiasAttrib.MAuto)
        self.disableMouse()
        p=UpcomingBlockDisplay(self)
        z=GamePlayCamera(p.displayRegion,self.render,None)
        z.reset()
        # z.move_with_interval()
        #self.render.analyze()


loadPrcFileData('', 'win-size 800 800')
# loadPrcFileData('', 'want-pstats 1')


app = MyApp()
app.setFrameRateMeter(True)
app.run()
