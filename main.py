from direct.showbase.ShowBase import ShowBase, ClockObject
from direct.showbase.ShowBaseGlobal import globalClock

from model.GameManager import GameManager
from panda3d.core import loadPrcFileData



class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.gM = GameManager(self)
        self.gM.drop_new()
        self.taskMgr.add(self.gM.play, "MovAll")
        globalClock.setMode(ClockObject.MLimited)
        globalClock.setFrameRate(120)

        #self.render.analyze()

loadPrcFileData('', 'win-size 600 600')
#loadPrcFileData('', 'want-pstats 1')



app = MyApp()

app.setFrameRateMeter(True)

app.run()
