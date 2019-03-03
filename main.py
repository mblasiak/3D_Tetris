
from direct.showbase.ShowBase import ShowBase, ClockObject, Camera, NodePath
from direct.showbase.ShowBaseGlobal import globalClock

from game.GameManager import GameManager
from panda3d.core import loadPrcFileData


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.gM = GameManager(self)
        self.gM.drop_new()
        self.taskMgr.add(self.gM.play, "MovAll")
        globalClock.setMode(ClockObject.MLimited)
        globalClock.setFrameRate(120)

        displayRegion = self.win.makeDisplayRegion(0, 1, 0.8, 1)
        displayRegion.setSort(20)
        camNode = Camera('cam')

        camNP = NodePath(camNode)
        render2 = NodePath('render2')
        env = self.loader.loadModel('environment.egg')
        env.reparentTo(render2)
        camNP.reparentTo(render2)
        displayRegion.setCamera(camNP)

        # self.render.analyze()


loadPrcFileData('', 'win-size 800 800')
# loadPrcFileData('', 'want-pstats 1')


app = MyApp()
app.setFrameRateMeter(True)
app.run()
