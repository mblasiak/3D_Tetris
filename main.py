from direct.showbase.ShowBase import ShowBase
from model.GameManager import GameManager


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.gM = GameManager(self)
        self.gM.drop_new()
        self.taskMgr.add(self.gM.moveBlocks, "MovAll")

app = MyApp()
app.setFrameRateMeter(True)

app.run()
